# WEBSTORM-CONFIGURATION

## Overview

This document provides comprehensive information about the WebStorm 2025.2 configuration environment, including directory structure, configuration files, plugins, and integration with the keyboard productivity system.

**Configuration Locations:**
- **Application Support**: `/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2`
- **Logs**: `/Users/artem/Library/Logs/JetBrains/WebStorm2025.2`
- **Project Configs**: `configs/webstorm/` (version controlled)

**Active Keymap**: `macOS copy2`

## Directory Structure

### Application Support Directory

**Total Items**: 43 top-level directories and files

#### Key Subdirectories:

##### `/keymaps/` - Keyboard Mappings
**7 keymap files** (all synced to `configs/webstorm/keymaps/`):
- `macOS copy.xml` (5,616 bytes) - Original base keymap
- `macOS copy2.xml` (6,805 bytes) - **Currently active**
- `macOS copy1.xml` (6,096 bytes)
- `macOS copy3.xml` (6,689 bytes)
- `macOS My setup.xml` (10,893 bytes)
- `macOS NewOne Modified.xml` (10,900 bytes)
- `macOS my key map.xml` (8,507 bytes)

**Keymap Features:**
- All inherit from "Mac OS X 10.5+" parent keymap
- HJKL navigation bindings (`alt h/j/k/l`)
- Split window management (`shift ctrl alt h/j/k/l`)
- Tab navigation (`shift meta h/l`)
- Multi-cursor support (`alt j/k`)
- See [[WEBSTORM-KEYMAPS]] for complete reference

##### `/quicklists/` - Action Panels
**5 quick list definitions** (all synced to `configs/webstorm/quicklists/`):
- `Terminal Actions.xml` - Terminal management commands
- `Copy.xml` - Copy operations
- `Deployment.xml` - Deployment workflows
- `JavaScript_Node_js Development.xml` - Node.js tools
- `Markdown.xml` - Markdown editing actions

See [[WEBSTORM-QUICK-LISTS]] for detailed quick list usage

##### `/options/` - Configuration Settings
**142 XML configuration files** covering all IDE settings

**Keyboard/Navigation Related:**
- `mac/keymap.xml` - Active keymap selector (points to `macOS copy2`)
- `vim_settings.xml` (4,067 bytes) - IdeaVim main configuration
- `vim_settings_local.xml` (913,722 bytes) - IdeaVim local state and history
- `keymapFlags.xml` - Keymap feature flags
- `abbrevs.xml` (2KB) - Action abbreviations for Search Everywhere (double-shift search)
- `macros.xml` (650 bytes) - Recorded macro sequences with custom names

**Editor Settings:**
- `editor.xml` - Editor behavior (camel words, breadcrumbs, trailing spaces)
- `editor-font.xml` - Font configuration
- `ui.lnf.xml` - UI preferences (tab limits, compact mode, navigation bar)
- `window.layouts.xml` - Window layout persistence

**Plugin Configurations:**
- `claude-code-plugin-settings.xml` - Claude Code integration
- `CodeGlancePro.xml` - Code minimap
- `material_theme_new.xml` - Material Theme UI
- `KeyPromoterXSettings.xml` - Keyboard shortcut learning
- `git_toolbox_2.xml` - Git integration enhancements

**Project/Workspace:**
- `project.default.xml` - Default project settings
- `projectView.xml` - Project view preferences
- `recentProjects.xml` - Recent project metadata

##### `/plugins/` - Installed Extensions
**73 plugins installed** (35 disabled)

**Vim & Navigation Plugins (Active):**
- **IdeaVIM** - Vim emulation engine
- **IdeaVim-EasyMotion** - Enhanced jump navigation
- **ideavim-quickscope** - Character jump highlighting
- **Key Promoter X** - Keyboard shortcut learning tool
- **IDEA_Which-Key** - Keybinding discovery overlay
- **acejump** - Quick character-based navigation

**Productivity Plugins (Active):**
- **claude-code-jetbrains-plugin** - AI assistance
- **Material Theme UI** - UI customization
- **CodeGlancePro** - Code minimap
- **Rainbow CSV** - CSV file highlighting
- **LivePlugin** - IDE scripting
- **Obsidian.jar** - Obsidian integration
- **DBNavigator** - Database tools

**Notable Disabled Plugins (35 total):**
- GitHub Copilot
- React, Angular, Vue frameworks
- Next.js, Vite, Webpack tooling
- Tailwind CSS
- GitToolBox

##### `/workspace/` - Project-Specific State
**106 XML files** - One per project workspace
- Project-specific keybindings
- Local IDE state per project
- Tool window layouts
- Recent file lists

##### `/colors/`, `/codestyles/`, `/templates/`
- **43 color schemes** installed
- Code style definitions (JavaScript, TypeScript, etc.)
- File and live templates

### Logs Directory

**73 log files** including:
- Rotating idea.log files (idea.log through idea.12.log)
- Telemetry and diagnostics data
- Plugin logs
- Performance metrics

## IdeaVim Configuration

### Enabled Vim Plugins
From `vim_settings.xml`:
- **Sneak** - Efficient motion with `s` and `S`
- **EasyMotion** - Quick navigation with `<leader><leader>`
- **Surround** - Manipulate surrounding characters
- **Multiple Cursors** - Multi-cursor functionality
- **Which-Key** - Display available keybindings
- **QuickScope** - Highlight targets for f/F/t/T motions
- **Highlighted Yank** - Highlight yanked text

### Shortcut Conflicts

**30 tracked shortcut conflicts** between IDE and Vim:

**Resolved in favor of Vim:**
- `ctrl pressed H/J/K/L` - Navigation (Vim wins)
- `shift pressed UP/DOWN/LEFT/RIGHT` - Selection (Vim wins)
- `alt pressed N` - Next occurrence (Vim wins)

**Resolved in favor of IDE:**
- `ctrl pressed K` - ShowNavBar (IDE wins)
- `meta pressed SEMICOLON` - Completion (IDE wins)

**Conflict Resolution Strategy:**
- Navigation keys favor Vim for muscle memory
- IDE-specific features (ShowNavBar, Completion) favor IDE
- Documented in `vim_settings.xml` for reference

See [[IDEAVIM-CONFIG]] for complete IdeaVim configuration

## Action Abbreviations & Macros

### Action Abbreviations (`abbrevs.xml`)

**Purpose**: Custom shortcuts for finding actions in Search Everywhere (double-shift) and Find Action (⌘⇧A)

**Location**:
- IDE: `~/Library/Application Support/JetBrains/WebStorm2025.2/options/abbrevs.xml`
- Repo: `configs/webstorm/options/abbrevs.xml`

**Current Abbreviations** (63 total):

| Abbreviation | Action | Description |
|--------------|--------|-------------|
| `md` | QuickList.Markdown | Markdown quick list |
| `npm` | QuickList.JavaScript/Node.js Development | Node.js development quick list |
| `co`, `copy` | QuickList.Copy | Copy operations quick list |
| `rt` | Terminal.RenameSession | Rename terminal session |
| `git` | VcsGroups | Version control actions |
| `task` | tasks.and.contexts | Tasks and contexts menu |
| `mep` | ManageRecentProjects | Manage recent projects |
| `string` | ActivateStringManipulationToolWindow | String manipulation tool |
| `ed` | TextEditorWithPreview.Layout.EditorOnly | Editor only view |
| `ep` | TextEditorWithPreview.Layout.EditorAndPreview | Editor + preview view |
| `edp` | TextEditorWithPreview.Layout.PreviewOnly | Preview only view |
| `op` | RecentProjectListGroup | Open project list |
| `va` | VimActions | Vim action menu |
| `spr` | MoveTabRight | Split right |
| `file` | FileMenu | File menu |

**XML Format**:
```xml
<application>
  <component name="AbbreviationManager">
    <abbreviations>
      <action id="QuickList.Markdown">
        <abbreviation name="md" />
      </action>
      <action id="Terminal.RenameSession">
        <abbreviation name="rt" />
      </action>
    </abbreviations>
  </component>
</application>
```

**Usage Workflow**:
1. Press ⇧⇧ (double-shift) to open Search Everywhere
2. Type abbreviation (e.g., `md` or `npm`)
3. Hit Enter to execute the action

**Benefits**:
- Faster action discovery than memorizing full action names
- Customizable aliases for frequently used actions
- Works across all search contexts (files, actions, symbols)
- Especially useful for Quick Lists and complex action groups

### Macros (`macros.xml`)

**Purpose**: Recorded action sequences for automating repetitive tasks

**Location**:
- IDE: `~/Library/Application Support/JetBrains/WebStorm2025.2/options/macros.xml`
- Repo: `configs/webstorm/options/macros.xml`

**Current Macros** (1 macro):

**"create controller"** - 14-step sequence:
1. Create directory (`NewDir`)
2. Type "user"
3. Press Enter
4. Create new file (`NewFile`)
5. Type "fuelMetric.controller.js"
6. Press Enter

**XML Format**:
```xml
<application>
  <component name="ActionMacroManager">
    <macro name="create controller">
      <action id="NewDir" />
      <typing text-keycode="85:0;83:0;69:0;82:0">user</typing>
      <shortuct text="ENTER" />
      <action id="NewElement" />
      <action id="NewFile" />
      <shortuct text="ENTER" />
      <typing text-keycode="...">fuelMetric.controller.js</typing>
      <shortuct text="ENTER" />
    </macro>
  </component>
</application>
```

**How to Record Macros**:
1. Go to Edit → Macros → Start Macro Recording
2. Perform actions (type, navigate, invoke commands)
3. Edit → Macros → Stop Macro Recording
4. Name your macro
5. Assign keyboard shortcut in Settings → Keymap

**Macro Types**:
- **Typing sequences**: Automated text entry
- **Action invocations**: Executing IDE commands
- **Shortcuts**: Keyboard combinations
- **Navigation**: Cursor movements and selections

**Use Cases**:
- Project-specific file creation patterns
- Boilerplate code generation
- Repetitive refactoring sequences
- Complex search/replace workflows
- Multi-step configuration changes

### Integration with Quick Lists

Abbreviations work seamlessly with Quick Lists:

**Example Flow**:
1. Type `npm` in Search Everywhere
2. Opens "JavaScript/Node.js Development" quick list
3. Select action (e.g., "Run npm install")
4. Execute immediately

**Abbreviation Strategies**:
- **Mnemonic**: `md` for Markdown, `git` for VCS
- **Short codes**: `co` for copy, `op` for open project
- **Action hints**: `rt` for rename terminal, `spr` for split right
- **Multi-char**: Avoid single-letter abbreviations to prevent conflicts

### Sync and Backup

**Manual Sync** (from IDE to project):
```bash
cp "/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2/options/abbrevs.xml" \
   configs/webstorm/options/

cp "/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2/options/macros.xml" \
   configs/webstorm/options/
```

**Restore** (from project to IDE):
```bash
cp configs/webstorm/options/abbrevs.xml \
   "/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2/options/"

cp configs/webstorm/options/macros.xml \
   "/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2/options/"
```

**Backup**:
```bash
yarn backup configs/webstorm/options/abbrevs.xml
yarn backup configs/webstorm/options/macros.xml
```

## Integration with Five-Layer Architecture

This WebStorm configuration integrates into the [[FIVE-LAYER-ARCHITECTURE]]:

### Layer -1: macOS Text System
- [[DEFAULT-KEY-BINDING-CONFIG]] (`configs/macos/DefaultKeyBinding.dict`)
- Provides HJKL navigation in all text fields

### Layer 0: System UI
- Full Keyboard Access for system-wide tab navigation
- [[HOMEROW-CONFIG]] for mouse-free UI interaction

### Layer 1: Hardware Layer
- [[KARABINER-CONFIG]] (`configs/karabiner/karabiner.json`)
- Hyper key mappings
- Dual-role key configurations

### Layer 2: Application Layer (WebStorm)
- **Keymaps**: `configs/webstorm/keymaps/macOS copy2.xml`
- **Quick Lists**: `configs/webstorm/quicklists/*.xml`
- **Options**: `configs/webstorm/options/vim_settings.xml`

### Layer 3: Editor Layer (IdeaVim)
- [[IDEAVIM-CONFIG]] (`configs/idea-vim/.ideavimrc`)
- 300+ lines of custom mappings
- Leader key sequences
- Vim plugins integration

## Version Control Strategy

### Files Tracked in Git

**Synced to Project** (`configs/webstorm/`):
```
keymaps/
├── macOS copy.xml
├── macOS copy2.xml (active)
├── macOS copy1.xml
├── macOS copy3.xml
├── macOS My setup.xml
├── macOS NewOne Modified.xml
└── macOS my key map.xml

quicklists/
├── Terminal Actions.xml
├── Copy.xml
├── Deployment.xml
├── JavaScript_Node_js Development.xml
└── Markdown.xml

options/
├── vim_settings.xml
├── vim_settings_local.xml
├── abbrevs.xml
└── macros.xml
```

**NOT Tracked:**
- `/workspace/*.xml` - Project-specific, auto-generated
- `/tasks/*.zip` - Task context (large, transient)
- Database state files
- Recent files lists
- Log files

### Backup Strategy

**Automated Backups:**
- Yarn script: `yarn backup <file_path>`
- Timestamped backups in `.claude/hooks/backups/`
- Hooks automatically backup before modifications

**Backup Command:**
```bash
yarn backup "configs/webstorm/macOS copy2.xml"
```

## Keyboard Productivity System

### HJKL Navigation Bindings

From active keymap `macOS copy2.xml`:

**Horizontal Navigation (H/L):**
```xml
<!-- Word Movement -->
<action id="EditorPreviousWord">
  <keyboard-shortcut first-keystroke="alt h" />
</action>
<action id="EditorNextWord">
  <keyboard-shortcut first-keystroke="alt l" />
</action>

<!-- Tab Navigation -->
<action id="PreviousTab">
  <keyboard-shortcut first-keystroke="shift meta h" />
</action>
<action id="NextTab">
  <keyboard-shortcut first-keystroke="shift meta l" />
</action>

<!-- Window Splits -->
<action id="StretchSplitToLeft">
  <keyboard-shortcut first-keystroke="shift ctrl alt h" />
</action>
<action id="StretchSplitToRight">
  <keyboard-shortcut first-keystroke="shift ctrl alt l" />
</action>
```

**Vertical Navigation (J/K):**
```xml
<!-- Multi-Cursor -->
<action id="EditorCloneCaretBelow">
  <keyboard-shortcut first-keystroke="alt j" />
</action>
<action id="EditorCloneCaretAbove">
  <keyboard-shortcut first-keystroke="alt k" />
</action>

<!-- Line Movement -->
<action id="MoveLineDown">
  <keyboard-shortcut first-keystroke="ctrl alt j" />
</action>
<action id="MoveLineUp">
  <keyboard-shortcut first-keystroke="ctrl alt k" />
</action>

<!-- Window Switching -->
<action id="SwitcherForward">
  <keyboard-shortcut first-keystroke="shift meta j" />
</action>
<action id="SwitcherBackward">
  <keyboard-shortcut first-keystroke="shift meta k" />
</action>

<!-- Window Splits -->
<action id="StretchSplitToBottom">
  <keyboard-shortcut first-keystroke="shift ctrl alt j" />
</action>
<action id="StretchSplitToTop">
  <keyboard-shortcut first-keystroke="shift ctrl alt k" />
</action>
```

**Modifier Pattern:**
- `alt` - Base navigation (word/caret)
- `ctrl alt` - Line manipulation
- `shift meta` - Window/tab navigation
- `shift ctrl alt` - Window split management

See [[HJKL-NAVIGATION]] for navigation philosophy

### ActionID Integration

All keybindings use official IntelliJ ActionIDs:
- Reference: `docs/reference/List of ActionIDs.mhtml` (6000+ ActionIDs)
- YAML mapping: `keyboard-config/hjkl-actionid-mapping.yaml`
- See [[WEBSTORM-KEYMAP]] for complete ActionID list

## Automation & Scripts

### Yarn Scripts

From `package.json`:

**WebStorm Sync:**
```bash
# Sync active keymap from Library to project
yarn webstorm:sync

# Create backup before modifications
yarn backup <file_path>
```

**Validation:**
```bash
# Check for binding conflicts
yarn check:conflicts

# Validate YAML configuration
yarn validate:yaml
```

**Documentation:**
```bash
# Generate docs from YAML
yarn generate:docs

# Export CSV for analysis
yarn export:csv
```

### Hook System

**Configured Hooks** (`~/.claude/hooks/keyboard-config-hooks.json`):
- Automatic YAML validation on edits
- Timestamped backups before changes
- Multi-system conflict detection
- Auto-documentation regeneration

See [[CLAUDE-HOOKS-LEARNING]] for hooks documentation

## Configuration Queries

### Useful Commands

**Find all HJKL bindings:**
```bash
grep -r "alt [hjkl]" "/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2/keymaps/"
```

**List all keyboard shortcuts in active keymap:**
```bash
cat "/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2/keymaps/macOS copy2.xml"
```

**Check Vim conflict resolutions:**
```bash
cat "/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2/options/vim_settings.xml" | grep -A 1 "shortcut-conflict"
```

**Track recent setting changes:**
```bash
ls -lt "/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2/options/" | head -20
```

**Sync keymaps to project:**
```bash
cp "/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2/keymaps/macOS copy2.xml" \
   ~/WebstormProjects/MISC/hot-keys-tuning/configs/webstorm/
```

## Statistics

**Configuration Scale:**
- **142 XML option files** - Highly customized setup
- **73 plugins** - Extensive tooling (38 active, 35 disabled)
- **7 keymap variations** - Iterative keymap development
- **5 quick lists** - Workflow automation
- **43 color schemes** - UI customization
- **30 Vim conflicts** - Documented resolution strategy
- **6000+ ActionIDs** - Available for binding

**Keymap Bindings:**
- HJKL navigation: 16 bindings
- Multi-cursor: 2 bindings
- Tab navigation: 2 bindings
- Window management: 4 split bindings
- Quick actions: 15+ custom shortcuts

## Recommendations

### Configuration Management

1. **Regular Sync**: Sync active keymap to project weekly
2. **Conflict Monitoring**: Run `yarn check:conflicts` after changes
3. **Documentation**: Update this file when adding keymaps
4. **Testing**: Test bindings across all 5 layers

### Future Enhancements

**Potential Improvements:**
- [ ] Automate keymap sync on IDE restart
- [ ] Create Quick Lists for project-specific workflows
- [ ] Extract all ActionIDs to YAML for automation
- [ ] Document plugin keyboard shortcuts
- [ ] Create WebStorm-specific conflict detection
- [ ] Add keymap diff tool for comparing variations

### Integration Tasks

**Cross-System Validation:**
- [ ] Verify HJKL consistency across Karabiner/IdeaVim/WebStorm
- [ ] Document conflicts in `keyboard-config/data/*.yaml`
- [ ] Update [[HJKL-NAVIGATION]] with WebStorm specifics
- [ ] Add WebStorm layer to conflict detection script

## Related Documentation

- [[WEBSTORM-KEYMAPS]] - Complete keymap reference
- [[WEBSTORM-QUICK-LISTS]] - Quick list usage guide
- [[IDEAVIM-CONFIG]] - IdeaVim configuration
- [[KARABINER-CONFIG]] - Karabiner hardware layer
- [[DEFAULT-KEY-BINDING-CONFIG]] - macOS text system
- [[HJKL-NAVIGATION]] - Navigation philosophy
- [[FIVE-LAYER-ARCHITECTURE]] - System architecture
- [[MODIFIER-COMBINATIONS]] - Keyboard shortcut patterns
- [[PHILOSOPHY-INSPIRATION]] - Design principles
- [[CLAUDE-HOOKS-LEARNING]] - Automation system

## Status

**Configuration Status**: Production
**Active Keymap**: macOS copy2
**Sync Status**: ✅ Synced (2025-11-01)
**Documentation**: Complete
**Automation**: 5 hooks active
**Version Control**: All keymaps, quicklists, vim settings tracked

---

**Last Updated**: 2025-11-01
**WebStorm Version**: 2025.2
**Configuration Directory**: `/Users/artem/Library/Application Support/JetBrains/WebStorm2025.2`
