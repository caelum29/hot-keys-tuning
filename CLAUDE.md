# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a unified keyboard productivity configuration system that enhances developer workflow across multiple tools:

- **[[KARABINER-CONFIG]]**: System-wide keyboard modifications and complex key mappings
- **[[IDEAVIM-CONFIG]]**: Vim emulation for JetBrains IDEs with custom keybindings
- **[[WEBSTORM-KEYMAP]]**: Custom keymap configurations for IDE productivity
- **[[HOMEROW-CONFIG]]**: macOS keyboard navigation tool for mouse-free UI interaction with [[HJKL-NAVIGATION]] scrolling and dynamic element labeling
- **[[OBSIDIAN-INTEGRATION]]**: Knowledge management system for tracking keyboard learning journey, binding documentation, and workflow optimization
- **Documentation**: Comprehensive guides for keyboard navigation and productivity patterns
- **[[PHILOSOPHY-INSPIRATION]]**: Core design principles and systematic approach to keyboard productivity integration
- **[[DEFAULT-KEY-BINDING-CONFIG]]**: macOS text system configuration for universal [[HJKL-NAVIGATION]]

## Architecture

### Core Components

- `configs/karabiner/` - Karabiner Elements configuration files
  - `karabiner.json` - Main configuration with complex modifications, dual-role keys, and navigation mappings
  - `dual_role_keys.json` - Specialized dual-role key configurations
  - `downloaded/vim.json` - Vim-style navigation rules
- `configs/idea-vim/.ideavimrc` - IdeaVim configuration with 300+ lines of custom mappings
- `configs/webstorm/macOS copy.xml` - WebStorm keymap with HJKL navigation integration
- `docs/` - Extensive documentation on keyboard productivity patterns
  - `philosophy/PHILOSOPHY-INSPIRATION.md` - **UPDATED: 5-layer architecture with DefaultKeyBinding.dict integration**
  - `guides/DEFAULTKEYBINDING-COMPLETE-GUIDE.md` - **NEW: Comprehensive 4000+ line guide to macOS text system mastery**
  - `reference/KEY-BINDING-COMBINATIONS.md` - Complete reference of all 57+ possible key binding combinations for a single key
  - `learning-claude-code/` - Claude Code automation and learning materials
    - `CLAUDE-HOOKS-LEARNING.md` - Comprehensive guide for Claude Code hooks and subagents
    - `CLAUDE-CODE-GUIDE.md` - Complete Claude Code feature reference and tutorial
    - `TEST-HOOKS-DEMO.md` - Demonstration results of hooks and subagents implementation
- `keyboard-config/` - **NEW: YAML-based configuration system with ActionID integration**
  - `data/` - Source YAML files (single source of truth for all bindings)
    - `horizontal-navigation.yaml` - H/L key bindings with IntelliJ ActionIDs, technical details, and planned action descriptions
    - `vertical-navigation.yaml` - J/K key bindings with IntelliJ ActionIDs, structured data, and planned action descriptions
    - `schemas/binding-schema.yaml` - Validation rules for data consistency including ActionID support
  - `generated/` - Auto-generated documentation and exports
    - `KEY-MAP.md` - Enhanced markdown tables with ActionIDs displayed prominently in bold
    - `bindings.csv` - Full dataset with ActionID column for spreadsheet analysis
    - `bindings-summary.csv` - Statistics breakdown
    - `bindings-pivot.csv` - Pivot table ready format with ActionID integration
  - `scripts/` - Generation and export tools
    - `generate-docs.py` - YAML → Markdown converter with ActionID display support
    - `export-csv.py` - YAML → Multiple CSV formats including ActionID columns
  - `hooks/` - **NEW: Automation and validation scripts**
    - `validate-yaml.sh` - YAML syntax and schema validation with virtual environment
    - `backup-changes.sh` - Automated backup system with timestamped versions
    - `check-conflicts.py` - Multi-system conflict detection (Karabiner + IdeaVim + WebStorm)
  - `hjkl-actionid-mapping.yaml` - Comprehensive ActionID reference mapping for HJKL navigation
- `configs/macos/DefaultKeyBinding.dict` - **NEW: macOS text system configuration with vim-style HJKL navigation**
- `docs/reference/List of ActionIDs.mhtml` - IntelliJ 2024.2.3 official ActionID reference (6000+ entries)

### Key Concepts

**Navigation Philosophy**: Uses [[HJKL-NAVIGATION]] keys (borrowed from Vim) as primary navigation with modifier combinations:
- H/L for horizontal movement (left/right)
- J/K for vertical movement (down/up)
- [[HYPER-KEY-MAPPINGS]] (✱) implemented as right-side modifier combination (⌘⌥⌃⇧)

**[[MODIFIER-COMBINATIONS]]**: Multiple modifier combinations create different navigation modes:
- Base: Character movement
- ⇧ (Shift): Selection/window switching
- ⌃ (Control): Desktop management
- ⌥ (Option): Word movement/mouse control
- ⌘ (Command): Application actions
- ✱ (Hyper): System-wide navigation layer

**[[FIVE-LAYER-ARCHITECTURE]]**: Consistent keybindings across 5 layers:
- **Layer -1**: [[DEFAULT-KEY-BINDING-CONFIG]] (macOS Text System)
- **Layer 0**: System UI (Full Keyboard Access)
- **Layer 1**: [[KARABINER-CONFIG]] (Hardware)
- **Layer 2**: [[WEBSTORM-KEYMAP]] (Application)
- **Layer 3**: [[IDEAVIM-CONFIG]] (Editor)
- UI navigation ([[HOMEROW-CONFIG]] with [[HJKL-NAVIGATION]] scrolling and [[HYPER-KEY-MAPPINGS]] activation)

**Combination Possibilities**: Each single key supports 57+ unique binding combinations:
- 16 standard modifier combinations (⇧⌃⌥⌘)
- 5 hyper key combinations (✱ with modifiers)
- 18+ [[LEADER-SEQUENCES]] (Vim-style prefixes)
- 5 double tap variations (timing-based)
- 8+ multi-key sequences (text objects)
- Additional chord, long press, and context-aware patterns
- See `docs/reference/KEY-BINDING-COMBINATIONS.md` for complete reference

**ActionID Integration**: Production-ready IntelliJ/WebStorm integration:
- **6000+ ActionIDs**: Official IntelliJ 2024.2.3 ActionID reference in `docs/reference/List of ActionIDs.mhtml`
- **Verified mappings**: All navigation ActionIDs validated against official list (e.g., `EditorLeft/EditorRight`, `EditorDownWithSelection`)
- **Comprehensive coverage**: 95 bindings with specific ActionIDs for navigation, selection, text editing, window management
- **Ready for automation**: ActionIDs enable automatic keymap.xml generation and IDE configuration
- **HJKL reference**: `hjkl-actionid-mapping.yaml` provides complete mapping reference for horizontal/vertical navigation

## Development Workflow

This project doesn't have traditional build/test commands as it consists primarily of configuration files. Key operations:

### Karabiner Configuration
- Edit `configs/karabiner/karabiner.json` for complex modifications
- Use Karabiner Elements GUI to import/export configurations
- Test modifications require Karabiner Elements restart

### IdeaVim Configuration  
- Edit `configs/idea-vim/.ideavimrc`
- Reload with `:source ~/.ideavimrc` in IDE
- Test mappings directly in JetBrains IDEs

### WebStorm Keymap
- Import `configs/webstorm/macOS copy.xml` through WebStorm settings
- Modifications require IDE restart to take effect

### Homerow Configuration
- Download and install from https://github.com/nchudleigh/homerow
- Activate with `Hypher+F` (default) or configure Hyper key activation
- Uses HJKL for scrolling (consistent with Vim navigation philosophy)
- Provides mouse-free UI interaction with dynamic element labeling
- Supports search, click, scroll, and keyboard navigation workflows

### DefaultKeyBinding.dict Configuration
- Edit `configs/macos/DefaultKeyBinding.dict` for macOS text system modifications
- Install to `~/Library/KeyBindings/DefaultKeyBinding.dict` for system-wide effect
- Restart applications for changes to take effect
- See `docs/guides/DEFAULTKEYBINDING-COMPLETE-GUIDE.md` for comprehensive implementation

### Documentation
- Markdown files in `docs/` provide implementation guides
- README.md contains the master navigation reference table
- **docs/philosophy/PHILOSOPHY-INSPIRATION.md**: Core design principles, 5-layer architecture, and systematic keyboard productivity approach
- **docs/guides/DEFAULTKEYBINDING-COMPLETE-GUIDE.md**: Complete macOS text system mastery guide

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
- Maintain consistency across all 5 layers: DefaultKeyBinding.dict, Full Keyboard Access, Karabiner, Applications, and IdeaVim
- Follow the [[HJKL-NAVIGATION]] paradigm established throughout
- Test changes across all systems (macOS text system, System UI, Hardware, Apps, Editor)
- Document any new key combinations in README.md tables
- Use descriptive names in Karabiner rule descriptions for maintainability
- Consider integration between DefaultKeyBinding.dict (text fields) and other layers

## Documentation Standards

**File Creation and Naming**:
- **MANDATORY**: All markdown documentation files MUST use CAPS_LOCK.md naming style with hyphens between words (e.g., `PHILOSOPHY.md`, `KEYBOARD-ARCHITECTURE.md`, `BINDING-CONFLICTS.md`)
- Place new documentation in appropriate directories: `docs/` for main docs, `obsidian-vault/` for vault-specific content
- **ALWAYS use [[CAPS-LOCK-WITH-HYPHENS]] format for all wikilinks**
- Reference documents with wikilinks: [[PHILOSOPHY]] or [[KEYBOARD-ARCHITECTURE]]
- **NO EXCEPTIONS**: CamelCase or mixed case file names are not allowed

**Obsidian Integration**:
- **ALWAYS use Obsidian MCP tools for searching markdown files** instead of grep/find commands
- Use `obsidian_search_notes` to find existing documentation before creating new files
- Use `obsidian_read_notes` to read multiple markdown files for research
- **MANDATORY**: Create wikilinks using `[[CAPS-LOCK-WITH-HYPHENS]]` format (e.g., `[[KEYBOARD-PRODUCTIVITY]]`, `[[NAVIGATION-PATTERNS]]`)
- All new markdown files should integrate into the Obsidian knowledge graph
- **ENFORCE**: All wikilinks must use CAPS_LOCK naming with hyphens, no CamelCase allowed

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
- **Use Obsidian MCP first**: Always search existing documentation with `obsidian_search_notes` before creating new files
- **YAML for data**: YAML provides clear structure for all binding details (action IDs, key codes, config references, planned descriptions)
- **Obsidian for research**: Use `obsidian_read_notes` to read multiple documentation files for comprehensive research
- **Wikilinks for connections**: Create [[wikilinks]] to integrate new content into the knowledge graph
- **Schema validation**: Ensures consistency and prevents errors
- **Single source of truth**: Eliminates documentation drift and duplication

### Data Structure Benefits:
- **Obsidian Integration**: All markdown files discoverable through Obsidian graph and search
- **Parsing**: YAML is much easier for LLMs to understand than complex markdown tables
- **Editing**: Structured format prevents column alignment and formatting errors
- **Validation**: Schema catches missing fields and invalid values
- **Extensibility**: Can easily add new fields or binding types
- **Knowledge Graph**: Wikilinks create discoverable relationships between concepts

### Claude Code Learning Resources (NEW)
- **`docs/learning-claude-code/CLAUDE-HOOKS-LEARNING.md`**: Complete 350+ line guide covering hooks fundamentals, practical examples, subagent usage, security practices, and troubleshooting
- **`docs/learning-claude-code/CLAUDE-CODE-GUIDE.md`**: Comprehensive feature reference with project-specific examples
- **`docs/learning-claude-code/TEST-HOOKS-DEMO.md`**: Results and demonstration of implemented automation systems

## Model Context Protocol (MCP) Integration

This project integrates with Claude Code through **Model Context Protocol (MCP)** servers for enhanced AI-assisted development and knowledge management.

### MCP Servers Configured

#### 1. **Context7 MCP Server** (Upstash)
- **Purpose**: Advanced context management and code analysis with semantic search
- **Provider**: Upstash (https://context7.com)
- **Configuration**: Cloud-hosted service with API key authentication
- **Features**:
  - Semantic search across keyboard configuration files
  - Context windows for navigation patterns
  - Code indexing for YAML, JSON, XML, and Vim files

#### 2. **Obsidian MCP Server** (@kazuph/mcp-obsidian) - **PRIMARY FOR MARKDOWN WORK**
- **Purpose**: Direct integration with Obsidian vault for knowledge management
- **Package**: `@kazuph/mcp-obsidian@1.0.2`
- **Configuration**: Local vault access pointing to current project directory
- **REQUIRED USAGE**: Always use this for markdown file search and research instead of grep/find
- **Features**:
  - Read/write access to all markdown notes
  - Full-text search across vault (`obsidian_search_notes`)
  - Note creation and management (`obsidian_write_note`)
  - Multi-file reading (`obsidian_read_notes`)
  - Tag and frontmatter handling
  - Wikilink resolution and graph integration

### Setup Instructions

#### Context7 Setup
1. **Get API Key**: Visit https://context7.com/dashboard to obtain your API key
2. **Update Configuration**: Replace `YOUR_API_KEY_HERE` in `claude.json` with your actual API key
3. **Verification**: Context7 automatically indexes project files upon connection

#### Obsidian Setup
1. **Package Installation**: Already installed via `yarn add @kazuph/mcp-obsidian`
2. **Vault Path**: Pre-configured to current project directory
3. **Permissions**: MCP server has read/write access to all markdown files
4. **Verification**: Test with `yarn mcp:test`

### Available MCP Scripts

```bash
# Test Obsidian MCP server
yarn mcp:test

# Run Obsidian MCP with explicit vault path
yarn mcp:obsidian

# View current MCP configuration
yarn mcp:config
```

### Integration Benefits

#### For Claude Code Development
- **Context7**: Enhanced understanding of keyboard configuration relationships
- **Obsidian**: Direct note creation for learning logs and documentation updates
- **Combined**: Comprehensive project knowledge and automated documentation workflows

#### For Knowledge Management
- **Automated Documentation**: MCP servers enable automatic updates to learning notes
- **Semantic Search**: Find related keyboard patterns and configurations instantly
- **Cross-Reference**: Link keyboard configurations with usage documentation
- **Learning Tracking**: Maintain vault-based learning progress and effectiveness metrics

### **Obsidian MCP Workflow (REQUIRED)**

#### Before Creating Any Markdown File:
1. **Search First**: Use `obsidian_search_notes` to find existing related documentation
2. **Research Context**: Use `obsidian_read_notes` to read multiple related files for context
3. **Check Naming**: Follow CAPS_LOCK.md naming convention (e.g., `KEYBOARD_SHORTCUTS.md`)
4. **Plan Integration**: Identify which existing files need [[wikilinks]] to the new content

#### When Writing Documentation:
1. **Create with MCP**: Use `obsidian_write_note` instead of Write tool for markdown files
2. **Add Wikilinks**: Include [[CAPS-LOCK-WITH-HYPHENS]] wikilinks to related concepts and files
3. **Use Frontmatter**: Include created, modified, tags, and aliases fields
4. **Reference Integration**: Update index files ([[INDEX]], [[CONFIGS]], [[WORKFLOWS]]) with links to new content
5. **Naming Enforcement**: ALL file names must be CAPS_LOCK.md with hyphens (e.g., `ADVANCED-NAVIGATION.md`)

#### Research and Analysis Workflow:
1. **Never use grep/find for markdown**: Always use `obsidian_search_notes` for searching documentation
2. **Multi-file research**: Use `obsidian_read_notes` with array of paths for comprehensive research
3. **Follow the graph**: Use existing wikilinks to discover related documentation
4. **Maintain connections**: Ensure new content integrates into the existing knowledge graph

### Security Considerations

- **Context7**: Cloud-hosted with API key authentication (no local file access)
- **Obsidian**: Local server with full vault read/write permissions
- **Backup**: Always backup vault before using MCP servers (they're in active development)
- **Git**: Recommended for version control of all configuration changes

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

**Current Statistics**: 124 total bindings (45 implemented, 71 planned, 7 available, 1 needs attention), ActionID integration complete, planned action descriptions complete
**ActionID Status**: 6000+ official IntelliJ ActionIDs available, 95 bindings with verified ActionIDs, production-ready for IDE automation  
**Automation Status**: 5 hooks active, 3 validation scripts, multi-system conflict detection functional, yarn scripts operational  
**Package.json**: Updated with 8 convenient yarn scripts for project automation (validate, backup, conflict detection, documentation generation)
**Testing Results**: All automation systems verified working (YAML validation, timestamped backups, ActionID integration, CSV exports functional)

## Obsidian Integration

This vault serves as both a configuration repository and knowledge management system for keyboard productivity learning.

**Obsidian Vault Guidelines:**
- All notes are Markdown files (.md) with capslock naming
- Use [[wikilinks]] for internal connections between configuration topics
- Tag system based on TAGS.md for consistent categorization
- Frontmatter YAML for metadata and automated organization
- Preserve existing link formats when editing notes
- Internal embeds with ![[NOTE-NAME]] for referencing configuration examples

**Note Organization:**
- `obsidian-vault/notes/` - Daily logs and general observations
- `obsidian-vault/research/` - Keyboard research and experiments
- `obsidian-vault/templates/` - Reusable note structures
- `obsidian-vault/archive/` - Old configurations and deprecated bindings

**Tagging Strategy:**
- Always reference obsidian-vault/TAGS.md for consistent tag hierarchy
- Use keyboard-specific tags: #keyboard/tool, #binding/type, #workflow/category
- Tag new discoveries and learning progress
- Link configuration changes to learning notes

**Knowledge Base Integration:**
- Connect keyboard configurations with usage documentation
- Track learning progress and binding effectiveness over time
- Document conflict resolutions and optimization decisions
- Maintain wiki-style connections between related concepts
