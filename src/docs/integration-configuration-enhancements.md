# Integration Configuration Enhancements

*Specific configuration snippets for implementing the unified keyboard productivity system*

## Table of Contents

1. [Karabiner-Elements Enhancements](#karabiner-elements-enhancements)
2. [WebStorm Keymap Enhancements](#webstorm-keymap-enhancements) 
3. [IdeaVim Configuration Enhancements](#ideavim-configuration-enhancements)
4. [Configuration Templates](#configuration-templates)
5. [Testing Configurations](#testing-configurations)

---

## Karabiner-Elements Enhancements

### **WebStorm-Specific Integration Rules**

Add these rules to your existing sophisticated Karabiner configuration to enhance WebStorm integration:

```json
{
  "description": "WebStorm Development Enhancement",
  "manipulators": [
    {
      "description": "Hyper + Semicolon → AceJump in WebStorm",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "semicolon",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option"] }
      },
      "to": [{ "key_code": "semicolon", "modifiers": ["control"] }],
      "type": "basic"
    },
    {
      "description": "Hyper + Slash → Comment Toggle in WebStorm",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "slash",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option"] }
      },
      "to": [{ "key_code": "slash", "modifiers": ["command"] }],
      "type": "basic"
    },
    {
      "description": "Hyper + R → Run in WebStorm",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "r",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_control"] }
      },
      "to": [{ "key_code": "r", "modifiers": ["control"] }],
      "type": "basic"
    },
    {
      "description": "Hyper + D → Debug in WebStorm", 
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "d",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_control"] }
      },
      "to": [{ "key_code": "d", "modifiers": ["control"] }],
      "type": "basic"
    },
    {
      "description": "Hyper + Shift + R → Run Coverage in WebStorm",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "r", 
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_shift"] }
      },
      "to": [{ "key_code": "r", "modifiers": ["control", "shift"] }],
      "type": "basic"
    }
  ]
}
```

### **Enhanced Git Integration via Karabiner**

```json
{
  "description": "Git Operations WebStorm Integration",
  "manipulators": [
    {
      "description": "Hyper + G + C → Git Commit (Cmd+K)",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "c",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_command"] }
      },
      "to": [{ "key_code": "k", "modifiers": ["command"] }],
      "type": "basic"
    },
    {
      "description": "Hyper + G + P → Git Push (Cmd+Shift+K)", 
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "p",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_command"] }
      },
      "to": [{ "key_code": "k", "modifiers": ["command", "shift"] }],
      "type": "basic"
    },
    {
      "description": "Hyper + G + L → Git Log (Cmd+9)",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "l",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_command"] }
      },
      "to": [{ "key_code": "9", "modifiers": ["command"] }],
      "type": "basic"
    },
    {
      "description": "Hyper + G + D → Git Diff (Cmd+Shift+Alt+D)",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "d",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_command"] }
      },
      "to": [{ "key_code": "d", "modifiers": ["command", "shift", "option"] }],
      "type": "basic"
    }
  ]
}
```

### **Testing Workflow Enhancement**

```json
{
  "description": "Testing Operations WebStorm Integration",
  "manipulators": [
    {
      "description": "Hyper + T + R → Run Tests",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "r",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_control"] }
      },
      "to": [{ "key_code": "r", "modifiers": ["control"] }],
      "type": "basic"
    },
    {
      "description": "Hyper + T + D → Debug Tests",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "d",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_control"] }
      },
      "to": [{ "key_code": "d", "modifiers": ["control"] }],
      "type": "basic"  
    },
    {
      "description": "Hyper + T + F → Rerun Failed Tests",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "f",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_control"] }
      },
      "to": [{ "key_code": "f", "modifiers": ["control", "shift"] }],
      "type": "basic"
    }
  ]
}
```

### **Code Generation Enhancement**

```json
{
  "description": "Code Generation WebStorm Integration",
  "manipulators": [
    {
      "description": "Hyper + C + G → Generate Menu (Cmd+N)",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "g",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_control"] }
      },
      "to": [{ "key_code": "n", "modifiers": ["command"] }],
      "type": "basic"
    },
    {
      "description": "Hyper + C + C → Generate Constructor",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "c",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option", "left_control"] }
      },
      "to": [{ "key_code": "c", "modifiers": ["command", "shift"] }],
      "type": "basic"
    }
  ]
}
```

## WebStorm Keymap Enhancements

### **Priority 1: Git Integration Shortcuts**

Add these to your WebStorm keymap (`macOS copy1`):

| Action | Current Shortcut | New Shortcut | Reason |
|--------|------------------|--------------|---------|
| **Check-in Project** | None (disabled) | `Cmd+K` | Standard Git commit |
| **Git Push** | None (disabled) | `Cmd+Shift+K` | Logical progression from commit |
| **Git Log** | None | `Cmd+9` | Quick access, consistent with tool window pattern |
| **Git Branches** | None | `Ctrl+Shift+\`` | Easy access for branch switching |
| **Show Changes** | None | `Cmd+Shift+Alt+D` | Visual diff access |
| **Annotate** | None | `Cmd+Alt+A` | Git blame integration |
| **Show History** | None | `Cmd+Alt+H` | File history access |

### **Priority 2: Testing Workflow**

| Action | New Shortcut | Integration |
|--------|--------------|-------------|
| **Run Configuration** | `Cmd+R` | Works with Karabiner `Hyper+Ctrl+R` |
| **Debug Configuration** | `Cmd+D` | Works with Karabiner `Hyper+Ctrl+D` |
| **Run Class** | `Ctrl+R` | Context-specific running |
| **Debug Class** | `Ctrl+D` | Context-specific debugging |
| **Run Coverage** | `Ctrl+Shift+R` | Enhanced testing |
| **Rerun Failed Tests** | `Ctrl+Shift+F` | Failure-focused testing |

### **Priority 3: Code Generation**

| Action | New Shortcut | Purpose |
|--------|--------------|---------|
| **Generate Menu** | `Cmd+N` | Primary code generation |
| **Generate Constructor** | `Cmd+Shift+C` | Quick constructor creation |
| **Generate Getter/Setter** | `Cmd+Shift+G` | Property generation |
| **Generate toString** | `Cmd+Shift+T` | Debug string generation |
| **Generate equals/hashCode** | `Cmd+Shift+E` | Object comparison methods |

### **Enhanced Navigation (Building on Existing)**

Keep your existing navigation enhancements and add:

| Action | Enhanced Shortcut | Integration Benefit |
|--------|-------------------|-------------------|
| **Go to File** | `Cmd+Shift+O` (existing) | Works with Karabiner navigation |
| **Go to Class** | `Cmd+O` | Quick class access |
| **Go to Symbol** | `Cmd+Alt+O` | Enhanced with universal navigation |
| **Search Everywhere** | `Double Shift` | Enhanced by system-level typing |

### **Window Management Simplification**

Replace complex `Shift+Ctrl+Alt+K/J/H/L` with simpler alternatives:

| Current Complex | New Simple | Karabiner Integration |
|----------------|------------|---------------------|
| `Shift+Ctrl+Alt+K` | `Cmd+Alt+Up` | Leverages system navigation |
| `Shift+Ctrl+Alt+J` | `Cmd+Alt+Down` | Consistent with system patterns |  
| `Shift+Ctrl+Alt+H` | `Cmd+Alt+Left` | Works with Hyper navigation |
| `Shift+Ctrl+Alt+L` | `Cmd+Alt+Right` | Seamless integration |

## IdeaVim Configuration Enhancements

### **Enhanced .ideavimrc for Integration**

Replace/enhance your existing `.ideavimrc` with these additions:

```vim
" === UNIFIED INTEGRATION ENHANCEMENTS ===
" Enhanced configuration for Karabiner + WebStorm + IdeaVim integration

" Leader key (keep existing)
let mapleader = " "

" === SYSTEM INTEGRATION ===

" Detect Karabiner enhancement and adapt behavior  
function! HasKarabinerEnhancement()
  return system('pgrep karabiner_console_user_server') != ''
endfunction

" Detect WebStorm context for intelligent behavior
function! IsWebStorm()
  return has('ide') && &ide =~? 'webstorm'
endfunction

" === ENHANCED NAVIGATION INTEGRATION ===

" Context-aware navigation that complements Karabiner
" These work WITH your existing Hyper+HJKL system navigation
map <expr> <leader>h IsWebStorm() ? ':action EditorLeft<CR>' : 'h'
map <expr> <leader>j IsWebStorm() ? ':action EditorDown<CR>' : 'j'  
map <expr> <leader>k IsWebStorm() ? ':action EditorUp<CR>' : 'k'
map <expr> <leader>l IsWebStorm() ? ':action EditorRight<CR>' : 'l'

" Enhanced word movement (complements Karabiner CapsLock+N/M)
map <expr> <leader>w IsWebStorm() ? ':action EditorNextWord<CR>' : 'w'
map <expr> <leader>b IsWebStorm() ? ':action EditorPreviousWord<CR>' : 'b'

" === GIT INTEGRATION (Priority 1) ===
" Complement Karabiner git shortcuts with IdeaVim actions

if IsWebStorm()
    " Git operations (work with Karabiner Hyper+G shortcuts)
    map <leader>gs :action Vcs.Show.Local.Changes<CR>
    map <leader>gd :action Compare.SameVersion<CR>  
    map <leader>gb :action Annotate<CR>
    map <leader>gh :action Vcs.ShowTabbedFileHistory<CR>
    map <leader>gf :action Git.Fetch<CR>
    map <leader>gu :action Vcs.UpdateProject<CR>
    map <leader>gr :action Vcs.RollbackChangedLines<CR>
    
    " Git branch operations
    map <leader>gB :action Git.Branches<CR>
    map <leader>gm :action Git.Merge<CR>
    map <leader>gt :action Git.Stash<CR>
    map <leader>gT :action Git.Unstash<CR>
endif

" === TESTING INTEGRATION (Priority 1) ===
" Enhanced testing workflow with Karabiner integration

if IsWebStorm()
    " Testing operations (work with Karabiner Hyper+T shortcuts)
    map <leader>tr :action RunClass<CR>
    map <leader>td :action DebugClass<CR>
    map <leader>tc :action RunCoverage<CR>
    map <leader>tf :action RerunFailedTests<CR>
    map <leader>ta :action RunAllTests<CR>
    map <leader>tt :action RunConfiguration<CR>
    
    " Test navigation
    map <leader>tn :action GotoNextError<CR>
    map <leader>tp :action GotoPreviousError<CR>
    map <leader>te :action ShowErrorDescription<CR>
endif

" === CODE GENERATION INTEGRATION (Priority 1) ===

if IsWebStorm()
    " Code generation (work with Karabiner Hyper+C shortcuts)
    map <leader>cg :action Generate<CR>
    map <leader>cc :action GenerateConstructor<CR>
    map <leader>ct :action GenerateToString<CR>
    map <leader>ce :action GenerateEquals<CR>
    map <leader>cgs :action GenerateGetterAndSetter<CR>
    map <leader>ci :action ImplementMethods<CR>
    map <leader>co :action OverrideMethods<CR>
endif

" === ENHANCED REFACTORING ===

if IsWebStorm()
    " Refactoring operations
    map <leader>rn :action RenameElement<CR>
    map <leader>rm :action ExtractMethod<CR>
    map <leader>rv :action IntroduceVariable<CR>
    map <leader>ri :action Inline<CR>
    map <leader>rs :action ChangeSignature<CR>
    map <leader>rp :action IntroduceParameter<CR>
    map <leader>rf :action IntroduceField<CR>
    map <leader>rc :action IntroduceConstant<CR>
endif

" === INTELLIGENT CONTEXT MAPPINGS ===

" Smart paste behavior that adapts to mode
map <expr> <leader>p mode() == 'i' ? '<C-r>+' : '"+p'
map <expr> <leader>P mode() == 'i' ? '<C-r>*' : '"*p'

" Context-sensitive search
map <expr> <leader>f &ft == 'typescript' ? ':action GotoTypeDeclaration<CR>' : ':action GotoDeclaration<CR>'

" Intelligent comment toggle 
map <expr> gc &ft == 'vim' ? 'I" <Esc>' : ':action CommentByLineComment<CR>'

" Smart bracket handling for different file types
inoremap <expr> { getline('.')[col('.')-1] =~ '\w' ? '{' : '{}<Left>'
inoremap <expr> [ getline('.')[col('.')-1] =~ '\w' ? '[' : '[]<Left>'
inoremap <expr> ( getline('.')[col('.')-1] =~ '\w' ? '(' : '()<Left>'

" === FILE TYPE SPECIFIC BEHAVIOR ===

" Dynamic behavior based on file type
map <expr> <leader>r &ft == 'javascript' ? ':action RunJsbtTask<CR>' :
                   \ &ft == 'typescript' ? ':action RunTsTask<CR>' :
                   \ &ft == 'python' ? ':action RunPython<CR>' :
                   \ IsWebStorm() ? ':action Run<CR>' :
                   \ ':echo "No runner configured"<CR>'

" Format code intelligently
map <expr> <leader>= &ft == 'json' ? ':action ReformatCode<CR>' :
                   \ &ft == 'xml' ? ':action ReformatCode<CR>' :
                   \ &ft == 'html' ? ':action ReformatCode<CR>' :
                   \ IsWebStorm() ? ':action ReformatCode<CR>' :
                   \ 'gg=G<C-o><C-o>'

" === ENHANCED WHICH-KEY INTEGRATION ===

" Update Which-Key groups for new mappings
let g:WhichKey_KeysOfGroups = {
  \ '<leader>g': 'Git',
  \ '<leader>r': 'Refactor/Run',
  \ '<leader>t': 'Test',
  \ '<leader>c': 'Code Generation',
  \ '<leader>w': 'Window',
  \ '<leader>f': 'Find/File',
  \ '<leader>s': 'Search',
  \ '<leader>a': 'Analysis',
  \ '<leader>d': 'Debug',
  \ '<leader>j': 'Jump',
  \ '<leader>h': 'Help/Documentation'
  \ }

" === SYSTEM INTEGRATION HELPERS ===

" Debug integration status
map <leader>debug :echo "Karabiner: " . (HasKarabinerEnhancement() ? "✓" : "✗") . 
                      \ " | WebStorm: " . (IsWebStorm() ? "✓" : "✗")<CR>

" Quick action finder (enhanced by system typing)
map <leader>a :action GotoAction<CR>

" === 2024 ADVANCED FEATURES INTEGRATION ===

if IsWebStorm()
    " Database tools (2024 feature)
    map <leader>dq :action Console.Open<CR>
    map <leader>dt :action ActivateDatabaseToolWindow<CR>
    
    " AI-powered features
    map <leader>ai :action ShowIntentionActions<CR>
    map <leader>ac :action AIAssistant.OpenChat<CR>
    
    " Advanced code analysis
    map <leader>an :action RunInspection<CR>
    map <leader>af :action ShowReformatFileDialog<CR>
    map <leader>ao :action OptimizeImports<CR>
endif

" === DEBUGGING HELPERS ===

" Show available actions for current context
map <leader>? :action ShowShortcuts<CR>

" Test leader key functionality  
map <leader><leader>test :echo "IdeaVim integration working! Leader: " . mapleader<CR>
```

### **Expression Mapping Examples for Advanced Users**

```vim
" === ADVANCED EXPRESSION MAPPINGS ===

" Time-aware greetings (fun but useful for mood)
map <expr> <leader>hello strftime('%H') < 12 ? 
                      \ ':echo "Good morning, ready to code!"<CR>' :
                      \ strftime('%H') < 18 ?
                      \ ':echo "Good afternoon, keep coding!"<CR>' :
                      \ ':echo "Good evening, almost done!"<CR>'

" Project-type detection and smart actions
function! DetectProjectType()
  if filereadable('package.json')
    return 'node'
  elseif filereadable('pom.xml')
    return 'maven'
  elseif filereadable('Cargo.toml') 
    return 'rust'
  else
    return 'unknown'
  endif
endfunction

map <expr> <leader>build DetectProjectType() == 'node' ? ':action Npm.Build<CR>' :
                       \ DetectProjectType() == 'maven' ? ':action Maven.Compile<CR>' :
                       \ ':action CompileProject<CR>'

" Smart word motion based on content
function! SmartWordMotion()
  let current_word = expand('<cword>')
  if current_word =~ '\u\l'  " CamelCase
    return ':action EditorNextWordInDifferentHumpsMode<CR>'
  elseif current_word =~ '_'  " snake_case
    return 'W'
  else
    return 'w'
  endif
endfunction

map <expr> <leader>w SmartWordMotion()
```

## Configuration Templates

### **Quick Setup Template for New Machines**

Create `~/keyboard-setup/install.sh`:

```bash
#!/bin/bash
# Unified Keyboard Productivity Setup Script

echo "🚀 Setting up unified keyboard productivity system..."

# 1. Backup existing configurations
echo "📦 Creating backups..."
mkdir -p ~/keyboard-backups/$(date +%Y%m%d)
cp ~/.config/karabiner/karabiner.json ~/keyboard-backups/$(date +%Y%m%d)/ 2>/dev/null || true
cp ~/.ideavimrc ~/keyboard-backups/$(date +%Y%m%d)/ 2>/dev/null || true

# 2. Install Karabiner-Elements if not present
if ! command -v karabiner &> /dev/null; then
    echo "🔧 Installing Karabiner-Elements..."
    brew install --cask karabiner-elements
fi

# 3. Copy enhanced configurations
echo "⚙️ Installing enhanced configurations..."
# (You would copy your enhanced config files here)

# 4. Restart Karabiner services
echo "🔄 Restarting Karabiner services..."
sudo launchctl kickstart -k system/com.pqrs.karabiner.karabiner_console_user_server

# 5. Validation
echo "✅ Setup complete! Please:"
echo "   1. Open WebStorm and verify IdeaVim is enabled"
echo "   2. Test CapsLock+H/J/K/L navigation" 
echo "   3. Test Space leader shortcuts in WebStorm"
echo "   4. Run integration tests from the guide"

echo "🎉 Unified keyboard productivity system installed!"
```

### **Configuration Validation Template**

Create `~/keyboard-setup/validate.sh`:

```bash
#!/bin/bash
# Validation script for integrated keyboard system

echo "🧪 Testing unified keyboard productivity integration..."

# Test 1: Karabiner running
echo "Testing Karabiner-Elements..."
if pgrep karabiner_console_user_server > /dev/null; then
    echo "✅ Karabiner-Elements is running"
else
    echo "❌ Karabiner-Elements not running"
    exit 1
fi

# Test 2: WebStorm bundle detection
echo "Testing WebStorm bundle ID detection..."
WEBSTORM_ID=$(osascript -e 'tell application "WebStorm" to get id' 2>/dev/null || echo "not_found")
if [[ "$WEBSTORM_ID" == "com.jetbrains.WebStorm" ]]; then
    echo "✅ WebStorm bundle ID detected correctly"
else
    echo "⚠️  WebStorm not running or bundle ID issue: $WEBSTORM_ID"
fi

# Test 3: IdeaVim configuration
echo "Testing IdeaVim configuration..."
if [[ -f ~/.ideavimrc ]]; then
    if grep -q "let mapleader" ~/.ideavimrc; then
        echo "✅ IdeaVim leader key configured"
    else
        echo "⚠️  IdeaVim leader key not found in config"
    fi
else
    echo "❌ IdeaVim configuration file not found"
fi

# Test 4: Configuration backup
echo "Testing backup system..."
if [[ -d ~/keyboard-backups ]]; then
    BACKUP_COUNT=$(ls ~/keyboard-backups | wc -l)
    echo "✅ Backup system ready ($BACKUP_COUNT backups available)"
else
    echo "⚠️  Backup directory not found - creating..."
    mkdir -p ~/keyboard-backups
fi

echo "🎯 Validation complete! Ready for integrated workflow."
```

## Testing Configurations

### **Integration Test Scenarios**

#### **Test 1: Basic Navigation Integration**
```bash
# Manual test procedure
echo "🧪 Test 1: Basic Navigation Integration"
echo "1. Open WebStorm with a project"
echo "2. Press CapsLock+H/J/K/L → Should move cursor globally"
echo "3. In WebStorm, press H/J/K/L in normal mode → Should work for Vim"
echo "4. Press Arrow keys → Should work normally (enhanced by Karabiner)"
echo "✅ Pass if all navigation feels smooth and consistent"
```

#### **Test 2: Leader Key Hierarchy**
```bash
echo "🧪 Test 2: Leader Key Hierarchy" 
echo "1. Press CapsLock+G → Should launch WebStorm (system level)"
echo "2. In WebStorm, press Space+f → Should open file finder (IdeaVim level)"
echo "3. Press Cmd+Shift+O → Should open WebStorm file search (IDE level)"
echo "✅ Pass if each leader context works independently"
```

#### **Test 3: Git Workflow Integration**
```bash
echo "🧪 Test 3: Git Workflow Integration"
echo "1. Make a file change in WebStorm"
echo "2. Press Space+gs → Should show local changes (IdeaVim)"
echo "3. Press Cmd+K → Should open commit dialog (WebStorm)" 
echo "4. Press Cmd+Shift+K → Should push changes (WebStorm)"
echo "✅ Pass if git workflow feels seamless"
```

#### **Test 4: Context Switching**
```bash
echo "🧪 Test 4: Context Switching"
echo "1. Switch between WebStorm and other apps using CapsLock shortcuts"
echo "2. Verify navigation works in both contexts"
echo "3. Check that WebStorm-specific shortcuts only work in WebStorm"
echo "4. Verify system shortcuts work everywhere"
echo "✅ Pass if context switching is seamless"
```

### **Automated Validation Script**

Create `~/keyboard-setup/test-integration.applescript`:

```applescript
-- AppleScript for automated integration testing
tell application "WebStorm"
    activate
    delay 1
end tell

-- Test basic WebStorm activation
if application "WebStorm" is running then
    display notification "WebStorm activated ✅" with title "Integration Test"
else
    display notification "WebStorm failed to activate ❌" with title "Integration Test"
end if

-- Test bundle ID detection
tell application "WebStorm"
    set webstormID to id
    if webstormID is "com.jetbrains.WebStorm" then
        display notification "Bundle ID correct ✅" with title "Integration Test"
    else
        display notification "Bundle ID incorrect ❌" with title "Integration Test"
    end if
end tell

-- You can extend this with more automated tests
```

### **Performance Testing**

```bash
#!/bin/bash
# Performance test for keyboard system integration

echo "⚡ Testing system performance with integration..."

# Test Karabiner CPU usage
echo "Testing Karabiner CPU usage..."
KARABINER_CPU=$(ps aux | grep karabiner_console_user_server | grep -v grep | awk '{print $3}')
echo "Karabiner CPU usage: ${KARABINER_CPU:-0}%"

if (( $(echo "$KARABINER_CPU < 5.0" | bc -l) )); then
    echo "✅ Karabiner CPU usage acceptable"
else
    echo "⚠️  Karabiner CPU usage high: $KARABINER_CPU%"
fi

# Test input latency (manual test)
echo "🖱️  Manual latency test:"
echo "1. Press CapsLock+H rapidly 10 times"
echo "2. Movement should feel instant (<100ms perceived)"
echo "3. If laggy, check Karabiner configuration complexity"

# Test memory usage
echo "Testing memory usage..."
KARABINER_MEM=$(ps aux | grep karabiner_console_user_server | grep -v grep | awk '{print $6}')
echo "Karabiner memory: ${KARABINER_MEM:-0}KB"

echo "✅ Performance testing complete"
```

---

This comprehensive configuration enhancement document provides all the specific code snippets, templates, and testing procedures needed to implement the unified keyboard productivity system successfully.