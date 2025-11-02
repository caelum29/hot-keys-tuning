# KARABINER-HJKL-REMAPPING-PLAN

> **Comprehensive guide for removing mouse bindings and creating a system-wide vim-like navigation layer in Karabiner Elements**

---

## Table of Contents

1. [Background & Capslock Philosophy](#1-background--capslock-philosophy)
2. [Current State Analysis](#2-current-state-analysis)
3. [Mouse Bindings Audit](#3-mouse-bindings-audit)
4. [HJKL Cluster Deep Dive](#4-hjkl-cluster-deep-dive)
5. [Removal Strategy](#5-removal-strategy)
6. [New Extended Navigation Mappings](#6-new-extended-navigation-mappings)
7. [Virtual Keys Strategy](#7-virtual-keys-strategy)
8. [Implementation Phases](#8-implementation-phases)
9. [Five-Layer Architecture Alignment](#9-five-layer-architecture-alignment)
10. [Capslock Compatibility Analysis](#10-capslock-compatibility-analysis)

---

## 1. Background & Capslock Philosophy

### Attribution

This Karabiner configuration is based on the excellent [Vonng/Capslock](https://github.com/Vonng/Capslock) project, which provides a comprehensive keyboard-centric workflow for macOS.

**Capslock Repository:** https://github.com/Vonng/Capslock  
**Author:** Vonng  
**Concept:** Turn CapsLock into a "Hyper" modifier to create a 16-plane control system

### Original Capslock Design Philosophy

The Capslock project introduces a powerful concept:

1. **Hyper Key (✱)**: CapsLock becomes a modifier when held (right ⌘⌥⌃⇧), escape when tapped
2. **16-Plane System**: Hyper + 4 standard modifiers (⌘⌥⌃⇧) = 16 unique combinations per key
3. **HJKL Navigation**: Vim-style directional keys as foundation
4. **Mouse Integration**: Keyboard-based mouse control for truly hands-on-keyboard workflow
5. **Comprehensive Coverage**: Window management, app switching, clipboard, terminal, and more

### Why We're Based on Capslock

Capslock provides:
- ✅ Proven HJKL navigation patterns
- ✅ Well-thought-out modifier combinations
- ✅ Comprehensive rule organization
- ✅ Battle-tested across macOS versions
- ✅ Large community and documentation

### Why We're Diverging

While Capslock is excellent, we're adopting a [[FIVE-LAYER-ARCHITECTURE]] approach that requires **separation of concerns**:

| Layer | Purpose | Tool | Mouse Control? |
|-------|---------|------|----------------|
| -1 | Text System | [[DEFAULT-KEY-BINDING-CONFIG]] | No |
| 0 | System UI | [[HOMEROW-CONFIG]] | **YES** ← mouse here |
| 1 | Hardware | [[KARABINER-CONFIG]] | **NO** ← navigation only |
| 2 | Application | [[WEBSTORM-KEYMAP]] | No |
| 3 | Editor | [[IDEAVIM-CONFIG]] | No |

**Key insight:** Mouse control should be handled by Homerow (Layer 0), not Karabiner (Layer 1). This keeps each layer focused and prevents conflicts.

### Current Config Evolution

Our `karabiner-copy.json` started from Capslock but has been customized:
- ✅ Retained: Hyper key concept, HJKL navigation, window management
- 🔄 Modified: Added extensive mouse integration (125 bindings)
- 🆕 Added: Custom deletion patterns, clipboard management, terminal bindings

**This plan**: Remove mouse integration, enhance vim-like navigation, prepare for [[WEBSTORM-KEYMAP]] integration via virtual keys.

---

## 2. Current State Analysis

### Configuration Statistics

**Profile Name:** `Enhencment V3`  
**Total Lines:** 3,761  
**Total Manipulators:** 302  
**Total Rules:** 13

### Rule Breakdown

| Rule Name | Manipulators | Category | Action |
|-----------|--------------|----------|--------|
| CapsLock to Hyper | 4 | Core | ✅ Keep |
| Hyper Navigation | 102 | Focus Area | 🔄 Modify |
| Hyper Deletion | 12 | Enhancement | 🟡 Enhance |
| Hyper MouseKey | 63 | **Remove** | 🔴 Delete |
| Hyper Window | 19 | Window Mgmt | ✅ Keep |
| Hyper Application | 18 | App Switch | ✅ Keep |
| Hyper Clipboard | 20 | Clipboard | ✅ Keep |
| Hyper Terminal | 10 | Terminal | ✅ Keep |
| Hyper Launcher | 8 | Apps | ✅ Keep |
| Hyper Media | 6 | Media | ✅ Keep |
| Hyper Finder | 12 | Finder | ✅ Keep |
| Hyper System | 14 | System | ✅ Keep |
| Semicolon Modifier | 14 | Custom | ✅ Keep |
| **TOTAL** | **302** | | |

### Visual Breakdown

```
Current: 302 manipulators
├─ Keep unchanged: 114 (38%)
├─ Modify (Hyper Navigation): 102 (34%)
│  ├─ Keep: ~70 (navigation, tabs, desktop)
│  └─ Remove: ~32 (mouse bindings)
└─ Remove entirely: 63 (21%) ← Hyper MouseKey rule
   Plus ~30 more mouse bindings in other rules

Target: ~177 manipulators (after cleanup)
        + ~44 new vim navigation bindings
        = ~221 total (26% reduction, more focused)
```

### Key Observations

1. **Mouse Heavy**: 125 manipulators (41%) are mouse-related
2. **Well Organized**: Rules are clearly separated by function
3. **HJKL Focused**: Navigation rule has 102 manipulators (largest single rule)
4. **Capslock Foundation**: Core structure matches original Capslock design
5. **Custom Extensions**: Added clipboard, terminal, launcher beyond base Capslock

---

## 3. Mouse Bindings Audit

### Overview

**Total Mouse Bindings to Remove:** 125

These fall into 4 categories:

1. **HJKL Mouse Movement** (32 bindings) - in "Hyper Navigation" rule
2. **UIOP Mouse Actions** (16 bindings) - in "Hyper Navigation" rule  
3. **Arrow/Enter Mouse** (14 bindings) - in "Hyper Navigation" rule
4. **Keypad MouseKey** (63 bindings) - entire "Hyper MouseKey" rule

### 3.1 HJKL Mouse Bindings (32 total)

#### H Key Mouse Bindings (8 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Option+H` | Mouse left slow | ~137 | 🔴 Yes |
| `Hyper+Shift+Option+H` | Mouse left fast | ~146 | 🔴 Yes |
| `Hyper+Shift+Control+H` | Mouse wheel left | ~155 | 🔴 Yes |
| `Hyper+Shift+Command+H` | Mouse wheel left fast | ~164 | 🔴 Yes |

**JSON Example (to remove):**
```json
{
  "description": "option + h = mouse left",
  "from": {
    "key_code": "h",
    "modifiers": {
      "mandatory": ["left_option", "right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{ "mouse_key": { "x": -1600 } }],
  "type": "basic"
}
```

#### J Key Mouse Bindings (8 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Option+J` | Mouse down slow | ~246 | 🔴 Yes |
| `Hyper+Shift+Option+J` | Mouse down fast | ~255 | 🔴 Yes |
| `Hyper+Shift+Control+J` | Mouse wheel down | ~264 | 🔴 Yes |
| `Hyper+Shift+Command+J` | Mouse wheel down fast | ~273 | 🔴 Yes |

#### K Key Mouse Bindings (8 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Option+K` | Mouse up slow | ~355 | 🔴 Yes |
| `Hyper+Shift+Option+K` | Mouse up fast | ~364 | 🔴 Yes |
| `Hyper+Shift+Control+K` | Mouse wheel up | ~373 | 🔴 Yes |
| `Hyper+Shift+Command+K` | Mouse wheel up fast | ~382 | 🔴 Yes |

#### L Key Mouse Bindings (8 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Option+L` | Mouse right slow | ~456 | 🔴 Yes |
| `Hyper+Shift+Option+L` | Mouse right fast | ~465 | 🔴 Yes |
| `Hyper+Shift+Control+L` | Mouse wheel right | ~474 | 🔴 Yes |
| `Hyper+Shift+Command+L` | Mouse wheel right fast | ~483 | 🔴 Yes |

**Total HJKL Mouse:** 32 bindings removed, freeing 32 combinations

### 3.2 UIOP Mouse Bindings (16 total)

#### U Key Mouse Bindings (4 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Option+U` | Mouse left click | ~557 | 🔴 Yes |
| `Hyper+Shift+Option+U` | Mouse left click (dup) | ~566 | 🔴 Yes |
| `Hyper+Shift+Control+U` | Mouse wheel left (rev) | ~575 | 🔴 Yes |
| `Hyper+Shift+Command+U` | Mouse wheel left fast (rev) | ~584 | 🔴 Yes |

#### I Key Mouse Bindings (4 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Option+I` | Mouse right click | ~663 | 🔴 Yes |
| `Hyper+Shift+Option+I` | Mouse right click (dup) | ~672 | 🔴 Yes |
| `Hyper+Shift+Control+I` | Mouse wheel down (rev) | ~681 | 🔴 Yes |
| `Hyper+Shift+Command+I` | Mouse wheel down fast (rev) | ~690 | 🔴 Yes |

#### O Key Mouse Bindings (4 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Option+O` | Mouse backward button | ~765 | 🔴 Yes |
| `Hyper+Shift+Option+O` | Mouse backward (dup) | ~774 | 🔴 Yes |
| `Hyper+Shift+Control+O` | Mouse wheel up (rev) | ~783 | 🔴 Yes |
| `Hyper+Shift+Command+O` | Mouse wheel up fast (rev) | ~792 | 🔴 Yes |

#### P Key Mouse Bindings (4 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Option+P` | Mouse forward button | ~861 | 🔴 Yes |
| `Hyper+Shift+Option+P` | Mouse forward (dup) | ~870 | 🔴 Yes |
| `Hyper+Shift+Control+P` | Mouse wheel right (rev) | ~879 | 🔴 Yes |
| `Hyper+Shift+Command+P` | Mouse wheel right fast (rev) | ~888 | 🔴 Yes |

**Total UIOP Mouse:** 16 bindings removed, freeing 16 combinations

### 3.3 Arrow Keys Mouse Bindings (24 total)

#### Base Arrow + Hyper (4 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+↑` | Mouse up | ~1140 | 🔴 Yes |
| `Hyper+↓` | Mouse down | ~1149 | 🔴 Yes |
| `Hyper+←` | Mouse left | ~1158 | 🔴 Yes |
| `Hyper+→` | Mouse right | ~1167 | 🔴 Yes |

#### Arrow + Option (4 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Option+↑` | Mouse up slow | ~1068 | 🔴 Yes |
| `Hyper+Option+↓` | Mouse down slow | ~1077 | 🔴 Yes |
| `Hyper+Option+←` | Mouse left slow | ~1086 | 🔴 Yes |
| `Hyper+Option+→` | Mouse right slow | ~1095 | 🔴 Yes |

#### Arrow + Command (4 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Command+↑` | Mouse up fast | ~1104 | 🔴 Yes |
| `Hyper+Command+↓` | Mouse down fast | ~1113 | 🔴 Yes |
| `Hyper+Command+←` | Mouse left fast | ~1122 | 🔴 Yes |
| `Hyper+Command+→` | Mouse right fast | ~1131 | 🔴 Yes |

#### Arrow + Shift (wheel) (4 bindings)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Shift+↑` | Mouse wheel up | ~960 | 🔴 Yes |
| `Hyper+Shift+↓` | Mouse wheel down | ~969 | 🔴 Yes |
| `Hyper+Shift+←` | Mouse wheel left | ~978 | 🔴 Yes |
| `Hyper+Shift+→` | Mouse wheel right | ~987 | 🔴 Yes |

#### Arrow + Shift+Option (slow wheel) (4 bindings)

| Combination | Current Action | Remove? |
|-------------|---------------|---------|
| `Hyper+Shift+Option+↑` | Mouse wheel up slow | 🔴 Yes |
| `Hyper+Shift+Option+↓` | Mouse wheel down slow | 🔴 Yes |
| `Hyper+Shift+Option+←` | Mouse wheel left slow | 🔴 Yes |
| `Hyper+Shift+Option+→` | Mouse wheel right slow | 🔴 Yes |

#### Arrow + Shift+Command (fast wheel) (4 bindings)

| Combination | Current Action | Remove? |
|-------------|---------------|---------|
| `Hyper+Shift+Command+↑` | Mouse wheel up fast | 🔴 Yes |
| `Hyper+Shift+Command+↓` | Mouse wheel down fast | 🔴 Yes |
| `Hyper+Shift+Command+←` | Mouse wheel left fast | 🔴 Yes |
| `Hyper+Shift+Command+→` | Mouse wheel right fast | 🔴 Yes |

**Total Arrow Mouse:** 24 bindings removed

### 3.4 Enter Key Mouse Bindings (6 total)

| Combination | Current Action | Line # | Remove? |
|-------------|---------------|--------|---------|
| `Hyper+Enter` | Mouse left click | ~915 | 🔴 Yes |
| `Hyper+Command+Enter` | Mouse right click | ~924 | 🔴 Yes |
| `Hyper+Option+Enter` | Mouse middle click | ~933 | 🔴 Yes |
| `Hyper+Shift+Enter` | Mouse back button | ~942 | 🔴 Yes |
| `Hyper+Control+Enter` | Mouse forward button | ~951 | 🔴 Yes |
| `Hyper+Control+Shift+Enter` | Mouse left click (dup) | ~906 | 🔴 Yes |

**Total Enter Mouse:** 6 bindings removed

### 3.5 Keypad MouseKey (63 total)

**Entire "Hyper MouseKey" rule to be deleted**

This rule contains:
- Keypad 0-9 with various modifiers for mouse movement (45 bindings)
- Keypad operators for mouse wheel (9 bindings)
- Keypad special keys for mouse clicks (9 bindings)

**Rationale for complete removal:**
- User doesn't have external numeric keypad
- These combinations can't be used effectively
- Removing entire rule simplifies config

---

## 4. HJKL Cluster Deep Dive

### Overview

The HJKL cluster includes:
- **Core navigation:** H, J, K, L
- **Extended row:** U, I, O, P
- **Deletion cluster:** N, M, comma (,), period (.)
- **Brackets:** [, ]

Each key supports up to 16 modifier combinations in the Capslock philosophy.

### 4.1 H Key (Left) - All 16 Combinations

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+H` | ← Left arrow | 🟢 Keep | ← Left arrow |
| `Hyper+Command+H` | ⇧← Select left | 🟢 Keep | ⇧← Select left |
| `Hyper+Shift+H` | ⌃⇧Tab (prev tab) | 🟢 Keep | ⌃⇧Tab (prev tab) |
| `Hyper+Control+H` | ⌃← (prev desktop) | 🟢 Keep | ⌃← (prev desktop) |
| `Hyper+Option+H` | Mouse left | 🔴 Remove | **⌥← Word backward** |
| `Hyper+Command+Option+H` | ⇧⌥← Select word | 🟢 Keep | ⇧⌥← Select word back |
| `Hyper+Shift+Option+H` | Mouse fast | 🔴 Remove | **⇧⌥← Select word back** |
| `Hyper+Shift+Control+H` | Mouse wheel | 🔴 Remove | **Virtual: Mark jump back** |
| `Hyper+Shift+Command+H` | Mouse wheel fast | 🔴 Remove | **Virtual: Recent files** |
| Other combos (9-16) | Not used | 🆕 Available | Future expansion |

### 4.2 J Key (Down) - All 16 Combinations

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+J` | ↓ Down arrow | 🟢 Keep | ↓ Down arrow |
| `Hyper+Command+J` | ⇧↓ Select down | 🟢 Keep | ⇧↓ Select down |
| `Hyper+Shift+J` | ⌘Tab (next app) | 🟢 Keep | ⌘Tab (next app) |
| `Hyper+Control+J` | ⌃↓ (app focus) | 🟢 Keep | ⌃↓ (app focus) |
| `Hyper+Option+J` | Mouse down | 🔴 Remove | **⌘↓ Paragraph down** |
| `Hyper+Command+Option+J` | 3x ⇧↓ (para select) | 🟢 Keep | **⇧⌘↓ Select para down** |
| `Hyper+Shift+Option+J` | Mouse fast | 🔴 Remove | **⇧⌘↓ Select para down** |
| `Hyper+Shift+Control+J` | Mouse wheel | 🔴 Remove | **Virtual: Next error** |
| `Hyper+Shift+Command+J` | Mouse wheel fast | 🔴 Remove | **Virtual: Go to symbol** |
| Other combos (9-16) | Not used | 🆕 Available | Future expansion |

### 4.3 K Key (Up) - All 16 Combinations

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+K` | ↑ Up arrow | 🟢 Keep | ↑ Up arrow |
| `Hyper+Command+K` | ⇧↑ Select up | 🟢 Keep | ⇧↑ Select up |
| `Hyper+Shift+K` | ⌘⇧Tab (prev app) | 🟢 Keep | ⌘⇧Tab (prev app) |
| `Hyper+Control+K` | ⌃↑ (expose all) | 🟢 Keep | ⌃↑ (expose all) |
| `Hyper+Option+K` | Mouse up | 🔴 Remove | **⌘↑ Paragraph up** |
| `Hyper+Command+Option+K` | 3x ⇧↑ (para select) | 🟢 Keep | **⇧⌘↑ Select para up** |
| `Hyper+Shift+Option+K` | Mouse fast | 🔴 Remove | **⇧⌘↑ Select para up** |
| `Hyper+Shift+Control+K` | Mouse wheel | 🔴 Remove | **Virtual: Prev error** |
| `Hyper+Shift+Command+K` | Mouse wheel fast | 🔴 Remove | **Virtual: Actions menu** |
| Other combos (9-16) | Not used | 🆕 Available | Future expansion |

### 4.4 L Key (Right) - All 16 Combinations

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+L` | → Right arrow | 🟢 Keep | → Right arrow |
| `Hyper+Command+L` | ⇧→ Select right | 🟢 Keep | ⇧→ Select right |
| `Hyper+Shift+L` | ⌃Tab (next tab) | 🟢 Keep | ⌃Tab (next tab) |
| `Hyper+Control+L` | ⌃→ (next desktop) | 🟢 Keep | ⌃→ (next desktop) |
| `Hyper+Option+L` | Mouse right | 🔴 Remove | **⌥→ Word forward** |
| `Hyper+Command+Option+L` | ⇧⌥→ Select word | 🟢 Keep | ⇧⌥→ Select word fwd |
| `Hyper+Shift+Option+L` | Mouse fast | 🔴 Remove | **⇧⌥→ Select word fwd** |
| `Hyper+Shift+Control+L` | Mouse wheel | 🔴 Remove | **Virtual: Mark jump fwd** |
| `Hyper+Shift+Command+L` | Mouse wheel fast | 🔴 Remove | **Virtual: Quick doc** |
| Other combos (9-16) | Not used | 🆕 Available | Future expansion |

### 4.5 U Key (Page Up) - Combinations

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+U` | Page Up | 🟢 Keep | Page Up |
| `Hyper+Command+U` | ⇧Page Up | 🟢 Keep | ⇧Page Up (select) |
| `Hyper+Shift+U` | ⌥⌘- (zoom out) | 🟢 Keep | ⌥⌘- (zoom out) |
| `Hyper+Control+U` | ⌃⌘F (fullscreen) | 🟢 Keep | ⌃⌘F (fullscreen) |
| `Hyper+Option+U` | Mouse click | 🔴 Remove | **⌘↑ Document start** |
| `Hyper+Command+Option+U` | ⇧Page Up (dup) | 🟡 Simplify | ⇧⌘Home (select to start) |
| `Hyper+Shift+Option+U` | Mouse click | 🔴 Remove | **Virtual: Collapse all** |
| `Hyper+Shift+Control+U` | Mouse wheel | 🔴 Remove | **Virtual: Run tests** |
| `Hyper+Shift+Command+U` | Mouse wheel fast | 🔴 Remove | **Virtual: Undo** |

### 4.6 I Key (Home/Line Start) - Combinations

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+I` | Home | 🟢 Keep | Home (line start) |
| `Hyper+Command+I` | ⇧Home | 🟢 Keep | ⇧Home (select to start) |
| `Hyper+Shift+I` | ⌘⇧` (prev window) | 🟢 Keep | ⌘⇧` (prev window) |
| `Hyper+Control+I` | ⌘H (hide window) | 🟢 Keep | ⌘H (hide window) |
| `Hyper+Option+I` | Mouse right click | 🔴 Remove | **Home (alt mapping)** |
| `Hyper+Command+Option+I` | Complex selection | 🟡 Simplify | End, ⇧Home, ⇧Home |
| `Hyper+Shift+Option+I` | Mouse down fast | 🔴 Remove | **Virtual: Expand fold** |
| `Hyper+Shift+Control+I` | Mouse wheel | 🔴 Remove | **Virtual: Debug file** |
| `Hyper+Shift+Command+I` | Mouse wheel fast | 🔴 Remove | **Virtual: Insert snippet** |

### 4.7 O Key (End/Line End) - Combinations

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+O` | End | 🟢 Keep | End (line end) |
| `Hyper+Command+O` | ⇧End | 🟢 Keep | ⇧End (select to end) |
| `Hyper+Shift+O` | ⌘` (next window) | 🟢 Keep | ⌘` (next window) |
| `Hyper+Control+O` | ⌃↑ (expose all) | 🟢 Keep | ⌃↑ (expose all) |
| `Hyper+Option+O` | Mouse backward | 🔴 Remove | **End (alt mapping)** |
| `Hyper+Command+Option+O` | Home, ⇧End | 🟡 Simplify | Home, ⇧End (select line) |
| `Hyper+Shift+Option+O` | Mouse backward | 🔴 Remove | **Virtual: Toggle fold** |
| `Hyper+Shift+Control+O` | Mouse wheel | 🔴 Remove | **Virtual: Step over** |
| `Hyper+Shift+Command+O` | Mouse wheel fast | 🔴 Remove | **Virtual: Open file** |

### 4.8 P Key (Page Down) - Combinations

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+P` | Page Down | 🟢 Keep | Page Down |
| `Hyper+Command+P` | ⇧Page Down | 🟢 Keep | ⇧Page Down (select) |
| `Hyper+Shift+P` | ⌥⌘= (zoom in) | 🟢 Keep | ⌥⌘= (zoom in) |
| `Hyper+Control+P` | Open Launchpad | 🟢 Keep | Open Launchpad |
| `Hyper+Option+P` | Mouse forward | 🔴 Remove | **⌘↓ Document end** |
| `Hyper+Command+Option+P` | ⇧Page Down (dup) | 🟡 Simplify | ⇧⌘End (select to end) |
| `Hyper+Shift+Option+P` | Mouse forward | 🔴 Remove | **Virtual: Format code** |
| `Hyper+Shift+Control+P` | Mouse wheel | 🔴 Remove | **Virtual: Breakpoint** |
| `Hyper+Shift+Command+P` | Mouse wheel fast | 🔴 Remove | **Virtual: Parameter info** |

### 4.9 NM<> Deletion Cluster

#### N Key (Delete Word Back)

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+N` | ⌥Delete (word back) | 🟢 Keep | ⌥Delete (word back) |
| `Hyper+Command+N` | ⌘⇧←, Delete (line back) | 🟢 Keep | ⌘⇧←, Delete |
| `Hyper+Option+N` | ⌘Delete (line back alt) | 🟢 Keep | ⌘Delete (line back) |

#### M Key (Delete Char Back)

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+M` | Delete | 🟢 Keep | Delete (char back) |
| `Hyper+Command+M` | ⌥Delete (word back) | 🟢 Keep | ⌥Delete (word back) |
| `Hyper+Option+M` | ⌥⇧↓ (move line down) | 🟢 Keep | ⌥⇧↓ (move line down) |

#### Comma Key (Delete Char Forward)

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+,` | Forward Delete | 🟢 Keep | Forward Delete |
| `Hyper+Command+,` | ⌥Forward Delete (word fwd) | 🟢 Keep | ⌥Forward Delete |
| `Hyper+Option+,` | ⌥⇧↑ (move line up) | 🟢 Keep | ⌥⇧↑ (move line up) |

#### Period Key (Delete Word Forward)

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+.` | ⌥Forward Delete | 🟢 Keep | ⌥Forward Delete |
| `Hyper+Command+.` | ⌘⇧→, Delete (line fwd) | 🟢 Keep | ⌘⇧→, Delete |
| `Hyper+Option+.` | ⌘Delete (line delete) | 🟢 Keep | ⌘Delete (line delete) |

**Deletion cluster is already well-designed, no changes needed.**

### 4.10 Bracket Keys [] - Currently Empty

| Combination | Current Action | Status | Proposed Action |
|-------------|---------------|--------|-----------------|
| `Hyper+[` | Not used | 🆕 New | **F13 (prev tab)** |
| `Hyper+]` | Not used | 🆕 New | **F14 (next tab)** |
| `Hyper+Shift+[` | Not used | 🆕 New | **F15 (move tab left)** |
| `Hyper+Shift+]` | Not used | 🆕 New | **F16 (move tab right)** |
| Other combos | Not used | 🆕 Available | Future expansion |

---

## 5. Removal Strategy

### Phase-by-Phase Removal

#### Phase 1: Backup Current Config

**Action:** Create timestamped backup
```bash
cp configs/karabiner/karabiner-copy.json \
   configs/karabiner/backups/karabiner-copy-backup-$(date +%Y%m%d-%H%M%S).json
```

**Commit:** `git commit -m "backup: Create pre-removal backup of Karabiner config"`

#### Phase 2: Remove Hyper MouseKey Rule (63 bindings)

**Target:** Delete entire "Hyper MouseKey" rule (lines ~1337-~2000)

**What to remove:**
- All keypad 0-9 mouse movement combinations
- All keypad operators for wheel control
- All keypad special keys for clicks

**JSON structure to delete:**
```json
{
  "description": "Hyper MouseKey",
  "manipulators": [
    // ... 63 manipulators here
  ]
}
```

**Testing:**
1. Open Karabiner-EventViewer
2. Press `Hyper+Keypad5` → Should do nothing (no mouse move)
3. Verify other Hyper keys still work (H, J, K, L navigation)

**Commit:** `git commit -m "remove: Delete Hyper MouseKey rule (63 keypad bindings)"`

#### Phase 3: Remove HJKL+Option Mouse Movement (4 bindings)

**Target:** Lines ~132-175 (H, J, K, L with Option)

**What to remove:**
```json
{
  "description": "option + h = mouse left",
  "from": { "key_code": "h", "modifiers": { "mandatory": ["left_option", ...] } },
  "to": [{ "mouse_key": { "x": -1600 } }],
  "type": "basic"
}
// Similar for J, K, L
```

**Testing:**
1. Press `Hyper+Option+H` → Should do nothing
2. Verify `Hyper+H` still moves cursor left
3. Verify `Hyper+Command+H` still selects left

**Commit:** `git commit -m "remove: HJKL+Option mouse movement (4 bindings)"`

#### Phase 4: Remove HJKL+Shift+Option Fast Mouse (4 bindings)

**Target:** Lines ~141-184

**Commit:** `git commit -m "remove: HJKL+Shift+Option fast mouse (4 bindings)"`

#### Phase 5: Remove HJKL+Shift+Control Mouse Wheel (4 bindings)

**Target:** Lines ~150-193

**Commit:** `git commit -m "remove: HJKL+Shift+Control mouse wheel (4 bindings)"`

#### Phase 6: Remove HJKL+Shift+Command Fast Wheel (4 bindings)

**Target:** Lines ~159-202

**Commit:** `git commit -m "remove: HJKL+Shift+Command fast wheel (4 bindings)"`

#### Phase 7: Remove UIOP Mouse Bindings (16 bindings)

**Target:** U, I, O, P with Option/Shift+Option/Shift+Control/Shift+Command

**Commit:** `git commit -m "remove: UIOP mouse bindings (16 total)"`

#### Phase 8: Remove Arrow Key Mouse Bindings (24 bindings)

**Target:** All arrow combinations with Hyper (except existing navigation)

**Commit:** `git commit -m "remove: Arrow key mouse bindings (24 total)"`

#### Phase 9: Remove Enter Key Mouse Clicks (6 bindings)

**Target:** Enter with various modifiers (button1-5)

**Commit:** `git commit -m "remove: Enter key mouse click bindings (6 total)"`

### Summary After Removal

**Before:** 302 manipulators  
**After Phase 9:** ~177 manipulators  
**Removed:** 125 mouse bindings (41% reduction)

**What remains:**
- ✅ All HJKL navigation (character, selection, tabs, desktops)
- ✅ All deletion cluster bindings
- ✅ All window management
- ✅ All application switching
- ✅ All clipboard operations
- ✅ All terminal, launcher, media, finder, system bindings

**What's freed up for new mappings:**
- 32 HJKL combinations (Option, Shift+Option, Shift+Control, Shift+Command)
- 16 UIOP combinations (same modifiers)
- 24 Arrow combinations
- 6 Enter combinations
- 4 Bracket combinations (never used)

---

## 6. New Extended Navigation Mappings

### 6.1 HJKL + Option: Word/Paragraph Movement

**Philosophy:** Option modifier for "bigger jumps" (consistent with macOS text system)

#### Implementation

```json
{
  "description": "option + h = word backward",
  "from": {
    "key_code": "h",
    "modifiers": {
      "mandatory": ["left_option", "right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{
    "key_code": "left_arrow",
    "modifiers": ["left_option"]
  }],
  "type": "basic"
}
```

| Combination | Action | Native Keys | Use Case |
|-------------|--------|-------------|----------|
| `Hyper+Option+H` | Word backward | ⌥← | Jump to start of previous word |
| `Hyper+Option+J` | Paragraph down | ⌘↓ | Jump to next paragraph/block |
| `Hyper+Option+K` | Paragraph up | ⌘↑ | Jump to previous paragraph/block |
| `Hyper+Option+L` | Word forward | ⌥→ | Jump to start of next word |

**Testing:**
1. Open TextEdit with multi-paragraph text
2. Press `Hyper+Option+L` repeatedly → Cursor jumps by words
3. Press `Hyper+Option+J` → Cursor jumps to next paragraph
4. Works in: TextEdit, Notes, browser text fields, terminal, WebStorm

**Phase 10 Commit:** `git commit -m "add: HJKL+Option word/paragraph navigation"`

### 6.2 HJKL + Shift+Option: Word/Paragraph Selection

**Philosophy:** Adding Shift to any movement = selection (standard macOS behavior)

#### Implementation

```json
{
  "description": "shift + option + h = select word backward",
  "from": {
    "key_code": "h",
    "modifiers": {
      "mandatory": ["left_shift", "left_option", "right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{
    "key_code": "left_arrow",
    "modifiers": ["left_shift", "left_option"]
  }],
  "type": "basic"
}
```

| Combination | Action | Native Keys | Use Case |
|-------------|--------|-------------|----------|
| `Hyper+Shift+Option+H` | Select word back | ⇧⌥← | Select previous word |
| `Hyper+Shift+Option+J` | Select para down | ⇧⌘↓ | Select next paragraph |
| `Hyper+Shift+Option+K` | Select para up | ⇧⌘↑ | Select previous paragraph |
| `Hyper+Shift+Option+L` | Select word fwd | ⇧⌥→ | Select next word |

**Note:** Some existing mappings already implement multi-arrow presses (3x ⇧↓). May need to harmonize.

**Testing:**
1. Place cursor mid-sentence
2. Press `Hyper+Shift+Option+L` → Next word selected
3. Press again → Selection extends to next word
4. Verify works in all text contexts

**Phase 11 Commit:** `git commit -m "add: HJKL+Shift+Option word/paragraph selection"`

### 6.3 UIOP: Line/Document Navigation

**Philosophy:** UIOP maps to Page Up/Home/End/Page Down (already mostly implemented)

**Current state:** Already good! Just document clearly.

| Key | Base (Hyper+) | +Command (Selection) | +Option (Document) |
|-----|---------------|----------------------|--------------------|
| U | Page Up | ⇧Page Up | ⌘↑ (doc start) |
| I | Home (line start) | ⇧Home (select to start) | Home (alt) |
| O | End (line end) | ⇧End (select to end) | End (alt) |
| P | Page Down | ⇧Page Down | ⌘↓ (doc end) |

**Enhancements needed:**

```json
{
  "description": "option + u = document start",
  "from": {
    "key_code": "u",
    "modifiers": {
      "mandatory": ["left_option", "right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{
    "key_code": "up_arrow",
    "modifiers": ["left_command"]
  }],
  "type": "basic"
}
```

**Phase 12 Commit:** `git commit -m "add: UIOP+Option document bounds navigation"`

### 6.4 Brackets []: Tab Management via Virtual Keys

**Philosophy:** Virtual keys (F13-F24) create clean separation between Karabiner and app layers

#### Why Virtual Keys?

1. **Layer Separation:** Karabiner generates F13, WebStorm consumes it
2. **No Conflicts:** F13-F24 rarely used by system or apps
3. **IDE Freedom:** WebStorm can easily bind ActionIDs to virtual keys
4. **Flexibility:** Different apps can bind different actions to same virtual key

#### Implementation

```json
{
  "description": "[ = previous tab (via F13)",
  "from": {
    "key_code": "open_bracket",
    "modifiers": {
      "mandatory": ["right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{
    "key_code": "f13"
  }],
  "type": "basic"
}
```

| Combination | Virtual Key | Intended Action (WebStorm) | ActionID |
|-------------|-------------|----------------------------|----------|
| `Hyper+[` | F13 | Previous tab | `PreviousTab` |
| `Hyper+]` | F14 | Next tab | `NextTab` |
| `Hyper+Shift+[` | F15 | Move tab left | `MoveTabLeft` |
| `Hyper+Shift+]` | F16 | Move tab right | `MoveTabRight` |

**Phase 13 Commit:** `git commit -m "add: Bracket keys tab management via F13-F16"`

### 6.5 HJKL + Shift+Control: Extended Actions (Virtual Keys)

**Philosophy:** These freed combinations can be virtual keys for IDE-specific actions

| Combination | Virtual Key | Intended Action | ActionID |
|-------------|-------------|-----------------|----------|
| `Hyper+Shift+Control+H` | F17 | Jump to previous mark | `GotoPreviousBookmark` |
| `Hyper+Shift+Control+J` | F18 | Next error/warning | `GotoNextError` |
| `Hyper+Shift+Control+K` | F19 | Previous error/warning | `GotoPreviousError` |
| `Hyper+Shift+Control+L` | F20 | Jump to next mark | `GotoNextBookmark` |

**Implementation:**

```json
{
  "description": "shift + control + j = next error (via F18)",
  "from": {
    "key_code": "j",
    "modifiers": {
      "mandatory": ["left_shift", "left_control", "right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{
    "key_code": "f18"
  }],
  "type": "basic"
}
```

**Phase 14 Commit:** `git commit -m "add: HJKL+Shift+Control extended actions via F17-F20"`

### 6.6 HJKL + Shift+Command: Quick Actions (Virtual Keys)

| Combination | Virtual Key | Intended Action | ActionID |
|-------------|-------------|-----------------|----------|
| `Hyper+Shift+Command+H` | F21 | Recent files | `RecentFiles` |
| `Hyper+Shift+Command+J` | F22 | Go to symbol | `GotoSymbol` |
| `Hyper+Shift+Command+K` | F23 | Show actions menu | `ShowIntentionActions` |
| `Hyper+Shift+Command+L` | F24 | Quick documentation | `QuickJavaDoc` |

**Phase 15 Commit:** `git commit -m "add: HJKL+Shift+Command quick actions via F21-F24"`

### 6.7 UIOP Extended Actions (Optional Future)

Currently keeping UIOP simple with document navigation. Future expansion could add:
- `Hyper+Shift+Control+U/I/O/P` for code structure (folds, blocks)
- `Hyper+Shift+Command+U/I/O/P` for refactoring actions

**Note:** Leaving these undefined for now, will add based on actual usage patterns.

---

## 7. Virtual Keys Strategy

### Overview

**Virtual Keys:** Function keys F13-F24 (12 keys total)  
**Purpose:** Bridge between Karabiner (Layer 1) and WebStorm (Layer 2)  
**Status:** F13-F16 allocated, F17-F24 reserved

### Allocation Table

| Virtual Key | Karabiner Trigger | Intended Use | WebStorm ActionID | Status |
|-------------|-------------------|--------------|-------------------|--------|
| F13 | `Hyper+[` | Previous tab | `PreviousTab` | ✅ Planned |
| F14 | `Hyper+]` | Next tab | `NextTab` | ✅ Planned |
| F15 | `Hyper+Shift+[` | Move tab left | `MoveTabLeft` | ✅ Planned |
| F16 | `Hyper+Shift+]` | Move tab right | `MoveTabRight` | ✅ Planned |
| F17 | `Hyper+Shift+Control+H` | Prev bookmark/mark | `GotoPreviousBookmark` | ✅ Planned |
| F18 | `Hyper+Shift+Control+J` | Next error | `GotoNextError` | ✅ Planned |
| F19 | `Hyper+Shift+Control+K` | Prev error | `GotoPreviousError` | ✅ Planned |
| F20 | `Hyper+Shift+Control+L` | Next bookmark/mark | `GotoNextBookmark` | ✅ Planned |
| F21 | `Hyper+Shift+Command+H` | Recent files | `RecentFiles` | ✅ Planned |
| F22 | `Hyper+Shift+Command+J` | Go to symbol | `GotoSymbol` | ✅ Planned |
| F23 | `Hyper+Shift+Command+K` | Actions menu | `ShowIntentionActions` | ✅ Planned |
| F24 | `Hyper+Shift+Command+L` | Quick docs | `QuickJavaDoc` | ✅ Planned |

### Benefits of Virtual Key Architecture

#### 1. Layer Separation
```
┌─────────────────────────────────────┐
│ Layer 1: Karabiner                  │
│ "When user presses Hyper+[,         │
│  generate F13"                      │
└──────────────┬──────────────────────┘
               │ F13
               ↓
┌─────────────────────────────────────┐
│ Layer 2: WebStorm                   │
│ "When F13 pressed in WebStorm,      │
│  run PreviousTab action"            │
└─────────────────────────────────────┘
```

#### 2. No System Conflicts

**Problem with direct bindings:**
- `Hyper+[` might conflict with system shortcuts
- Hard to coordinate between Karabiner and IDE
- Testing requires both layers

**Solution with virtual keys:**
- F13-F24 almost never used by system
- Karabiner and WebStorm can be configured independently
- Easy to test each layer separately

#### 3. Application-Specific Behavior

Different apps can interpret same virtual key differently:

| Virtual Key | WebStorm Action | Terminal Action | Browser Action |
|-------------|----------------|-----------------|----------------|
| F13 | Previous tab | Previous terminal tab | Previous browser tab |
| F14 | Next tab | Next terminal tab | Next browser tab |
| F18 | Next IDE error | Next shell error | Next console error |

#### 4. Easy WebStorm Integration

In WebStorm keymap.xml:
```xml
<action id="PreviousTab">
  <keyboard-shortcut first-keystroke="F13" />
</action>
<action id="NextTab">
  <keyboard-shortcut first-keystroke="F14" />
</action>
```

Much cleaner than trying to coordinate complex Hyper+modifier combinations!

### Karabiner JSON Pattern

**Template for virtual key generation:**

```json
{
  "description": "[human-readable] = [action] (via F##)",
  "from": {
    "key_code": "[trigger_key]",
    "modifiers": {
      "mandatory": ["right_command", "right_control", "right_shift", "right_option"],
      "optional": ["left_shift", "left_command", "left_control", "left_option"]
    }
  },
  "to": [{
    "key_code": "f##"
  }],
  "type": "basic"
}
```

**Example:**
```json
{
  "description": "[ = previous tab (via F13)",
  "from": {
    "key_code": "open_bracket",
    "modifiers": {
      "mandatory": ["right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{
    "key_code": "f13"
  }],
  "type": "basic"
}
```

### Testing Virtual Keys

1. **Karabiner Layer Test:**
   ```bash
   # Open Karabiner-EventViewer
   # Press Hyper+[
   # Should see: f13 key down/up events
   ```

2. **WebStorm Layer Test:**
   ```bash
   # In WebStorm, open Settings > Keymap
   # Search for "PreviousTab"
   # Add keyboard shortcut: Press F13
   # Test: F13 should switch tabs
   ```

3. **Integration Test:**
   ```bash
   # With both layers configured
   # Press Hyper+[
   # Should: Switch to previous tab in WebStorm
   ```

### Future Expansion

**Additional virtual keys available:**
- Shift+F13 through Shift+F24 (12 more)
- Control+F13 through Control+F24 (12 more)
- Option+F13 through Option+F24 (12 more)

**Total possible:** 48 virtual key combinations before running out of function keys!

---

## 8. Implementation Phases

### Detailed 15-Phase Rollout

Each phase includes: what to change, how to test, expected behavior, and rollback strategy.

---

#### Phase 1: Backup Current Config ✅

**What:**
- Create timestamped backup of current config
- Initialize git tracking if not already done

**Commands:**
```bash
# Create backup directory if doesn't exist
mkdir -p configs/karabiner/backups

# Backup current config
cp configs/karabiner/karabiner-copy.json \
   configs/karabiner/backups/karabiner-copy-backup-$(date +%Y%m%d-%H%M%S).json

# Git commit
git add configs/karabiner/
git commit -m "backup: Create pre-removal backup of Karabiner config"
```

**Test:** Verify backup file exists and is valid JSON
```bash
cat configs/karabiner/backups/karabiner-copy-backup-*.json | jq . > /dev/null && echo "✅ Valid JSON"
```

**Rollback:** N/A (this IS the backup)

---

#### Phase 2: Remove Hyper MouseKey Rule 🔴

**What:**
- Delete entire "Hyper MouseKey" rule (63 manipulators)
- Lines approximately 1337-2000 in karabiner-copy.json

**Changes:**
1. Open karabiner-copy.json
2. Find the rule: `"description": "Hyper MouseKey"`
3. Delete entire rule object (opening `{` to closing `}`)
4. Ensure proper JSON structure (comma handling)

**JSON structure being removed:**
```json
{
  "description": "Hyper MouseKey",
  "manipulators": [
    // 63 manipulators for keypad mouse control
  ]
}
```

**Testing:**
1. Open Karabiner Elements → Complex Modifications
2. Verify rule count decreased by 1
3. Open Karabiner-EventViewer
4. Press any keypad key → Should see keypad event, no mouse movement
5. Test existing navigation: `Hyper+H` → Cursor moves left ✅

**Expected Behavior:**
- ❌ Keypad keys do nothing in Hyper mode
- ✅ All other Hyper bindings work normally

**Rollback:**
```bash
git checkout HEAD -- configs/karabiner/karabiner-copy.json
```

**Commit:**
```bash
git add configs/karabiner/karabiner-copy.json
git commit -m "remove: Delete Hyper MouseKey rule (63 keypad bindings)"
```

---

#### Phase 3: Remove HJKL+Option Mouse Movement 🔴

**What:**
- Remove 4 mouse movement bindings (H, J, K, L with Option)
- Lines approximately 132-175

**Manipulators to remove:**
```json
{
  "description": "option + h = mouse left",
  "from": { "key_code": "h", "modifiers": { "mandatory": ["left_option", "right_command", "right_control", "right_shift", "right_option"] } },
  "to": [{ "mouse_key": { "x": -1600 } }],
  "type": "basic"
}
// Similar for J, K, L
```

**Testing:**
1. Press `Hyper+Option+H` → No mouse movement ❌
2. Press `Hyper+H` → Cursor left ✅
3. Press `Hyper+Command+H` → Select left ✅
4. Repeat for J, K, L

**Rollback:** `git checkout HEAD~1 -- configs/karabiner/karabiner-copy.json`

**Commit:** `git commit -m "remove: HJKL+Option mouse movement (4 bindings)"`

---

#### Phase 4: Remove HJKL+Shift+Option Fast Mouse 🔴

**What:** Remove 4 fast mouse movement bindings

**Testing:** Same pattern as Phase 3, verify `Hyper+Shift+Option+[HJKL]` does nothing

**Commit:** `git commit -m "remove: HJKL+Shift+Option fast mouse (4 bindings)"`

---

#### Phase 5: Remove HJKL+Shift+Control Mouse Wheel 🔴

**What:** Remove 4 mouse wheel bindings

**Testing:** Verify `Hyper+Shift+Control+[HJKL]` does nothing

**Commit:** `git commit -m "remove: HJKL+Shift+Control mouse wheel (4 bindings)"`

---

#### Phase 6: Remove HJKL+Shift+Command Fast Wheel 🔴

**What:** Remove 4 fast mouse wheel bindings

**Testing:** Verify `Hyper+Shift+Command+[HJKL]` does nothing

**Commit:** `git commit -m "remove: HJKL+Shift+Command fast wheel (4 bindings)"`

---

#### Phase 7: Remove UIOP Mouse Bindings 🔴

**What:** Remove 16 mouse bindings from U, I, O, P keys

**Testing:**
1. Press `Hyper+Option+U` → No mouse click ❌
2. Press `Hyper+U` → Page Up still works ✅
3. Repeat for I, O, P with all modifier combinations

**Commit:** `git commit -m "remove: UIOP mouse bindings (16 total)"`

---

#### Phase 8: Remove Arrow Key Mouse Bindings 🔴

**What:** Remove 24 arrow key mouse bindings

**Testing:**
1. Arrow keys still work for system navigation
2. `Hyper+Arrow` combinations do nothing (freed up)

**Commit:** `git commit -m "remove: Arrow key mouse bindings (24 total)"`

---

#### Phase 9: Remove Enter Key Mouse Clicks 🔴

**What:** Remove 6 enter key mouse click bindings

**Testing:**
1. Press `Hyper+Enter` → No mouse click ❌
2. Press Enter normally → Still works ✅

**Commit:** `git commit -m "remove: Enter key mouse click bindings (6 total)"`

---

**🎉 Removal Complete! Config now has ~177 manipulators (down from 302)**

---

#### Phase 10: Add HJKL+Option Word/Paragraph Movement 🆕

**What:** Add 4 new navigation bindings

**Manipulators to add:**
```json
{
  "description": "option + h = word backward",
  "from": {
    "key_code": "h",
    "modifiers": {
      "mandatory": ["left_option", "right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{
    "key_code": "left_arrow",
    "modifiers": ["left_option"]
  }],
  "type": "basic"
}
// Similar for J (⌘↓), K (⌘↑), L (⌥→)
```

**Testing:**
1. Open TextEdit with multi-paragraph text
2. Place cursor mid-word
3. Press `Hyper+Option+L` → Cursor jumps to next word ✅
4. Press `Hyper+Option+K` → Cursor jumps to paragraph start ✅

**Expected Behavior:**
- H/L: Word-level horizontal navigation
- J/K: Paragraph-level vertical navigation

**Commit:** `git commit -m "add: HJKL+Option word/paragraph navigation"`

---

#### Phase 11: Add HJKL+Shift+Option Selection 🆕

**What:** Add 4 selection variants

**Manipulators to add:**
```json
{
  "description": "shift + option + h = select word backward",
  "from": {
    "key_code": "h",
    "modifiers": {
      "mandatory": ["left_shift", "left_option", "right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{
    "key_code": "left_arrow",
    "modifiers": ["left_shift", "left_option"]
  }],
  "type": "basic"
}
```

**Testing:**
1. Place cursor in text
2. Press `Hyper+Shift+Option+L` → Next word selected ✅
3. Press again → Selection extends ✅

**Commit:** `git commit -m "add: HJKL+Shift+Option word/paragraph selection"`

---

#### Phase 12: Add UIOP+Option Document Bounds 🆕

**What:** Enhance UIOP with document-level navigation

**Manipulators to add:**
```json
{
  "description": "option + u = document start",
  "from": {
    "key_code": "u",
    "modifiers": {
      "mandatory": ["left_option", "right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{
    "key_code": "up_arrow",
    "modifiers": ["left_command"]
  }],
  "type": "basic"
}
// Similar for P (⌘↓ document end)
```

**Testing:**
1. Open long document
2. Scroll to middle
3. Press `Hyper+Option+U` → Jump to document start ✅
4. Press `Hyper+Option+P` → Jump to document end ✅

**Commit:** `git commit -m "add: UIOP+Option document bounds navigation"`

---

#### Phase 13: Add [] Bracket Tab Management (F13-F16) 🆕

**What:** Add 4 virtual key bindings for tab management

**Manipulators to add:**
```json
{
  "description": "[ = previous tab (via F13)",
  "from": {
    "key_code": "open_bracket",
    "modifiers": {
      "mandatory": ["right_command", "right_control", "right_shift", "right_option"]
    }
  },
  "to": [{ "key_code": "f13" }],
  "type": "basic"
}
// Similar for ], Shift+[, Shift+]
```

**Testing Karabiner Layer:**
1. Open Karabiner-EventViewer
2. Press `Hyper+[` → See "f13 key down" event ✅
3. Verify no system action happens (F13 not bound to anything yet)

**Testing WebStorm Integration (separate step):**
1. Open WebStorm Settings → Keymap
2. Search "PreviousTab"
3. Add shortcut: F13
4. Repeat for F14 (NextTab), F15/F16 (MoveTab)
5. Test: `Hyper+[` switches tabs ✅

**Commit:** `git commit -m "add: Bracket keys tab management via F13-F16 virtual keys"`

---

#### Phase 14: Add HJKL+Shift+Control Extended Actions (F17-F20) 🆕

**What:** Add 4 virtual key bindings for bookmark/error navigation

**Commit:** `git commit -m "add: HJKL+Shift+Control extended actions via F17-F20"`

---

#### Phase 15: Add HJKL+Shift+Command Quick Actions (F21-F24) 🆕

**What:** Add 4 virtual key bindings for quick actions

**Commit:** `git commit -m "add: HJKL+Shift+Command quick actions via F21-F24"`

---

### Post-Implementation Checklist

After all 15 phases:

- [ ] Total manipulators: ~221 (was 302)
- [ ] All mouse bindings removed: 125 ✅
- [ ] New navigation added: 12 bindings ✅
- [ ] Virtual keys configured: 12 keys (F13-F24) ✅
- [ ] Git history: 15 commits ✅
- [ ] YAML configs updated (next step)
- [ ] Documentation regenerated (next step)
- [ ] Obsidian notes updated (next step)

---

## 9. Five-Layer Architecture Alignment

### Layer Responsibilities

Our configuration adheres to a strict **5-layer architecture** where each layer has specific responsibilities:

```
┌────────────────────────────────────────────────────────────┐
│ Layer -1: DefaultKeyBinding.dict (macOS Text System)       │
│ Purpose: Universal text navigation in text fields          │
│ Config: configs/macos/DefaultKeyBinding.dict               │
│ Navigation: Ctrl+HJKL in ANY text field                    │
│ Mouse: ❌ No                                                │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ Layer 0: System UI (Full Keyboard Access + Homerow)        │
│ Purpose: Navigate UI elements without mouse                │
│ Config: System Preferences + Homerow app                   │
│ Navigation: Tab/Shift+Tab, Homerow labels (Hyper+F)        │
│ Mouse: ✅ YES - Homerow handles ALL mouse control          │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ Layer 1: Karabiner (Hardware/System-wide)  ← THIS PLAN     │
│ Purpose: System-wide vim-like keyboard navigation          │
│ Config: configs/karabiner/karabiner-copy.json             │
│ Navigation: Hyper+HJKL everywhere                          │
│ Mouse: ❌ NO - Removed all 125 bindings                    │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ Layer 2: Application (WebStorm/IDE Keymap)                 │
│ Purpose: IDE-specific actions and workflows                │
│ Config: configs/webstorm/macOS copy.xml                    │
│ Navigation: Consumes F13-F24 virtual keys from Layer 1     │
│ Mouse: ❌ No                                                │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ Layer 3: Editor (IdeaVim)                                   │
│ Purpose: Vim emulation in editor pane only                 │
│ Config: configs/idea-vim/.ideavimrc                        │
│ Navigation: Standard vim (hjkl, w, b, e, $, 0, gg, G)      │
│ Mouse: ❌ No                                                │
└────────────────────────────────────────────────────────────┘
```

### Mouse Control: Single Responsibility

**Before (Capslock approach):**
- ❌ Mouse in Karabiner (125 bindings)
- ❌ Also have Homerow for UI clicking
- ❌ Duplication and confusion

**After (Our approach):**
- ✅ Mouse ONLY in Homerow (Layer 0)
- ✅ Karabiner focuses on keyboard navigation (Layer 1)
- ✅ Clean separation

### Navigation Distribution

| Action | Layer -1 | Layer 0 | Layer 1 | Layer 2 | Layer 3 |
|--------|----------|---------|---------|---------|---------|
| **Character** | Ctrl+HJKL (text) | — | Hyper+HJKL | — | hjkl |
| **Word** | — | — | Hyper+Opt+HL | — | w, b, e |
| **Line** | — | — | Hyper+IO | — | 0, $ |
| **Paragraph** | — | — | Hyper+Opt+JK | — | {, } |
| **Page** | — | — | Hyper+UP | — | Ctrl+F/B |
| **Document** | — | — | Hyper+Opt+UP | — | gg, G |
| **Tab** | — | — | F13-F16 → | Layer 2 | gt, gT |
| **Window** | — | Homerow | Hyper+QWE | — | — |
| **UI Click** | — | **Homerow** | — | — | — |
| **Mouse Move** | — | **Homerow** | — | — | — |
| **Scroll** | — | **Homerow HJKL** | — | — | Ctrl+D/U |

### Integration Points

#### DefaultKeyBinding ↔ Karabiner

**No conflicts:**
- DefaultKeyBinding uses `Ctrl+H/J/K/L` in text fields
- Karabiner uses `Hyper+H/J/K/L` system-wide
- Different modifiers, different scope

#### Homerow ↔ Karabiner

**Perfect separation:**
- Homerow: Activated by `Hyper+F`, handles ALL mouse/UI
- Karabiner: Provides HJKL navigation, no mouse bindings
- Homerow scrolling: Uses same HJKL keys (in Homerow mode only)

#### Karabiner ↔ WebStorm

**Clean interface:**
- Karabiner generates: F13-F24 virtual keys
- WebStorm consumes: Binds ActionIDs to F13-F24
- No direct coordination needed

**Example flow:**
```
User presses: Hyper+[
   ↓
Karabiner generates: F13
   ↓
WebStorm receives: F13
   ↓
WebStorm runs: PreviousTab action
   ↓
Result: Tab switches
```

#### WebStorm ↔ IdeaVim

**Mode-based:**
- Normal text editing: WebStorm keymap active
- Editor pane in vim mode: IdeaVim takes over
- No conflicts because different contexts

### Benefits of This Architecture

1. **Testability:**
   - Each layer can be tested independently
   - Disable Karabiner → Other layers still work
   - Disable IdeaVim → Karabiner still works

2. **Maintainability:**
   - Each config file has single responsibility
   - Changes in one layer don't affect others
   - Clear boundaries for troubleshooting

3. **Flexibility:**
   - Can swap WebStorm for VSCode (change Layer 2 only)
   - Can swap Homerow for different mouse tool (change Layer 0 only)
   - Karabiner navigation works everywhere

4. **Composability:**
   - Layers stack cleanly
   - Each layer adds specific capabilities
   - No duplication of functionality

### Alignment with Philosophy

From [[PHILOSOPHY-INSPIRATION]], the core principles:

1. ✅ **Consistency:** HJKL navigation across all layers
2. ✅ **Efficiency:** Hands stay on home row
3. ✅ **Separation:** Each layer has clear responsibility
4. ✅ **Composability:** Layers work together
5. ✅ **Vim-inspired:** But not dogmatic about pure vim

This plan **fully aligns** with the philosophy by:
- Removing mouse from wrong layer (Karabiner)
- Adding vim-like navigation enhancements
- Using virtual keys for clean layer separation
- Preserving what works (window mgmt, deletion cluster)

---

## 10. Capslock Compatibility Analysis

### What We Keep from Capslock ✅

#### Core Concepts (100% preserved)

1. **Hyper Key Concept**
   - CapsLock as dual-role key (Escape on tap, Hyper on hold)
   - Hyper = right ⌘⌥⌃⇧ (all right-side modifiers)
   - 16-plane control system (Hyper + 4 modifiers)
   - ✅ Identical to Capslock

2. **HJKL Navigation Foundation**
   - H/J/K/L as primary directional keys
   - Vim-like philosophy
   - Home row centric
   - ✅ Identical to Capslock

3. **Window Management**
   - App switching
   - Window arrangement
   - Desktop navigation
   - ✅ Identical to Capslock

4. **Deletion Cluster (N, M, comma, period)**
   - Word/character deletion
   - Line deletion
   - ✅ Identical to Capslock

#### Rule Organization (structure preserved)

```
Both configs use:
├─ CapsLock to Hyper (core)
├─ Hyper Navigation (HJKL cluster)
├─ Hyper Deletion (N, M, comma, period)
├─ Hyper Window
├─ Hyper Application
└─ Other utility rules
```

✅ We maintain the same organizational structure

### What We Modify from Capslock 🔄

#### 1. Mouse Integration (removed entirely)

**Capslock approach:**
- ✅ Comprehensive: 125+ mouse bindings
- ✅ Keyboard-centric: No need to touch mouse
- ❌ Layer violation: Mixes navigation with mouse control
- ❌ Duplication: Conflicts with Homerow (Layer 0)

**Our approach:**
- ✅ Single responsibility: Karabiner = navigation only
- ✅ Homerow for mouse: Proper layer (Layer 0 = UI)
- ✅ No duplication: One tool per job
- ✅ Cleaner config: 41% size reduction

**Rationale:** [[FIVE-LAYER-ARCHITECTURE]] requires separation. Mouse belongs in Layer 0 (System UI), not Layer 1 (Hardware).

#### 2. Extended Navigation (enhanced)

**Capslock approach:**
- Basic HJKL navigation ✅
- Some word movement ⚠️ (limited)
- Mouse for "faster" movement ❌

**Our approach:**
- Basic HJKL navigation ✅ (kept)
- Word movement via Option ✅ (added)
- Paragraph movement via Option ✅ (added)
- Document bounds via UIOP+Option ✅ (added)
- No mouse needed ✅

**Rationale:** Vim-like navigation should be complete WITHOUT mouse. We add what Capslock left out.

#### 3. Virtual Keys for IDE Integration (new concept)

**Capslock approach:**
- Some F-key bindings for specific apps
- Mostly hardcoded actions
- No systematic virtual key strategy

**Our approach:**
- F13-F24 reserved as virtual keys
- Clean Layer 1 ↔ Layer 2 interface
- WebStorm/IDE consumes virtual keys
- Extensible to other IDEs

**Rationale:** Better separation between system-wide (Karabiner) and app-specific (WebStorm).

### What We Add Beyond Capslock 🆕

#### 1. Integration with 5-Layer Architecture

**New concepts not in Capslock:**
- Layer -1: [[DEFAULT-KEY-BINDING-CONFIG]] (text system)
- Layer 0: [[HOMEROW-CONFIG]] (UI navigation)
- Explicit layer boundaries
- Mouse only in Layer 0

#### 2. YAML-Based Documentation System

**Our additions:**
- `keyboard-config/data/` YAML files
- Single source of truth for all bindings
- ActionID integration
- Automatic markdown generation
- CSV exports for analysis

#### 3. Obsidian Knowledge Management

**Our additions:**
- `obsidian-vault/` for documentation
- Wikilinks between concepts
- Learning progress tracking
- Comprehensive documentation

#### 4. Virtual Key Allocation Strategy

**Systematic planning:**
- F13-F24 reserved and documented
- Clear mapping to intended actions
- WebStorm ActionID integration ready
- Future expansion documented

### Compatibility Matrix

| Feature | Capslock | Our Config | Status |
|---------|----------|------------|--------|
| Hyper key concept | ✅ | ✅ | ✅ Identical |
| HJKL base navigation | ✅ | ✅ | ✅ Identical |
| Window management | ✅ | ✅ | ✅ Identical |
| App switching | ✅ | ✅ | ✅ Identical |
| Deletion cluster | ✅ | ✅ | ✅ Identical |
| Clipboard tools | ✅ | ✅ | ✅ Identical |
| Terminal bindings | ✅ | ✅ | ✅ Identical |
| Mouse control | ✅ 125 | ❌ 0 | 🔄 Removed |
| Word/para navigation | ⚠️ Partial | ✅ Full | 🔄 Enhanced |
| Virtual keys | ⚠️ Ad-hoc | ✅ Systematic | 🆕 Added |
| 5-layer architecture | ❌ | ✅ | 🆕 Added |
| YAML config system | ❌ | ✅ | 🆕 Added |
| Obsidian docs | ❌ | ✅ | 🆕 Added |

### Philosophy Alignment

**Capslock philosophy:**
> "Capslock makes the most powerful keyboard: Keyboard for ultimate productivity."
> 
> Focus: Complete keyboard-centric workflow including mouse

**Our philosophy ([[PHILOSOPHY-INSPIRATION]]):**
> "Five layers of keyboard productivity, each with clear responsibility and separation of concerns."
> 
> Focus: Composable layers, single responsibility, vim-inspired navigation

**Differences:**
- Capslock: **Monolithic** (one config does everything including mouse)
- Ours: **Layered** (5 configs, each focused on specific layer)

**Compatibility:**
- ✅ Share same core: Hyper key + HJKL navigation
- 🔄 Differ on: Mouse placement and layer separation
- 🆕 We add: Documentation system, virtual keys, multi-layer architecture

### Migration Path

**Can Capslock users adopt our approach?**

Yes! In phases:

1. **Phase 1 (Compatible):** Use Capslock as-is, add Homerow for UI
2. **Phase 2 (Transition):** Start removing mouse bindings, rely more on Homerow
3. **Phase 3 (Our Approach):** Full removal, add enhanced navigation, adopt 5-layer model

**Can we go back to Capslock?**

Yes! We maintain compatibility:
- All core Capslock bindings still work
- Just remove our enhancements
- Re-add mouse bindings if desired
- Git history preserves all changes

### Conclusion

**Capslock is:**
- ✅ Excellent foundation
- ✅ Well-designed core
- ✅ Battle-tested
- ⚠️ Monolithic approach
- ⚠️ Mixes concerns (navigation + mouse)

**Our config is:**
- ✅ Built on Capslock foundation
- ✅ Enhanced with vim-like navigation
- ✅ Layered architecture
- ✅ Clear separation of concerns
- 🆕 Documentation and automation

**We're 90% Capslock, 10% architectural refinement.**

---

## Summary

This plan provides a comprehensive roadmap for:

1. ✅ Removing 125 mouse bindings from Karabiner
2. ✅ Adding enhanced vim-like navigation (word, paragraph, document)
3. ✅ Implementing virtual keys (F13-F24) for WebStorm integration
4. ✅ Aligning with [[FIVE-LAYER-ARCHITECTURE]] philosophy
5. ✅ Maintaining compatibility with Capslock foundations
6. ✅ Documenting everything with wikilinks and YAML configs

**Next Steps:**
1. Begin Phase 1 (backup)
2. Execute phases 2-9 (removal)
3. Execute phases 10-15 (additions)
4. Update YAML configuration files
5. Regenerate markdown documentation
6. Update Obsidian vault with wikilinks

---

## Related Documentation

- [[KARABINER-CONFIG]] - Main configuration reference
- [[HJKL-NAVIGATION]] - Navigation patterns across all layers
- [[HYPER-KEY-MAPPINGS]] - Hyper key concept and usage
- [[FIVE-LAYER-ARCHITECTURE]] - Complete architecture philosophy
- [[HOMEROW-CONFIG]] - Mouse control and UI navigation (Layer 0)
- [[WEBSTORM-KEYMAP]] - IDE integration (Layer 2)
- [[IDEAVIM-CONFIG]] - Vim emulation (Layer 3)
- [[DEFAULT-KEY-BINDING-CONFIG]] - Text system (Layer -1)
- [[PHILOSOPHY-INSPIRATION]] - Core design principles

---

**Document Version:** 1.0  
**Last Updated:** 2025-02-11  
**Status:** Planning Complete, Ready for Implementation
