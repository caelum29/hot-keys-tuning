# IdeaVim Expression Mappings Examples & Advanced Ideas

*Comprehensive collection of dynamic, conditional mappings for modern development workflows*

## 🎯 **What Are Expression Mappings?**

Expression mappings (`map <expr>`) transform static keybindings into **intelligent, context-aware commands** that adapt their behavior based on current state, file type, cursor position, and more.

### **Basic Syntax**
```vim
map <expr> {key} {expression-that-returns-string}
```

The expression is **evaluated every time** the key is pressed, returning different commands based on current context.

---

## 🚀 **Essential Expression Mapping Patterns**

### **1. Mode-Aware Paste**
```vim
" Smart paste that adapts to current mode
map <expr> <leader>p mode() == 'i' ? '<C-r>+' : '"+p'
map <expr> <leader>P mode() == 'i' ? '<C-r>*' : '"*p'
```

### **2. Context-Sensitive Navigation**
```vim
" Navigation that respects word wrap
map <expr> j (v:count == 0 ? 'gj' : 'j')
map <expr> k (v:count == 0 ? 'gk' : 'k')

" Smart home/end
map <expr> <Home> col('.') == 1 ? '^' : '0'
map <expr> <End> col('.') == col('$') ? 'g_' : '$'
```

### **3. Intelligent Completion**
```vim
" Smart tab completion
inoremap <expr> <Tab> pumvisible() ? '<C-n>' : '<Tab>'
inoremap <expr> <S-Tab> pumvisible() ? '<C-p>' : '<S-Tab>'

" Smart enter for completion
inoremap <expr> <CR> pumvisible() ? '<C-y>' : '<CR>'
```

---

## 🏗️ **File-Type Specific Intelligence**

### **1. Language Runners**
```vim
" Dynamic file runner based on file type
map <expr> <leader>r &ft == 'python' ? ':!python %<CR>' :
                   \ &ft == 'javascript' ? ':!node %<CR>' :
                   \ &ft == 'typescript' ? ':!npx ts-node %<CR>' :
                   \ &ft == 'go' ? ':!go run %<CR>' :
                   \ &ft == 'rust' ? ':!cargo run<CR>' :
                   \ &ft == 'java' ? ':!javac % && java %:r<CR>' :
                   \ &ft == 'php' ? ':!php %<CR>' :
                   \ &ft == 'ruby' ? ':!ruby %<CR>' :
                   \ ':echo "No runner for " . &ft<CR>'

" REPL integration
map <expr> <leader>R &ft == 'python' ? ':action Console.Open<CR>' :
                   \ &ft == 'javascript' ? ':action JavaScriptDebugger.Console<CR>' :
                   \ &ft == 'scala' ? ':action Scala.RunWorksheet<CR>' :
                   \ ':action Console.Open<CR>'
```

### **2. Smart Formatters**
```vim
" File-type specific formatting
map <expr> <leader>= &ft == 'json' ? ':action ReformatCode<CR>' :
                   \ &ft == 'xml' ? ':action ReformatCode<CR>' :
                   \ &ft == 'html' ? ':action ReformatCode<CR>' :
                   \ &ft == 'css' ? ':action ReformatCode<CR>' :
                   \ &ft == 'sql' ? ':action DatabaseView.FormatSql<CR>' :
                   \ &ft == 'markdown' ? 'gqap' :
                   \ 'gg=G<C-o><C-o>'
```

### **3. Language-Specific Comments**
```vim
" Smart commenting based on file type
map <expr> <leader>/ &ft == 'vim' ? 'I" <Esc>' :
                   \ &ft == 'python' ? 'I# <Esc>' :
                   \ &ft == 'javascript' ? 'I// <Esc>' :
                   \ &ft == 'css' ? 'I/* <Esc>A */<Esc>' :
                   \ &ft == 'html' ? 'I<!-- <Esc>A --><Esc>' :
                   \ 'gcc'
```

---

## 🏢 **IDE Integration Patterns**

### **1. IDE-Specific Actions**
```vim
" Different actions for different JetBrains IDEs
map <expr> <leader>d &ide =~? 'intellij' ? ':action Debug<CR>' :
                   \ &ide =~? 'webstorm' ? ':action Javascript.Debugger.Start<CR>' :
                   \ &ide =~? 'pycharm' ? ':action Debug<CR>' :
                   \ &ide =~? 'phpstorm' ? ':action PhpDebugger.Start<CR>' :
                   \ ':action Debug<CR>'

" Navigation based on IDE
map <expr> <leader>f &ide =~? 'intellij' ? ':action GotoClass<CR>' :
                   \ &ide =~? 'webstorm' ? ':action GotoFile<CR>' :
                   \ &ide =~? 'datagrip' ? ':action GotoTable<CR>' :
                   \ ':action GotoFile<CR>'
```

### **2. Project-Context Awareness**
```vim
" Build system detection
map <expr> <leader>b filereadable('package.json') ? ':action Npm.Build<CR>' :
                   \ filereadable('pom.xml') ? ':action Maven.Compile<CR>' :
                   \ filereadable('build.gradle') ? ':action Gradle.Build<CR>' :
                   \ filereadable('Cargo.toml') ? ':action Rust.Cargo.Build<CR>' :
                   \ filereadable('CMakeLists.txt') ? ':action CMake.Build<CR>' :
                   \ ':action CompileProject<CR>'

" Test runner selection
map <expr> <leader>t filereadable('jest.config.js') ? ':action Jest.Run<CR>' :
                   \ filereadable('pytest.ini') ? ':action Python.RunPytest<CR>' :
                   \ filereadable('phpunit.xml') ? ':action PhpUnit.Run<CR>' :
                   \ ':action RunClass<CR>'
```

---

## 🧠 **Advanced Context Intelligence**

### **1. Cursor Position Logic**
```vim
" Smart line operations based on cursor position
map <expr> o line('.') == line('$') ? 'o' : 'o<Esc>S'
map <expr> O line('.') == 1 ? 'O' : 'O<Esc>S'

" Beginning/end of line awareness
map <expr> I col('.') == 1 ? 'I' : '^i'
map <expr> A col('.') == col('$') - 1 ? 'A' : '$a'

" Smart delete to beginning/end
map <expr> D col('.') == col('$') ? 'dd' : 'D'
map <expr> C col('.') == col('$') ? 'S' : 'C'
```

### **2. Buffer State Awareness**
```vim
" Window management based on window count
map <expr> <C-h> winnr('$') > 1 ? '<C-w>h' : ':bprev<CR>'
map <expr> <C-l> winnr('$') > 1 ? '<C-w>l' : ':bnext<CR>'
map <expr> <C-j> winnr('$') > 1 ? '<C-w>j' : ':bbelow<CR>'
map <expr> <C-k> winnr('$') > 1 ? '<C-w>k' : ':babove<CR>'

" Tab vs space awareness
map <expr> <leader>i &expandtab ? ':set noexpandtab<CR>' : ':set expandtab<CR>'
```

### **3. Git Context Intelligence**
```vim
" Branch-aware operations (requires function)
function! GitBranch()
  return system('git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "none"')
endfunction

map <expr> <leader>g GitBranch() =~# 'main\|master' ? 
                  \ ':echo "On main branch - be careful!"<CR>' :
                  \ ':action CheckinProject<CR>'

" Git status awareness
map <expr> <leader>s system('git status --porcelain 2>/dev/null') == '' ?
                   \ ':echo "Working tree clean"<CR>' :
                   \ ':action Vcs.Show.Local.Changes<CR>'
```

---

## 🔧 **Development Workflow Patterns**

### **1. Environment-Aware Operations**
```vim
" Environment detection
map <expr> <leader>e $NODE_ENV == 'development' ? 
                   \ ':action ShowLogs<CR>' :
                   \ $NODE_ENV == 'production' ?
                   \ ':echo "Production - logs restricted"<CR>' :
                   \ ':action ShowEnvironment<CR>'

" Debug vs Release builds
map <expr> <leader>B exists('g:debug_mode') && g:debug_mode ?
                   \ ':action BuildDebug<CR>' :
                   \ ':action BuildRelease<CR>'
```

### **2. Plugin State Awareness**
```vim
" NERDTree toggle with state awareness
map <expr> <leader>n exists('g:loaded_nerdtree') && g:NERDTree.IsOpen() ?
                   \ ':NERDTreeClose<CR>' :
                   \ ':NERDTreeToggle<CR>'

" Git gutter toggle
map <expr> <leader>G exists('g:gitgutter_enabled') && g:gitgutter_enabled ?
                   \ ':GitGutterDisable<CR>' :
                   \ ':GitGutterEnable<CR>'
```

### **3. Smart Error Navigation**
```vim
" Error navigation with context
map <expr> ]e getqflist() == [] ? 
           \ ':action GotoNextError<CR>' :
           \ ':cnext<CR>'

map <expr> [e getqflist() == [] ? 
           \ ':action GotoPreviousError<CR>' :
           \ ':cprev<CR>'
```

---

## 🎨 **Creative Expression Patterns**

### **1. Time-Based Mappings**
```vim
" Time-aware greetings
map <expr> <leader>h strftime('%H') < 12 ? 
                   \ ':echo "Good morning!"<CR>' :
                   \ strftime('%H') < 18 ?
                   \ ':echo "Good afternoon!"<CR>' :
                   \ ':echo "Good evening!"<CR>'
```

### **2. Random Behavior**
```vim
" Random quote or tip
map <expr> <leader>q rand() % 2 ? 
                   \ ':echo "Tip: Use . to repeat last command"<CR>' :
                   \ ':echo "Remember: You are awesome!"<CR>'
```

### **3. Progressive Disclosure**
```vim
" Help that adapts to experience level
let g:vim_experience = 0
map <expr> <F1> g:vim_experience < 5 ? 
                \ ':action ShowVimTutorial<CR>' :
                \ g:vim_experience < 20 ?
                \ ':action ShowAdvancedHelp<CR>' :
                \ ':action ShowExpertTips<CR>'
```

---

## 🛠️ **Helper Functions for Complex Logic**

### **1. File Detection Helper**
```vim
function! DetectProjectType()
  if filereadable('package.json')
    return 'node'
  elseif filereadable('pom.xml')
    return 'maven'
  elseif filereadable('Cargo.toml')
    return 'rust'
  elseif filereadable('go.mod')
    return 'go'
  else
    return 'unknown'
  endif
endfunction

map <expr> <leader>P ':echo "Project: ' . DetectProjectType() . '"<CR>'
```

### **2. Smart Word Detection**
```vim
function! SmartWordMotion()
  let current_word = expand('<cword>')
  if current_word =~ '\u\l' " CamelCase
    return 'w'
  elseif current_word =~ '_'  " snake_case
    return 'W'
  else
    return 'w'
  endif
endfunction

map <expr> w SmartWordMotion()
```

### **3. Context Stack Helper**
```vim
let g:context_stack = []

function! PushContext()
  call add(g:context_stack, {'file': expand('%'), 'pos': getpos('.')})
  return ':echo "Context pushed"<CR>'
endfunction

function! PopContext()
  if !empty(g:context_stack)
    let ctx = remove(g:context_stack, -1)
    exec 'edit ' . ctx.file
    call setpos('.', ctx.pos)
    return ''
  endif
  return ':echo "Context stack empty"<CR>'
endfunction

map <expr> <leader>[ PushContext()
map <expr> <leader>] PopContext()
```

---

## 💡 **Best Practices & Tips**

### **1. Performance Considerations**
```vim
" Cache expensive operations
let g:project_type_cache = ''
function! GetProjectType()
  if g:project_type_cache == ''
    let g:project_type_cache = DetectProjectType()
  endif
  return g:project_type_cache
endfunction
```

### **2. Debugging Expression Mappings**
```vim
" Debug helper for expression mappings
function! DebugExpr(expr_result)
  echom 'Expression result: ' . a:expr_result
  return a:expr_result
endfunction

" Use in mappings for debugging
map <expr> <leader>d DebugExpr(':action Debug<CR>')
```

### **3. Fallback Patterns**
```vim
" Always provide fallbacks
map <expr> <leader>r has_key(g:runners, &ft) ? 
                   \ ':!' . g:runners[&ft] . ' %<CR>' :
                   \ ':echo "No runner for " . &ft<CR>'
```

---

## 🌟 **Advanced Integration Ideas**

### **1. API Integration**
```vim
" Weather-based productivity advice (requires external command)
map <expr> <leader>w system('curl -s wttr.in/?format="%t"') =~ '[0-9]\+' ?
                   \ ':echo "Perfect coding weather!"<CR>' :
                   \ ':echo "Stay focused!"<CR>'
```

### **2. Machine Learning Context**
```vim
" Suggest next action based on recent commands (conceptual)
function! SuggestNextAction()
  " Analyze command history and suggest next likely action
  " This would require implementing ML logic
  return ':echo "Suggested: refactor variable"<CR>'
endfunction

map <expr> <leader>? SuggestNextAction()
```

### **3. Team Integration**
```vim
" Pair programming awareness
let g:pairing_mode = 0
map <expr> <leader>pair g:pairing_mode ? 
                      \ 'let g:pairing_mode=0 | echo "Solo mode"<CR>' :
                      \ 'let g:pairing_mode=1 | echo "Pair mode"<CR>'

" Adjust behavior for pairing
map <expr> <leader>c g:pairing_mode ? 
                   \ ':echo "Explaining: " | :action ShowQuickDocumentation<CR>' :
                   \ ':action CommentByLineComment<CR>'
```

---

## 🔮 **Future-Proof Patterns**

Expression mappings represent the evolution from static keybindings to **intelligent, adaptive interfaces**. These patterns enable:

- **Context awareness** that reduces cognitive load
- **Adaptive behavior** that learns your workflow
- **Intelligent automation** that prevents errors
- **Dynamic tooling** that evolves with your needs

Master these patterns to transform your IdeaVim setup from a simple editor into a **contextually aware development assistant**.

---

*This collection represents cutting-edge expression mapping techniques for modern development workflows. Start with simple patterns and gradually build complexity as you become comfortable with the concepts.*