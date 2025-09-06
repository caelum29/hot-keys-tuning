# WebStorm Keybinding Enhancements

Based on analysis of your current `webstorm-keymaps.md` setup, here are recommended enhancements to improve your development workflow.

## 🎯 Priority 1: Quick Wins (High Impact, Easy to Add)

### Git Integration (Currently Missing)
Add these to your `.ideavimrc`:
```vim
" Git operations
nnoremap <leader>gc :action CheckinProject<CR>
nnoremap <leader>gp :action Vcs.Push<CR>
nnoremap <leader>gl :action Vcs.UpdateProject<CR>
nnoremap <leader>gd :action Compare.SameVersion<CR>
nnoremap <leader>gb :action Annotate<CR>
nnoremap <leader>gh :action Vcs.ShowTabbedFileHistory<CR>
nnoremap <leader>gs :action ChangesView.Refresh<CR>
nnoremap <leader>gf :action Git.Fetch<CR>
```

### Testing Shortcuts
```vim
" Testing operations
nnoremap <leader>tr :action RunClass<CR>
nnoremap <leader>tt :action RunConfiguration<CR>
nnoremap <leader>td :action DebugClass<CR>
nnoremap <leader>tc :action RunCoverage<CR>
nnoremap <leader>tf :action RerunFailedTests<CR>
```

### Code Generation
```vim
" Code generation
nnoremap <leader>cg :action Generate<CR>
nnoremap <leader>cc :action GenerateConstructor<CR>
nnoremap <leader>ct :action GenerateToString<CR>
nnoremap <leader>ce :action GenerateEquals<CR>
nnoremap <leader>cgs :action GenerateGetterAndSetter<CR>
```

## 🚀 Priority 2: Workflow Enhancements

### Enhanced Debugging
```vim
" Debug operations (complement your existing <Space>d)
nnoremap <leader>db :action ToggleLineBreakpoint<CR>
nnoremap <leader>dc :action Resume<CR>
nnoremap <leader>dn :action StepOver<CR>
nnoremap <leader>di :action StepInto<CR>
nnoremap <leader>do :action StepOut<CR>
nnoremap <leader>de :action EvaluateExpression<CR>
```

### Advanced Refactoring
```vim
" Refactoring operations
nnoremap <leader>rm :action ExtractMethod<CR>
nnoremap <leader>rv :action IntroduceVariable<CR>
nnoremap <leader>ri :action Inline<CR>
nnoremap <leader>rr :action RenameElement<CR>
nnoremap <leader>rs :action ChangeSignature<CR>
nnoremap <leader>rp :action IntroduceParameter<CR>
```

### Search & Replace Improvements
```vim
" Enhanced search operations
nnoremap <leader>sr :action ReplaceInPath<CR>
nnoremap <leader>sf :action FindInPath<CR>
nnoremap <leader>sp :action SearchEverywhere<CR>
nnoremap <leader>su :action FindUsages<CR>
nnoremap <leader>sh :action HighlightUsagesInFile<CR>
```

## 🎨 Priority 3: Ergonomic Improvements

### Simplified Window Management
Replace your complex `Shift + Ctrl + Alt + K/J/H/L` shortcuts:
```vim
" Window operations (simpler than current complex shortcuts)
nnoremap <leader>wk :action StretchSplitToTop<CR>
nnoremap <leader>wj :action StretchSplitToBottom<CR>
nnoremap <leader>wh :action StretchSplitToLeft<CR>
nnoremap <leader>wl :action StretchSplitToRight<CR>
nnoremap <leader>wm :action MaximizeEditorInSplit<CR>
nnoremap <leader>wu :action UnsplitAll<CR>
```

### Consistent Navigation Patterns
```vim
" Navigation improvements
nnoremap <leader>n :action FindNext<CR>
nnoremap <leader>N :action FindPrevious<CR>
nnoremap <leader>* :action FindWordAtCaret<CR>
nnoremap <leader>ji :action GotoImplementation<CR>
nnoremap <leader>jd :action GotoDeclaration<CR>
nnoremap <leader>jt :action GotoTypeDeclaration<CR>
```

## 🔧 Priority 4: Missing Modern Development Features

### Database Tools
```vim
" Database operations (complement your Big Data Tool Window)
nnoremap <leader>dq :action Console.Open<CR>
nnoremap <leader>dt :action ActivateDatabaseToolWindow<CR>
```

### Code Analysis
```vim
" Code quality operations
nnoremap <leader>ai :action RunInspection<CR>
nnoremap <leader>ac :action ReformatCode<CR>
nnoremap <leader>ao :action OptimizeImports<CR>
nnoremap <leader>af :action ShowReformatFileDialog<CR>
```

### Terminal Enhancements
```vim
" Terminal operations (complement your Ctrl+,)
nnoremap <leader>tn :action Terminal.OpenInTerminal<CR>
nnoremap <leader>tk :action Terminal.Close<CR>
```

## 📊 Organization Improvements

### Recommended Leader Key Groups

Organize your shortcuts by logical groups for better memorability:

- **`<Space>f*`** - File operations
- **`<Space>g*`** - Git operations  
- **`<Space>r*`** - Refactoring operations
- **`<Space>d*`** - Debug operations
- **`<Space>t*`** - Testing operations
- **`<Space>w*`** - Window operations
- **`<Space>c*`** - Code generation
- **`<Space>s*`** - Search operations
- **`<Space>a*`** - Analysis operations

### Which-Key Integration
Update your Which-Key configuration to include these new groups:

```vim
" Add to your .ideavimrc Which-Key settings
let g:WhichKey_KeysOfGroups = {
  \ '<leader>g': 'Git',
  \ '<leader>r': 'Refactor', 
  \ '<leader>t': 'Test',
  \ '<leader>w': 'Window',
  \ '<leader>c': 'Code',
  \ '<leader>s': 'Search',
  \ '<leader>a': 'Analysis',
  \ '<leader>d': 'Debug',
  \ '<leader>j': 'Jump'
  \ }
```

## 🔍 Potential Conflicts to Review

### Duplicate Functionality
1. **Tab closing**: You have `<Space>q`, `<Space>gx`, and `<Space>co` - consider keeping only `<Space>q`
2. **Paste operations**: Multiple shortcuts (`Cmd+P`, `Cmd+V`, `Alt+V`, `<Space>v`) - maybe remove `<Space>v`
3. **Tab navigation**: Review if you need both `Tab/Shift+Tab` AND `Shift+Cmd+H/L`

### Recommended Consolidation
```vim
" Remove redundant mappings and keep these:
" <Space>q - Close current tab (keep this)
" Cmd+V - Standard paste (keep this)  
" Alt+V - Paste multiple (keep this)
" Remove: <Space>v, <Space>gx, <Space>co
```

## 🏆 Power User Additions

### Macro Support
```vim
" Macro operations
nnoremap <leader>mr :action StartRecordingAction<CR>
nnoremap <leader>mp :action PlaybackLastMacro<CR>
```

### Code Folding
```vim
" Folding operations
nnoremap <leader>zo :action ExpandRegion<CR>
nnoremap <leader>zc :action CollapseRegion<CR>
nnoremap <leader>za :action ExpandCollapseToggle<CR>
nnoremap <leader>zr :action ExpandAll<CR>
nnoremap <leader>zm :action CollapseAll<CR>
```

### Advanced Features
```vim
" Power user operations  
nnoremap <leader>bf :action RecentChangedFiles<CR>
nnoremap <leader>bl :action RecentLocations<CR>
nnoremap <leader>bs :action Switcher<CR>
nnoremap <leader>bp :action ParameterInfo<CR>
```

## 🚀 Implementation Priority

1. **Week 1**: Add Git integration shortcuts (highest daily impact)
2. **Week 2**: Add testing shortcuts (essential for development)  
3. **Week 3**: Implement ergonomic improvements (comfort gains)
4. **Week 4**: Add power user features (advanced workflows)

## 💡 Tips for Implementation

1. **Add gradually**: Don't implement all at once - muscle memory needs time
2. **Test conflicts**: Check each new shortcut doesn't conflict with existing ones
3. **Use Which-Key**: Let it guide you to discover new shortcuts
4. **Document changes**: Update your main keymaps file as you add these
5. **Backup configs**: Save your current setup before making changes

## 🔧 Quick Implementation Script

Add this to the end of your `.ideavimrc`:
```vim
" === ENHANCEMENTS FROM webstorm-keybindings-enhancements.md ===
" Git operations
nnoremap <leader>gc :action CheckinProject<CR>
nnoremap <leader>gp :action Vcs.Push<CR>
nnoremap <leader>gl :action Vcs.UpdateProject<CR>

" Testing operations  
nnoremap <leader>tr :action RunClass<CR>
nnoremap <leader>tt :action RunConfiguration<CR>

" Start with these essentials, then add more gradually
```

---

*This enhancement guide complements your existing webstorm-keymaps.md setup. Implement gradually and adjust based on your workflow preferences.*