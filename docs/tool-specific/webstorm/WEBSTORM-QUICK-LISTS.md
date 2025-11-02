# WebStorm Quick Lists Guide

## Overview

**Quick Lists** are custom action groups that create popup menus of frequently-used IDE commands. They function like customizable command panels accessible via keyboard shortcuts or Search Everywhere.

**Key Benefits:**
- No plugin development required (built-in WebStorm feature)
- Accessible via Search Everywhere (double-shift)
- Actions numbered 0-9 for instant selection
- Integrates with [[HJKL-NAVIGATION]] keyboard workflow
- Reduces menu navigation overhead

## What Are Quick Lists?

Quick Lists solve the problem of repeatedly navigating menus for common actions. Instead of:
```
Menu → Submenu → Action (3-5 clicks)
```

You get:
```
Shortcut → Number key (2 keystrokes)
```

## Creating Quick Lists

### Step 1: Open Quick Lists Settings

**macOS:** `Cmd + ,` → Appearance & Behavior → Quick Lists
**Windows/Linux:** `Ctrl + Alt + S` → Appearance & Behavior → Quick Lists

### Step 2: Create New List

- Click `+` or press `Alt + Insert` (Win/Linux) / `Cmd + N` (macOS)
- Enter a **Display Name** (e.g., "Dev Tools", "Git Actions")
- Add optional **Description**

### Step 3: Add Actions

In the right pane:
- Click `+` to add action
- Search for WebStorm actions (e.g., "Terminal", "Run Tests", "Git Pull")
- Add **separators** to group related actions
- Reorder with `Alt + Up/Down`

**Action Numbering:**
- Actions are automatically numbered 0-9
- After 9, continues alphabetically (a, b, c...)
- **Best Practice:** Keep lists under 10 items for instant access

### Step 4: Assign Keyboard Shortcut

1. Open **Keymap** settings (`Cmd + ,` → Keymap)
2. Expand **Quick Lists** node
3. Right-click your Quick List
4. Select **Add Keyboard Shortcut**
5. Press desired key combination

**Recommended:** Use modifier combinations that fit your [[HJKL-NAVIGATION]] system:
- `Ctrl + Shift + D` - Dev Tools
- `Ctrl + Shift + G` - Git Actions
- `Ctrl + Shift + T` - Terminal Commands

## Accessing Quick Lists

### Method 1: Keyboard Shortcut
Press your assigned shortcut → Quick List popup appears → Press number (0-9)

### Method 2: Search Everywhere
1. Double-tap `Shift`
2. Type Quick List name (e.g., "Dev Tools")
3. Press `Enter` → Select action by number

### Method 3: Actions Menu
`Cmd + Shift + A` (macOS) / `Ctrl + Shift + A` (Win/Linux) → Search for Quick List name

## Example Quick Lists

### 1. Dev Tools Panel

**Name:** Dev Tools
**Shortcut:** `Ctrl + Shift + D`
**Actions:**
```
0: Terminal
1: Run Current File
2: Debug Current File
3: Stop All Processes
4: Reformat Code
5: Optimize Imports
6: Show Structure
7: File Structure Popup
8: Toggle Line Breakpoint
9: Run Tests
```

### 2. Git Actions Panel

**Name:** Git Actions
**Shortcut:** `Ctrl + Shift + G`
**Actions:**
```
0: Git Pull
1: Git Push
2: Commit Changes
3: Show Git Log
4: Compare with Branch
5: Revert File
6: Annotate (Git Blame)
7: Show Diff
8: Fetch
9: Update Project
```

### 3. Terminal Commands

**Name:** Terminal Tools
**Shortcut:** `Ctrl + Shift + T`
**Actions:**
```
0: Terminal
1: Run npm install
2: Run yarn build
3: Run yarn test
4: Clear Terminal Buffer
------- [Separator] -------
5: New Terminal Tab
6: Split Terminal Right
7: Rename Terminal Session
```

### 4. Navigation & Windows

**Name:** Window Management
**Shortcut:** `Ctrl + Shift + W`
**Actions:**
```
0: Hide All Tool Windows
1: Maximize Editor
2: Restore Default Layout
3: Recent Files
4: Recent Locations
5: Jump to Navigation Bar
------- [Separator] -------
6: Close All Editors
7: Close Unmodified Editors
8: Reopen Closed Tab
9: Pin/Unpin Active Tab
```

### 5. Code Actions

**Name:** Code Tools
**Shortcut:** `Ctrl + Shift + C`
**Actions:**
```
0: Rename Element
1: Extract Method
2: Extract Variable
3: Inline Variable
4: Move Element
5: Change Signature
------- [Separator] -------
6: Surround With
7: Generate Code
8: Override Methods
9: Implement Methods
```

## Integration with Your Workflow

### HJKL Navigation Compatibility

Quick Lists complement your [[HJKL-NAVIGATION]] system:

**Current System:**
- `H/L` - Horizontal navigation
- `J/K` - Vertical navigation
- Modifiers - Context switching

**Quick Lists Add:**
- **Action grouping** - Related commands in one popup
- **Numeric access** - No need to navigate lists
- **Search integration** - Double-shift discovery

### Suggested Shortcuts

Following your [[MODIFIER-COMBINATIONS]] philosophy:

```
Ctrl + Shift + D  - Dev Tools (Development)
Ctrl + Shift + G  - Git Actions (Git)
Ctrl + Shift + T  - Terminal Tools (Terminal)
Ctrl + Shift + W  - Window Management (Windows)
Ctrl + Shift + C  - Code Actions (Code)
Ctrl + Shift + R  - Refactoring Tools (Refactor)
Ctrl + Shift + N  - Navigation Tools (Navigate)
```

## Best Practices

### 1. Keep Lists Concise
**Limit to 10 actions** - Numbers 0-9 allow instant selection without searching

### 2. Logical Grouping
Group related actions by:
- **Tool** (Git, Terminal, Database)
- **Context** (Editing, Navigation, Debugging)
- **Frequency** (Daily, Weekly, Occasional)

### 3. Use Separators
Break lists into sections with separators for visual clarity

### 4. Memorable Names
Use clear, searchable names:
- ✅ "Dev Tools", "Git Actions", "Terminal Commands"
- ❌ "My List", "Quick 1", "Stuff"

### 5. Consistent Shortcuts
Follow a pattern for keyboard shortcuts:
- All use same modifier base (`Ctrl + Shift + X`)
- Letter corresponds to list name (`D` = Dev, `G` = Git)

### 6. Action Prioritization
Place most-used actions at top (0-3 positions) for muscle memory

## Advanced Usage

### Dynamic Context

Some actions behave differently based on context:
- **Run Current File** - Adapts to file type
- **Debug Current File** - Uses appropriate debugger
- **Show Structure** - Shows relevant structure panel

### Combine with IdeaVim

Quick Lists work seamlessly with [[IDEAVIM-CONFIG]]:
- Use in normal mode
- Trigger with `<Leader>` sequences
- Example: Map `<Leader>d` to Dev Tools Quick List

**IdeaVim Integration:**
```vim
" Map leader-d to Dev Tools Quick List
nnoremap <Leader>d :action QuickListPopupAction<CR>
```

### Combine with Which-Key

If using [[IDEAVIM-CONFIG]] with Which-Key plugin:
- Quick Lists appear in Which-Key menu
- Shows available shortcuts after pressing `<Leader>`
- Provides discoverability for new Quick Lists

## Troubleshooting

### Quick List Not Appearing in Search Everywhere

**Solution:** Ensure the Quick List:
1. Has been saved (click OK in settings)
2. Has a clear, unique name
3. Restart WebStorm if just created

### Actions Not Working

**Check:**
- Action is available in current context
- Action hasn't been disabled in settings
- WebStorm version supports the action

### Keyboard Shortcut Conflicts

**Resolution:**
1. Open Keymap settings
2. Search for the conflicting shortcut
3. Remove or reassign the conflicting binding
4. See [[WEBSTORM-KEYMAPS]] for current shortcuts

## Documentation & Updates

When creating/modifying Quick Lists:

1. **Update this file** with new configurations
2. **Update [[WEBSTORM-KEYMAPS]]** with assigned shortcuts
3. **Document in Obsidian** for knowledge graph integration
4. **Track effectiveness** in usage notes

## Related Documentation

- [[WEBSTORM-KEYMAPS]] - Complete keymap reference
- [[IDEAVIM-CONFIG]] - Vim integration
- [[HJKL-NAVIGATION]] - Navigation philosophy
- [[MODIFIER-COMBINATIONS]] - Keyboard shortcuts system
- [[PHILOSOPHY-INSPIRATION]] - Overall design principles

## ActionID Reference

For programmatic access or advanced configuration, Quick Lists use ActionIDs:
- See `docs/reference/List of ActionIDs.mhtml` for complete list
- Quick Lists themselves: `QuickListPopupAction`
- Individual actions use their standard ActionIDs

## Future Enhancements

**Potential Improvements:**
- [ ] Create Quick Lists for each major tool (Git, Terminal, Database)
- [ ] Integrate with project-specific workflows
- [ ] Document in [[OBSIDIAN-INTEGRATION]] vault
- [ ] Add to [[WEBSTORM-KEYMAP]] learning notes
- [ ] Create Quick List templates for common dev workflows

---

**Status:** Active documentation
**Last Updated:** 2025-10-31
**Related:** [[WEBSTORM-KEYMAPS]], [[HJKL-NAVIGATION]], [[IDEAVIM-CONFIG]]