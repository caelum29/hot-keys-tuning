# WebStorm Custom Keymaps

## Current Keymap: macOS copy1

Based on "Mac OS X 10.5+" with custom modifications.

### Custom Shortcuts

#### Terminal & Tools
- **Terminal**: `Ctrl + ,`
- **Big Data Tool Window**: `Shift + Ctrl + Cmd + B`

#### Code Completion
- **Code Completion**: `Alt + '`
- **Smart Type Completion**: `Shift + Alt + '`
- **Complete Statement**: `Cmd + L` (additional to `Shift + Cmd + Enter`)

#### Editor Navigation
- **Word Movement**: 
  - Next word: `Alt + L` (additional to `Alt + Right`)
  - Previous word: `Alt + H` (additional to `Alt + Left`)
  - With selection: `Shift + Alt + H/L`
- **Line Movement**:
  - Line start: `Cmd + Left` (additional to `Home`)
  - Line end: `Cmd + Right` (additional to `End`)

#### Multi-Cursor & Selection
- **Clone Caret Above**: `Alt + K`
- **Clone Caret Below**: `Alt + J`
- **Highlight Usages**: `Alt + F` (additional to `Shift + Cmd + F7`)

#### Line Operations
- **Join Lines**: `Ctrl + J`
- **Move Line Up**: `Ctrl + Alt + K` (additional to `Shift + Alt + Up`)
- **Move Line Down**: `Ctrl + Alt + J` (additional to `Shift + Alt + Down`)

#### Clipboard & Paste
- **Paste**: `Cmd + P` (additional to `Cmd + V`)
- **Paste Multiple**: `Alt + V` (additional to `Shift + Cmd + V`)

#### Tab Navigation
- **Next Tab**: `Shift + Cmd + L` (additional to `Ctrl + Right`)
- **Previous Tab**: `Shift + Cmd + H` (additional to `Ctrl + Left`)

#### Window Switching
- **Switcher Forward**: `Shift + Cmd + J`
- **Switcher Backward**: `Shift + Cmd + K`

#### Navigation & Search
- **Show Navigation Bar**: `Ctrl + K` (additional to `Cmd + Up`, `Alt + Home`)
- **Show Usages**: `Alt + S` (additional to `Cmd + Alt + F7`)
- **Quick Documentation**: `F1` (additional to `Ctrl + Q`)

#### Window Management
- **Stretch Split**:
  - To Top: `Shift + Ctrl + Alt + K`
  - To Bottom: `Shift + Ctrl + Alt + J`
  - To Left: `Shift + Ctrl + Alt + H`
  - To Right: `Shift + Ctrl + Alt + L`

#### Editor Toggles
- **Toggle Breadcrumbs**: `Alt + W`

#### Terminal Operations
- **Clear Buffer**: `Cmd + K`

### Disabled Actions
The following actions have been disabled (no shortcuts assigned):
- Check-in Project
- Database Properties Action
- Editor Cut Line End
- Editor Down/Up with Selection
- Editor Left/Right with Selection
- Editor Unindent Selection
- Emmet Edit Points
- File Chooser Toggle Path
- Git/Hg Commit and Push
- Go to Line/Row
- Method Hierarchy
- Parameter Info
- Switcher (default)
- VCS Log Focus Text Filter
- VCS Push
- Copilot Dispose Inlays
- Markdown Toggle Italic

## IdeaVim Configuration

### Vim Plugins Enabled
- **Sneak**: Efficient motion with `s` and `S`
- **EasyMotion**: Quick navigation with `<leader><leader>`
- **Surround**: Manipulate surrounding characters
- **Multiple Cursors**: Multi-cursor functionality
- **Which-Key**: Display available keybindings
- **QuickScope**: Highlight targets for f/F/t/T motions
- **Highlighted Yank**: Highlight yanked text

### Leader Key
- **Leader**: `Space`

### Vim Settings
- `scrolloff=7` - Keep 7 lines of context
- `smartcase` - Case-insensitive search unless uppercase used
- `incsearch` - Highlight matches as you type
- `relativenumber` - Show relative line numbers
- `showmode` - Display current mode
- `showcmd` - Show partial commands
- `visualbell` - Visual flash instead of beeping
- `clipboard+=unnamed` - Copy to system clipboard
- `ideajoin` - Use IntelliJ's smart line joining
- `ideamarks` - Enable IntelliJ-style marks
- `notimeout` - Disable timeout for keybindings

### Which-Key Settings
- Font size: 14
- Prefix color: `C792EA` (purple)
- Command color: `82AAFF` (blue)
- Prefix style: bold
- Sort order: by key prefix first
- Default delay: 600ms
- Hide typed sequence

### QuickScope Settings
- Primary color: `F8E71C` (yellow)
- Highlight on keys: `f`, `F`, `t`, `T`

### Custom Vim Keybindings

#### Leader-based Actions (`<Space>` + key)
- `<Space>ed` - Show error description
- `<Space>v` - Paste multiple items
- `<Space>or` - Open recent project
- `<Space>a` - Open action menu (GotoAction)
- `<Space>q` - Close current tab
- `<Space>Q` - Reopen closed tab
- `<Space>jj` - AceJump general navigation
- `<Space>jl` - AceJump line navigation
- `<Space>y` - AceJump target navigation
- `<Space>sm` - String manipulation menu
- `<Space>d` - Start debugging
- `<Space>z` - Toggle Zen Mode
- `<Space>fs` - File structure popup
- `<Space>RF` - Rename file
- `<Space>re` - Rename element
- `<Space>mv` - Move element
- `<Space>ha` - Hide all windows
- `<Space>co` - Close all editors but active
- `<Space>t` - Activate terminal
- `<Space>rf` - Show recent files
- `<Space>rF` - Show recent changed files
- `<Space>cu` - Close all unmodified editors
- `<Space>sw` - Surround with
- `<Space>mo` - Move editor to opposite tab group
- `<Space>ms` - Maximize editor in split
- `<Space>b` - Toggle line breakpoint
- `<Space>mm` - Toggle bookmark with mnemonic
- `<Space>gx` - Close all editors but active

#### Navigation (g + key)
- `ge` - Go to next error
- `gE` - Go to previous error
- `gz` - Next splitter
- `gZ` - Previous splitter
- `gh` - Move to beginning of line (^)
- `gl` - Move to end of line ($)
- `go` - Move to matching parenthesis (%)
- `gj` - Next method
- `gk` - Previous method
- `gp` - Reselect pasted text
- `gi` - Jump to last change
- `gI` - Jump to next change
- `gb` - Show bookmarks

#### Line Operations (z + key)
- `zj` - Create new line below (stay in normal mode)
- `zk` - Create new line above (stay in normal mode)
- `zsU` - Close all splits (UnsplitAll)
- `zH` - Scroll left 50 columns
- `zL` - Scroll right 50 columns

#### Multiple Cursors
- `Ctrl+n` - Next whole occurrence
- `g Ctrl+n` - Next occurrence
- `Ctrl+x` - Skip occurrence
- `Ctrl+p` - Remove occurrence
- `Shift+Ctrl+n` - All whole occurrences

#### Bookmarks
- `mm` - Toggle bookmark
- `mp` - Pin active tab toggle
- `L` - Go to next bookmark
- `H` - Go to previous bookmark

#### Tab Navigation
- `Tab` - Next tab
- `Shift+Tab` - Previous tab

#### Text Objects & Editing
- `K` (visual) - Expand selection to word
- `J` (visual) - Shrink selection from word
- `Q` - Format paragraph
- `U` - Redo
- `E` - Go to end of previous word (ge)
- `vv` - Select entire line (V)

#### Camel Case Navigation & Editing
- `cL` - Change to next camel hump
- `cH` - Change to previous camel hump
- `cih` - Change inner camel hump
- `dL` - Delete to next camel hump
- `dH` - Delete to previous camel hump
- `dih` - Delete inner camel hump

#### Parentheses Editing
- `c)` - Change to closing parenthesis
- `d)` - Delete to closing parenthesis
- `c(` - Change to opening parenthesis
- `d(` - Delete to opening parenthesis

#### Special Actions
- `dm` - Delete method (custom macro)
- `dam` - Delete method and clean empty lines
- `J` - Smart join lines (Ctrl+J)
- `tt` - Toggle editor preview only

### Notes
- This keymap combines vim-inspired navigation (`H/J/K/L`) with standard macOS shortcuts
- Many actions have both original and custom shortcuts for flexibility
- Focus on productivity with multi-cursor support and efficient navigation
- Leader key (Space) provides quick access to most IDE functions
- Vim plugins enhance navigation and text manipulation capabilities
- QuickScope highlights make f/F/t/T motions more efficient
- Which-Key shows available shortcuts after pressing leader or prefix keys