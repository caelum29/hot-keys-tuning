# WebStorm Keyboard Productivity Improvement Plan

Based on your priorities (keyboard shortcuts, navigation, refactoring) and keeping current HJKL setup, here's the focused improvement plan.

## Phase 1: IdeaVim Leader Key Shortcuts (High Impact)

Add ~60 missing leader-key shortcuts to `.ideavimrc` based on WEBSTORM-KEYBINDINGS-ENHANCEMENTS.md:

### Git Operations (8 shortcuts)
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

### Testing Operations (5 shortcuts)
```vim
" Testing operations
nnoremap <leader>tr :action RunClass<CR>
nnoremap <leader>tt :action RunConfiguration<CR>
nnoremap <leader>td :action DebugClass<CR>
nnoremap <leader>tc :action RunCoverage<CR>
nnoremap <leader>tf :action RerunFailedTests<CR>
```

### Refactoring Operations (7 shortcuts)
```vim
" Refactoring operations
nnoremap <leader>rm :action ExtractMethod<CR>
nnoremap <leader>rv :action IntroduceVariable<CR>
nnoremap <leader>ri :action Inline<CR>
nnoremap <leader>rr :action RenameElement<CR>
nnoremap <leader>rs :action ChangeSignature<CR>
nnoremap <leader>rp :action IntroduceParameter<CR>
nnoremap <leader>rf :action Refactorings.QuickListPopupAction<CR>
```

### Debug Operations (7 shortcuts)
```vim
" Debug operations
nnoremap <leader>db :action ToggleLineBreakpoint<CR>
nnoremap <leader>dc :action Resume<CR>
nnoremap <leader>dn :action StepOver<CR>
nnoremap <leader>di :action StepInto<CR>
nnoremap <leader>do :action StepOut<CR>
nnoremap <leader>de :action EvaluateExpression<CR>
nnoremap <leader>dr :action RunToCursor<CR>
```

### Search Operations (6 shortcuts)
```vim
" Search operations
nnoremap <leader>sf :action FindInPath<CR>
nnoremap <leader>sr :action ReplaceInPath<CR>
nnoremap <leader>su :action FindUsages<CR>
nnoremap <leader>sh :action HighlightUsagesInFile<CR>
nnoremap <leader>sp :action SearchEverywhere<CR>
nnoremap <leader>si :action GotoImplementation<CR>
```

### Code Generation (6 shortcuts)
```vim
" Code generation
nnoremap <leader>cg :action Generate<CR>
nnoremap <leader>cc :action GenerateConstructor<CR>
nnoremap <leader>cgs :action GenerateGetterAndSetter<CR>
nnoremap <leader>ct :action GenerateToString<CR>
nnoremap <leader>ce :action GenerateEquals<CR>
nnoremap <leader>ci :action ImplementMethods<CR>
```

### Window Management (6 shortcuts)
```vim
" Window management (simpler than Shift+Ctrl+Alt+HJKL)
nnoremap <leader>wh :action StretchSplitToLeft<CR>
nnoremap <leader>wj :action StretchSplitToBottom<CR>
nnoremap <leader>wk :action StretchSplitToTop<CR>
nnoremap <leader>wl :action StretchSplitToRight<CR>
nnoremap <leader>wm :action MaximizeEditorInSplit<CR>
nnoremap <leader>wu :action UnsplitAll<CR>
```

### Code Analysis (5 shortcuts)
```vim
" Code analysis
nnoremap <leader>ai :action RunInspection<CR>
nnoremap <leader>ac :action ReformatCode<CR>
nnoremap <leader>ao :action OptimizeImports<CR>
nnoremap <leader>af :action ShowReformatFileDialog<CR>
nnoremap <leader>ae :action ShowErrorDescription<CR>
```

### Navigation Enhancements (8 shortcuts)
```vim
" Navigation improvements
nnoremap <leader>n :action FindNext<CR>
nnoremap <leader>N :action FindPrevious<CR>
nnoremap <leader>* :action FindWordAtCaret<CR>
nnoremap <leader>ji :action GotoImplementation<CR>
nnoremap <leader>jd :action GotoDeclaration<CR>
nnoremap <leader>jt :action GotoTypeDeclaration<CR>
nnoremap <leader>bf :action RecentChangedFiles<CR>
nnoremap <leader>bl :action RecentLocations<CR>
```

### Which-Key Group Configuration
```vim
" Add to Which-Key configuration for group labels
let g:WhichKeyDesc_git = "<leader>g Git operations"
let g:WhichKeyDesc_git_commit = "<leader>gc Commit"
let g:WhichKeyDesc_git_push = "<leader>gp Push"
let g:WhichKeyDesc_git_pull = "<leader>gl Pull/Update"
let g:WhichKeyDesc_git_diff = "<leader>gd Diff"
let g:WhichKeyDesc_git_blame = "<leader>gb Blame/Annotate"
let g:WhichKeyDesc_git_history = "<leader>gh History"
let g:WhichKeyDesc_git_status = "<leader>gs Status"
let g:WhichKeyDesc_git_fetch = "<leader>gf Fetch"

let g:WhichKeyDesc_test = "<leader>t Test operations"
let g:WhichKeyDesc_test_run = "<leader>tr Run test"
let g:WhichKeyDesc_test_config = "<leader>tt Run configuration"
let g:WhichKeyDesc_test_debug = "<leader>td Debug test"
let g:WhichKeyDesc_test_coverage = "<leader>tc Coverage"
let g:WhichKeyDesc_test_failed = "<leader>tf Rerun failed"

let g:WhichKeyDesc_refactor = "<leader>r Refactor operations"
let g:WhichKeyDesc_refactor_method = "<leader>rm Extract method"
let g:WhichKeyDesc_refactor_variable = "<leader>rv Extract variable"
let g:WhichKeyDesc_refactor_inline = "<leader>ri Inline"
let g:WhichKeyDesc_refactor_rename = "<leader>rr Rename"
let g:WhichKeyDesc_refactor_signature = "<leader>rs Change signature"
let g:WhichKeyDesc_refactor_parameter = "<leader>rp Introduce parameter"
let g:WhichKeyDesc_refactor_menu = "<leader>rf Refactor menu"

let g:WhichKeyDesc_debug = "<leader>d Debug operations"
let g:WhichKeyDesc_debug_breakpoint = "<leader>db Toggle breakpoint"
let g:WhichKeyDesc_debug_continue = "<leader>dc Continue/Resume"
let g:WhichKeyDesc_debug_next = "<leader>dn Step over"
let g:WhichKeyDesc_debug_into = "<leader>di Step into"
let g:WhichKeyDesc_debug_out = "<leader>do Step out"
let g:WhichKeyDesc_debug_eval = "<leader>de Evaluate"
let g:WhichKeyDesc_debug_cursor = "<leader>dr Run to cursor"

let g:WhichKeyDesc_search = "<leader>s Search operations"
let g:WhichKeyDesc_search_files = "<leader>sf Find in files"
let g:WhichKeyDesc_search_replace = "<leader>sr Replace in files"
let g:WhichKeyDesc_search_usages = "<leader>su Find usages"
let g:WhichKeyDesc_search_highlight = "<leader>sh Highlight usages"
let g:WhichKeyDesc_search_everywhere = "<leader>sp Search everywhere"
let g:WhichKeyDesc_search_implementation = "<leader>si Go to implementation"

let g:WhichKeyDesc_code = "<leader>c Code generation"
let g:WhichKeyDesc_code_generate = "<leader>cg Generate menu"
let g:WhichKeyDesc_code_constructor = "<leader>cc Constructor"
let g:WhichKeyDesc_code_getter_setter = "<leader>cgs Getter/Setter"
let g:WhichKeyDesc_code_tostring = "<leader>ct toString"
let g:WhichKeyDesc_code_equals = "<leader>ce equals/hashCode"
let g:WhichKeyDesc_code_implement = "<leader>ci Implement methods"

let g:WhichKeyDesc_window = "<leader>w Window management"
let g:WhichKeyDesc_window_left = "<leader>wh Stretch left"
let g:WhichKeyDesc_window_down = "<leader>wj Stretch down"
let g:WhichKeyDesc_window_up = "<leader>wk Stretch up"
let g:WhichKeyDesc_window_right = "<leader>wl Stretch right"
let g:WhichKeyDesc_window_maximize = "<leader>wm Maximize"
let g:WhichKeyDesc_window_unsplit = "<leader>wu Unsplit all"

let g:WhichKeyDesc_analysis = "<leader>a Code analysis"
let g:WhichKeyDesc_analysis_inspect = "<leader>ai Run inspection"
let g:WhichKeyDesc_analysis_format = "<leader>ac Reformat code"
let g:WhichKeyDesc_analysis_optimize = "<leader>ao Optimize imports"
let g:WhichKeyDesc_analysis_dialog = "<leader>af Reformat dialog"
let g:WhichKeyDesc_analysis_error = "<leader>ae Show error"

let g:WhichKeyDesc_jump = "<leader>j Jump operations"
let g:WhichKeyDesc_jump_implementation = "<leader>ji Implementation"
let g:WhichKeyDesc_jump_declaration = "<leader>jd Declaration"
let g:WhichKeyDesc_jump_type = "<leader>jt Type declaration"

let g:WhichKeyDesc_buffer = "<leader>b Buffer operations"
let g:WhichKeyDesc_buffer_recent_files = "<leader>bf Recent files"
let g:WhichKeyDesc_buffer_recent_locations = "<leader>bl Recent locations"
```

## Phase 2: WebStorm Keymap Enhancements (Medium Impact)

Add missing "Core 5" and power user shortcuts to `macOS copy.xml`:

### Navigation Shortcuts
```xml
<!-- Recent Locations -->
<action id="RecentLocations">
    <keyboard-shortcut first-keystroke="shift meta e" />
</action>

<!-- File Structure -->
<action id="FileStructurePopup">
    <keyboard-shortcut first-keystroke="meta f12" />
</action>

<!-- Go to Symbol -->
<action id="GotoSymbol">
    <keyboard-shortcut first-keystroke="shift meta alt o" />
</action>

<!-- Expression Type Info -->
<action id="ExpressionTypeInfo">
    <keyboard-shortcut first-keystroke="shift ctrl p" />
</action>

<!-- Parameter Info -->
<action id="ParameterInfo">
    <keyboard-shortcut first-keystroke="meta p" />
</action>

<!-- Navigate to Next/Previous Bookmark -->
<action id="GotoNextBookmark">
    <keyboard-shortcut first-keystroke="alt n" />
</action>
<action id="GotoPreviousBookmark">
    <keyboard-shortcut first-keystroke="alt p" />
</action>
```

### Refactoring Shortcuts
```xml
<!-- Refactor This Menu -->
<action id="Refactorings.QuickListPopupAction">
    <keyboard-shortcut first-keystroke="ctrl t" />
</action>

<!-- Extract Variable -->
<action id="IntroduceVariable">
    <keyboard-shortcut first-keystroke="shift meta alt v" />
</action>

<!-- Extract Method -->
<action id="ExtractMethod">
    <keyboard-shortcut first-keystroke="shift meta alt m" />
</action>

<!-- Extract Constant -->
<action id="IntroduceConstant">
    <keyboard-shortcut first-keystroke="shift meta alt c" />
</action>

<!-- Move File/Class -->
<action id="Move">
    <keyboard-shortcut first-keystroke="f6" />
</action>
```

### Code Manipulation Shortcuts
```xml
<!-- Extend Selection -->
<action id="EditorSelectWord">
    <keyboard-shortcut first-keystroke="alt up" />
</action>

<!-- Shrink Selection -->
<action id="EditorUnSelectWord">
    <keyboard-shortcut first-keystroke="alt down" />
</action>

<!-- Select Next Occurrence -->
<action id="SelectNextOccurrence">
    <keyboard-shortcut first-keystroke="ctrl g" />
</action>

<!-- Select All Occurrences -->
<action id="SelectAllOccurrences">
    <keyboard-shortcut first-keystroke="shift ctrl meta g" />
</action>

<!-- Complete Current Statement -->
<action id="EditorCompleteStatement">
    <keyboard-shortcut first-keystroke="shift meta enter" />
</action>

<!-- Smart Type Completion -->
<action id="SmartTypeCompletion">
    <keyboard-shortcut first-keystroke="shift ctrl space" />
</action>

<!-- Duplicate Line or Selection -->
<action id="EditorDuplicate">
    <keyboard-shortcut first-keystroke="meta d" />
</action>
```

## Phase 3: Live Templates & Postfix Completion

Create custom productivity templates via Settings → Editor → Live Templates:

### React/TypeScript Templates

#### React Functional Component (`rfc`)
```javascript
import React from 'react';

const $COMPONENT_NAME$ = () => {
  return (
    <div>
      $END$
    </div>
  );
};

export default $COMPONENT_NAME$;
```

#### React Arrow Function Component Export (`rafce`)
```javascript
const $COMPONENT_NAME$ = () => {
  $END$
};

export default $COMPONENT_NAME$;
```

#### useEffect Hook (`uef`)
```javascript
useEffect(() => {
  $END$
}, [$DEPENDENCIES$]);
```

#### useState Hook (`ust`)
```javascript
const [$STATE$, set$STATE_CAPITALIZED$] = useState($INITIAL_VALUE$);$END$
```

#### useCallback Hook (`ucb`)
```javascript
const $CALLBACK_NAME$ = useCallback(() => {
  $END$
}, [$DEPENDENCIES$]);
```

#### useMemo Hook (`umemo`)
```javascript
const $MEMOIZED_VALUE$ = useMemo(() => {
  $END$
}, [$DEPENDENCIES$]);
```

### JavaScript Patterns

#### Console Log with Variable (`log`)
```javascript
console.log('$VAR_NAME$:', $VAR_NAME$);$END$
```

#### Console Error (`err`)
```javascript
console.error('$ERROR_MESSAGE$:', $ERROR$);$END$
```

#### Try-Catch Block (`trycatch`)
```javascript
try {
  $END$
} catch (error) {
  console.error('$ERROR_MESSAGE$:', error);
}
```

#### Promise Template (`promise`)
```javascript
new Promise((resolve, reject) => {
  $END$
});
```

#### Async Function (`async`)
```javascript
async function $FUNCTION_NAME$($PARAMS$) {
  $END$
}
```

### Testing Templates

#### Describe Block (`desc`)
```javascript
describe('$TEST_SUITE$', () => {
  $END$
});
```

#### Test/It Block (`test`)
```javascript
it('should $TEST_DESCRIPTION$', () => {
  $END$
});
```

#### Expect Assertion (`expect`)
```javascript
expect($ACTUAL$).toBe($EXPECTED$);$END$
```

## Phase 4: Documentation & Learning

### Update Configuration Files

1. **Update YAML files** with newly implemented shortcuts
   - Mark leader-key shortcuts as "implemented" in appropriate YAML files
   - Update `status` fields from "planned" to "implemented"
   - Add references to `.ideavimrc` line numbers

2. **Regenerate KEY-MAP.md** with current state
   - Run `yarn generate:docs` after updating YAML
   - Verify ActionID mappings are displayed correctly

3. **Export updated CSV** for analysis
   - Run `yarn export:csv` to generate fresh exports
   - Review statistics for implemented vs planned bindings

### Create Learning Resources

1. **New Obsidian note: `WEBSTORM-LEADER-KEY-GUIDE.md`**
   ```markdown
   # WebStorm Leader Key Guide

   Quick reference for all leader-key shortcuts organized by category.

   ## Git Operations (`<leader>g`)
   - `gc` - Commit
   - `gp` - Push
   - `gl` - Pull/Update
   ...

   ## Testing (`<leader>t`)
   - `tr` - Run test
   - `tt` - Run configuration
   ...
   ```

2. **Update `WEBSTORM-KEYMAP.md`** with new mappings
   - Add new leader-key sections
   - Include Which-Key configuration examples
   - Document conflicts and resolutions

3. **Create quick reference card** for most-used shortcuts
   - Top 20 shortcuts by category
   - Printable format for desk reference

### Workflow Documentation

1. **Navigation patterns**
   - Recent Files (`Cmd+E`) → File Structure (`Cmd+F12`) → Back/Forward (`Cmd+[/]`)
   - Search Everywhere (`Double Shift`) → Go to Declaration (`Cmd+B`) → Find Usages (`Alt+F7`)

2. **Refactoring workflows**
   - Select code → Refactor This (`Ctrl+T`) → Choose refactoring
   - Rename (`Shift+F6`) → Preview → Apply
   - Extract Method (`<leader>rm`) → Adjust parameters → Confirm

3. **Multi-cursor patterns**
   - Select word → Next Occurrence (`Ctrl+G`) → Edit all
   - Column selection (`Alt+Drag`) → Multi-line edit
   - Add cursors (`Alt+Click`) → Simultaneous editing

4. **Debugging workflows**
   - Set breakpoint (`<leader>db`) → Run debug → Step through (`<leader>dn/di/do`)
   - Evaluate expression (`<leader>de`) → Modify values → Continue (`<leader>dc`)

## Implementation Order

### Day 1: Git & Testing Shortcuts (Immediate Workflow Improvement)
- [ ] Add 8 Git operations to `.ideavimrc`
- [ ] Add 5 Testing operations to `.ideavimrc`
- [ ] Add Which-Key descriptions for Git and Test groups
- [ ] Test all shortcuts for conflicts
- [ ] Update `.ideavimrc` with organized comments

### Day 2: Refactoring & Debug Shortcuts (High-Impact Development)
- [ ] Add 7 Refactoring operations to `.ideavimrc`
- [ ] Add 7 Debug operations to `.ideavimrc`
- [ ] Add Which-Key descriptions for Refactor and Debug groups
- [ ] Test refactoring workflows
- [ ] Document common refactoring patterns

### Day 3: Search & Code Generation Shortcuts (Complete Leader-Key System)
- [ ] Add 6 Search operations to `.ideavimrc`
- [ ] Add 6 Code Generation operations to `.ideavimrc`
- [ ] Add 6 Window Management operations to `.ideavimrc`
- [ ] Add 5 Code Analysis operations to `.ideavimrc`
- [ ] Add 8 Navigation enhancements to `.ideavimrc`
- [ ] Complete Which-Key configuration
- [ ] Verify no conflicts with existing shortcuts

### Day 4: WebStorm Keymap Enhancements (Core Navigation & Refactoring)
- [ ] Add navigation shortcuts to `macOS copy.xml`
- [ ] Add refactoring shortcuts to `macOS copy.xml`
- [ ] Add code manipulation shortcuts to `macOS copy.xml`
- [ ] Import updated keymap in WebStorm
- [ ] Test all new shortcuts
- [ ] Document any conflicts or adjustments

### Day 5: Live Templates for React/TypeScript
- [ ] Create React component templates (rfc, rafce)
- [ ] Create React hooks templates (uef, ust, ucb, umemo)
- [ ] Create JavaScript utility templates (log, err, trycatch, promise, async)
- [ ] Create testing templates (desc, test, expect)
- [ ] Export templates for team sharing
- [ ] Document template usage patterns

### Day 6: Documentation and Learning Materials
- [ ] Update YAML configuration files with implementation status
- [ ] Regenerate KEY-MAP.md with `yarn generate:docs`
- [ ] Export fresh CSV files with `yarn export:csv`
- [ ] Create `WEBSTORM-LEADER-KEY-GUIDE.md` in Obsidian vault
- [ ] Update `WEBSTORM-KEYMAP.md` with new shortcuts
- [ ] Create quick reference card (top 20 shortcuts)
- [ ] Document navigation workflows
- [ ] Document refactoring workflows
- [ ] Document multi-cursor patterns
- [ ] Document debugging workflows

## Expected Outcomes

After completing this plan, you will have:

### Productivity Gains
- **60+ new keyboard shortcuts** organized by logical groups
- **8 categories of operations** accessible via leader key
- **Custom Live Templates** for 80% faster React/TypeScript scaffolding
- **Complete documentation** of all shortcuts in Obsidian vault

### No Disruption to Current Setup
- **HJKL bindings unchanged** - respecting your current navigation
- **No plugin installations** - all built-in WebStorm features
- **Gradual implementation** - learn new shortcuts over 6 days
- **Which-Key integration** - discover shortcuts as you learn

### Workflow Improvements
- **Git operations** at your fingertips (no more mouse clicks)
- **Testing workflows** streamlined with shortcuts
- **Refactoring confidence** with quick access to all operations
- **Debug efficiency** with keyboard-driven debugging
- **Search mastery** with comprehensive search shortcuts

### Documentation & Knowledge
- **Complete shortcut reference** in Obsidian vault
- **Workflow patterns documented** for common tasks
- **Quick reference card** for desk/monitor
- **Team-shareable configs** for consistent workflows

## Files to Modify

### Configuration Files
1. `configs/idea-vim/.ideavimrc` - Add ~60 new leader-key mappings
2. `configs/webstorm/macOS copy.xml` - Add ~25 new WebStorm shortcuts
3. Live Templates - Create via WebStorm UI (Settings → Editor → Live Templates)

### Documentation Files
4. `obsidian-vault/WEBSTORM-LEADER-KEY-GUIDE.md` - New comprehensive guide (to be created)
5. `obsidian-vault/WEBSTORM-KEYMAP.md` - Update with new mappings
6. `docs/tool-specific/webstorm/WEBSTORM-KEYBINDINGS-ENHANCEMENTS.md` - Mark as implemented

### YAML Configuration Files (status updates only)
7. `keyboard-config/data/horizontal-navigation.yaml` - Update implementation status
8. `keyboard-config/data/vertical-navigation.yaml` - Update implementation status

### Generated Files (via scripts)
9. `keyboard-config/generated/KEY-MAP.md` - Regenerate with updated data
10. `keyboard-config/generated/bindings.csv` - Regenerate with updated data

## Conflict Resolution Strategy

### Known Potential Conflicts
- `<leader>w*` - Currently no window shortcuts, safe to add
- `<leader>g*` - Check against existing Git shortcuts
- `<leader>t*` - Verify no conflicts with terminal shortcuts
- `<leader>r*` - Ensure no conflicts with existing refactoring

### Conflict Testing Checklist
- [ ] Test each new shortcut in isolation
- [ ] Verify Which-Key popup shows correct description
- [ ] Check against existing keymap with `Cmd+Shift+A` → "Find Shortcut"
- [ ] Document any conflicts in WEBSTORM-KEYMAP.md
- [ ] Adjust shortcuts if conflicts found

### Fallback Strategy
If a shortcut conflicts with existing functionality:
1. Use alternative key within same group (e.g., `<leader>gx` instead of `<leader>gc`)
2. Use double-letter pattern (e.g., `<leader>gg` for Git menu)
3. Use capital letter (e.g., `<leader>G` for Git operations)
4. Document the chosen alternative in WEBSTORM-LEADER-KEY-GUIDE.md

## Success Metrics

### Quantitative Measures
- **60 new shortcuts** implemented and documented
- **8 Live Templates** created for React/TypeScript
- **6 workflow patterns** documented
- **100% Which-Key integration** for all leader-key groups

### Qualitative Measures
- **Reduced mouse usage** for Git, testing, refactoring operations
- **Faster code generation** with Live Templates
- **Improved muscle memory** with consistent leader-key patterns
- **Better workflow documentation** for team knowledge sharing

### Time Investment vs. Return
- **Implementation**: 6 days × 1-2 hours = 6-12 hours total
- **Learning curve**: 1-2 weeks to build muscle memory
- **Long-term savings**: 10-20 minutes per day = 40-80 hours per year
- **ROI**: Breaks even in 1-2 months, compound gains thereafter

## Next Steps After Implementation

### Week 2-4: Muscle Memory Building
- Practice new shortcuts daily
- Use Which-Key to discover shortcuts
- Document frequently used shortcuts separately
- Adjust any uncomfortable key combinations

### Month 2: Optimization
- Review usage patterns
- Identify underused shortcuts
- Add custom shortcuts for frequent operations
- Share configuration with team

### Ongoing: Continuous Improvement
- Add new templates as patterns emerge
- Document new workflows as discovered
- Keep YAML and documentation synchronized
- Export settings for backup and sharing

---

**Ready to begin implementation! Start with Day 1: Git & Testing shortcuts for immediate workflow improvements.**