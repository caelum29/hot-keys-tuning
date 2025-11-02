# KARABINER-CONFIG

> **System-wide keyboard configuration using Karabiner Elements**

## Overview

Karabiner Elements is the Layer 1 ([[FIVE-LAYER-ARCHITECTURE]]) configuration that provides system-wide vim-like keyboard navigation on macOS.

## Key Concepts

- **[[HYPER-KEY-MAPPINGS]]**: CapsLock as dual-role key (Escape on tap, Hyper on hold)
- **[[HJKL-NAVIGATION]]**: Vim-style directional navigation system-wide
- **16-Plane System**: Hyper + 4 modifiers = 16 unique combinations per key
- **Virtual Keys**: F13-F24 as bridge to [[WEBSTORM-KEYMAP]]

## Configuration Files

### Main Configuration
- **Location**: `configs/karabiner/karabiner-copy.json`
- **Profile**: `super` (main profile)
- **Manipulators**: ~177 after mouse removal (was 302)

### Documentation
- **[[KARABINER-HJKL-REMAPPING-PLAN]]**: Comprehensive 2000+ line plan for removing mouse bindings and adding vim-like enhancements
- **Generated docs**: `configs/karabiner/karabiner_documentation.md` (auto-generated)

## Core Rules

### 1. CapsLock to Hyper (4 manipulators)
- CapsLock held = Hyper (right ⌘⌥⌃⇧)
- CapsLock tapped = Escape
- Hyper+Escape = Toggle CapsLock
- Hyper+Space = Language switch

### 2. Hyper Navigation (70+ manipulators)
The main navigation layer using [[HJKL-NAVIGATION]]:

#### HJKL Core (character movement)
- `Hyper+H/J/K/L` → Arrow keys (←↓↑→)
- `Hyper+Command+H/J/K/L` → Shift+Arrow (selection)
- `Hyper+Shift+H/L` → Tab switching (prev/next)
- `Hyper+Control+H/L` → Desktop switching

#### HJKL Extended (word/paragraph)
- `Hyper+Option+H/L` → Word backward/forward
- `Hyper+Option+J/K` → Paragraph down/up
- `Hyper+Shift+Option+H/J/K/L` → Word/paragraph selection

#### UIOP (line/document)
- `Hyper+U/P` → Page Up/Down
- `Hyper+I/O` → Home/End (line start/end)
- `Hyper+Option+U/P` → Document start/end

### 3. Hyper Deletion (12 manipulators)
- `Hyper+N` → Delete word backward
- `Hyper+M` → Delete char backward
- `Hyper+,` → Delete char forward
- `Hyper+.` → Delete word forward
- With Command modifier: line deletion

### 4. Bracket Keys (4 manipulators)
Virtual keys for tab management:
- `Hyper+[` → F13 (previous tab)
- `Hyper+]` → F14 (next tab)
- `Hyper+Shift+[` → F15 (move tab left)
- `Hyper+Shift+]` → F16 (move tab right)

### 5. Window Management (19 manipulators)
- Window positioning (QWER keys)
- Window resizing
- Display management

### 6. Application Switching (18 manipulators)
- Quick launch favorite apps
- Application toggle shortcuts

### 7. Other Rules
- Clipboard management (20)
- Terminal shortcuts (10)
- Media controls (6)
- Finder shortcuts (12)
- System controls (14)

## Implementation Status

### ✅ Completed
- Core Hyper key implementation
- Basic HJKL navigation (arrows, selection, tabs)
- Deletion cluster
- Window management
- Application switching

### 🚧 In Progress
See [[KARABINER-HJKL-REMAPPING-PLAN]] for detailed implementation phases:
- Removing 125 mouse bindings (Phases 2-9)
- Adding enhanced navigation (Phases 10-12)
- Adding virtual keys (Phases 13-15)

### 📋 Planned
- Complete virtual key allocation (F13-F24)
- WebStorm integration via virtual keys
- YAML configuration system integration

## Integration with Other Layers

### Layer -1: [[DEFAULT-KEY-BINDING-CONFIG]]
- No conflicts (uses Ctrl+HJKL in text fields)
- Karabiner uses Hyper+HJKL system-wide

### Layer 0: [[HOMEROW-CONFIG]]
- Homerow handles ALL mouse control
- Karabiner removed all mouse bindings
- Homerow activated via `Hyper+F`

### Layer 2: [[WEBSTORM-KEYMAP]]
- Consumes F13-F24 virtual keys from Karabiner
- Maps ActionIDs to virtual keys
- Clean separation of concerns

### Layer 3: [[IDEAVIM-CONFIG]]
- No conflicts (different context)
- IdeaVim active in editor pane
- Karabiner active everywhere else

## Foundation: Vonng/Capslock

This configuration is based on [Vonng/Capslock](https://github.com/Vonng/Capslock):
- ✅ Kept: Hyper key concept, HJKL foundation, window management
- 🔄 Modified: Removed all mouse bindings (125 total)
- 🆕 Added: Enhanced vim navigation, virtual keys, 5-layer architecture

See [[KARABINER-HJKL-REMAPPING-PLAN]] Section 10 for complete compatibility analysis.

## Testing & Development

### Testing Individual Bindings
1. Open **Karabiner-EventViewer**
2. Press key combinations
3. Verify expected key events generated

### Testing System-Wide
1. Test in multiple apps (TextEdit, browser, terminal, WebStorm)
2. Verify navigation works consistently
3. Verify no conflicts with app shortcuts

### Backup & Rollback
```bash
# Backup before changes
cp configs/karabiner/karabiner-copy.json \
   configs/karabiner/backups/karabiner-backup-$(date +%Y%m%d-%H%M%S).json

# Rollback if issues
git checkout HEAD -- configs/karabiner/karabiner-copy.json
```

## Related Documentation

- [[KARABINER-HJKL-REMAPPING-PLAN]] - Comprehensive implementation plan
- [[HJKL-NAVIGATION]] - Navigation patterns across all layers
- [[HYPER-KEY-MAPPINGS]] - Hyper key concept and usage
- [[FIVE-LAYER-ARCHITECTURE]] - Complete architecture philosophy
- [[HOMEROW-CONFIG]] - Mouse control (Layer 0)
- [[WEBSTORM-KEYMAP]] - IDE integration (Layer 2)
- [[IDEAVIM-CONFIG]] - Vim emulation (Layer 3)
- [[PHILOSOPHY-INSPIRATION]] - Core design principles

## Statistics

- **Total Manipulators**: ~177 (after mouse removal)
- **Removed**: 125 mouse bindings (41% reduction)
- **Added**: 44 new vim navigation bindings
- **Virtual Keys**: 12 allocated (F13-F24)
- **Active Profile**: `super`

---

**Last Updated**: 2025-02-11  
**Status**: Active configuration with ongoing enhancements