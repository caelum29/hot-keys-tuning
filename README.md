# Unified Keyboard Productivity Configuration System

A comprehensive keyboard productivity setup that enhances developer workflow across multiple tools using [[HJKL Navigation]] and systematic key binding management through a [[Five-Layer Architecture]].

## 🎯 Overview

This project provides a unified approach to keyboard productivity across:

- **[[Karabiner Config]]** - System-wide keyboard modifications
- **[[IdeaVim Config]]** - Vim emulation for JetBrains IDEs
- **[[WebStorm Keymap]]** - Custom IDE keymap configurations
- **[[Homerow Config]]** - macOS mouse-free UI navigation
- **[[DefaultKeyBinding Config]]** - macOS text system enhancements
- **[[Obsidian Integration]]** - Knowledge management and learning tracking

## 🏗️ Project Structure

```
hot-keys-tuning/
├── 📁 configs/                     # Configuration files
│   ├── karabiner/                  # Karabiner Elements configs
│   ├── idea-vim/                   # IdeaVim configuration
│   ├── webstorm/                   # WebStorm keymap
│   └── macos/                      # macOS system configurations
│
├── 📁 keyboard-config/             # YAML-based binding system
│   ├── data/                       # Source YAML files
│   ├── generated/                  # Auto-generated docs & exports
│   ├── scripts/                    # Generation tools
│   └── hooks/                      # Automation scripts
│
├── 📁 docs/                        # Comprehensive documentation
│   ├── philosophy/                 # Core design principles
│   ├── guides/                     # Implementation guides
│   ├── reference/                  # Reference materials
│   ├── tool-specific/              # Tool-specific docs
│   └── learning-claude-code/       # AI automation guides
│
├── 📁 obsidian-vault/              # Knowledge management
│   ├── notes/                      # Daily logs & observations
│   ├── research/                   # Research & experiments
│   ├── templates/                  # Note templates
│   └── archive/                    # Historical content
│
├── 📁 resources/                   # External resources
└── 📁 temp/                        # Temporary files
```

## ⚡ Quick Start

### 1. Core Philosophy
Read [[PHILOSOPHY-INSP IRATION]] to understand the [[Five-Layer Architecture]] and [[HJKL Navigation]] paradigm.

### 2. Configuration Setup

#### Karabiner Elements
```bash
# Copy configuration
cp configs/karabiner/karabiner.json ~/.config/karabiner/
# Restart Karabiner Elements
```

#### IdeaVim
```bash
# Copy configuration
cp configs/idea-vim/.ideavimrc ~/
# Restart JetBrains IDE
```

#### WebStorm Keymap
1. Open WebStorm → Settings → Keymap
2. Import `configs/webstorm/macOS copy.xml`
3. Set as active keymap

#### macOS Text System
```bash
# Copy configuration
cp configs/macos/DefaultKeyBinding.dict ~/Library/KeyBindings/
# Restart applications for changes to take effect
```

### 3. YAML Configuration System

The project uses a [[YAML Configuration]] system for managing keyboard bindings:

```bash
# Install dependencies
yarn install
yarn setup

# Validate configurations
yarn validate:all-yaml

# Generate documentation
yarn generate:docs

# Export data for analysis
yarn export:csv
```

## 🎹 Key Features

### [[HJKL Navigation]] Paradigm
- **H/L**: Horizontal movement (left/right)
- **J/K**: Vertical movement (down/up)
- **[[Hyper Key Mappings]] (✱)**: Right-side modifier combination (⌘⌥⌃⇧)

### [[Five-Layer Architecture]]
1. **Layer -1**: [[DefaultKeyBinding Config]] (macOS Text System)
2. **Layer 0**: System UI (Full Keyboard Access)
3. **Layer 1**: [[Karabiner Config]] (Hardware)
4. **Layer 2**: [[WebStorm Keymap]] (Application)
5. **Layer 3**: [[IdeaVim Config]] (Editor)

### [[Modifier Combinations]]
- **Base**: Character movement
- **⇧ (Shift)**: Selection/window switching
- **⌃ (Control)**: Desktop management
- **⌥ (Option)**: Word movement/mouse control
- **⌘ (Command)**: Application actions
- **✱ (Hyper)**: System-wide navigation

### 57+ Key Binding Possibilities
Each key supports multiple binding types:
- 16 standard modifier combinations
- 5 hyper key combinations
- 18+ [[Leader Sequences]]
- 5 double tap variations
- 8+ multi-key sequences
- Additional chord and context-aware patterns

## 📊 Current Status

- **124 total bindings** (45 implemented, 71 planned, 7 available, 1 needs attention)
- **6000+ ActionIDs** available for IntelliJ/WebStorm automation
- **95 bindings** with verified ActionIDs
- **Production-ready** IDE automation system

## 🤖 Automation Features

### Claude Code Integration
- **YAML validation** on file edits
- **Automated backups** with timestamps
- **Conflict detection** across all systems
- **Auto-documentation** generation
- **Subagent analysis** for optimization

### MCP Server Integration
- **Context7**: Semantic search and code analysis
- **Obsidian**: Direct vault integration for knowledge management

### Available Scripts
```bash
# Validation
yarn validate:yaml                 # Validate specific YAML
yarn validate:all-yaml            # Validate all YAML files

# Backup & Conflict Detection
yarn backup <file_path>           # Create timestamped backup
yarn check:conflicts             # Find binding conflicts

# Documentation & Export
yarn generate:docs               # Generate markdown from YAML
yarn export:csv                  # Export CSV/TSV for analysis

# System Status
yarn hooks:status                # Show hook logs and backup status
```

## 📚 Documentation

### Essential Reading
1. **[Core Philosophy](PHILOSOPHY-INSP%20IRATION.md)** - 5-layer architecture
2. **[Complete macOS Guide](docs/guides/DEFAULTKEYBINDING-COMPLETE-GUIDE.md)** - 4000+ line implementation guide
3. **[Key Combinations Reference](docs/reference/KEY-BINDING-COMBINATIONS.md)** - All 57+ possibilities
4. **[Claude Code Automation](docs/learning-claude-code/CLAUDE-HOOKS-LEARNING.md)** - AI-assisted workflows

### Quick References
- **[ActionID List](docs/reference/List%20of%20ActionIDs.mhtml)** - 6000+ IntelliJ ActionIDs
- **[HJKL Possibilities](docs/reference/HJKL-MOVEMENT-POSSIBILITIES.md)** - Navigation options
- **[Documentation Index](docs/README.md)** - Complete docs overview

## 🛠️ Development

### Requirements
- macOS (for DefaultKeyBinding.dict and Karabiner)
- Karabiner Elements
- JetBrains IDE (for IdeaVim)
- Node.js & Yarn (for automation scripts)
- Python 3.x (for YAML processing)

### Contributing
1. Edit YAML files in `keyboard-config/data/`
2. Run validation: `yarn validate:all-yaml`
3. Generate docs: `yarn generate:docs`
4. Test configurations across all tools
5. Update learning notes in Obsidian vault

## 🔗 Related Tools

- **[Karabiner Elements](https://karabiner-elements.pqrs.org/)** - macOS keyboard customization
- **[Homerow](https://github.com/nchudleigh/homerow)** - Mouse-free UI navigation
- **[IdeaVim](https://plugins.jetbrains.com/plugin/164-ideavim)** - Vim emulation for JetBrains
- **[Obsidian](https://obsidian.md/)** - Knowledge management system

## 📄 License

This project contains configuration files and documentation for personal keyboard productivity. Use and modify according to your needs.

---

*For detailed implementation guidance, see [`docs/README.md`](docs/README.md)*