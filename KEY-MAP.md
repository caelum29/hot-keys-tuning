# Keybindings for Horizontal and Vertical Navigation

This document lists the desired key–modifier combinations for horizontal and vertical navigation.

- For **horizontal navigation**, **H** corresponds to moving left and **L** corresponds to moving right.
- For **vertical navigation**, **J** corresponds to moving down and **K** corresponds to moving up.

Modifiers are represented as follows:

- **Shift**: <kbd>⇧</kbd>
- **Control**: <kbd>⌃</kbd>
- **Option**: <kbd>⌥</kbd>
- **Command**: <kbd>⌘</kbd>
- **Hyper**: <kbd>✱</kbd>  
  (_Note: <kbd>✱</kbd> is implemented as the combination of all right modifiers: <kbd>⌘</kbd><kbd>⌥</kbd><kbd>
  ⌃</kbd><kbd>⇧</kbd>._ [karabiner remap documentation](./src/downloaded/README.md#navigation) and [documentation](https://github.com/Vonng/Capslock#Navigation or [Navigation](###Navigation))
  )

### Navigation

* <kbd>H</kbd>, <kbd>J</kbd>, <kbd>K</kbd>, <kbd>L</kbd>, <kbd>U</kbd>, <kbd>I</kbd>, <kbd>O</kbd>, <kbd>P</kbd> are used as **Navigators**. Maps to <kbd>←</kbd><kbd>↓</kbd><kbd>↑</kbd><kbd>→</kbd><kbd>⇞</kbd><kbd>↖</kbd><kbd>↘</kbd><kbd>⇟</kbd> by default. (pink area).
* 9 control planes has already been allocated for navigators.
* Hold additional <kbd>⌘</kbd> Command for **selection**.  (like holding <kbd>⇧</kbd>shift in normal), additional <kbd>⌥</kbd> Option for **word/para selection**.
* Hold additional <kbd>⇧</kbd> Shift for **app/win/tab switching**.  Hold additional <kbd>⌃</kbd> Control for **desktop management** .
* Hold additional <kbd>⌥</kbd> Option for 🖱️ **mouse move**.  Add <kbd>⇧</kbd>shift to **⏫ accelerate**.  (<kbd>U</kbd>, <kbd>I</kbd>, <kbd>O</kbd>, <kbd>P</kbd> maps to mouse buttons) .
* <kbd>⇧</kbd><kbd>⌥</kbd> turns navigator to **🖲️ mouse wheel**, and <kbd>⇧</kbd><kbd>⌘</kbd> is the ⏫ **accelerated** version .  `HJKL` for wheel, wihle `UIOP` for reversed wheel move.

| Feature | **Move** | **Select** | **WordSel** | **Window** | **Desktop** | 🖱️  | **🖱️⏫** | 🖲️ | 🖲️⏫ |
|:-------:|:--------:|:----------:|:-----------:|:----------:|:-----------:|:----:|:--------:|:---:|:----:|
| Key\Mod |    ✱     |     ⌘      |     ⌘⌥      |     ⇧      |      ⌃      |  ⌥   |    ⇧⌥    | ⇧⌃  |  ⇧⌘  |
|    H    |   Left   | word left  |  word left  |  prev tab  |  prev desk  |  ⬅️  |   ⬅️⏫    | ⬅️  | ⬅️⏫  |
|    J    |   Down   | line down  | 3 line down |  next app  |    focus    |  ⬇️  |   ⬇️⏫    | ⬇️  | ⬇️⏫  |
|    K    |    Up    |  line up   |  3 line up  |  prev app  | expose all  |  ⬆️  |   ⬆️⏫    | ⬆️  | ⬆️⏫  |
|    L    |  Right   | word right | word right  |  next tab  |  next desk  |  ➡️  |   ➡️⏫    | ➡️  | ➡️⏫  |
<!-- later 
|    U    |   PgUp   | prev page  |  prev page  |   zoom-    | fullscreen  | 🖱️L |   🖱️L   | ➡️  | ➡️⏫  |
|    I    |   Home   | line head  |  end2head   |  prev win  |    hide     | 🖱️R |   🖱️R   | ⬆️  | ⬆️⏫  |
|    O    |   End    |  line end  |  head2end   |  next win  |  hide all   | 🖱️B |   🖱️B   | ⬇️  | ⬇️⏫  |
|    P    |   PgDn   | next page  |  next page  |   zoom+    |  Launchpad  | 🖱️F |   🖱️F   | ⬅️  | ⬅️⏫  | 
-->


---

## Horizontal Navigation Key Bindings (H / L)

| Modifier Combination | Keystroke Notation        | Vim | Action                                                        |
|----------------------|---------------------------|-----|---------------------------------------------------------------|
| None                 | H / L                     | [x] | *IdeaVim: Previous/Next bookmark (overrides default)*         |
| ⇧                    | ⇧ + H / L                 | [x] | *" Navigate to the previous/next bookmark*                    |
| ⌃                    | ⌃ + H / L                 | [x] | *EditorJoinLines/Custom action*                               |
| ⌥                    | ⌥ + H / L                 |     | *Move caret to Next/Previous word*                            |
| ⌘                    | ⌘ + H / L                 |     | *Custom action/EditorCompleteStatement*                       |
| ⇧ + ⌃                | ⇧ + ⌃ + H / L             |     | *Custom action/Custom action*                                 |
| ⇧ + ⌥                | ⇧ + ⌥ + H / L             |     | *EditorPreviousWordWithSelection/EditorNextWordWithSelection* |
| ⇧ + ⌘                | ⇧ + ⌘ + H / L             |     | *SelectPreviousTab/SelectNextTab*                             |
| ⌃ + ⌥                | ⌃ + ⌥ + H / L             |     | *Custom action/Custom action*                                 |
| ⌃ + ⌘                | ⌃ + ⌘ + H / L             |     | *Custom action/Custom action*                                 |
| ⌥ + ⌘                | ⌥ + ⌘ + H / L             |     | *Custom action/ReformatCode*                                  |
| ⇧ + ⌃ + ⌥            | ⇧ + ⌃ + ⌥ + H / L         |     | *StretchSplitToLeft/StretchSplitToRight*                      |
| ⇧ + ⌃ + ⌘            | ⇧ + ⌃ + ⌘ + H / L         |     | *Custom action/Custom action*                                 |
| ⇧ + ⌥ + ⌘            | ⇧ + ⌥ + ⌘ + H / L         |     | *PopupHector/ShowReformatFileDialog*                          |
| ⌃ + ⌥ + ⌘            | ⌃ + ⌥ + ⌘ + H / L         |     | *Custom action/Custom action*                                 |
| ⇧ + ⌃ + ⌥ + ⌘        | ⇧ + ⌃ + ⌥ + ⌘ + H / L     |     | *Custom action*                                               |
| ✱                    | ✱ + H / L                 |     | *Move left/right one character* [Navigation](#Navigation)     |
| ✱ + ⇧                | ✱ + ⇧ + H / L             |     |                                                               |
| ✱ + ⌃                | ✱ + ⌃ + H / L             |     | *prev desk/next desk*[Navigation](#Navigation)                |
| ✱ + ⌥                | ✱ + ⌥ + H / L             |     | *need to remap*       [Navigation](#Navigation)               |
| ✱ + ⌘                | ✱ + ⌘ + H / L             |     | *Switcher/Switcher*[Navigation](#Navigation)                  |
| ✱ + ⇧ + ⌃            | ✱ + ⇧ + ⌃ + H / L         |     | *Custom action/Custom action*   [Navigation](#Navigation)     |
| ✱ + ⇧ + ⌥            | ✱ + ⇧ + ⌥ + H / L         |     | *Custom action* [Navigation](#Navigation)                     |
| ✱ + ⇧ + ⌘            | ✱ + ⇧ + ⌘ + H / L         |     | *Custom action* [Navigation](#Navigation)                     |
| ✱ + ⌃ + ⌥            | ✱ + ⌃ + ⌥ + H / L         |     | *Custom action* [Navigation](#Navigation)                     |
| ✱ + ⌃ + ⌘            | ✱ + ⌃ + ⌘ + H / L         |     | *Custom action* [Navigation](#Navigation)                     |
| ✱ + ⌥ + ⌘            | ✱ + ⌥ + ⌘ + H / L         |     | *Custom action* [Navigation](#Navigation)                     |
| ✱ + ⇧ + ⌃ + ⌥        | ✱ + ⇧ + ⌃ + ⌥ + H / L     |     | *Custom action* [Navigation](#Navigation)                     |
| ✱ + ⇧ + ⌃ + ⌘        | ✱ + ⇧ + ⌃ + ⌘ + H / L     |     | *Custom action* [Navigation](#Navigation)                     |
| ✱ + ⇧ + ⌥ + ⌘        | ✱ + ⇧ + ⌥ + ⌘ + H / L     |     | *Custom action* [Navigation](#Navigation)                     |
| ✱ + ⌃ + ⌥ + ⌘        | ✱ + ⌃ + ⌥ + ⌘ + H / L     |     | *Custom action* [Navigation](#Navigation)                     |
| ✱ + ⇧ + ⌃ + ⌥ + ⌘    | ✱ + ⇧ + ⌃ + ⌥ + ⌘ + H / L |     | *Custom action* [Navigation](#Navigation)                     |
| G                    | G -> H / L                | [x] | *" Move to the beginning/end of the line*                     |
| cH / cL              | cH / cL                   | [x] | *IdeaVim: Change camel hump backward/forward*                 |
| dH / dL              | dH / dL                   | [x] | *IdeaVim: Delete camel hump backward/forward*                 |
| cih / dih            | cih / dih                 | [x] | *IdeaVim: Change/Delete inner camel hump*                     |
| zH / zL              | zH / zL                   | [x] | *IdeaVim: Scroll left/right 50 characters*                    |

## Vertical Navigation Key Bindings (J / K)

| Modifier Combination | Keystroke Notation        | Vim | Action                                                |
|----------------------|---------------------------|-----|-------------------------------------------------------|
| None                 | J / K                     | [x] | *IdeaVim: J=Join lines, K in Visual=Expand selection* | 
| ⇧                    | ⇧ + J / K                 |     | *Extend selection down/up*                            |
| ⌃                    | ⌃ + J / K                 |     | *Custom action/ShowNavBar*                            |
| ⌥                    | ⌥ + J / K                 |     | *EditorCloneCaretBelow/EditorCloneCaretAbove*         |
| ⌘                    | ⌘ + J / K                 |     | *InsertLiveTemplate/Custom action*                    |
| ⇧ + ⌃                | ⇧ + ⌃ + J / K             |     | *Custom action/Custom action*                         |
| ⇧ + ⌥                | ⇧ + ⌥ + J / K             |     | *Ô/*                                                 |
| ⇧ + ⌘                | ⇧ + ⌘ + J / K             |     | *EditorJoinLines/Vcs.Push*                            |
| ⌃ + ⌥                | ⌃ + ⌥ + J / K             |     | *MoveLineDown/MoveLineUp*                             |
| ⌃ + ⌘                | ⌃ + ⌘ + J / K             |     | *Custom action/Custom action*                         |
| ⌥ + ⌘                | ⌥ + ⌘ + J / K             |     | *SurroundWithLiveTemplate/Custom action*              |
| ⇧ + ⌃ + ⌥            | ⇧ + ⌃ + ⌥ + J / K         |     | *Custom action/Custom action*                         |
| ⇧ + ⌃ + ⌘            | ⇧ + ⌃ + ⌘ + J / K         |     | *Custom action/Custom action*                         |
| ⇧ + ⌥ + ⌘            | ⇧ + ⌥ + ⌘ + J / K         |     | *Custom action/Custom action*                         |
| ⌃ + ⌥ + ⌘            | ⌃ + ⌥ + ⌘ + J / K         |     | *Custom action/Custom action*                         |
| ⇧ + ⌃ + ⌥ + ⌘        | ⇧ + ⌃ + ⌥ + ⌘ + J / K     |     | *Custom action/Custom action*                         |
| ✱                    | ✱ + J / K                 |     | *Move down/up one line* [Navigation](#Navigation)     |
| ✱ + ⇧                | ✱ + ⇧ + J / K             |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⌃                | ✱ + ⌃ + J / K             |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⌥                | ✱ + ⌥ + J / K             |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⌘                | ✱ + ⌘ + J / K             |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⇧ + ⌃            | ✱ + ⇧ + ⌃ + J / K         |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⇧ + ⌥            | ✱ + ⇧ + ⌥ + J / K         |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⇧ + ⌘            | ✱ + ⇧ + ⌘ + J / K         |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⌃ + ⌥            | ✱ + ⌃ + ⌥ + J / K         |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⌃ + ⌘            | ✱ + ⌃ + ⌘ + J / K         |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⌥ + ⌘            | ✱ + ⌥ + ⌘ + J / K         |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⇧ + ⌃ + ⌥        | ✱ + ⇧ + ⌃ + ⌥ + J / K     |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⇧ + ⌃ + ⌘        | ✱ + ⇧ + ⌃ + ⌘ + J / K     |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⇧ + ⌥ + ⌘        | ✱ + ⇧ + ⌥ + ⌘ + J / K     |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⌃ + ⌥ + ⌘        | ✱ + ⌃ + ⌥ + ⌘ + J / K     |     | *Custom action* [Navigation](#Navigation)             |
| ✱ + ⇧ + ⌃ + ⌥ + ⌘    | ✱ + ⇧ + ⌃ + ⌥ + ⌘ + J / K |     | *Custom action* [Navigation](#Navigation)             |
| G                    | G -> J / K                | [x] | *" Navigate previous/next method*                     |

---
