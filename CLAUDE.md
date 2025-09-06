# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a unified keyboard productivity configuration system that enhances developer workflow across multiple tools:

- **Karabiner Elements**: System-wide keyboard modifications and complex key mappings
- **IdeaVim**: Vim emulation for JetBrains IDEs with custom keybindings  
- **WebStorm**: Custom keymap configurations for IDE productivity
- **Documentation**: Comprehensive guides for keyboard navigation and productivity patterns
- **src/docs/PHILOSOPHY.md**: Core design principles and systematic approach to keyboard productivity integration

## Architecture

### Core Components

- `src/karabiner/` - Karabiner Elements configuration files
  - `karabiner.json` - Main configuration with complex modifications, dual-role keys, and navigation mappings
  - `dual_role_keys.json` - Specialized dual-role key configurations
  - `downloaded/vim.json` - Vim-style navigation rules
- `src/idea-vim/.ideavimrc` - IdeaVim configuration with 300+ lines of custom mappings
- `src/webstorm-keymap/macOS copy.xml` - WebStorm keymap with HJKL navigation integration
- `src/docs/` - Extensive documentation on keyboard productivity patterns
  - `KEY-BINDING-COMBINATIONS.md` - **NEW: Complete reference of all 57+ possible key binding combinations for a single key**
  - `learning-claude-code/` - **NEW: Claude Code automation and learning materials**
    - `CLAUDE-HOOKS-LEARNING.md` - Comprehensive guide for Claude Code hooks and subagents
    - `CLAUDE-CODE-GUIDE.md` - Complete Claude Code feature reference and tutorial
    - `TEST-HOOKS-DEMO.md` - Demonstration results of hooks and subagents implementation
- `keyboard-config/` - **NEW: YAML-based configuration system**
  - `data/` - Source YAML files (single source of truth for all bindings)
    - `horizontal-navigation.yaml` - H/L key bindings with full technical details
    - `vertical-navigation.yaml` - J/K key bindings with structured data
    - `schemas/binding-schema.yaml` - Validation rules for data consistency
  - `generated/` - Auto-generated documentation and exports
    - `KEY-MAP.md` - Enhanced markdown tables with statistics
    - `bindings.csv` - Full dataset for spreadsheet analysis
    - `bindings-summary.csv` - Statistics breakdown
    - `bindings-pivot.csv` - Pivot table ready format
  - `scripts/` - Generation and export tools
    - `generate-docs.py` - YAML → Markdown converter
    - `export-csv.py` - YAML → Multiple CSV formats
  - `hooks/` - **NEW: Automation and validation scripts**
    - `validate-yaml.sh` - YAML syntax and schema validation with virtual environment
    - `backup-changes.sh` - Automated backup system with timestamped versions
    - `check-conflicts.py` - Multi-system conflict detection (Karabiner + IdeaVim + WebStorm)

### Key Concepts

**Navigation Philosophy**: Uses HJKL keys (borrowed from Vim) as primary navigation with modifier combinations:
- H/L for horizontal movement (left/right)
- J/K for vertical movement (down/up)  
- Hyper key (✱) implemented as right-side modifier combination (⌘⌥⌃⇧)

**Modifier Layers**: Multiple modifier combinations create different navigation modes:
- Base: Character movement
- ⇧ (Shift): Selection/window switching
- ⌃ (Control): Desktop management
- ⌥ (Option): Word movement/mouse control
- ⌘ (Command): Application actions
- ✱ (Hyper): System-wide navigation layer

**Integration Strategy**: Consistent keybindings across:
- System level (Karabiner)
- IDE level (WebStorm keymap)
- Editor level (IdeaVim)

**Combination Possibilities**: Each single key supports 57+ unique binding combinations:
- 16 standard modifier combinations (⇧⌃⌥⌘)
- 5 hyper key combinations (✱ with modifiers)
- 18+ leader key sequences (Vim-style prefixes)
- 5 double tap variations (timing-based)
- 8+ multi-key sequences (text objects)
- Additional chord, long press, and context-aware patterns
- See `src/docs/KEY-BINDING-COMBINATIONS.md` for complete reference

## Development Workflow

This project doesn't have traditional build/test commands as it consists primarily of configuration files. Key operations:

### Karabiner Configuration
- Edit `src/karabiner/karabiner.json` for complex modifications
- Use Karabiner Elements GUI to import/export configurations
- Test modifications require Karabiner Elements restart

### IdeaVim Configuration  
- Edit `src/idea-vim/.ideavimrc`
- Reload with `:source ~/.ideavimrc` in IDE
- Test mappings directly in JetBrains IDEs

### WebStorm Keymap
- Import `src/webstorm-keymap/macOS copy.xml` through WebStorm settings
- Modifications require IDE restart to take effect

### Documentation
- Markdown files in `src/docs/` provide implementation guides
- README.md contains the master navigation reference table
- **src/docs/PHILOSOPHY.md**: Core design principles, vim philosophy integration, and systematic keyboard productivity approach

### YAML Configuration System (NEW)
- **Primary workflow**: Edit YAML files in `keyboard-config/data/`
- **Generate docs**: `python scripts/generate-docs.py` (creates enhanced markdown)
- **Export data**: `python scripts/export-csv.py` (creates CSV/TSV for analysis)
- **Virtual environment**: `source keyboard-config/venv/bin/activate` before running scripts
- **Validation**: Schema enforces data consistency across all bindings

### Claude Code Automation & Hooks (NEW)
- **Hook configuration**: `~/.claude/hooks/keyboard-config-hooks.json` - Automated workflows
- **Validation workflow**: Automatic YAML validation on file edits
- **Backup system**: Timestamped backups before modifications
- **Conflict detection**: Multi-system keyboard binding conflict analysis
- **Auto-documentation**: Regenerate docs when YAML files change
- **Subagent analysis**: Complex keyboard binding analysis and optimization recommendations

## File Structure Notes

- Configuration files use JSON (Karabiner) and XML (WebStorm keymap) formats
- The `.ideavimrc` uses Vim script syntax
- Documentation follows standard Markdown with extensive tables for key combinations
- Version control tracks all configuration changes for rollback capability

## Key Patterns

When working with this codebase:
- Maintain consistency between Karabiner, IdeaVim, and WebStorm configurations
- Follow the HJKL navigation paradigm established throughout
- Test changes across all three systems (macOS, WebStorm, IdeaVim) 
- Document any new key combinations in README.md tables
- Use descriptive names in Karabiner rule descriptions for maintainability

## Documentation Standards

**File Creation and Naming**:
- All markdown documentation files created by Claude Code should be placed in `src/docs/`
- Use ALL CAPS naming convention for all documents (e.g., `PHILOSOPHY.md`, `ARCHITECTURE.md`)
- Reference documents with full path: `src/docs/PHILOSOPHY.md`

## LLM-Friendly Workflow (Claude Code)

**Preferred approach for AI assistance:**

### For Keyboard Binding Changes:
1. **Edit YAML files**: Modify `keyboard-config/data/*.yaml` (structured, easy to parse)
2. **Auto-validation**: Hooks automatically validate YAML syntax and schema on edits
3. **Auto-backup**: Timestamped backups created before any modifications
4. **Auto-generate docs**: Run generation scripts to update all documentation  
5. **Conflict checking**: Use subagents or scripts to detect binding conflicts
6. **Avoid direct markdown editing**: Generated files will be overwritten

### For Technical Implementation:
- YAML provides clear structure for all binding details (action IDs, key codes, config references)
- Schema validation prevents errors and ensures consistency
- CSV exports enable data analysis and bulk operations
- Single source of truth eliminates documentation drift

### Data Structure Benefits:
- **Parsing**: YAML is much easier for LLMs to understand than complex markdown tables
- **Editing**: Structured format prevents column alignment and formatting errors  
- **Validation**: Schema catches missing fields and invalid values
- **Extensibility**: Can easily add new fields or binding types
- **Integration**: Data can drive config file generation and validation tools

### Claude Code Learning Resources (NEW)
- **`src/docs/learning-claude-code/CLAUDE-HOOKS-LEARNING.md`**: Complete 350+ line guide covering hooks fundamentals, practical examples, subagent usage, security practices, and troubleshooting
- **`src/docs/learning-claude-code/CLAUDE-CODE-GUIDE.md`**: Comprehensive feature reference with project-specific examples
- **`src/docs/learning-claude-code/TEST-HOOKS-DEMO.md`**: Results and demonstration of implemented automation systems

## Testing & Validation Commands

### Yarn Scripts (Recommended)
The project now includes convenient yarn scripts in `package.json` for all common operations:

```bash
# YAML validation
yarn validate:yaml                    # Validate horizontal-navigation.yaml
yarn validate:all-yaml               # Validate all YAML files in data/

# Backup system
yarn backup <file_path>              # Create timestamped backup of any file

# Conflict detection  
yarn check:conflicts                 # Find binding conflicts across all systems

# Documentation generation
yarn generate:docs                   # Generate markdown from YAML files
yarn export:csv                      # Export CSV/TSV for analysis

# System status
yarn hooks:status                    # Show hook logs and backup status

# Setup
yarn setup                          # Initialize Python venv and install dependencies
```

### Direct Commands (Alternative)
```bash
# Run full conflict analysis across all systems
CLAUDE_PROJECT_DIR=$PWD keyboard-config/hooks/check-conflicts.py

# Validate specific YAML file
keyboard-config/hooks/validate-yaml.sh keyboard-config/data/horizontal-navigation.yaml

# Create manual backup
keyboard-config/hooks/backup-changes.sh keyboard-config/data/vertical-navigation.yaml

# List all backups
ls -la ~/.claude/hooks/backups/

# Check validation logs
cat ~/.claude/hooks/yaml-validation.log

# Check backup logs
cat ~/.claude/hooks/backup.log
```

### Hook System Status
```bash
# View hook configuration
cat ~/.claude/hooks/keyboard-config-hooks.json

# Check hook logs
tail -f ~/.claude/hooks/conflict-check.log
tail -f ~/.claude/hooks/edit-log.txt
```

**Current Statistics**: 48 total bindings (28 implemented, 19 planned, 1 needs attention), 5 real conflicts detected
**Automation Status**: 5 hooks active, 3 validation scripts, multi-system conflict detection functional, yarn scripts operational  
**Package.json**: Updated with 8 convenient yarn scripts for project automation (validate, backup, conflict detection, documentation generation)
**Testing Results**: All automation systems verified working (YAML validation, timestamped backups, conflict detection across 436 total bindings)
