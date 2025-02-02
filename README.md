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
  ⌃</kbd><kbd>⇧</kbd>._)

---

## Horizontal Navigation Key Bindings (H / L)

| Modifier Combination | Keystroke Notation        | Vim | Action                                                                                                      |
|----------------------|---------------------------|-----|-------------------------------------------------------------------------------------------------------------|
| None                 | H / L                     |     | *Default: Move left/right one character*                                                                    |
| ⇧                    | ⇧ + H / L                 | [x] | *" Navigate to the previous/next bookmark*                                                                  |
| ⌃                    | ⌃ + H / L                 | [x] | *EditorJoinLines/Custom action*                                                                             |
| ⌥                    | ⌥ + H / L                 |     | *Move caret to Next/Previous word*                                                                          |
| ⌘                    | ⌘ + H / L                 |     | *Custom action/EditorCompleteStatement*                                                                     |
| ⇧ + ⌃                | ⇧ + ⌃ + H / L             |     | *Custom action/Custom action*                                                                               |
| ⇧ + ⌥                | ⇧ + ⌥ + H / L             |     | *EditorPreviousWordWithSelection/EditorNextWordWithSelection*                                               |
| ⇧ + ⌘                | ⇧ + ⌘ + H / L             |     | *Custom action/Custom action*                                                                               |
| ⌃ + ⌥                | ⌃ + ⌥ + H / L             |     | *Custom action/Custom action*                                                                               |
| ⌃ + ⌘                | ⌃ + ⌘ + H / L             |     | *Custom action/Custom action*                                                                               |
| ⌥ + ⌘                | ⌥ + ⌘ + H / L             |     | *Custom action/ReformatCode*                                                                                |
| ⇧ + ⌃ + ⌥            | ⇧ + ⌃ + ⌥ + H / L         |     | *StretchSplitToLeft/StretchSplitToRight*                                                                    |
| ⇧ + ⌃ + ⌘            | ⇧ + ⌃ + ⌘ + H / L         |     | *Custom action/Custom action*                                                                               |
| ⇧ + ⌥ + ⌘            | ⇧ + ⌥ + ⌘ + H / L         |     | *PopupHector/ShowReformatFileDialog*                                                                        |
| ⌃ + ⌥ + ⌘            | ⌃ + ⌥ + ⌘ + H / L         |     | *Custom action/Custom action*                                                                               |
| ⇧ + ⌃ + ⌥ + ⌘        | ⇧ + ⌃ + ⌥ + ⌘ + H / L     |     | *Custom action*                                                                                             |
| ✱                    | ✱ + H / L                 |     | *Move left/right one character*                                                                             |
| ✱ + ⇧                | ✱ + ⇧ + H / L             |     | *Switcher/Switcher*                                                                                         |
| ✱ + ⌃                | ✱ + ⌃ + H / L             |     | *Custom action*                                                                                             |
| ✱ + ⌥                | ✱ + ⌥ + H / L             |     | *Custom action*                                                                                             |
| ✱ + ⌘                | ✱ + ⌘ + H / L             |     | *EditorLeftWithSelection/EditorRightWithSelection* [karabiner remap](./src/downloaded/README.md#navigation) |
| ✱ + ⇧ + ⌃            | ✱ + ⇧ + ⌃ + H / L         |     | *Custom action/Custom action*                                                                               |
| ✱ + ⇧ + ⌥            | ✱ + ⇧ + ⌥ + H / L         |     | *Custom action*                                                                                             |
| ✱ + ⇧ + ⌘            | ✱ + ⇧ + ⌘ + H / L         |     | *Custom action*                                                                                             |
| ✱ + ⌃ + ⌥            | ✱ + ⌃ + ⌥ + H / L         |     | *Custom action*                                                                                             |
| ✱ + ⌃ + ⌘            | ✱ + ⌃ + ⌘ + H / L         |     | *Custom action*                                                                                             |
| ✱ + ⌥ + ⌘            | ✱ + ⌥ + ⌘ + H / L         |     | *Custom action*                                                                                             |
| ✱ + ⇧ + ⌃ + ⌥        | ✱ + ⇧ + ⌃ + ⌥ + H / L     |     | *Custom action*                                                                                             |
| ✱ + ⇧ + ⌃ + ⌘        | ✱ + ⇧ + ⌃ + ⌘ + H / L     |     | *Custom action*                                                                                             |
| ✱ + ⇧ + ⌥ + ⌘        | ✱ + ⇧ + ⌥ + ⌘ + H / L     |     | *Custom action*                                                                                             |
| ✱ + ⌃ + ⌥ + ⌘        | ✱ + ⌃ + ⌥ + ⌘ + H / L     |     | *Custom action*                                                                                             |
| ✱ + ⇧ + ⌃ + ⌥ + ⌘    | ✱ + ⇧ + ⌃ + ⌥ + ⌘ + H / L |     | *Custom action*                                                                                             |
| G                    | G -> H / L                | [x] | *" Move to the beginning/end of the line*                                                                   |

## Vertical Navigation Key Bindings (J / K)

| Modifier Combination | Keystroke Notation        | Vim | Action                                         |
|----------------------|---------------------------|-----|------------------------------------------------|
| None                 | J / K                     |     | *Default: Move down/up one line*               | 
| ⇧                    | ⇧ + J / K                 |     | *Extend selection down/up*                     |
| ⌃                    | ⌃ + J / K                 |     | *Move down/up by one paragraph or custom step* |
| ⌥                    | ⌥ + J / K                 |     | *Jump to beginning/end of block*               |
| ⌘                    | ⌘ + J / K                 |     | *Custom IDE action (if needed)*                |
| ⇧ + ⌃                | ⇧ + ⌃ + J / K             |     | *Custom action*                                |
| ⇧ + ⌥                | ⇧ + ⌥ + J / K             |     | *Custom action*                                |
| ⇧ + ⌘                | ⇧ + ⌘ + J / K             |     | *Custom action*                                |
| ⌃ + ⌥                | ⌃ + ⌥ + J / K             |     | *Custom action*                                |
| ⌃ + ⌘                | ⌃ + ⌘ + J / K             |     | *Custom action*                                |
| ⌥ + ⌘                | ⌥ + ⌘ + J / K             |     | *Custom action*                                |
| ⇧ + ⌃ + ⌥            | ⇧ + ⌃ + ⌥ + J / K         |     | *Custom action*                                |
| ⇧ + ⌃ + ⌘            | ⇧ + ⌃ + ⌘ + J / K         |     | *Custom action*                                |
| ⇧ + ⌥ + ⌘            | ⇧ + ⌥ + ⌘ + J / K         |     | *Custom action*                                |
| ⌃ + ⌥ + ⌘            | ⌃ + ⌥ + ⌘ + J / K         |     | *Custom action*                                |
| ⇧ + ⌃ + ⌥ + ⌘        | ⇧ + ⌃ + ⌥ + ⌘ + J / K     |     | *Custom action*                                |
| ✱                    | ✱ + J / K                 |     | *Move down/up one line*                        |
| ✱ + ⇧                | ✱ + ⇧ + J / K             |     | *Custom action*                                |
| ✱ + ⌃                | ✱ + ⌃ + J / K             |     | *Custom action*                                |
| ✱ + ⌥                | ✱ + ⌥ + J / K             |     | *Custom action*                                |
| ✱ + ⌘                | ✱ + ⌘ + J / K             |     | *Custom action*                                |
| ✱ + ⇧ + ⌃            | ✱ + ⇧ + ⌃ + J / K         |     | *Custom action*                                |
| ✱ + ⇧ + ⌥            | ✱ + ⇧ + ⌥ + J / K         |     | *Custom action*                                |
| ✱ + ⇧ + ⌘            | ✱ + ⇧ + ⌘ + J / K         |     | *Custom action*                                |
| ✱ + ⌃ + ⌥            | ✱ + ⌃ + ⌥ + J / K         |     | *Custom action*                                |
| ✱ + ⌃ + ⌘            | ✱ + ⌃ + ⌘ + J / K         |     | *Custom action*                                |
| ✱ + ⌥ + ⌘            | ✱ + ⌥ + ⌘ + J / K         |     | *Custom action*                                |
| ✱ + ⇧ + ⌃ + ⌥        | ✱ + ⇧ + ⌃ + ⌥ + J / K     |     | *Custom action*                                |
| ✱ + ⇧ + ⌃ + ⌘        | ✱ + ⇧ + ⌃ + ⌘ + J / K     |     | *Custom action*                                |
| ✱ + ⇧ + ⌥ + ⌘        | ✱ + ⇧ + ⌥ + ⌘ + J / K     |     | *Custom action*                                |
| ✱ + ⌃ + ⌥ + ⌘        | ✱ + ⌃ + ⌥ + ⌘ + J / K     |     | *Custom action*                                |
| ✱ + ⇧ + ⌃ + ⌥ + ⌘    | ✱ + ⇧ + ⌃ + ⌥ + ⌘ + J / K |     | *Custom action*                                |
| G                    | G -> J / K                | [x] | *" Navigate previous/next method*              |

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
