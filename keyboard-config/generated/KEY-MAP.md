# Keyboard Configuration System

Generated from YAML configuration data. **DO NOT EDIT MANUALLY** - changes will be overwritten.

This document provides comprehensive keyboard binding documentation for all configured keys in the unified productivity system.

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

### Category Icons
- ⏱️ **Timing**: Double tap, long press, tap/hold patterns
- 🎹 **Chord**: Multiple keys pressed simultaneously
- 👑 **Leader**: Leader key prefix sequences
- 🔗 **Sequence**: Multi-step key sequences
- 🧭 **Navigation**: Movement and positioning
- ✏️ **Selection**: Text and object selection
- 📝 **Text Edit**: Text manipulation and editing
- 🪟 **Window**: Window and pane management
- 🖥️ **Desktop**: Desktop and workspace control
- ⚙️ **Action**: IDE actions and commands
- 🎛️ **Custom**: Custom or unspecified actions
- 🖱️ **Mouse**: Mouse-related operations

### Field Indicators
- ⏱️500ms: Timing window (double tap/long press)
- 🔗double_tap: Sequence type
- 🎹H+J: Chord keys combination
- 👆hold: Press type requirement

---

## Implementation Summary

### Configuration Overview
| Navigation Type | Bindings | Description |
|----------------|----------|-------------|
| Bracket | 14 | Previous/next navigation with brackets |
| Horizontal | 48 | Left/right navigation (H/L keys) |
| Individual | 14 | Single key bindings |
| Vertical | 47 | Up/down navigation (J/K keys) |

### Status Overview
| Status | Count | Percentage |
|--------|-------|------------|
| ✅ Implemented | 44 | 35.8% |
| ⚠️ Needs_Attention | 1 | 0.8% |
| 📋 Planned | 78 | 63.4% |

### System Distribution
| System | Count | Description |
|--------|-------|-------------|
| - | 44 | Not implemented |
| I | 40 | IdeaVim only |
| K | 14 | Karabiner only |
| W | 23 | WebStorm only |
| W+I | 2 | WebStorm + IdeaVim |

### Sequence Types
| Type | Count | Description |
|------|-------|-------------|
| chord | 6 | Multiple keys pressed together |
| double_tap | 11 | Double key press within timeout |
| leader | 15 | Leader key prefix sequences |
| long_press | 3 | Hold key for extended period |
| tap_hold | 2 | Different actions for tap vs hold |
| vim_prefix | 16 | Vim-style prefix commands |

## Bracket Navigation Key Bindings ([, ])

**Navigation Type**: Bracket  
**Keys**: [, ]  
**Description**: Previous/next item navigation using bracket keys for code blocks, errors, changes, and more

| Modifier | Keystroke | System | Status | Category | Action | **IDE Action ID** | Karabiner Code | IdeaVim Command | Config Reference |
|----------|-----------|---------|---------|----------|---------|-------------------|----------------|-----------------|------------------|
| None | [ / ] | I | ✅ | 🧭 Navigation | Previous/Next method or code block | `MethodUp/MethodDown` | `open_bracket/close_bracket` | `[[/]]` | .ideavimrc:L200 |
| Shift | ⇧[ / ⇧] | W | ✅ | ✏️ Selection | Select to previous/next code block | `EditorCodeBlockStartWithSelection/EditorCodeBlockEndWithSelection` | `shift+open_bracket/shift+close_bracket` | `v[[/v]]` | keymap.xml:L150 |
| Ctrl | ⌃[ / ⌃] | W+I | ✅ | 🧭 Navigation | Previous/Next error or issue | `GotoPreviousError/GotoNextError` | `ctrl+open_bracket/ctrl+close_bracket` | `[e/]e` | keymap.xml:L160 |
| Alt | ⌥[ / ⌥] | W | ✅ | 🧭 Navigation | Navigate to previous/next change marker | `VcsShowPrevChangeMarker/VcsShowNextChangeMarker` | `alt+open_bracket/alt+close_bracket` | `[c/]c` | keymap.xml:L170 |
| Cmd | ⌘[ / ⌘] | W | ✅ | 🧭 Navigation | Back/Forward in navigation history | `Back/Forward` | `cmd+open_bracket/cmd+close_bracket` | `:action Back/:action Forward` | keymap.xml:L180 |
| Shift Ctrl | ⇧⌃[ / ⇧⌃] | - | 📋 | ✏️ Selection | Select to previous/next paragraph | `EditorBackwardParagraphWithSelection/EditorForwardParagraphWithSelection` | `shift+ctrl+open_bracket/shift+ctrl+close_bracket` | `v{/v}` | - |
| Shift Alt | ⇧⌥[ / ⇧⌥] | - | 📋 | ✏️ Selection | Select to previous/next fold | `EditorMoveToPageTopWithSelection/EditorMoveToPageBottomWithSelection` | `shift+alt+open_bracket/shift+alt+close_bracket` | - | - |
| Shift Cmd | ⇧⌘[ / ⇧⌘] | W | ✅ | 🧭 Navigation | Navigate tabs left/right | `PreviousTab/NextTab` | `shift+cmd+open_bracket/shift+cmd+close_bracket` | `gt/gT` | keymap.xml:L190 |
| Ctrl Alt | ⌃⌥[ / ⌃⌥] | - | 📋 | 🧭 Navigation | Navigate between split panes | `PrevSplitter/NextSplitter` | `ctrl+alt+open_bracket/ctrl+alt+close_bracket` | `:wincmd h/:wincmd l` | - |
| Ctrl Cmd | ⌃⌘[ / ⌃⌘] | - | 📋 | 🧭 Navigation | Previous/Next bookmark | `GotoPreviousBookmark/GotoNextBookmark` | `ctrl+cmd+open_bracket/ctrl+cmd+close_bracket` | `[m/]m` | - |
| Alt Cmd | ⌥⌘[ / ⌥⌘] | - | 📋 | ⚙️ Action | Fold/Unfold code block | `CollapseBlock/ExpandBlock` | `alt+cmd+open_bracket/alt+cmd+close_bracket` | `zc/zo` | - |
| Curly Bracket | [{ / ]} | I | ✅ | 🧭 Navigation | Jump to previous/next unmatched brace 🔗vim_prefix | `EditorMatchBrace` | `-` | `[{/]}` | .ideavimrc:L220 |
| Double Bracket | [[ / ]] | I | ✅ | 🧭 Navigation | Jump to previous/next function 🔗vim_prefix | `MethodUp/MethodDown` | `-` | `[[/]]` | .ideavimrc:L210 |
| Paren Bracket | [( / ]) | I | ✅ | 🧭 Navigation | Jump to previous/next unmatched parenthesis 🔗vim_prefix | `EditorMatchBrace` | `-` | `[(/])` | .ideavimrc:L230 |

## Horizontal Navigation Key Bindings (H, L)

**Navigation Type**: Horizontal  
**Keys**: H, L  
**Description**: Left/right navigation and related actions

| Modifier | Keystroke | System | Status | Category | Action | **IDE Action ID** | Karabiner Code | IdeaVim Command | Config Reference |
|----------|-----------|---------|---------|----------|---------|-------------------|----------------|-----------------|------------------|
| None | H / L | I | ✅ | 🧭 Navigation | Previous/Next bookmark | `BookmarksAction` | `h/l` | `]'/'[` | .ideavimrc:L120 |
| Shift | ⇧H / ⇧L | W | ✅ | ✏️ Selection | Navigate to prev/next bookmark | `SelectPreviousTab/SelectNextTab` | `shift+h/l` | `:action SelectPreviousTab` | keymap.xml:L56 |
| Ctrl | ⌃H / ⌃L | W+I | ✅ | 📝 Text Edit | Editor join lines/Custom | `EditorJoinLines` | `ctrl+h/l` | `J` | keymap.xml:L33 |
| Alt | ⌥H / ⌥L | W | ✅ | 🧭 Navigation | Move caret to prev/next word | `EditorPreviousWord/EditorNextWord` | `alt+h/l` | `nnoremap <A-h> b` | keymap.xml:L48 |
| Cmd | ⌘H / ⌘L | W | ✅ | ⚙️ Action | Custom action/Complete statement | `EditorCompleteStatement` | `cmd+h/l` | - | keymap.xml:L24 |
| Shift Ctrl | ⇧⌃H / ⇧⌃L | - | 📋 | ✏️ Selection | Select to word start/end with hump mode | `EditorPreviousWordInDifferentHumpsModeWithSelection/EditorNextWordInDifferentHumpsModeWithSelection` | `shift+ctrl+h/l` | - | - |
| Shift Alt | ⇧⌥H / ⇧⌥L | W | ✅ | ✏️ Selection | Prev/Next word with selection | `EditorPreviousWordWithSelection` | `shift+alt+h/l` | - | keymap.xml:L55 |
| Shift Cmd | ⇧⌘H / ⇧⌘L | W | ✅ | 🪟 Window | Select prev/next tab | `SelectPreviousTab/SelectNextTab` | `shift+cmd+h/l` | `:action SelectPreviousTab` | keymap.xml:L56 |
| Ctrl Alt | ⌃⌥H / ⌃⌥L | - | 📋 | 🧭 Navigation | Page navigation left/right | `EditorPageUp/EditorPageDown` | `ctrl+alt+h/l` | - | - |
| Ctrl Cmd | ⌃⌘H / ⌃⌘L | - | 📋 | 🧭 Navigation | Move to page top/bottom | `EditorMoveToPageTop/EditorMoveToPageBottom` | `ctrl+cmd+h/l` | - | - |
| Alt Cmd | ⌥⌘H / ⌥⌘L | W | ✅ | ⚙️ Action | Custom action/Reformat code | `ReformatCode` | `alt+cmd+h/l` | - | keymap.xml:L59 |
| Shift Ctrl Alt | ⇧⌃⌥H / ⇧⌃⌥L | W | ✅ | 🪟 Window | Stretch split left/right | `StretchSplitToLeft/StretchSplitToRight` | `shift+ctrl+alt+h/l` | - | keymap.xml:L60 |
| Shift Ctrl Cmd | ⇧⌃⌘H / ⇧⌃⌘L | - | 📋 | 🎛️ Custom | Custom action | `Custom` | `shift+ctrl+cmd+h/l` | - | - |
| Shift Alt Cmd | ⇧⌥⌘H / ⇧⌥⌘L | W | ✅ | ⚙️ Action | Popup hector/Reformat dialog | `PopupHector/ShowReformatFileDialog` | `shift+alt+cmd+h/l` | - | keymap.xml:L62 |
| Ctrl Alt Cmd | ⌃⌥⌘H / ⌃⌥⌘L | - | 📋 | 🎛️ Custom | Custom action | `Custom` | `ctrl+alt+cmd+h/l` | - | - |
| Shift Ctrl Alt Cmd | ⇧⌃⌥⌘H / ⇧⌃⌥⌘L | - | 📋 | 🎛️ Custom | Custom action | `Custom` | `shift+ctrl+alt+cmd+h/l` | - | - |
| Hyper | ✱H / ✱L | K | ✅ | 🧭 Navigation | Move left/right one char | `left_arrow/right_arrow` | `right_shift+right_ctrl+right_alt+right_cmd+h/l` | - | karabiner.json:L65 |
| Hyper Shift | ✱⇧H / ✱⇧L | K | 📋 | ✏️ Selection | Tab switching | `SelectPreviousTab` | `-` | - | - |
| Hyper Ctrl | ✱⌃H / ✱⌃L | K | ✅ | 🖥️ Desktop | Prev/next desktop | `left_control+left_arrow` | `-` | - | karabiner.json:L67 |
| Hyper Alt | ✱⌥H / ✱⌥L | K | ⚠️ | 🖱️ Mouse | Need to remap | `mouse_move` | `-` | - | - |
| Hyper Cmd | ✱⌘H / ✱⌘L | W | ✅ | 🪟 Window | App switcher | `Switcher` | `-` | - | keymap.xml:L69 |
| Double Tap | HH / LL | - | 📋 | ⏱️ Timing | Double tap action ⏱️500ms 🔗double_tap 👆double | `Custom` | `h+h/l+l` | - | - |
| Shift Double Tap | ⇧HH / ⇧LL | - | 📋 | ⏱️ Timing | Shift + double tap ⏱️500ms 🔗double_tap 👆double | `Custom` | `shift+h+h/l+l` | - | - |
| Ctrl Double Tap | ⌃HH / ⌃LL | - | 📋 | ⏱️ Timing | Control + double tap ⏱️500ms 🔗double_tap 👆double | `Custom` | `ctrl+h+h/l+l` | - | - |
| Alt Double Tap | ⌥HH / ⌥LL | - | 📋 | ⏱️ Timing | Alt + double tap ⏱️500ms 🔗double_tap 👆double | `Custom` | `alt+h+h/l+l` | - | - |
| Cmd Double Tap | ⌘HH / ⌘LL | - | 📋 | ⏱️ Timing | Command + double tap ⏱️500ms 🔗double_tap 👆double | `Custom` | `cmd+h+h/l+l` | - | - |
| Leader | <Leader>H / <Leader>L | I | 📋 | 👑 Leader | Leader + horizontal nav 🔗leader | `Custom` | `-` | `<Leader>h/<Leader>l` | - |
| Leader Shift | <Leader>⇧H / <Leader>⇧L | I | 📋 | 👑 Leader | Leader + shift + horizontal 🔗leader | `Custom` | `-` | `<Leader>H/<Leader>L` | - |
| Leader Ctrl | <Leader>⌃H / <Leader>⌃L | I | 📋 | 👑 Leader | Leader + control + horizontal 🔗leader | `Custom` | `-` | `<Leader><C-h>/<Leader><C-l>` | - |
| Leader Alt | <Leader>⌥H / <Leader>⌥L | I | 📋 | 👑 Leader | Leader + alt + horizontal 🔗leader | `Custom` | `-` | `<Leader><A-h>/<Leader><A-l>` | - |
| Leader Cmd | <Leader>⌘H / <Leader>⌘L | I | 📋 | 👑 Leader | Leader + command + horizontal 🔗leader | `Custom` | `-` | `<Leader><D-h>/<Leader><D-l>` | - |
| Double Leader | <Leader><Leader>H / <Leader><Leader>L | I | 📋 | 👑 Leader | Double leader + horizontal 🔗leader | `Custom` | `-` | `<Leader><Leader>h/<Leader><Leader>l` | - |
| Long Press | H(hold) / L(hold) | - | 📋 | ⏱️ Timing | Long press activation ⏱️1000ms 🔗long_press 👆hold | `Custom` | `h_hold/l_hold` | - | - |
| Tap Hold | H(tap/hold) / L(tap/hold) | - | 📋 | ⏱️ Timing | Different actions for tap vs hold ⏱️200ms 🔗tap_hold 👆tap_or_hold | `Custom` | `h_tap_hold/l_tap_hold` | - | - |
| Chord Vertical | H+J / L+K | - | 📋 | 🎹 Chord | Horizontal + vertical chord 🔗chord 🎹J+K | `Custom` | `h+j/l+k` | - | - |
| Chord Mouse | H+click / L+click | - | 📋 | 🎹 Chord | Key + mouse button 🔗chord 🎹click | `Custom` | `h+click/l+click` | - | - |
| Chord Scroll | H+scroll / L+scroll | - | 📋 | 🎹 Chord | Key + scroll wheel 🔗chord 🎹scroll | `Custom` | `h+scroll/l+scroll` | - | - |
| G Prefix | GH / GL | I | ✅ | 🧭 Navigation | Move to line beginning/end | `EditorLineStart/EditorLineEnd` | `-` | `0/$` | .ideavimrc:L81 |
| Change Camel | cH / cL | I | ✅ | 📝 Text Edit | Change camel hump back/forward | `CamelHumpAction` | `-` | `cb/cw` | .ideavimrc:L82 |
| Delete Camel | dH / dL | I | ✅ | 📝 Text Edit | Delete camel hump back/forward | `CamelHumpAction` | `-` | `db/dw` | .ideavimrc:L83 |
| Inner Camel | cih / dih | I | ✅ | 📝 Text Edit | Change/delete inner camel hump | `CamelHumpAction` | `-` | `ciw/diw` | .ideavimrc:L84 |
| Scroll Horizontal | zH / zL | I | ✅ | 🧭 Navigation | Scroll left/right 50 chars | `ScrollAction` | `-` | `zh/zl` | .ideavimrc:L85 |
| Yank Horizontal | yH / yL | I | 📋 | 🔗 Sequence | Yank horizontal motion 🔗vim_prefix | `Custom` | `-` | `yh/yl` | - |
| Visual Horizontal | vH / vL | I | 📋 | 🔗 Sequence | Visual horizontal motion 🔗vim_prefix | `Custom` | `-` | `vh/vl` | - |
| Mark Horizontal | mH / mL | I | 📋 | 🔗 Sequence | Mark horizontal position 🔗vim_prefix | `Custom` | `-` | `mh/ml` | - |
| Jump Mark | 'H / 'L | I | 📋 | 🔗 Sequence | Jump to horizontal mark 🔗vim_prefix | `Custom` | `-` | `'h/'l` | - |
| Register Horizontal | "H / "L | I | 📋 | 🔗 Sequence | Register horizontal action 🔗vim_prefix | `Custom` | `-` | `"h/"l` | - |
| Backslash Leader | \H / \L | I | 📋 | 👑 Leader | Backslash leader horizontal 🔗leader | `Custom` | `-` | `\h/\l` | - |

## Individual Key Bindings (Space)

**Navigation Type**: Individual  
**Keys**: Space  
**Description**: Space bar productivity bindings with modifier combinations for quick actions

| Modifier | Keystroke | System | Status | Category | Action | **IDE Action ID** | Karabiner Code | IdeaVim Command | Config Reference |
|----------|-----------|---------|---------|----------|---------|-------------------|----------------|-----------------|------------------|
| None | Space | K | ✅ | ⚙️ Action | Insert space character | `EditorSpace` | `spacebar` | ` ` | karabiner.json:L500 |
| Shift | ⇧Space | K | ✅ | ⚙️ Action | Page up (reverse scroll) | `EditorPageUp` | `shift+spacebar` | `⌃b` | karabiner.json:L510 |
| Ctrl | ⌃Space | W | ✅ | ⚙️ Action | Basic code completion | `CodeCompletion` | `ctrl+spacebar` | `:action CodeCompletion` | keymap.xml:L300 |
| Alt | ⌥Space | K | ✅ | 🪟 Window | Spotlight search | `System.Spotlight` | `alt+spacebar` | - | karabiner.json:L520 |
| Cmd | ⌘Space | K | ✅ | 🪟 Window | Spotlight search (system default) | `System.Spotlight` | `cmd+spacebar` | - | system:default |
| Shift Ctrl | ⇧⌃Space | W | ✅ | ⚙️ Action | Smart code completion | `SmartTypeCompletion` | `shift+ctrl+spacebar` | `:action SmartTypeCompletion` | keymap.xml:L310 |
| Shift Alt | ⇧⌥Space | - | 📋 | 🪟 Window | Toggle window manager mode | `Custom` | `shift+alt+spacebar` | - | - |
| Shift Cmd | ⇧⌘Space | - | 📋 | ⚙️ Action | Character viewer | `System.CharacterViewer` | `shift+cmd+spacebar` | - | - |
| Ctrl Alt | ⌃⌥Space | - | 📋 | 🪟 Window | Application switcher | `Custom` | `ctrl+alt+spacebar` | - | - |
| Ctrl Cmd | ⌃⌘Space | W | ✅ | ⚙️ Action | Emoji picker | `System.EmojiPicker` | `ctrl+cmd+spacebar` | - | system:default |
| Alt Cmd | ⌥⌘Space | - | 📋 | 🪟 Window | Finder search | `System.FinderSearch` | `alt+cmd+spacebar` | - | - |
| Double Tap | Space Space | K | 📋 | ⏱️ Timing | Quick action menu ⏱️300ms 🔗double_tap 👆double | `GotoAction` | `spacebar+spacebar` | `:action GotoAction` | - |
| Long Press | Space(hold) | K | 📋 | ⏱️ Timing | Activate window management mode ⏱️500ms 🔗long_press 👆hold | `Custom` | `spacebar_hold` | - | - |
| Leader Space | <Leader>Space | I | 📋 | 👑 Leader | Clear search highlighting 🔗leader | `Custom` | `-` | `<Leader><Space>` | - |

## Vertical Navigation Key Bindings (J, K)

**Navigation Type**: Vertical  
**Keys**: J, K  
**Description**: Up/down navigation and related actions

| Modifier | Keystroke | System | Status | Category | Action | **IDE Action ID** | Karabiner Code | IdeaVim Command | Config Reference |
|----------|-----------|---------|---------|----------|---------|-------------------|----------------|-----------------|------------------|
| None | J / K | I | ✅ | 🧭 Navigation | Move down/up line by line | `EditorDown/EditorUp` | `j/k` | `J/<C-v>k` | .ideavimrc:L91 |
| Shift | ⇧J / ⇧K | W | ✅ | ✏️ Selection | Extend selection down/up | `EditorDownWithSelection/EditorUpWithSelection` | `shift+j/k` | `vj/vk` | keymap.xml:L92 |
| Ctrl | ⌃J / ⌃K | W | ✅ | 🧭 Navigation | Scroll down/up with cursor | `EditorMoveDownAndScroll/EditorMoveUpAndScroll` | `ctrl+j/k` | - | keymap.xml:L93 |
| Alt | ⌥J / ⌥K | W | ✅ | 📝 Text Edit | Clone caret below/above | `EditorCloneCaretBelow/EditorCloneCaretAbove` | `alt+j/k` | - | keymap.xml:L18 |
| Cmd | ⌘J / ⌘K | W | ✅ | ⚙️ Action | Insert live template/Custom | `InsertLiveTemplate` | `cmd+j/k` | - | keymap.xml:L95 |
| Shift Ctrl | ⇧⌃J / ⇧⌃K | - | 📋 | ✏️ Selection | Select paragraph up/down | `EditorBackwardParagraphWithSelection/EditorForwardParagraphWithSelection` | `shift+ctrl+j/k` | - | - |
| Shift Alt | ⇧⌥J / ⇧⌥K | - | 📋 | ✏️ Selection | Select with scroll up/down | `EditorMoveUpAndScrollWithSelection/EditorMoveDownAndScrollWithSelection` | `shift+alt+j/k` | - | - |
| Shift Cmd | ⇧⌘J / ⇧⌘K | W | ✅ | ⚙️ Action | Editor join lines/VCS push | `EditorJoinLines/Vcs.Push` | `shift+cmd+j/k` | - | keymap.xml:L98 |
| Ctrl Alt | ⌃⌥J / ⌃⌥K | W | ✅ | 📝 Text Edit | Move line down/up | `MoveLineDown/MoveLineUp` | `ctrl+alt+j/k` | - | keymap.xml:L99 |
| Ctrl Cmd | ⌃⌘J / ⌃⌘K | - | 📋 | 🧭 Navigation | Document start/end navigation | `EditorTextStart/EditorTextEnd` | `ctrl+cmd+j/k` | - | - |
| Alt Cmd | ⌥⌘J / ⌥⌘K | W | ✅ | ⚙️ Action | Surround with template/Custom | `SurroundWithLiveTemplate` | `alt+cmd+j/k` | - | keymap.xml:L101 |
| Shift Ctrl Alt | ⇧⌃⌥J / ⇧⌃⌥K | - | 📋 | ✏️ Selection | Select to document start/end | `EditorTextStartWithSelection/EditorTextEndWithSelection` | `shift+ctrl+alt+j/k` | - | - |
| Shift Ctrl Cmd | ⇧⌃⌘J / ⇧⌃⌘K | - | 📋 | 🎛️ Custom | Custom action | `Custom` | `shift+ctrl+cmd+j/k` | - | - |
| Shift Alt Cmd | ⇧⌥⌘J / ⇧⌥⌘K | - | 📋 | 🎛️ Custom | Custom action | `Custom` | `shift+alt+cmd+j/k` | - | - |
| Ctrl Alt Cmd | ⌃⌥⌘J / ⌃⌥⌘K | - | 📋 | 🎛️ Custom | Custom action | `Custom` | `ctrl+alt+cmd+j/k` | - | - |
| Shift Ctrl Alt Cmd | ⇧⌃⌥⌘J / ⇧⌃⌥⌘K | - | 📋 | 🎛️ Custom | Custom action | `Custom` | `shift+ctrl+alt+cmd+j/k` | - | - |
| Hyper | ✱J / ✱K | K | ✅ | 🧭 Navigation | Move down/up one line | `down_arrow/up_arrow` | `right_shift+right_ctrl+right_alt+right_cmd+j/k` | - | karabiner.json:L107 |
| Hyper Shift | ✱⇧J / ✱⇧K | K | 📋 | 🧭 Navigation | App switching | `AppSwitcher` | `-` | - | - |
| Hyper Ctrl | ✱⌃J / ✱⌃K | K | 📋 | 🖥️ Desktop | Focus/expose | `MissionControl` | `-` | - | - |
| Hyper Alt | ✱⌥J / ✱⌥K | K | 📋 | 🖱️ Mouse | Mouse move | `mouse_move` | `-` | - | - |
| Hyper Cmd | ✱⌘J / ✱⌘K | - | 📋 | 🎛️ Custom | Custom action | `Custom` | `-` | - | - |
| Double Tap | JJ / KK | - | 📋 | ⏱️ Timing | Double tap vertical action ⏱️500ms 🔗double_tap 👆double | `Custom` | `j+j/k+k` | - | - |
| Shift Double Tap | ⇧JJ / ⇧KK | - | 📋 | ⏱️ Timing | Shift + double tap vertical ⏱️500ms 🔗double_tap 👆double | `Custom` | `shift+j+j/k+k` | - | - |
| Ctrl Double Tap | ⌃JJ / ⌃KK | - | 📋 | ⏱️ Timing | Control + double tap vertical ⏱️500ms 🔗double_tap 👆double | `Custom` | `ctrl+j+j/k+k` | - | - |
| Alt Double Tap | ⌥JJ / ⌥KK | - | 📋 | ⏱️ Timing | Alt + double tap vertical ⏱️500ms 🔗double_tap 👆double | `Custom` | `alt+j+j/k+k` | - | - |
| Cmd Double Tap | ⌘JJ / ⌘KK | - | 📋 | ⏱️ Timing | Command + double tap vertical ⏱️500ms 🔗double_tap 👆double | `Custom` | `cmd+j+j/k+k` | - | - |
| Leader | <Leader>J / <Leader>K | I | 📋 | 👑 Leader | Leader + vertical nav 🔗leader | `Custom` | `-` | `<Leader>j/<Leader>k` | - |
| Leader Shift | <Leader>⇧J / <Leader>⇧K | I | 📋 | 👑 Leader | Leader + shift + vertical 🔗leader | `Custom` | `-` | `<Leader>J/<Leader>K` | - |
| Leader Ctrl | <Leader>⌃J / <Leader>⌃K | I | 📋 | 👑 Leader | Leader + control + vertical 🔗leader | `Custom` | `-` | `<Leader><C-j>/<Leader><C-k>` | - |
| Leader Alt | <Leader>⌥J / <Leader>⌥K | I | 📋 | 👑 Leader | Leader + alt + vertical 🔗leader | `Custom` | `-` | `<Leader><A-j>/<Leader><A-k>` | - |
| Leader Cmd | <Leader>⌘J / <Leader>⌘K | I | 📋 | 👑 Leader | Leader + command + vertical 🔗leader | `Custom` | `-` | `<Leader><D-j>/<Leader><D-k>` | - |
| Double Leader | <Leader><Leader>J / <Leader><Leader>K | I | 📋 | 👑 Leader | Double leader + vertical 🔗leader | `Custom` | `-` | `<Leader><Leader>j/<Leader><Leader>k` | - |
| Long Press | J(hold) / K(hold) | - | 📋 | ⏱️ Timing | Long press vertical activation ⏱️1000ms 🔗long_press 👆hold | `Custom` | `j_hold/k_hold` | - | - |
| Tap Hold | J(tap/hold) / K(tap/hold) | - | 📋 | ⏱️ Timing | Different actions for tap vs hold vertical ⏱️200ms 🔗tap_hold 👆tap_or_hold | `Custom` | `j_tap_hold/k_tap_hold` | - | - |
| Chord Horizontal | J+H / K+L | - | 📋 | 🎹 Chord | Vertical + horizontal chord 🔗chord 🎹H+L | `Custom` | `j+h/k+l` | - | - |
| Chord Mouse | J+click / K+click | - | 📋 | 🎹 Chord | Vertical + mouse button 🔗chord 🎹click | `Custom` | `j+click/k+click` | - | - |
| Chord Scroll | J+scroll / K+scroll | - | 📋 | 🎹 Chord | Vertical + scroll wheel 🔗chord 🎹scroll | `Custom` | `j+scroll/k+scroll` | - | - |
| G Prefix | GJ / GK | I | ✅ | 🧭 Navigation | Navigate prev/next method | `MethodUp/MethodDown` | `-` | `[m/]m` | .ideavimrc:L123 |
| Scroll Vertical | zJ / zK | I | 📋 | 🧭 Navigation | Scroll down/up multiple lines 🔗vim_prefix | `ScrollAction` | `-` | `zj/zk` | - |
| Yank Vertical | yJ / yK | I | 📋 | 🔗 Sequence | Yank vertical motion 🔗vim_prefix | `Custom` | `-` | `yj/yk` | - |
| Visual Vertical | vJ / vK | I | 📋 | 🔗 Sequence | Visual vertical motion 🔗vim_prefix | `Custom` | `-` | `vj/vk` | - |
| Mark Vertical | mJ / mK | I | 📋 | 🔗 Sequence | Mark vertical position 🔗vim_prefix | `Custom` | `-` | `mj/mk` | - |
| Jump Mark Vertical | 'J / 'K | I | 📋 | 🔗 Sequence | Jump to vertical mark 🔗vim_prefix | `Custom` | `-` | `'j/'k` | - |
| Register Vertical | "J / "K | I | 📋 | 🔗 Sequence | Register vertical action 🔗vim_prefix | `Custom` | `-` | `"j/"k` | - |
| Backslash Leader Vertical | \J / \K | I | 📋 | 👑 Leader | Backslash leader vertical 🔗leader | `Custom` | `-` | `\j/\k` | - |
| Bracket Prev | [J / [K | I | 📋 | 🔗 Sequence | Previous bracket vertical 🔗vim_prefix | `Custom` | `-` | `[j/[k` | - |
| Bracket Next | ]J / ]K | I | 📋 | 🔗 Sequence | Next bracket vertical 🔗vim_prefix | `Custom` | `-` | `]j/]k` | - |

---

*Generated automatically from YAML configuration data.*
*Source files: `bracket-navigation.yaml`, `horizontal-navigation.yaml`, `individual-navigation.yaml`, `vertical-navigation.yaml`*
