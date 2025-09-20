# IdeaVim Best Practices for 2024

Based on comprehensive research of current IdeaVim best practices, plugin configurations, and keymap optimization strategies.

## 🏆 Essential Configuration Foundation

### Core Settings (Order Matters)
```vim
"" Leader Key - MUST be set FIRST, before any plugins
let mapleader = " "

"" Essential Vim Settings
set scrolloff=10          " Keep 10 lines of context when scrolling
set linenumber           " Show line numbers
set showmode             " Display current mode
set showcmd              " Show partial commands
set smartcase            " Case-insensitive search unless uppercase used
set incsearch            " Highlight matches as you type
set hlsearch             " Highlight all search matches
set clipboard+=unnamed   " Copy to system clipboard
set visualbell           " Visual flash instead of beeping
set noerrorbells        " Disable error bells
set notimeout           " Disable timeout for key sequences
```

### Plugin Setup (Enable AFTER Leader Key)
```vim
"" Core Plugins - Enable in this order
set surround            " Manipulate surrounding characters
set highlightedyank     " Highlight yanked text briefly
set easymotion          " Enhanced cursor movement
set which-key           " Display available keybindings
set commentary          " Toggle comments
set multiple-cursors    " Multi-cursor functionality
set sneak               " Enhanced f/F/t/T motions
set ideajoin            " Use IntelliJ's smart line joining
set ideamarks           " Enable IntelliJ-style marks

"" Advanced Community Plugins (2024)
Plug 'tpope/vim-peekaboo'      " Show register contents
Plug 'mini.ai'                 " Enhanced text objects
Plug 'michaeljsmith/vim-indent-object'  " Select by indentation
Plug 'kana/vim-textobj-entire' " Select entire file
Plug 'kana/vim-textobj-function' " Function text objects
```

## 🔧 Advanced Plugin Configuration

### Which-Key Setup (2024 Standards)
```vim
"" Which-Key Configuration
let g:WhichKey_FontSize = 16
let g:WhichKey_CommandColor = "#41ead4"      " Cyan for commands
let g:WhichKey_PrefixColor = "#f335b2"       " Pink for prefixes
let g:WhichKey_SortOrder = "by_key_prefix_first"
let g:WhichKey_ShowVimActions = "true"
let g:WhichKey_DefaultDelay = 0
let g:WhichKey_KeysOfGroups = {
  \ '<leader>g': 'Git',
  \ '<leader>r': 'Refactor',
  \ '<leader>t': 'Test',
  \ '<leader>w': 'Window',
  \ '<leader>c': 'Code',
  \ '<leader>s': 'Search',
  \ '<leader>a': 'Analysis',
  \ '<leader>d': 'Debug',
  \ '<leader>f': 'File',
  \ '<leader>j': 'Jump'
  \ }
```

### Highlighted Yank Configuration
```vim
"" Highlighted Yank Settings
let g:highlightedyank_highlight_duration = 50  " Highlight for 50ms
```

### EasyMotion Setup
```vim
"" EasyMotion Configuration
" Note: Requires both IdeaVim-EasyMotion AND AceJump plugins installed
map <leader><leader>j <Plug>(easymotion-s)     " Single character search
map <leader><leader>w <Plug>(easymotion-bd-w)  " Word beginning
map <leader><leader>e <Plug>(easymotion-bd-e)  " Word end
map <leader><leader>f <Plug>(easymotion-f)     " Find character forward
map <leader><leader>F <Plug>(easymotion-F)     " Find character backward
```

## 🎯 IDE Integration Best Practices

### Action Mappings (2024 Standard)
```vim
"" IDE-Specific Mappings using Action IDs
if has('ide')
    " Navigation
    map <leader>f <Action>(GotoFile)
    map <leader>c <Action>(GotoClass)
    map <leader>s <Action>(GotoSymbol)
    map <leader>a <Action>(GotoAction)
    map <leader>e <Action>(RecentFiles)
    
    " Refactoring
    map <leader>rn <Action>(RenameElement)
    map <leader>rm <Action>(ExtractMethod)
    map <leader>rv <Action>(IntroduceVariable)
    map <leader>ri <Action>(Inline)
    map <leader>rs <Action>(ChangeSignature)
    
    " Git Integration
    map <leader>gc <Action>(CheckinProject)
    map <leader>gp <Action>(Vcs.Push)
    map <leader>gl <Action>(Vcs.UpdateProject)
    map <leader>gd <Action>(Compare.SameVersion)
    map <leader>gb <Action>(Annotate)
    map <leader>gh <Action>(Vcs.ShowTabbedFileHistory)
    
    " Testing
    map <leader>tr <Action>(RunClass)
    map <leader>tt <Action>(RunConfiguration)
    map <leader>td <Action>(DebugClass)
    map <leader>tc <Action>(RunCoverage)
    
    " Debug
    map <leader>db <Action>(ToggleLineBreakpoint)
    map <leader>dc <Action>(Resume)
    map <leader>dn <Action>(StepOver)
    map <leader>di <Action>(StepInto)
    map <leader>do <Action>(StepOut)
    
    " Code Generation
    map <leader>cg <Action>(Generate)
    map <leader>cc <Action>(GenerateConstructor)
    map <leader>ct <Action>(GenerateToString)
    
    " Search
    map <leader>sf <Action>(FindInPath)
    map <leader>sr <Action>(ReplaceInPath)
    map <leader>su <Action>(FindUsages)
    
    " Window Management
    map <leader>wh <Action>(StretchSplitToLeft)
    map <leader>wl <Action>(StretchSplitToRight)
    map <leader>wk <Action>(StretchSplitToTop)
    map <leader>wj <Action>(StretchSplitToBottom)
    map <leader>wu <Action>(UnsplitAll)
    
    " WebStorm-specific mappings
    if &ide =~? 'webstorm'
        map <leader>wr <Action>(Run)
        map <leader>wd <Action>(Debug)
        map <leader>ws <Action>(Stop)
    endif
endif
```

### Finding Action IDs
To discover IDE action IDs:
1. Press `Ctrl+Shift+A`
2. Type: "IdeaVim: Track Action Ids"
3. Enable tracking
4. Perform the IDE action you want to map
5. The action ID will be displayed

## 🚨 Conflict Resolution (2024 Method)

### Handler Priority Configuration
1. Open **Settings**: `Ctrl+Alt+S` (or `Cmd+,` on macOS)
2. Navigate to **Editor** → **Vim Emulation**
3. Review shortcut conflicts in the table
4. For each conflict, choose:
   - **IDE**: Use IntelliJ shortcut
   - **Vim**: Use IdeaVim shortcut
   - **Undefined**: Show popup to choose each time

### Recommended Handler Priorities
```
Ctrl+C       → IDE    (Standard copy)
Ctrl+V       → IDE    (Standard paste)
Ctrl+X       → IDE    (Standard cut)
Ctrl+Z       → IDE    (Standard undo)
Ctrl+Y       → IDE    (Standard redo)
Ctrl+A       → IDE    (Select all)
Ctrl+F       → IDE    (Find dialog)
Ctrl+R       → IDE    (Replace dialog)
Ctrl+W       → Vim    (Window operations)
Ctrl+D       → Vim    (Scroll down)
Ctrl+U       → Vim    (Scroll up)
Ctrl+B       → Vim    (Page up)
Ctrl+F       → Vim    (Page down) - if not using for Find
```

### Per-Mode Handler Configuration (Advanced)
Recent IdeaVim versions support per-mode handlers:
- **Normal Mode**: Prefer Vim handlers
- **Insert Mode**: Prefer IDE handlers  
- **Visual Mode**: Prefer Vim handlers

## 💡 2024 Advanced Features

### Essential Conflict-Free Mappings
```vim
"" Safe alternatives that don't conflict with IDE
inoremap jk <Esc>                    " Quick escape from insert mode
nnoremap Y y$                        " Yank to end of line
nnoremap Q <nop>                     " Disable Ex mode
nnoremap <leader><leader> :action AceAction<CR>  " Quick AceJump

"" Enhanced navigation
nnoremap H ^                         " Jump to first non-blank character
nnoremap L $                         " Jump to end of line
nnoremap J mzJ`z                     " Join lines but keep cursor position

"" Better search
nnoremap n nzzzv                     " Next search result, center screen
nnoremap N Nzzzv                     " Previous search result, center screen
nnoremap * *zzzv                     " Search word under cursor, center screen
```

## 🚀 Expression Mappings (2024 Feature)

### Dynamic Context-Aware Mappings
```vim
"" Conditional mappings based on file type
map <expr> <leader>r &ft == 'python' ? ':!python %<CR>' : &ft == 'javascript' ? ':!node %<CR>' : ':echo "No runner configured"<CR>'

"" Context-sensitive paste behavior
map <expr> <leader>p mode() == 'i' ? '<C-r>+' : '"+p'

"" Smart line insertion based on current position
map <expr> o line('.') == line('$') ? 'o' : 'o<Esc>S'

"" Adaptive search behavior
map <expr> / pumvisible() ? '<C-e>' : '/'

"" Dynamic action selection
map <expr> <leader>f &ft == 'typescript' ? ':action GotoTypeDeclaration<CR>' : ':action GotoDeclaration<CR>'
```

### Advanced Expression Patterns
```vim
"" Smart bracket handling
inoremap <expr> ( getline('.')[col('.')-1] =~ '\w' ? '(' : '()<Left>'

"" Intelligent code completion
inoremap <expr> <Tab> pumvisible() ? '<C-n>' : '<Tab>'
inoremap <expr> <S-Tab> pumvisible() ? '<C-p>' : '<S-Tab>'

"" Context-aware commenting
map <expr> gc &ft == 'vim' ? 'I" <Esc>' : 'gcc'

"" File-type specific formatters
map <expr> <leader>= &ft == 'json' ? ':action ReformatCode<CR>' : &ft == 'xml' ? ':action ReformatCode<CR>' : 'gg=G<C-o><C-o>'
```

## 🌟 Community-Driven Innovations

### Input Source Management (Multilingual Users)
```vim
"" Automatically switch to English in normal mode (for non-English keyboards)
autocmd InsertLeave * :silent !osascript -e 'tell application "System Events" to key code 49 using command down' >/dev/null 2>&1

"" Alternative for different systems
if has('mac')
    autocmd InsertLeave * :silent !osascript -e 'tell application "System Events" to key code 49 using command down'
endif
```

### Advanced Folding Techniques
```vim
"" Custom folding method based on indentation
set foldmethod=indent
set foldlevel=99

"" Smart folding for different file types
autocmd FileType python setlocal foldmethod=indent
autocmd FileType javascript,typescript setlocal foldmethod=syntax
autocmd FileType vim setlocal foldmethod=marker

"" Folding shortcuts
nnoremap <leader>za za
nnoremap <leader>zc zc
nnoremap <leader>zo zo
nnoremap <leader>zr zR
nnoremap <leader>zm zM
```

### External Tool Integration
```vim
"" LazyGit integration
if executable('lazygit')
    nnoremap <leader>gg :action Terminal.OpenInTerminal<CR>lazygit<CR>
endif

"" External IDE shortcuts
nnoremap <leader>ve :action Tool_External Tools_Open in Sublime Text<CR>
nnoremap <leader>vv :action Tool_External Tools_Open in VSCode<CR>

"" Open terminal in current file directory
nnoremap <leader>t :action Terminal.OpenInTerminal<CR>
```

### Advanced Clipboard Management
```vim
"" Enhanced clipboard operations
vnoremap <leader>y "+y
vnoremap <leader>d "+d
nnoremap <leader>p "+p
nnoremap <leader>P "+P

"" Paste without overwriting register
vnoremap <leader>P "0p
vnoremap <leader>p "0P

"" System clipboard shortcuts
nnoremap <C-c> "+yy
vnoremap <C-c> "+y
```

### Smart Error Navigation
```vim
"" Enhanced error navigation with centering
nnoremap <leader>x :action GotoNextError<CR>zz
nnoremap <leader>X :action GotoPreviousError<CR>zz

"" Quick error description
nnoremap <leader>ee :action ShowErrorDescription<CR>

"" Error list navigation
nnoremap <leader>el :action ActivateProblemsViewToolWindow<CR>
```

## 🎨 Enhanced Mapping Patterns

### Unimpaired-Style Mappings
```vim
"" Unimpaired-inspired navigation patterns
nnoremap [q :action PreviousOccurence<CR>
nnoremap ]q :action NextOccurence<CR>
nnoremap [e :action GotoPreviousError<CR>
nnoremap ]e :action GotoNextError<CR>
nnoremap [m :action MethodUp<CR>
nnoremap ]m :action MethodDown<CR>
nnoremap [c :action VcsShowPrevChangeMarker<CR>
nnoremap ]c :action VcsShowNextChangeMarker<CR>

"" Line manipulation
nnoremap [<space> O<esc>j
nnoremap ]<space> o<esc>k
```

### Advanced Leader Key Organization
```vim
"" Extended mnemonic groupings
let g:WhichKey_KeysOfGroups = {
  \ '<leader>b': 'Buffer/Bookmark',
  \ '<leader>c': 'Code',
  \ '<leader>d': 'Debug',
  \ '<leader>f': 'File',
  \ '<leader>g': 'Git',
  \ '<leader>h': 'Help/Documentation',
  \ '<leader>j': 'Jump',
  \ '<leader>l': 'LSP/Language',
  \ '<leader>p': 'Project',
  \ '<leader>r': 'Refactor/Run',
  \ '<leader>s': 'Search',
  \ '<leader>t': 'Test/Terminal',
  \ '<leader>w': 'Window',
  \ '<leader>x': 'Errors/Problems',
  \ '<leader>z': 'Folding/Zoom'
  \ }

"" Buffer operations
nnoremap <leader>bd :action CloseContent<CR>
nnoremap <leader>bn :action NextTab<CR>
nnoremap <leader>bp :action PreviousTab<CR>
nnoremap <leader>bl :action RecentFiles<CR>

"" Language server operations
nnoremap <leader>lr :action RenameElement<CR>
nnoremap <leader>lf :action ReformatCode<CR>
nnoremap <leader>li :action OptimizeImports<CR>
nnoremap <leader>ld :action ShowUsages<CR>

"" Help and documentation
nnoremap <leader>hh :action QuickJavaDoc<CR>
nnoremap <leader>hk :action ShowShortcuts<CR>
nnoremap <leader>ha :action HelpTopics<CR>
```

### Context-Sensitive IDE Mappings
```vim
"" IDE-specific conditional mappings
if &ide =~? 'intellij'
    nnoremap <leader>rf :action RunClass<CR>
    nnoremap <leader>rd :action DebugClass<CR>
    nnoremap <leader>rc :action RunConfiguration<CR>
elseif &ide =~? 'webstorm'
    nnoremap <leader>rf :action Run<CR>
    nnoremap <leader>rd :action Debug<CR>
    nnoremap <leader>rs :action Stop<CR>
    nnoremap <leader>rn :action RunNpm<CR>
elseif &ide =~? 'pycharm'
    nnoremap <leader>rf :action RunFile<CR>
    nnoremap <leader>rd :action DebugClass<CR>
    nnoremap <leader>rc :action RunConsole<CR>
endif

"" Language-specific mappings
autocmd FileType python nnoremap <buffer> <leader>ri :action Repl.Execute<CR>
autocmd FileType javascript,typescript nnoremap <buffer> <leader>ri :action RunJsbtTask<CR>
autocmd FileType java nnoremap <buffer> <leader>ri :action Repl.Execute<CR>
```

### Smart Movement Patterns
```vim
"" Enhanced text object movements
onoremap ih :<C-u>execute "normal! ?^==\\+$\r:nohlsearch\rkvg_"<CR>
onoremap ah :<C-u>execute "normal! ?^==\\+$\r:nohlsearch\rg_vk0"<CR>

"" Function boundaries
nnoremap [f :action MethodUp<CR>
nnoremap ]f :action MethodDown<CR>
nnoremap <leader>jf :action GotoDeclaration<CR>
nnoremap <leader>ji :action GotoImplementation<CR>

"" Smart paragraph movement
nnoremap { ?^$<CR>:nohlsearch<CR>
nnoremap } /^$<CR>:nohlsearch<CR>
```

## 🏆 Production-Ready Community Examples

### Professional Developer Configuration
```vim
"" Complete professional setup
let mapleader = " "
let maplocalleader = ","

"" Core productivity settings
set scrolloff=8
set sidescrolloff=8
set number relativenumber
set clipboard+=unnamed
set ignorecase smartcase
set incsearch hlsearch
set visualbell t_vb=

"" Essential plugins
set surround
set commentary  
set highlightedyank
set easymotion
set which-key
set sneak
set NERDTree

"" Professional key mappings
nnoremap <leader>ff :action GotoFile<CR>
nnoremap <leader>fg :action SearchEverywhere<CR>
nnoremap <leader>fb :action RecentFiles<CR>
nnoremap <leader>fs :action GotoSymbol<CR>

"" Git workflow
nnoremap <leader>gs :action Vcs.Show.Local.Changes<CR>
nnoremap <leader>gc :action CheckinProject<CR>
nnoremap <leader>gp :action Vcs.Push<CR>
nnoremap <leader>gl :action Vcs.UpdateProject<CR>
nnoremap <leader>gd :action Compare.SameVersion<CR>

"" Testing workflow
nnoremap <leader>tt :action RunConfiguration<CR>
nnoremap <leader>tf :action RerunFailedTests<CR>
nnoremap <leader>ta :action RunAllTests<CR>
nnoremap <leader>tc :action RunCoverage<CR>

"" Debugging
nnoremap <leader>dd :action Debug<CR>
nnoremap <leader>db :action ToggleLineBreakpoint<CR>
nnoremap <leader>dc :action Resume<CR>
nnoremap <leader>ds :action Stop<CR>
```

### Team Configuration Template
```vim
"" Team-friendly .ideavimrc template
"" Leader key - must be consistent across team
let mapleader = " "

"" Team standard settings
set scrolloff=5
set showmode
set showcmd
set smartcase
set incsearch
set visualbell
set clipboard+=unnamed

"" Required plugins for team workflow
set surround
set commentary
set highlightedyank
set which-key

"" Standard team mappings
nnoremap <leader>a :action GotoAction<CR>
nnoremap <leader>f :action GotoFile<CR>
nnoremap <leader>c :action GotoClass<CR>
nnoremap <leader>s :action GotoSymbol<CR>
nnoremap <leader>r :action RecentFiles<CR>

"" Code review workflow
nnoremap <leader>gd :action Compare.SameVersion<CR>
nnoremap <leader>gh :action Vcs.ShowTabbedFileHistory<CR>
nnoremap <leader>gb :action Annotate<CR>

"" Consistent refactoring
nnoremap <leader>rn :action RenameElement<CR>
nnoremap <leader>rm :action ExtractMethod<CR>
nnoremap <leader>rv :action IntroduceVariable<CR>

"" Error navigation
nnoremap <leader>e :action GotoNextError<CR>
nnoremap <leader>E :action GotoPreviousError<CR>
```

### Plugin Requirements Checklist

#### Required Plugin Installations
- **IdeaVim** (base plugin)
- **IdeaVim-EasyMotion** (for enhanced navigation)
- **AceJump** (required dependency for EasyMotion)

#### Installation Steps
1. Open **Settings** → **Plugins**
2. Search and install: "IdeaVim"
3. Search and install: "IdeaVim-EasyMotion"  
4. Search and install: "AceJump"
5. Restart IDE
6. Configure `.ideavimrc` with settings above

### Configuration Validation
```vim
"" Add to end of .ideavimrc for debugging
echo "IdeaVim configuration loaded successfully!"

"" Test essential mappings
nnoremap <leader>test :echo "Leader key working: " . mapleader<CR>
```

## 🔄 Configuration Migration Guide

### From Basic to Advanced Setup
1. **Backup current `.ideavimrc`**
2. **Add leader key at top** (if not already present)
3. **Add plugins gradually** (don't add all at once)
4. **Test each plugin** before adding the next
5. **Resolve conflicts** using Vim Emulation settings
6. **Add IDE actions** using `<Action>()` syntax

### Common Migration Issues
- **Plugin order matters**: Leader key must come first
- **EasyMotion needs AceJump**: Install both plugins
- **Conflicts break functionality**: Use Vim Emulation settings
- **Action IDs change**: Use action tracking to find current IDs

## 📚 Expert Tips

### Performance Optimization
```vim
"" Performance settings for large files
set ideawrite=all                    " Save all files automatically
set ideastatusicon=gray             " Show IdeaVim status in icon
set ideavimsupport=                 " Disable IdeaVim in dialog editors
```

### Advanced Customization
```vim
"" Custom text objects (advanced)
vnoremap il :<C-u>normal! ^v$h<CR>   " Inner line (without whitespace)
vnoremap al :<C-u>normal! 0v$<CR>    " A line (with whitespace)

"" Custom operators
nnoremap <leader>y "+y               " Copy to system clipboard
vnoremap <leader>y "+y               " Copy selection to system clipboard
nnoremap <leader>p "+p               " Paste from system clipboard
```

### Troubleshooting Common Issues

#### Issue: EasyMotion not working
**Solution**: 
1. Verify both IdeaVim-EasyMotion AND AceJump are installed
2. Check that `set easymotion` comes AFTER `let mapleader = " "`
3. Restart IDE after plugin installation

#### Issue: Which-Key not showing
**Solution**:
1. Ensure `set which-key` is in `.ideavimrc`
2. Check delay setting: `let g:WhichKey_DefaultDelay = 0`
3. Verify leader key is set correctly

#### Issue: IDE actions not working
**Solution**:
1. Enable action ID tracking: `Ctrl+Shift+A` → "IdeaVim: Track Action Ids"
2. Perform action to get correct ID
3. Update mapping with correct action ID

## 🎯 Your Current Setup Analysis

Based on your existing configuration, you already follow many 2024 best practices:

### ✅ What You're Doing Right
- Space leader key (industry standard)
- Comprehensive plugin setup
- Mnemonic groupings for shortcuts
- Which-Key integration
- Proper Vim settings

### 🔧 Recommended Enhancements
1. **Add more `<Action>()` mappings** for IDE integration
2. **Review Vim Emulation settings** for conflict resolution
3. **Verify plugin installations** (especially EasyMotion + AceJump)
4. **Add IDE-specific conditionals** for WebStorm features
5. **Implement conflict-free alternatives** for common shortcuts

Your setup is already sophisticated and follows modern best practices. The main opportunities are in deeper IDE integration and conflict optimization.

## 🌍 Community Insights & Modern Workflows

### Key Takeaways from GitHub Community (2024)
Based on analysis of the active [JetBrains IdeaVim discussions](https://github.com/JetBrains/ideavim/discussions/303):

1. **Expression Mappings (`map <expr>`)**: The most innovative 2024 feature for context-aware keybindings
2. **Multi-IDE Compatibility**: Use conditional mappings for different JetBrains IDEs
3. **Advanced Text Objects**: Community plugins like `mini.ai` and `textobj-function` are game-changers
4. **Input Source Management**: Essential for international developers with non-English keyboards
5. **Unimpaired-Style Navigation**: `[` and `]` prefixes for paired operations are becoming standard
6. **Professional Team Configurations**: Standardized setups across development teams

### Modern Plugin Ecosystem (2024)
The community has moved beyond basic plugins to sophisticated text manipulation:
- **Peekaboo**: Register contents visualization
- **Mini.ai**: Enhanced text objects with improved semantics
- **Function/Indent Objects**: Precise code structure navigation
- **Advanced Folding**: Language-specific folding strategies

### Production Best Practices from Active Developers
- **Gradual Migration**: Add plugins incrementally to avoid overwhelming muscle memory
- **Team Standardization**: Consistent `.ideavimrc` templates for collaborative development
- **IDE-Specific Optimization**: Leverage each JetBrains IDE's unique capabilities
- **Expression-Based Logic**: Use `<expr>` mappings for intelligent, adaptive keybindings
- **Community Learning**: Regular engagement with GitHub discussions for latest innovations

Your existing configuration already incorporates many of these modern practices, positioning you well for 2024's IdeaVim ecosystem evolution.

---

*This enhanced guide represents 2024 best practices compiled from official JetBrains documentation, active community expertise, GitHub discussions, and current plugin development standards.*