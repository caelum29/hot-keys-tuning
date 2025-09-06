# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a unified keyboard productivity configuration system that enhances developer workflow across multiple tools:

- **Karabiner Elements**: System-wide keyboard modifications and complex key mappings
- **IdeaVim**: Vim emulation for JetBrains IDEs with custom keybindings  
- **WebStorm**: Custom keymap configurations for IDE productivity
- **Documentation**: Comprehensive guides for keyboard navigation and productivity patterns

## Architecture

### Core Components

- `src/karabiner/` - Karabiner Elements configuration files
  - `karabiner.json` - Main configuration with complex modifications, dual-role keys, and navigation mappings
  - `dual_role_keys.json` - Specialized dual-role key configurations
  - `downloaded/vim.json` - Vim-style navigation rules
- `src/idea-vim/.ideavimrc` - IdeaVim configuration with 300+ lines of custom mappings
- `src/webstorm-keymap/macOS copy.xml` - WebStorm keymap with HJKL navigation integration
- `src/docs/` - Extensive documentation on keyboard productivity patterns

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