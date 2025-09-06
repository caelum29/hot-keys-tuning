# Keyboard Configuration System

**YAML + Generated Markdown + CSV** - A unified approach to managing keyboard bindings across multiple systems.

## Overview

This system transforms keyboard configuration from static documentation into a dynamic, LLM-friendly data management system. It provides:

- **Single source of truth**: YAML files contain all binding data
- **Multiple output formats**: Markdown for docs, CSV for analysis  
- **LLM-friendly**: Easy for Claude Code to parse and edit accurately
- **Version controlled**: Track all changes with meaningful diffs

## Structure

```
keyboard-config/
├── data/                           # Source data (edit these)
│   ├── horizontal-navigation.yaml  # H/L key bindings
│   ├── vertical-navigation.yaml    # J/K key bindings  
│   └── schemas/
│       └── binding-schema.yaml     # Validation rules
├── generated/                      # Generated files (don't edit)
│   ├── KEY-MAP.md                  # Pretty markdown tables
│   ├── bindings.csv                # Full dataset in CSV
│   ├── bindings.tsv                # Tab-separated version
│   ├── bindings-summary.csv        # Statistics summary
│   └── bindings-pivot.csv          # Pivot table ready format
└── scripts/
    ├── generate-docs.py             # YAML → Markdown
    └── export-csv.py                # YAML → CSV
```

## Usage

### 1. Edit Source Data
Modify the YAML files in `data/`:
- `horizontal-navigation.yaml` - All H/L key bindings
- `vertical-navigation.yaml` - All J/K key bindings

### 2. Generate Documentation
```bash
# Activate virtual environment
source venv/bin/activate

# Generate markdown documentation
python scripts/generate-docs.py

# Generate CSV exports
python scripts/export-csv.py
```

### 3. Use the Outputs
- **Markdown**: Use `generated/KEY-MAP.md` for documentation
- **CSV**: Import `generated/bindings.csv` into Excel/Sheets for analysis
- **TSV**: Use `generated/bindings.tsv` for other tools

## Data Structure

Each binding has this structure:

```yaml
binding_name:
  keystroke: "⌥H / ⌥L"                    # Human-readable format
  system: "W"                             # Which system handles it
  status: "implemented"                   # Implementation status
  category: "navigation"                  # Functional category
  action: "Move caret to prev/next word"  # What it does
  details:
    ide_action_id: "EditorPreviousWord"   # WebStorm action ID
    karabiner_code: "alt+h/l"             # Karabiner key code
    ideavim_command: "nnoremap <A-h> b"   # Vim mapping
    config_reference: "keymap.xml:L48"    # File location
    notes: ""                             # Optional notes
```

## System Codes

- **I**: IdeaVim (editor-level vim emulation)
- **W**: WebStorm (IDE-level keymaps)  
- **K**: Karabiner Elements (system-wide modifications)
- **W+I**, **K+W**, etc.: Multi-system bindings
- **-**: Not implemented

## Status Values

- `implemented`: Fully configured and working
- `planned`: Identified for future implementation  
- `needs_attention`: Requires fixes or remapping
- `disabled`: Intentionally disabled
- `conflict`: Conflicts with other bindings

## Benefits

### For LLMs (Claude Code)
- ✅ Easy to parse and edit YAML structure
- ✅ Clear validation rules prevent errors
- ✅ Consistent data format across all bindings
- ✅ Can generate configs directly from data

### For Humans
- 📋 Beautiful markdown tables for documentation
- 📊 CSV exports for spreadsheet analysis
- 🔍 Searchable and filterable data
- 📈 Built-in statistics and summaries

### For Development  
- 🚀 Single command regenerates all documentation
- 📝 Version control tracks meaningful changes
- 🔄 Can extend to auto-generate actual config files
- 🛡️ Schema validation prevents data corruption

## Current Stats

- **Total Bindings**: 48
- **Implemented**: 28 (58.3%)
- **Planned**: 19 (39.6%)
- **Needs Attention**: 1 (2.1%)

## Next Steps

This system can be extended to:
- Auto-generate actual config files (karabiner.json, .ideavimrc, etc.)
- Add validation scripts to check for conflicts
- Create web interface for editing bindings
- Generate configuration installation scripts