# HJKL Movement Possibilities: Complete Reference and Suggestions

## Executive Summary

This document provides a comprehensive analysis of all possible HJKL navigation combinations in the keyboard
productivity system, covering the full spectrum of 124 total bindings across horizontal (H/L) and vertical (J/K)
movements.

**Current Status:**

- **124 total bindings** defined across H/L and J/K keys
- **45 implemented** (36.3%) - Currently working bindings
- **71 planned** (57.3%) - Defined but not yet implemented
- **7 available** (5.6%) - Unmapped slots ready for assignment
- **1 needs attention** (0.8%) - Requires review or fixing

**System Coverage:**

- **IdeaVim (I):** 40 bindings (32.5%) - Vim-style navigation and text manipulation
- **WebStorm (W):** 22 bindings (17.9%) - IDE-specific actions and shortcuts
- **Karabiner (K):** 14 bindings (11.4%) - System-wide and mouse control
- **Combined (W+I):** 1 binding (0.8%) - Multi-system integration
- **Unmapped (-):** 46 bindings (37.4%) - Available for future implementation

## Complete Movement Matrix

### Horizontal Navigation (H / L) - 31 Combinations

#### **Standard Modifier Combinations**

| Keystroke | System | Status        | Category   | Action                  | Suggestion                                        |
|-----------|--------|---------------|------------|-------------------------|---------------------------------------------------|
| `H / L`   | I      | ✅ Implemented | Navigation | Character left/right    | **Perfect baseline**                              |
| `⇧H / ⇧L` | -      | 📋 Planned    | Navigation | Available               | **🔥 Priority 1: Character selection left/right** |
| `⌃H / ⌃L` | W      | ✅ Implemented | Navigation | Move left/no action     | **Improve: Make ⌃L word-right**                   |
| `⌥H / ⌥L` | W      | ✅ Implemented | Navigation | Word left/right         | **Excellent**                                     |
| `⌘H / ⌘L` | W      | ✅ Implemented | Action     | Hide/complete statement | **Could be line start/end**                       |

#### **Double Modifier Combinations**

| Keystroke   | System | Status        | Category  | Action                 | Suggestion                         |
|-------------|--------|---------------|-----------|------------------------|------------------------------------|
| `⇧⌃H / ⇧⌃L` | -      | 🟡 Available  | Unmapped  | No action              | **🔥 Block selection left/right**  |
| `⇧⌥H / ⇧⌥L` | W      | ✅ Implemented | Selection | Select word left/right | **Perfect**                        |
| `⇧⌘H / ⇧⌘L` | W      | ✅ Implemented | Action    | Tab/cascade actions    | **Good for IDE workflow**          |
| `⌃⌥H / ⌃⌥L` | -      | 🟡 Available  | Unmapped  | No action              | **🔥 Error navigation left/right** |
| `⌃⌘H / ⌃⌘L` | -      | 🟡 Available  | Unmapped  | No action              | **Change navigation left/right**   |
| `⌥⌘H / ⌥⌘L` | -      | 🟡 Available  | Unmapped  | No action              | **Bookmark navigation left/right** |

#### **Triple+ Modifier Combinations**

| Keystroke       | System | Status        | Category | Action                   | Suggestion                  |
|-----------------|--------|---------------|----------|--------------------------|-----------------------------|
| `⇧⌃⌥H / ⇧⌃⌥L`   | W      | ✅ Implemented | Window   | Stretch split left/right | **Perfect for splits**      |
| `⇧⌃⌘H / ⇧⌃⌘L`   | -      | 📋 Planned    | Custom   | Custom action            | **Workspace navigation**    |
| `⇧⌥⌘H / ⇧⌥⌘L`   | W      | ✅ Implemented | Action   | Popup/reformat           | **Good utility**            |
| `⌃⌥⌘H / ⌃⌘L`    | -      | 📋 Planned    | Custom   | Custom action            | **Project tree navigation** |
| `⇧⌃⌥⌘H / ⇧⌃⌥⌘L` | -      | 📋 Planned    | Custom   | Custom action            | **System-wide navigation**  |

#### **Hyper Key Combinations**

| Keystroke   | System | Status        | Category   | Action               | Suggestion                   |
|-------------|--------|---------------|------------|----------------------|------------------------------|
| `✱H / ✱L`   | K      | ✅ Implemented | Navigation | Character left/right | **System baseline**          |
| `✱⇧H / ✱⇧L` | K      | 📋 Planned    | Selection  | Tab switching        | **Application switching**    |
| `✱⌃H / ✱⌃L` | K      | ✅ Implemented | Desktop    | Desktop left/right   | **Perfect for macOS spaces** |
| `✱⌥H / ✱⌥L` | K      | ✅ Implemented | Mouse      | Cursor left/right    | **Mouse keyboard control**   |
| `✱⌘H / ✱⌘L` | W      | ✅ Implemented | Window     | App switcher         | **Great for workflow**       |

### Vertical Navigation (J / K) - 31 Combinations

#### **Standard Modifier Combinations**

| Keystroke | System | Status        | Category   | Action                  | Suggestion                   |
|-----------|--------|---------------|------------|-------------------------|------------------------------|
| `J / K`   | I      | ✅ Implemented | Navigation | Line down/up            | **Perfect baseline**         |
| `⇧J / ⇧K` | W      | ✅ Implemented | Navigation | Down/documentation      | **Should be line selection** |
| `⌃J / ⌃K` | W      | ✅ Implemented | Text Edit  | Join/nav bar            | **Good utility combo**       |
| `⌥J / ⌥K` | W      | ✅ Implemented | Text Edit  | Clone caret below/above | **Multi-cursor excellence**  |
| `⌘J / ⌘K` | W      | ✅ Implemented | Action     | Live template/no action | **⌘K available for search**  |

#### **Double Modifier Combinations**

| Keystroke   | System | Status        | Category  | Action                | Suggestion                          |
|-------------|--------|---------------|-----------|-----------------------|-------------------------------------|
| `⇧⌃J / ⇧⌃K` | -      | 🟡 Available  | Unmapped  | No action             | **🔥 Select syntax blocks up/down** |
| `⇧⌥J / ⇧⌥K` | -      | 🟡 Available  | Unmapped  | No action             | **🔥 Select paragraph up/down**     |
| `⇧⌘J / ⇧⌘K` | W      | ✅ Implemented | Action    | Switcher forward/back | **Perfect for app switching**       |
| `⌃⌥J / ⌃⌥K` | W      | ✅ Implemented | Text Edit | Move line down/up     | **Essential refactoring**           |
| `⌃⌘J / ⌃⌘K` | -      | 🟡 Available  | Unmapped  | No action             | **🔥 VCS change navigation**        |
| `⌥⌘J / ⌥⌘K` | W      | ✅ Implemented | Text Edit | Move line up/down     | **Duplicate of ⌃⌥ - could reuse**   |

#### **Advanced Combinations**

| Keystroke     | System | Status        | Category   | Action                       | Suggestion                 |
|---------------|--------|---------------|------------|------------------------------|----------------------------|
| `⇧⌃⌥J / ⇧⌃⌥K` | -      | 📋 Planned    | Selection  | Document start/end selection | **Useful for large files** |
| `✱J / ✱K`     | K      | ✅ Implemented | Navigation | Line down/up                 | **System baseline**        |
| `✱⌃J / ✱⌃K`   | K      | ✅ Implemented | Desktop    | Focus/Mission Control        | **macOS integration**      |

### Advanced Sequences - 62 Additional Combinations

#### **Double Tap Patterns (11 combinations)**

| Pattern     | Timing | Suggestion                      | Use Case                  |
|-------------|--------|---------------------------------|---------------------------|
| `HH / LL`   | 500ms  | **Previous/next word boundary** | Quick word jumping        |
| `JJ / KK`   | 500ms  | **Jump 5 lines down/up**        | Rapid vertical navigation |
| `⇧HH / ⇧LL` | 500ms  | **Select to word boundaries**   | Quick word selection      |
| `⇧JJ / ⇧KK` | 500ms  | **Select 5 lines down/up**      | Block selection           |
| `⌃HH / ⌃LL` | 500ms  | **Beginning/end of line**       | Line boundaries           |

#### **Leader Sequences (15 combinations)**

| Pattern               | Category | Suggestion                      | Use Case           |
|-----------------------|----------|---------------------------------|--------------------|
| `<Leader>H/L`         | Leader   | **Split navigation left/right** | Window management  |
| `<Leader>J/K`         | Leader   | **Split navigation up/down**    | Window management  |
| `<Leader>⇧H/L`        | Leader   | **Move split left/right**       | Split manipulation |
| `<Leader><Leader>H/L` | Leader   | **Jump to split left/right**    | Quick split access |

#### **Vim Prefix Sequences (16 combinations)**

| Pattern        | Category | Suggestion                          | Use Case         |
|----------------|----------|-------------------------------------|------------------|
| `GH / GL`      | Vim      | **Line start/end** (implemented)    | Line navigation  |
| `GJ / GK`      | Vim      | **Method prev/next** (implemented)  | Code structure   |
| `yH/yL, yJ/yK` | Vim      | **Yank with motion**                | Copy operations  |
| `cH/cL`        | Vim      | **Change camel hump** (implemented) | Code editing     |
| `zH/zL, zJ/zK` | Vim      | **Scroll horizontal/vertical**      | Viewport control |

#### **Timing-based Patterns**

| Pattern        | Timing | Status     | Suggestion                          |
|----------------|--------|------------|-------------------------------------|
| **Long Press** | 1000ms | 📋 Planned | **Continuous scrolling while held** |
| **Tap/Hold**   | 200ms  | 📋 Planned | **Tap=char, Hold=word movement**    |

#### **Chord Combinations (6 combinations)**

| Pattern               | Keys     | Suggestion                            | Use Case            |
|-----------------------|----------|---------------------------------------|---------------------|
| `H+J / L+K`           | Diagonal | **Diagonal movement in 2D contexts**  | Grid navigation     |
| `H+click / L+click`   | Mouse    | **Horizontal drag/select**            | Mouse integration   |
| `J+scroll / K+scroll` | Mouse    | **Vertical scroll with acceleration** | Precision scrolling |

## High-Priority Implementation Suggestions

### 🔥 **Immediate Priority (Fill Available Slots)**

#### 1. **Character Selection (⇧H/⇧L)**

```yaml
shift:
  keystroke: "⇧H / ⇧L"
  system: "W"
  status: "planned → implement"
  category: "selection"
  action: "Select character left/right"
  ide_action_id: "EditorLeftWithSelection/EditorRightWithSelection"
```

#### 2. **Block Selection (⇧⌃J/⇧⌃K)**

```yaml
shift_ctrl:
  keystroke: "⇧⌃J / ⇧⌃K"
  system: "W"
  status: "available → implement"
  category: "selection"
  action: "Select code block up/down"
  ide_action_id: "EditorCodeBlockStartWithSelection/EditorCodeBlockEndWithSelection"
```

#### 3. **Paragraph Selection (⇧⌥J/⇧⌥K)**

```yaml
shift_alt:
  keystroke: "⇧⌥J / ⇧⌥K"
  system: "W"
  status: "available → implement"
  category: "selection"
  action: "Select paragraph up/down"
  ide_action_id: "EditorBackwardParagraphWithSelection/EditorForwardParagraphWithSelection"
```

#### 4. **Error Navigation (⌃⌥H/⌃⌥L)**

```yaml
ctrl_alt:
  keystroke: "⌃⌥H / ⌃⌥L"
  system: "W"
  status: "available → implement"
  category: "navigation"
  action: "Previous/next error"
  ide_action_id: "GotoPreviousError/GotoNextError"
```

#### 5. **VCS Navigation (⌃⌘J/⌃⌘K)**

```yaml
ctrl_cmd:
  keystroke: "⌃⌘J / ⌃⌘K"
  system: "W"
  status: "available → implement"
  category: "navigation"
  action: "Previous/next change"
  ide_action_id: "VcsShowPrevChangeMarker/VcsShowNextChangeMarker"
```

### 🚀 **Enhanced Functionality (Improve Existing)**

#### 1. **Fix Inconsistent Selection (⇧J)**

Currently `⇧J` is just EditorDown instead of EditorDownWithSelection for consistency:

```yaml
shift:
  # CURRENT: EditorDown/-
  # IMPROVED: EditorDownWithSelection/EditorUpWithSelection
  ide_action_id: "EditorDownWithSelection/EditorUpWithSelection"
```

#### 2. **Optimize Word Navigation (⌃H/⌃L)**

Currently `⌃H` does character left, but should be word-left to complement `⌃L`:

```yaml
ctrl:
  # CURRENT: EditorLeft/-  
  # IMPROVED: EditorPreviousWord/EditorNextWord
  ide_action_id: "EditorPreviousWord/EditorNextWord"
```

#### 3. **Utilize Command+K (⌘K)**

Currently unmapped, perfect for search functionality:

```yaml
cmd:
  # CURRENT: InsertLiveTemplate/-
  # IMPROVED: InsertLiveTemplate/FindInPath
  ide_action_id: "InsertLiveTemplate/FindInPath"
```

### ⚡ **Double Tap Quick Wins**

#### 1. **Rapid Line Navigation (JJ/KK)**

```yaml
double_tap:
  keystroke: "JJ / KK"
  timing_ms: 500
  action: "Jump 5 lines down/up"
  ide_action_id: "EditorDown5/EditorUp5" # Custom implementation
```

#### 2. **Word Boundary Jumping (HH/LL)**

```yaml
double_tap:
  keystroke: "HH / LL"
  timing_ms: 500
  action: "Jump to prev/next word boundary"
  ide_action_id: "EditorPreviousWordBoundary/EditorNextWordBoundary" 
```

### 🎯 **Vim Integration Excellence**

#### 1. **Enable Yank Sequences**

```yaml
yank_horizontal:
  keystroke: "yH / yL"
  system: "I"
  status: "planned → implement"
  ideavim_command: "yh/yl"

yank_vertical:
  keystroke: "yJ / yK"
  system: "I"
  status: "planned → implement"
  ideavim_command: "yj/yk"
```

#### 2. **Bracket Navigation**

```yaml
bracket_prev:
  keystroke: "[J / [K"
  system: "I"
  status: "planned → implement"
  ideavim_command: "[m/[["
  action: "Previous method/fold beginning"

bracket_next:
  keystroke: "]J / ]K"
  system: "I"
  status: "planned → implement"
  ideavim_command: "]m/]]"
  action: "Next method/fold end"
```

### 🌟 **Advanced Features**

#### 1. **Smart Context Navigation**

Implement context-aware behavior:

- In **code**: Navigate by syntax elements
- In **comments**: Navigate by sentences
- In **strings**: Navigate by words
- In **git diff**: Navigate by changes

#### 2. **Progressive Enhancement**

- **Tap**: Basic movement (current behavior)
- **Double tap**: 5x movement
- **Hold**: Continuous movement
- **With shift**: Selection mode

#### 3. **Visual Feedback System**

- Show movement distance indicators
- Highlight targets before jumping
- Display available sequence options

## Implementation Roadmap

### Phase 1: Fill the Gaps (1-2 weeks)

1. ✅ Implement 5 available unmapped slots
2. ✅ Fix inconsistent selection behaviors
3. ✅ Add error and VCS navigation

### Phase 2: Double Tap Revolution (2-3 weeks)

1. 🚀 Implement JJ/KK rapid navigation
2. 🚀 Implement HH/LL word boundaries
3. 🚀 Add shift variants for selection

### Phase 3: Vim Integration (3-4 weeks)

1. 🎯 Enable all yank sequences
2. 🎯 Implement bracket navigation
3. 🎯 Add visual and mark operations

### Phase 4: Advanced Features (4-6 weeks)

1. 🌟 Smart context awareness
2. 🌟 Progressive enhancement system
3. 🌟 Visual feedback implementation

## Configuration Examples

### Karabiner Elements

```json
{
  "description": "Double tap JJ for rapid navigation",
  "manipulators": [
    {
      "type": "basic",
      "from": {
        "key_code": "j",
        "modifiers": {
          "optional": [
            "any"
          ]
        }
      },
      "to": [
        {
          "key_code": "down_arrow",
          "repeat": 5
        }
      ],
      "conditions": [
        {
          "type": "variable_if",
          "name": "j_pressed_once",
          "value": 1
        }
      ]
    }
  ]
}
```

### IdeaVim Configuration

```vim
" Enable yank sequences
nnoremap yh yh
nnoremap yl yl  
nnoremap yj yj
nnoremap yk yk

" Bracket navigation
nnoremap [j [m
nnoremap [k [[
nnoremap ]j ]m  
nnoremap ]k ]]
```

### WebStorm Keymap

```xml

<action id="EditorLeftWithSelection">
    <keyboard-shortcut first-keystroke="shift H"/>
</action>
<action id="GotoPreviousError">
<keyboard-shortcut first-keystroke="ctrl alt H"/>
</action>
<action id="EditorDownWithSelection">
<keyboard-shortcut first-keystroke="shift J"/>
</action>
```

## Conclusion

The HJKL navigation system has **tremendous untapped potential**. With 124 total possible combinations and only 45
currently implemented, there's a **179% expansion opportunity** waiting.

The highest impact improvements are:

1. **Filling the 7 available unmapped slots** with essential navigation
2. **Fixing inconsistencies** in existing bindings
3. **Adding double-tap sequences** for rapid movement
4. **Enhancing Vim integration** with complete sequence support

This comprehensive approach will create a **world-class navigation system** that rivals and exceeds any IDE's built-in
keyboard shortcuts while maintaining the elegant simplicity of the HJKL paradigm.

---
*Generated from YAML configuration data - Last updated: 2025-01-25*
