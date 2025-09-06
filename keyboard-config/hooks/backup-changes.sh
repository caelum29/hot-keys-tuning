#!/bin/bash

# Backup Hook for Keyboard Config Project
# Usage: backup-changes.sh <file_path> [backup_dir]

set -e

FILE_PATH="$1"
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
BACKUP_DIR="${2:-$PROJECT_DIR/.claude/hooks/backups}"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
LOG_FILE="$PROJECT_DIR/.claude/hooks/logs/backup.log"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

if [[ -z "$FILE_PATH" ]]; then
    echo "Error: No file path provided" | tee -a "$LOG_FILE"
    exit 1
fi

if [[ ! -f "$FILE_PATH" ]]; then
    echo "Warning: File does not exist: $FILE_PATH" | tee -a "$LOG_FILE"
    exit 0  # Not an error for new files
fi

# Create backup filename
BASENAME=$(basename "$FILE_PATH")
BACKUP_PATH="$BACKUP_DIR/${BASENAME}_${TIMESTAMP}.bak"

# Copy file to backup location
cp "$FILE_PATH" "$BACKUP_PATH"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Backed up: $FILE_PATH -> $BACKUP_PATH" >> "$LOG_FILE"

# Keep only last 10 backups for each file to prevent disk bloat
find "$BACKUP_DIR" -name "${BASENAME}_*.bak" -type f | sort -r | tail -n +11 | xargs -r rm -f

echo "✓ Backup created: $BACKUP_PATH"