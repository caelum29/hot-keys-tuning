# IdeaVim HJKL Extensions

###symotion-prefix) G-prefixed HJKL Motions

| Key | Action | IdeaVim Command | Description |
|-----|---------|-----------------|-------------|
| gh  | Move to line start | `^` | Beginning of line (first non-blank character) |
| gl  | Move to line end | `$` | End of line |
| gj  | Next method | `:action MethodDown` | Navigate to next method/function |
| gk  | Previous method | `:action MethodUp` | Navigate to previous method/function |

### Bookmark Navigation (H/L Override)

| Key | Action | IdeaVim Command | Description |
|-----|---------|-----------------|-------------|
| H   | Previous bookmark | `:action GotoPreviousBookmark` | Go to previous bookmark |
| L   | Next bookmark | `:action GotoNextBookmark` | Go to next bookmark |

### Camel Case Operations

| Key | Mode | Action | IdeaVim Command | Description |
|-----|------|---------|-----------------|-------------|
| cH  | Normal | Change camel hump backward | `c[b` | Change to previous camel case boundary |
| cL  | Normal | Change camel hump forward | `c[w` | Change to next camel case boundary |
| dH  | Normal | Delete camel hump backward | `d[b` | Delete to previous camel case boundary |
| dL  | Normal | Delete camel hump forward | `d[w` | Delete to next camel case boundary |
| cih | Normal | Change inner camel hump | `[bc[w` | Change current camel hump |
| dih | Normal | Delete inner camel hump | `[bd[w` | Delete current camel hump |

### Visual Mode HJKL

| Key | Mode | Action | Description |
|-----|------|---------|-------------|
| K   | Visual | Expand selection | `:action EditorSelectWord` - Expand selection to word |
| J   | Visual | Shrink selection | `:action EditorUnSelectWord` - Shrink selection from word |

### Horizontal Scrolling

| Key | Action | IdeaVim Command | Description |
|-----|---------|-----------------|-------------|
| zH  | Scroll left | `50zh` | Scroll 50 characters left |
| zL  | Scroll right | `50zl` | Scroll 50 characters right |

### Special J Bindings

| Key | Mode | Action | IdeaVim Command | Description |
|-----|------|---------|-----------------|-------------|
| J   | Normal | Join lines | `<C-J>` (mapped to `:action EditorJoinLines`) | Smart line joining |

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
