#!/bin/bash

# Wrapper to run Python script with virtual environment
cd "$(dirname "$0")/.."
source venv/bin/activate
python3 - << 'EOF'

"""
Keyboard Binding Conflict Detection Hook
Checks for duplicate key combinations across all config files
"""

import os
import sys
import json
import yaml
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def log_message(message):
    """Log message to hook log file"""
    log_file = Path.home() / ".claude/hooks/conflict-check.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(log_file, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

def parse_yaml_bindings(yaml_path):
    """Extract key combinations from YAML config files"""
    bindings = []
    
    try:
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
            
        if 'bindings' in data:
            for binding in data['bindings']:
                key = binding.get('key', '')
                modifiers = binding.get('modifiers', [])
                
                # Create normalized key combination
                mod_str = '+'.join(sorted(modifiers)) if modifiers else ''
                key_combo = f"{mod_str}+{key}" if mod_str else key
                
                bindings.append({
                    'combo': key_combo.lower(),
                    'source': str(yaml_path),
                    'action': binding.get('action', 'Unknown'),
                    'status': binding.get('status', 'Unknown')
                })
                
    except Exception as e:
        log_message(f"Error parsing YAML {yaml_path}: {e}")
        
    return bindings

def parse_karabiner_config(json_path):
    """Extract key combinations from Karabiner JSON config"""
    bindings = []
    
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            
        # Navigate Karabiner structure to find manipulators
        profiles = data.get('profiles', [])
        for profile in profiles:
            complex_mods = profile.get('complex_modifications', {}).get('rules', [])
            for rule in complex_mods:
                manipulators = rule.get('manipulators', [])
                for manip in manipulators:
                    from_key = manip.get('from', {})
                    key_code = from_key.get('key_code', '')
                    modifiers = from_key.get('modifiers', {}).get('mandatory', [])
                    
                    if key_code:
                        mod_str = '+'.join(sorted(modifiers)) if modifiers else ''
                        key_combo = f"{mod_str}+{key_code}" if mod_str else key_code
                        
                        bindings.append({
                            'combo': key_combo.lower(),
                            'source': str(json_path),
                            'action': rule.get('description', 'Karabiner rule'),
                            'status': 'Active'
                        })
                        
    except Exception as e:
        log_message(f"Error parsing Karabiner config {json_path}: {e}")
        
    return bindings

def parse_ideavim_config(ideavimrc_path):
    """Extract key combinations from .ideavimrc"""
    bindings = []
    
    try:
        with open(ideavimrc_path, 'r') as f:
            lines = f.readlines()
            
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Look for various Vim mapping commands
            mapping_patterns = [
                r'^(map|nmap|vmap|imap|nnoremap|vnoremap|inoremap)\s+(\S+)\s+(.+)$',
                r'^(noremap)\s+(\S+)\s+(.+)$'
            ]
            
            for pattern in mapping_patterns:
                match = re.match(pattern, line)
                if match:
                    map_type, key_combo, action = match.groups()
                    
                    bindings.append({
                        'combo': key_combo.lower(),
                        'source': f"{ideavimrc_path}:{line_num}",
                        'action': action.strip(),
                        'status': f"IdeaVim {map_type}"
                    })
                    break
                    
    except Exception as e:
        log_message(f"Error parsing IdeaVim config {ideavimrc_path}: {e}")
        
    return bindings

def find_conflicts(project_dir):
    """Find all keyboard binding conflicts in project"""
    project_path = Path(project_dir)
    all_bindings = []
    
    # Find YAML configs
    yaml_files = list(project_path.rglob("*.yaml"))
    yaml_files.extend(list(project_path.rglob("*.yml")))
    
    for yaml_file in yaml_files:
        if 'keyboard-config/data' in str(yaml_file):
            all_bindings.extend(parse_yaml_bindings(yaml_file))
    
    # Find Karabiner configs
    json_files = list(project_path.rglob("karabiner.json"))
    for json_file in json_files:
        all_bindings.extend(parse_karabiner_config(json_file))
    
    # Find IdeaVim configs
    ideavim_files = list(project_path.rglob(".ideavimrc"))
    for ideavim_file in ideavim_files:
        all_bindings.extend(parse_ideavim_config(ideavim_file))
    
    # Group by key combination to find conflicts
    combo_groups = defaultdict(list)
    for binding in all_bindings:
        combo_groups[binding['combo']].append(binding)
    
    # Find actual conflicts (same combo, different sources)
    conflicts = {}
    for combo, bindings in combo_groups.items():
        if len(bindings) > 1:
            # Check if they're from different config systems
            sources = set(binding['source'].split(':')[0] for binding in bindings)
            if len(sources) > 1:
                conflicts[combo] = bindings
    
    return conflicts, len(all_bindings)

def main():
    project_dir = os.environ.get('CLAUDE_PROJECT_DIR', os.getcwd())
    
    log_message("Starting conflict detection...")
    
    conflicts, total_bindings = find_conflicts(project_dir)
    
    if conflicts:
        print(f"🚨 Found {len(conflicts)} potential conflicts:")
        log_message(f"Found {len(conflicts)} conflicts out of {total_bindings} total bindings")
        
        for combo, bindings in conflicts.items():
            print(f"\nKey combination '{combo}' used in:")
            for binding in bindings:
                print(f"  - {binding['source']}: {binding['action']} ({binding['status']})")
                
    else:
        print(f"✅ No conflicts found! Checked {total_bindings} bindings.")
        log_message(f"No conflicts in {total_bindings} total bindings")

if __name__ == "__main__":
    main()
EOF