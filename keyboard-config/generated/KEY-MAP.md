# Keyboard Navigation Configuration

Generated from YAML configuration data. **DO NOT EDIT MANUALLY** - changes will be overwritten.

This document provides comprehensive keyboard binding documentation for the unified productivity system.

- For **horizontal navigation**, **H** corresponds to moving left and **L** corresponds to moving right.
- For **vertical navigation**, **J** corresponds to moving down and **K** corresponds to moving up.

## Legend

### Systems
- **I**: IdeaVim (editor-level vim emulation)
- **W**: WebStorm (IDE-level keymaps)
- **K**: Karabiner Elements (system-wide key modifications)
- Combinations indicate multi-system bindings

### Status Icons
- ✅ **Implemented**: Fully configured and working
- 📋 **Planned**: Identified for future implementation
- ⚠️ **Needs Attention**: Requires fixes or remapping
- ❌ **Disabled**: Intentionally disabled
- ⚡ **Conflict**: Conflicts with other bindings

---

## Implementation Summary

### Status Overview
| Status | Count | Percentage |
|--------|-------|------------|
| ✅ Implemented | 28 | 58.3% |
| ⚠️ Needs_Attention | 1 | 2.1% |
| 📋 Planned | 19 | 39.6% |

### System Distribution
| System | Count | Description |
|--------|-------|-------------|
| - | 15 | Not implemented |
| I | 8 | IdeaVim only |
| K | 8 | Karabiner only |
| W | 16 | WebStorm only |
| W+I | 1 | WebStorm + IdeaVim |

## Horizontal Navigation Key Bindings (H / L)

**Navigation Type**: Horizontal  
**Keys**: H, L  
**Description**: Left/right navigation and related actions

| Modifier | Keystroke | System | Status | Category | Action | IDE Action ID | Karabiner Code | IdeaVim Command | Config Reference |
|----------|-----------|---------|---------|----------|---------|---------------|----------------|-----------------|------------------|
| None | H / L | I | ✅ | Navigation | Previous/Next bookmark | `BookmarksAction` | `h/l` | `]'/'[` | .ideavimrc:L120 |
| Shift | ⇧H / ⇧L | W | ✅ | Selection | Navigate to prev/next bookmark | `SelectPreviousTab/SelectNextTab` | `shift+h/l` | `:action SelectPreviousTab` | keymap.xml:L56 |
| Ctrl | ⌃H / ⌃L | W+I | ✅ | Text Edit | Editor join lines/Custom | `EditorJoinLines` | `ctrl+h/l` | `J` | keymap.xml:L33 |
| Alt | ⌥H / ⌥L | W | ✅ | Navigation | Move caret to prev/next word | `EditorPreviousWord/EditorNextWord` | `alt+h/l` | `nnoremap <A-h> b` | keymap.xml:L48 |
| Cmd | ⌘H / ⌘L | W | ✅ | Action | Custom action/Complete statement | `EditorCompleteStatement` | `cmd+h/l` | - | keymap.xml:L24 |
| Shift Ctrl | ⇧⌃H / ⇧⌃L | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+h/l` | - | - |
| Shift Alt | ⇧⌥H / ⇧⌥L | W | ✅ | Selection | Prev/Next word with selection | `EditorPreviousWordWithSelection` | `shift+alt+h/l` | - | keymap.xml:L55 |
| Shift Cmd | ⇧⌘H / ⇧⌘L | W | ✅ | Window | Select prev/next tab | `SelectPreviousTab/SelectNextTab` | `shift+cmd+h/l` | `:action SelectPreviousTab` | keymap.xml:L56 |
| Ctrl Alt | ⌃⌥H / ⌃⌥L | - | 📋 | Custom | Custom action | `Custom` | `ctrl+alt+h/l` | - | - |
| Ctrl Cmd | ⌃⌘H / ⌃⌘L | - | 📋 | Custom | Custom action | `Custom` | `ctrl+cmd+h/l` | - | - |
| Alt Cmd | ⌥⌘H / ⌥⌘L | W | ✅ | Action | Custom action/Reformat code | `ReformatCode` | `alt+cmd+h/l` | - | keymap.xml:L59 |
| Shift Ctrl Alt | ⇧⌃⌥H / ⇧⌃⌥L | W | ✅ | Window | Stretch split left/right | `StretchSplitToLeft/StretchSplitToRight` | `shift+ctrl+alt+h/l` | - | keymap.xml:L60 |
| Shift Ctrl Cmd | ⇧⌃⌘H / ⇧⌃⌘L | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+cmd+h/l` | - | - |
| Shift Alt Cmd | ⇧⌥⌘H / ⇧⌥⌘L | W | ✅ | Action | Popup hector/Reformat dialog | `PopupHector/ShowReformatFileDialog` | `shift+alt+cmd+h/l` | - | keymap.xml:L62 |
| Ctrl Alt Cmd | ⌃⌥⌘H / ⌃⌥⌘L | - | 📋 | Custom | Custom action | `Custom` | `ctrl+alt+cmd+h/l` | - | - |
| Shift Ctrl Alt Cmd | ⇧⌃⌥⌘H / ⇧⌃⌥⌘L | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+alt+cmd+h/l` | - | - |
| Hyper | ✱H / ✱L | K | ✅ | Navigation | Move left/right one char | `left_arrow/right_arrow` | `right_shift+right_ctrl+right_alt+right_cmd+h/l` | - | karabiner.json:L65 |
| Hyper Shift | ✱⇧H / ✱⇧L | K | 📋 | Selection | Tab switching | `SelectPreviousTab` | `-` | - | - |
| Hyper Ctrl | ✱⌃H / ✱⌃L | K | ✅ | Desktop | Prev/next desktop | `left_control+left_arrow` | `-` | - | karabiner.json:L67 |
| Hyper Alt | ✱⌥H / ✱⌥L | K | ⚠️ | Mouse | Need to remap | `mouse_move` | `-` | - | - |
| Hyper Cmd | ✱⌘H / ✱⌘L | W | ✅ | Window | App switcher | `Switcher` | `-` | - | keymap.xml:L69 |
| G Prefix | GH / GL | I | ✅ | Navigation | Move to line beginning/end | `EditorLineStart/EditorLineEnd` | `-` | `0/$` | .ideavimrc:L81 |
| Change Camel | cH / cL | I | ✅ | Text Edit | Change camel hump back/forward | `CamelHumpAction` | `-` | `cb/cw` | .ideavimrc:L82 |
| Delete Camel | dH / dL | I | ✅ | Text Edit | Delete camel hump back/forward | `CamelHumpAction` | `-` | `db/dw` | .ideavimrc:L83 |
| Inner Camel | cih / dih | I | ✅ | Text Edit | Change/delete inner camel hump | `CamelHumpAction` | `-` | `ciw/diw` | .ideavimrc:L84 |
| Scroll Horizontal | zH / zL | I | ✅ | Navigation | Scroll left/right 50 chars | `ScrollAction` | `-` | `zh/zl` | .ideavimrc:L85 |

## Vertical Navigation Key Bindings (J / K)

**Navigation Type**: Vertical  
**Keys**: J, K  
**Description**: Up/down navigation and related actions

| Modifier | Keystroke | System | Status | Category | Action | IDE Action ID | Karabiner Code | IdeaVim Command | Config Reference |
|----------|-----------|---------|---------|----------|---------|---------------|----------------|-----------------|------------------|
| None | J / K | I | ✅ | Text Edit | Join lines/Visual selection | `EditorJoinLines` | `j/k` | `J/<C-v>k` | .ideavimrc:L91 |
| Shift | ⇧J / ⇧K | W | ✅ | Selection | Extend selection down/up | `EditorDownWithSelection/EditorUpWithSelection` | `shift+j/k` | `vj/vk` | keymap.xml:L92 |
| Ctrl | ⌃J / ⌃K | W | ✅ | Action | Custom action/Show navbar | `ShowNavBar` | `ctrl+j/k` | - | keymap.xml:L93 |
| Alt | ⌥J / ⌥K | W | ✅ | Text Edit | Clone caret below/above | `EditorCloneCaretBelow/EditorCloneCaretAbove` | `alt+j/k` | - | keymap.xml:L18 |
| Cmd | ⌘J / ⌘K | W | ✅ | Action | Insert live template/Custom | `InsertLiveTemplate` | `cmd+j/k` | - | keymap.xml:L95 |
| Shift Ctrl | ⇧⌃J / ⇧⌃K | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+j/k` | - | - |
| Shift Alt | ⇧⌥J / ⇧⌥K | - | 📋 | Custom | Special char | `Special` | `shift+alt+j/k` | - | - |
| Shift Cmd | ⇧⌘J / ⇧⌘K | W | ✅ | Action | Editor join lines/VCS push | `EditorJoinLines/Vcs.Push` | `shift+cmd+j/k` | - | keymap.xml:L98 |
| Ctrl Alt | ⌃⌥J / ⌃⌥K | W | ✅ | Text Edit | Move line down/up | `MoveLineDown/MoveLineUp` | `ctrl+alt+j/k` | - | keymap.xml:L99 |
| Ctrl Cmd | ⌃⌘J / ⌃⌘K | - | 📋 | Custom | Custom action | `Custom` | `ctrl+cmd+j/k` | - | - |
| Alt Cmd | ⌥⌘J / ⌥⌘K | W | ✅ | Action | Surround with template/Custom | `SurroundWithLiveTemplate` | `alt+cmd+j/k` | - | keymap.xml:L101 |
| Shift Ctrl Alt | ⇧⌃⌥J / ⇧⌃⌥K | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+alt+j/k` | - | - |
| Shift Ctrl Cmd | ⇧⌃⌘J / ⇧⌃⌘K | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+cmd+j/k` | - | - |
| Shift Alt Cmd | ⇧⌥⌘J / ⇧⌥⌘K | - | 📋 | Custom | Custom action | `Custom` | `shift+alt+cmd+j/k` | - | - |
| Ctrl Alt Cmd | ⌃⌥⌘J / ⌃⌥⌘K | - | 📋 | Custom | Custom action | `Custom` | `ctrl+alt+cmd+j/k` | - | - |
| Shift Ctrl Alt Cmd | ⇧⌃⌥⌘J / ⇧⌃⌥⌘K | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+alt+cmd+j/k` | - | - |
| Hyper | ✱J / ✱K | K | ✅ | Navigation | Move down/up one line | `down_arrow/up_arrow` | `right_shift+right_ctrl+right_alt+right_cmd+j/k` | - | karabiner.json:L107 |
| Hyper Shift | ✱⇧J / ✱⇧K | K | 📋 | Navigation | App switching | `AppSwitcher` | `-` | - | - |
| Hyper Ctrl | ✱⌃J / ✱⌃K | K | 📋 | Desktop | Focus/expose | `MissionControl` | `-` | - | - |
| Hyper Alt | ✱⌥J / ✱⌥K | K | 📋 | Mouse | Mouse move | `mouse_move` | `-` | - | - |
| Hyper Cmd | ✱⌘J / ✱⌘K | - | 📋 | Custom | Custom action | `Custom` | `-` | - | - |
| G Prefix | GJ / GK | I | ✅ | Navigation | Navigate prev/next method | `MethodUp/MethodDown` | `-` | `[m/]m` | .ideavimrc:L123 |

---

*Generated automatically from YAML configuration data.*
*Source files: `horizontal-navigation.yaml`, `vertical-navigation.yaml`*