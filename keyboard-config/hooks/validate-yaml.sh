#!/bin/bash

# YAML Validation Hook for Keyboard Config Project
# Usage: validate-yaml.sh <file_path>

set -e

YAML_FILE="$1"
# Convert to absolute path if relative
if [[ ! "$YAML_FILE" == /* ]]; then
    YAML_FILE="$(pwd)/$YAML_FILE"
fi
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
LOG_FILE="$PROJECT_DIR/.claude/hooks/logs/yaml-validation.log"

if [[ -z "$YAML_FILE" ]]; then
    echo "Error: No YAML file provided" | tee -a "$LOG_FILE"
    exit 1
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Validating YAML: $YAML_FILE" >> "$LOG_FILE"

# Check if file exists
if [[ ! -f "$YAML_FILE" ]]; then
    echo "Error: File does not exist: $YAML_FILE" | tee -a "$LOG_FILE"
    exit 1
fi

# Activate virtual environment and validate YAML syntax  
cd "$(dirname "$0")/.."
source venv/bin/activate
python3 -c "
import yaml
import sys
try:
    with open('$YAML_FILE', 'r') as f:
        yaml.safe_load(f)
    print('✓ YAML syntax valid: $YAML_FILE')
except yaml.YAMLError as e:
    print(f'✗ YAML syntax error in $YAML_FILE: {e}', file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f'✗ Error reading $YAML_FILE: {e}', file=sys.stderr)
    sys.exit(1)
" >> "$LOG_FILE" 2>&1

# If we're in the keyboard-config directory, also validate schema
if [[ "$YAML_FILE" == *"keyboard-config/data"* ]]; then
    echo "Checking keyboard config schema..." >> "$LOG_FILE"
    
    # Check for required fields in keyboard config YAML
    python3 -c "
import yaml
import sys

required_fields = ['bindings']
binding_required = ['key', 'action', 'status']

try:
    with open('$YAML_FILE', 'r') as f:
        data = yaml.safe_load(f)
    
    # Check top-level structure
    for field in required_fields:
        if field not in data:
            print(f'✗ Missing required field: {field}')
            sys.exit(1)
    
    # Check binding structure
    if isinstance(data.get('bindings'), list):
        for i, binding in enumerate(data['bindings']):
            for field in binding_required:
                if field not in binding:
                    print(f'✗ Binding {i}: Missing required field: {field}')
                    sys.exit(1)
    
    print('✓ Schema validation passed')
    
except Exception as e:
    print(f'✗ Schema validation error: {e}', file=sys.stderr)
    sys.exit(1)
" >> "$LOG_FILE" 2>&1
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Validation completed successfully" >> "$LOG_FILE"