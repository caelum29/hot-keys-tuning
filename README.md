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

| Modifier Combination | Keystroke Notation        | Vim | Action                                                                       |
|----------------------|---------------------------|-----|------------------------------------------------------------------------------|
| None                 | H / L                     |     | *Default: Move left/right one character*                                     |
| ⇧                    | ⇧ + H / L                 | [x] | *" Navigate to the previous/next bookmark*                                   |
| ⌃                    | ⌃ + H / L                 | [x] | *EditorJoinLines/Custom action*                                              |
| ⌥                    | ⌥ + H / L                 |     | *Move caret to Next/Previous word*                                           |
| ⌘                    | ⌘ + H / L                 |     | *Custom action/EditorCompleteStatement*                                      |
| ⇧ + ⌃                | ⇧ + ⌃ + H / L             |     | *Custom action/Custom action*                                                |
| ⇧ + ⌥                | ⇧ + ⌥ + H / L             |     | *EditorPreviousWordWithSelection/EditorNextWordWithSelection*                |
| ⇧ + ⌘                | ⇧ + ⌘ + H / L             |     | *Custom action/Custom action*                                                |
| ⌃ + ⌥                | ⌃ + ⌥ + H / L             |     | *Custom action/Custom action*                                                |
| ⌃ + ⌘                | ⌃ + ⌘ + H / L             |     | *Custom action/Custom action*                                                |
| ⌥ + ⌘                | ⌥ + ⌘ + H / L             |     | *Custom action/ReformatCode*                                                 |
| ⇧ + ⌃ + ⌥            | ⇧ + ⌃ + ⌥ + H / L         |     | *StretchSplitToLeft/StretchSplitToRight*                                     |
| ⇧ + ⌃ + ⌘            | ⇧ + ⌃ + ⌘ + H / L         |     | *Custom action/Custom action*                                                |
| ⇧ + ⌥ + ⌘            | ⇧ + ⌥ + ⌘ + H / L         |     | *PopupHector/ShowReformatFileDialog*                                         |
| ⌃ + ⌥ + ⌘            | ⌃ + ⌥ + ⌘ + H / L         |     | *Custom action/Custom action*                                                |
| ⇧ + ⌃ + ⌥ + ⌘        | ⇧ + ⌃ + ⌥ + ⌘ + H / L     |     | *Custom action*                                                              |
| ✱                    | ✱ + H / L                 |     | *Move left/right one character* [Navigation](#Navigation)                    |
| ✱ + ⇧                | ✱ + ⇧ + H / L             |     | *Switcher/Switcher*[Navigation](#Navigation)                                 |
| ✱ + ⌃                | ✱ + ⌃ + H / L             |     | *prev desk/next desk*[Navigation](#Navigation)                               |
| ✱ + ⌥                | ✱ + ⌥ + H / L             |     | *need to remap*       [Navigation](#Navigation)                              |
| ✱ + ⌘                | ✱ + ⌘ + H / L             |     | *EditorLeftWithSelection/EditorRightWithSelection* [Navigation](#Navigation) |
| ✱ + ⇧ + ⌃            | ✱ + ⇧ + ⌃ + H / L         |     | *Custom action/Custom action*   [Navigation](#Navigation)                    |
| ✱ + ⇧ + ⌥            | ✱ + ⇧ + ⌥ + H / L         |     | *Custom action* [Navigation](#Navigation)                                    |
| ✱ + ⇧ + ⌘            | ✱ + ⇧ + ⌘ + H / L         |     | *Custom action* [Navigation](#Navigation)                                    |
| ✱ + ⌃ + ⌥            | ✱ + ⌃ + ⌥ + H / L         |     | *Custom action* [Navigation](#Navigation)                                    |
| ✱ + ⌃ + ⌘            | ✱ + ⌃ + ⌘ + H / L         |     | *Custom action* [Navigation](#Navigation)                                    |
| ✱ + ⌥ + ⌘            | ✱ + ⌥ + ⌘ + H / L         |     | *Custom action* [Navigation](#Navigation)                                    |
| ✱ + ⇧ + ⌃ + ⌥        | ✱ + ⇧ + ⌃ + ⌥ + H / L     |     | *Custom action* [Navigation](#Navigation)                                    |
| ✱ + ⇧ + ⌃ + ⌘        | ✱ + ⇧ + ⌃ + ⌘ + H / L     |     | *Custom action* [Navigation](#Navigation)                                    |
| ✱ + ⇧ + ⌥ + ⌘        | ✱ + ⇧ + ⌥ + ⌘ + H / L     |     | *Custom action* [Navigation](#Navigation)                                    |
| ✱ + ⌃ + ⌥ + ⌘        | ✱ + ⌃ + ⌥ + ⌘ + H / L     |     | *Custom action* [Navigation](#Navigation)                                    |
| ✱ + ⇧ + ⌃ + ⌥ + ⌘    | ✱ + ⇧ + ⌃ + ⌥ + ⌘ + H / L |     | *Custom action* [Navigation](#Navigation)                                    |
| G                    | G -> H / L                | [x] | *" Move to the beginning/end of the line*                                    |

## Vertical Navigation Key Bindings (J / K)

| Modifier Combination | Keystroke Notation        | Vim | Action                                             |
|----------------------|---------------------------|-----|----------------------------------------------------|
| None                 | J / K                     |     | *Default: Move down/up one line*                   | 
| ⇧                    | ⇧ + J / K                 |     | *Extend selection down/up*                         |
| ⌃                    | ⌃ + J / K                 |     | *Custom action/ShowNavBar*                         |
| ⌥                    | ⌥ + J / K                 |     | *EditorCloneCaretBelow/EditorCloneCaretAbove*      |
| ⌘                    | ⌘ + J / K                 |     | *InsertLiveTemplate/Custom action*                 |
| ⇧ + ⌃                | ⇧ + ⌃ + J / K             |     | *Custom action/Custom action*                      |
| ⇧ + ⌥                | ⇧ + ⌥ + J / K             |     | *Ô/*                                              |
| ⇧ + ⌘                | ⇧ + ⌘ + J / K             |     | *EditorJoinLines/Vcs.Push*                         |
| ⌃ + ⌥                | ⌃ + ⌥ + J / K             |     | *MoveLineDown/MoveLineUp*                          |
| ⌃ + ⌘                | ⌃ + ⌘ + J / K             |     | *Custom action/Custom action*                      |
| ⌥ + ⌘                | ⌥ + ⌘ + J / K             |     | *SurroundWithLiveTemplate/Custom action*           |
| ⇧ + ⌃ + ⌥            | ⇧ + ⌃ + ⌥ + J / K         |     | *Custom action/Custom action*                      |
| ⇧ + ⌃ + ⌘            | ⇧ + ⌃ + ⌘ + J / K         |     | *Custom action/Custom action*                      |
| ⇧ + ⌥ + ⌘            | ⇧ + ⌥ + ⌘ + J / K         |     | *Custom action/Custom action*                      |
| ⌃ + ⌥ + ⌘            | ⌃ + ⌥ + ⌘ + J / K         |     | *Custom action/Custom action*                      |
| ⇧ + ⌃ + ⌥ + ⌘        | ⇧ + ⌃ + ⌥ + ⌘ + J / K     |     | *Custom action/Custom action*                      |
| ✱                    | ✱ + J / K                 |     | *Move down/up one line* [Navigation](#Navigation)  |
| ✱ + ⇧                | ✱ + ⇧ + J / K             |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⌃                | ✱ + ⌃ + J / K             |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⌥                | ✱ + ⌥ + J / K             |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⌘                | ✱ + ⌘ + J / K             |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⇧ + ⌃            | ✱ + ⇧ + ⌃ + J / K         |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⇧ + ⌥            | ✱ + ⇧ + ⌥ + J / K         |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⇧ + ⌘            | ✱ + ⇧ + ⌘ + J / K         |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⌃ + ⌥            | ✱ + ⌃ + ⌥ + J / K         |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⌃ + ⌘            | ✱ + ⌃ + ⌘ + J / K         |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⌥ + ⌘            | ✱ + ⌥ + ⌘ + J / K         |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⇧ + ⌃ + ⌥        | ✱ + ⇧ + ⌃ + ⌥ + J / K     |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⇧ + ⌃ + ⌘        | ✱ + ⇧ + ⌃ + ⌘ + J / K     |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⇧ + ⌥ + ⌘        | ✱ + ⇧ + ⌥ + ⌘ + J / K     |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⌃ + ⌥ + ⌘        | ✱ + ⌃ + ⌥ + ⌘ + J / K     |     | *Custom action* [Navigation](#Navigation)          |
| ✱ + ⇧ + ⌃ + ⌥ + ⌘    | ✱ + ⇧ + ⌃ + ⌥ + ⌘ + J / K |     | *Custom action* [Navigation](#Navigation)          |
| G                    | G -> J / K                | [x] | *" Navigate previous/next method*                  |

---

*Note:*

- For horizontal navigation, **H** corresponds to moving left and **L** corresponds to moving right.
- For vertical navigation, **J** corresponds to moving down and **K** corresponds to moving up.

### .ideavimrc

" Navigate previous/next method
nnoremap gj :action MethodDown <CR>
nnoremap gk :action MethodUp <CR>

" Move to the beginning/end of the line
map gh ^
map gl $

" Navigate to the previous/next bookmark
nnoremap L :action GotoNextBookmark<CR>
nnoremap H :action GotoPreviousBookmark<CR>

" Join lines smartly
nmap <C-j> <Action>(EditorJoinLines)
nnoremap J <C-J>

---
TODO: in karabiner need to rewrite "description": "F tap = F, F hold = left_command; D tap = D, D hold = left_option; S
tap = S, S hold = left_control",

---

<!-- webstorm keymap xml
<keymap version="1" name="macOS copy" parent="Mac OS X 10.5+">
    <action id="ActivateBigDataToolWindowToolWindow">
        <keyboard-shortcut first-keystroke="shift ctrl meta b" />
    </action>
    <action id="ActivateTerminalToolWindow">
        <keyboard-shortcut first-keystroke="ctrl comma" />
    </action>
    <action id="CheckinProject" />
    <action id="CodeCompletion">
        <keyboard-shortcut first-keystroke="alt quote" />
    </action>
    <action id="DatabaseView.PropertiesAction" />
    <action id="EditorChooseLookupItemReplace">
        <keyboard-shortcut first-keystroke="tab" />
        <keyboard-shortcut first-keystroke="alt semicolon" />
        <keyboard-shortcut first-keystroke="meta semicolon" />
    </action>
    <action id="EditorCloneCaretAbove">
        <keyboard-shortcut first-keystroke="alt k" />
    </action>
    <action id="EditorCloneCaretBelow">
        <keyboard-shortcut first-keystroke="alt j" />
    </action>
    <action id="EditorCompleteStatement">
        <keyboard-shortcut first-keystroke="shift meta enter" />
        <keyboard-shortcut first-keystroke="meta l" />
    </action>
    <action id="EditorCutLineEnd" />
    <action id="EditorDown">
        <keyboard-shortcut first-keystroke="down" />
    </action>
    <action id="EditorEnter">
        <keyboard-shortcut first-keystroke="enter" />
        <keyboard-shortcut first-keystroke="meta i" />
    </action>
    <action id="EditorJoinLines">
        <keyboard-shortcut first-keystroke="shift meta j" />
    </action>
    <action id="EditorLeft">
        <keyboard-shortcut first-keystroke="left" />
    </action>
    <action id="EditorLineEnd">
        <keyboard-shortcut first-keystroke="end" />
        <keyboard-shortcut first-keystroke="meta right" />
    </action>
    <action id="EditorLineStart">
        <keyboard-shortcut first-keystroke="home" />
        <keyboard-shortcut first-keystroke="meta left" />
    </action>
    <action id="EditorNextWord">
        <keyboard-shortcut first-keystroke="alt right" />
        <keyboard-shortcut first-keystroke="alt l" />
    </action>
    <action id="EditorNextWordWithSelection">
        <keyboard-shortcut first-keystroke="shift alt right" />
        <keyboard-shortcut first-keystroke="shift alt l" />
    </action>
    <action id="EditorPaste">
        <keyboard-shortcut first-keystroke="meta v" />
        <keyboard-shortcut first-keystroke="meta p" />
    </action>
    <action id="EditorPreviousWord">
        <keyboard-shortcut first-keystroke="alt left" />
        <keyboard-shortcut first-keystroke="alt h" />
    </action>
    <action id="EditorPreviousWordWithSelection">
        <keyboard-shortcut first-keystroke="shift alt left" />
        <keyboard-shortcut first-keystroke="shift alt h" />
    </action>
    <action id="EditorRight">
        <keyboard-shortcut first-keystroke="right" />
    </action>
    <action id="EditorToggleShowBreadcrumbs">
        <keyboard-shortcut first-keystroke="alt w" />
    </action>
    <action id="EditorUnindentSelection" />
    <action id="EditorUp">
        <keyboard-shortcut first-keystroke="up" />
    </action>
    <action id="EmmetNextEditPoint" />
    <action id="EmmetPreviousEditPoint" />
    <action id="FileChooser.TogglePathShowing" />
    <action id="Git.Commit.And.Push.Executor" />
    <action id="GotoLine" />
    <action id="GotoRow" />
    <action id="Hg.Commit.And.Push.Executor" />
    <action id="HighlightUsagesInFile">
        <keyboard-shortcut first-keystroke="shift meta f7" />
        <keyboard-shortcut first-keystroke="alt f" />
    </action>
    <action id="List-selectPreviousColumn">
        <keyboard-shortcut first-keystroke="left" />
    </action>
    <action id="MoveLineDown">
        <keyboard-shortcut first-keystroke="shift alt down" />
        <keyboard-shortcut first-keystroke="ctrl alt j" />
    </action>
    <action id="MoveLineUp">
        <keyboard-shortcut first-keystroke="shift alt up" />
        <keyboard-shortcut first-keystroke="ctrl alt k" />
    </action>
    <action id="NavBar-selectLeft">
        <keyboard-shortcut first-keystroke="left" />
    </action>
    <action id="ParameterInfo" />
    <action id="PasteMultiple">
        <keyboard-shortcut first-keystroke="shift meta v" />
        <keyboard-shortcut first-keystroke="alt v" />
    </action>
    <action id="ShowNavBar">
        <keyboard-shortcut first-keystroke="meta up" />
        <keyboard-shortcut first-keystroke="alt home" />
        <keyboard-shortcut first-keystroke="ctrl k" />
    </action>
    <action id="ShowUsages">
        <keyboard-shortcut first-keystroke="meta alt f7" />
        <keyboard-shortcut first-keystroke="alt s" />
    </action>
    <action id="SmartTypeCompletion">
        <keyboard-shortcut first-keystroke="shift ctrl space" />
        <keyboard-shortcut first-keystroke="shift alt quote" />
    </action>
    <action id="StretchSplitToBottom">
        <keyboard-shortcut first-keystroke="shift ctrl alt j" />
    </action>
    <action id="StretchSplitToLeft">
        <keyboard-shortcut first-keystroke="shift ctrl alt h" />
    </action>
    <action id="StretchSplitToRight">
        <keyboard-shortcut first-keystroke="shift ctrl alt l" />
    </action>
    <action id="StretchSplitToTop">
        <keyboard-shortcut first-keystroke="shift ctrl alt k" />
    </action>
    <action id="Terminal.ClearBuffer">
        <keyboard-shortcut first-keystroke="meta k" />
    </action>
    <action id="Tree-selectParent">
        <keyboard-shortcut first-keystroke="left" />
    </action>
    <action id="Vcs.Log.FocusTextFilter" />
    <action id="copilot.disposeInlays" />
    <action id="org.intellij.plugins.markdown.ui.actions.styling.ToggleItalicAction" />
</keymap>
-->
