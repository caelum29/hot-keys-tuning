---
created: 2025-01-20
modified: 2025-01-20
tags: [#index/configs, #configuration/all]
aliases: [Configuration Index, Config Hub, Setup Guide]
---

# Configuration Index

Links to all configuration documentation and setup guides.

## 🛠️ Primary Configuration Files

### Layer-Based Configuration
- **Layer -1**: [[DEFAULT-KEY-BINDING-CONFIG]] - macOS text system (configs/macos/)
- **Layer 0**: System UI (Full Keyboard Access integration)
- **Layer 1**: [[KARABINER-CONFIG]] - Hardware modifications (configs/karabiner/)
- **Layer 2**: [[WEBSTORM-KEYMAP]] - Application layer (configs/webstorm/)
- **Layer 3**: [[IDEAVIM-CONFIG]] - Editor layer (configs/idea-vim/)

### Supplementary Tools
- [[HOMEROW-CONFIG]] - Mouse-free UI navigation
- [[OBSIDIAN-INTEGRATION]] - Knowledge management integration

## 📁 Configuration File Locations

### Active Configuration Files
```
configs/
├── karabiner/
│   ├── karabiner.json           # Main Karabiner configuration
│   ├── dual_role_keys.json      # Dual-role key behaviors
│   └── downloaded/vim.json      # Vim navigation rules
├── idea-vim/
│   └── .ideavimrc              # IdeaVim configuration (300+ lines)
├── webstorm/
│   └── macOS copy.xml          # WebStorm keymap
└── macos/
    ├── DefaultKeyBinding.dict  # macOS text system
    └── StandardKeyBinding.xml  # Reference file
```

## ⚙️ Configuration Categories

### Core Navigation Patterns
- [[HJKL-NAVIGATION]] - Universal movement patterns
- [[MODIFIER-COMBINATIONS]] - Enhanced navigation modes
- [[HYPER-KEY-MAPPINGS]] - System-wide access layer
- [[LEADER-SEQUENCES]] - Multi-step workflows

### System Integration
- [[FIVE-LAYER-ARCHITECTURE]] - Complete integration strategy
- [[DUAL-ROLE-KEYS]] - Context-dependent behaviors
- [[WINDOW-MANAGEMENT]] - Window and pane control
- [[ACTIONID-REFERENCE]] - IDE automation integration

## 📊 Configuration Management

### YAML-Based System
- [[YAML-CONFIGURATION]] - Structured configuration management
- keyboard-config/data/*.yaml - Source configuration files
- keyboard-config/generated/ - Auto-generated documentation
- keyboard-config/scripts/ - Generation and validation tools

### Automation & Validation
- [[HOOK-AUTOMATION]] - Automated configuration validation
- [[CONFLICT-DETECTION]] - Multi-system conflict analysis
- [[CLAUDE-CODE-HOOKS]] - AI-assisted configuration management
- yarn scripts - Convenient automation commands

## 📚 Setup Documentation

### Implementation Guides
- docs/guides/[[DEFAULTKEYBINDING-COMPLETE-GUIDE]] - macOS text system (4000+ lines)
- docs/guides/[[UNIFIED-KEYBOARD-PRODUCTIVITY-MASTER-GUIDE]] - Complete system
- docs/reference/[[KEY-BINDING-COMBINATIONS]] - All 57+ possibilities

### Quick Setup
1. **Copy configurations** to appropriate system locations
2. **Restart applications** to activate changes
3. **Validate setup** using [[CONFLICT-DETECTION]]
4. **Learn patterns** starting with [[HJKL-NAVIGATION]]

## 🔧 Maintenance & Updates

### Regular Tasks
- **Backup configurations** before changes
- **Validate YAML** after modifications
- **Check conflicts** across all systems
- **Update documentation** when adding bindings

### Development Workflow
- **Edit YAML** sources in keyboard-config/data/
- **Generate docs** using yarn scripts
- **Test changes** across all layers
- **Commit updates** to version control

## 🔗 Related Resources

### Hub Navigation
- [[INDEX]] - Main system index
- [[WORKFLOWS]] - Workflow pattern index
- [[ORGANIZATION]] - Vault organization
- [[WIKI_LINKS]] - Linking conventions

### Technical Documentation
- [[ACTIONID-REFERENCE]] - Complete IDE action reference
- [[CONFLICT-DETECTION]] - Multi-system analysis
- [[YAML-CONFIGURATION]] - Structured data management
- [[HOOK-AUTOMATION]] - Automation system details

---

**Quick Access**: [[KARABINER-CONFIG]] | [[IDEAVIM-CONFIG]] | [[WEBSTORM-KEYMAP]] | [[DEFAULT-KEY-BINDING-CONFIG]]