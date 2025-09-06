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

| Modifier | Keystroke       | System | Status | Category   | Action                           | IDE Action ID                            | Karabiner Code                                   | IdeaVim Command             | Config Reference   |
|----------|-----------------|--------|--------|------------|----------------------------------|------------------------------------------|--------------------------------------------------|-----------------------------|--------------------|
| None     | H / L           | I      | ✅      | Navigation | Previous/Next bookmark           | `BookmarksAction`                        | `h/l`                                            | `]'/'[`                     | .ideavimrc:L120    |
| ⇧        | ⇧H / ⇧L         | W      | ✅      | Selection  | Navigate to prev/next bookmark   | `SelectPreviousTab/SelectNextTab`        | `shift+h/l`                                      | `:action SelectPreviousTab` | keymap.xml:L56     |
| ⌃        | ⌃H / ⌃L         | W+I    | ✅      | Text Edit  | Editor join lines/Custom         | `EditorJoinLines`                        | `ctrl+h/l`                                       | `J`                         | keymap.xml:L33     |
| ⌥        | ⌥H / ⌥L         | W      | ✅      | Navigation | Move caret to prev/next word     | `EditorPreviousWord/EditorNextWord`      | `alt+h/l`                                        | `nnoremap <A-h> b`          | keymap.xml:L48     |
| ⌘        | ⌘H / ⌘L         | W      | ✅      | Action     | Custom action/Complete statement | `EditorCompleteStatement`                | `cmd+h/l`                                        | -                           | keymap.xml:L24     |
| ⇧⌃       | ⇧⌃H / ⇧⌃L       | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | `shift+ctrl+h/l`                                 | -                           | -                  |
| ⇧⌥       | ⇧⌥H / ⇧⌥L       | W      | ✅      | Selection  | Prev/Next word with selection    | `EditorPreviousWordWithSelection`        | `shift+alt+h/l`                                  | -                           | keymap.xml:L55     |
| ⇧⌘       | ⇧⌘H / ⇧⌘L       | W      | ✅      | Window     | Select prev/next tab             | `SelectPreviousTab/SelectNextTab`        | `shift+cmd+h/l`                                  | `:action SelectPreviousTab` | keymap.xml:L56     |
| ⌃⌥       | ⌃⌥H / ⌃⌥L       | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | `ctrl+alt+h/l`                                   | -                           | -                  |
| ⌃⌘       | ⌃⌘H / ⌃⌘L       | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | `ctrl+cmd+h/l`                                   | -                           | -                  |
| ⌥⌘       | ⌥⌘H / ⌥⌘L       | W      | ✅      | Action     | Custom action/Reformat code      | `ReformatCode`                           | `alt+cmd+h/l`                                    | -                           | keymap.xml:L59     |
| ⇧⌃⌥      | ⇧⌃⌥H / ⇧⌃⌥L     | W      | ✅      | Window     | Stretch split left/right         | `StretchSplitToLeft/StretchSplitToRight` | `shift+ctrl+alt+h/l`                             | -                           | keymap.xml:L60     |
| ⇧⌃⌘      | ⇧⌃⌘H / ⇧⌃⌘L     | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | `shift+ctrl+cmd+h/l`                             | -                           | -                  |
| ⇧⌥⌘      | ⇧⌥⌘H / ⇧⌥⌘L     | W      | ✅      | Action     | Popup hector/Reformat dialog     | `PopupHector/ShowReformatFileDialog`     | `shift+alt+cmd+h/l`                              | -                           | keymap.xml:L62     |
| ⌃⌥⌘      | ⌃⌥⌘H / ⌃⌥⌘L     | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | `ctrl+alt+cmd+h/l`                               | -                           | -                  |
| ⇧⌃⌥⌘     | ⇧⌃⌥⌘H / ⇧⌃⌥⌘L   | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | `shift+ctrl+alt+cmd+h/l`                         | -                           | -                  |
| ✱        | ✱H / ✱L         | K      | ✅      | Navigation | Move left/right one char         | `left_arrow/right_arrow`                 | `right_shift+right_ctrl+right_alt+right_cmd+h/l` | -                           | karabiner.json:L65 |
| ✱⇧       | ✱⇧H / ✱⇧L       | K      | 📋     | Selection  | Tab switching                    | `SelectPreviousTab`                      | -                                                | -                           | -                  |
| ✱⌃       | ✱⌃H / ✱⌃L       | K      | ✅      | Desktop    | Prev/next desktop                | `left_control+left_arrow`                | -                                                | -                           | karabiner.json:L67 |
| ✱⌥       | ✱⌥H / ✱⌥L       | K      | ⚠️     | Mouse      | Need to remap                    | `mouse_move`                             | -                                                | -                           | -                  |
| ✱⌘       | ✱⌘H / ✱⌘L       | W      | ✅      | Window     | App switcher                     | `Switcher`                               | -                                                | -                           | keymap.xml:L69     |
| ✱⇧⌃      | ✱⇧⌃H / ✱⇧⌃L     | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| ✱⇧⌥      | ✱⇧⌥H / ✱⇧⌥L     | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| ✱⇧⌘      | ✱⇧⌘H / ✱⇧⌘L     | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| ✱⌃⌥      | ✱⌃⌥H / ✱⌃⌥L     | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| ✱⌃⌘      | ✱⌃⌘H / ✱⌃⌘L     | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| ✱⌥⌘      | ✱⌥⌘H / ✱⌥⌘L     | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| ✱⇧⌃⌥     | ✱⇧⌃⌥H / ✱⇧⌃⌥L   | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| ✱⇧⌃⌘     | ✱⇧⌃⌘H / ✱⇧⌃⌘L   | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| ✱⇧⌥⌘     | ✱⇧⌥⌘H / ✱⇧⌥⌘L   | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| ✱⌃⌥⌘     | ✱⌃⌥⌘H / ✱⌃⌥⌘L   | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| ✱⇧⌃⌥⌘    | ✱⇧⌃⌥⌘H / ✱⇧⌃⌥⌘L | -      | 📋     | Custom     | Custom action                    | `Custom`                                 | -                                                | -                           | -                  |
| G        | GH / GL         | I      | ✅      | Navigation | Move to line beginning/end       | `EditorLineStart/EditorLineEnd`          | -                                                | `0/$`                       | .ideavimrc:L81     |
| cH/cL    | cH / cL         | I      | ✅      | Text Edit  | Change camel hump back/forward   | `CamelHumpAction`                        | -                                                | `cb/cw`                     | .ideavimrc:L82     |
| dH/dL    | dH / dL         | I      | ✅      | Text Edit  | Delete camel hump back/forward   | `CamelHumpAction`                        | -                                                | `db/dw`                     | .ideavimrc:L83     |
| cih/dih  | cih / dih       | I      | ✅      | Text Edit  | Change/delete inner camel hump   | `CamelHumpAction`                        | -                                                | `ciw/diw`                   | .ideavimrc:L84     |
| zH/zL    | zH / zL         | I      | ✅      | Navigation | Scroll left/right 50 chars       | `ScrollAction`                           | -                                                | `zh/zl`                     | .ideavimrc:L85     |

## Vertical Navigation Key Bindings (J / K)

| Modifier | Keystroke | System | Status | Category | Action | IDE Action ID | Karabiner Code | IdeaVim Command | Config Reference |
|----------|-----------|---------|---------|----------|---------|---------------|----------------|-----------------|------------------|
| None | J / K | I | ✅ | Text Edit | Join lines/Visual selection | `EditorJoinLines` | `j/k` | `J/<C-v>k` | .ideavimrc:L91 |
| ⇧ | ⇧J / ⇧K | W | ✅ | Selection | Extend selection down/up | `EditorDownWithSelection/EditorUpWithSelection` | `shift+j/k` | `vj/vk` | keymap.xml:L92 |
| ⌃ | ⌃J / ⌃K | W | ✅ | Action | Custom action/Show navbar | `ShowNavBar` | `ctrl+j/k` | - | keymap.xml:L93 |
| ⌥ | ⌥J / ⌥K | W | ✅ | Text Edit | Clone caret below/above | `EditorCloneCaretBelow/EditorCloneCaretAbove` | `alt+j/k` | - | keymap.xml:L18 |
| ⌘ | ⌘J / ⌘K | W | ✅ | Action | Insert live template/Custom | `InsertLiveTemplate` | `cmd+j/k` | - | keymap.xml:L95 |
| ⇧⌃ | ⇧⌃J / ⇧⌃K | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+j/k` | - | - |
| ⇧⌥ | ⇧⌥J / ⇧⌥K | - | 📋 | Custom | Special char | `Special` | `shift+alt+j/k` | - | - |
| ⇧⌘ | ⇧⌘J / ⇧⌘K | W | ✅ | Action | Editor join lines/VCS push | `EditorJoinLines/Vcs.Push` | `shift+cmd+j/k` | - | keymap.xml:L98 |
| ⌃⌥ | ⌃⌥J / ⌃⌥K | W | ✅ | Text Edit | Move line down/up | `MoveLineDown/MoveLineUp` | `ctrl+alt+j/k` | - | keymap.xml:L99 |
| ⌃⌘ | ⌃⌘J / ⌃⌘K | - | 📋 | Custom | Custom action | `Custom` | `ctrl+cmd+j/k` | - | - |
| ⌥⌘ | ⌥⌘J / ⌥⌘K | W | ✅ | Action | Surround with template/Custom | `SurroundWithLiveTemplate` | `alt+cmd+j/k` | - | keymap.xml:L101 |
| ⇧⌃⌥ | ⇧⌃⌥J / ⇧⌃⌥K | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+alt+j/k` | - | - |
| ⇧⌃⌘ | ⇧⌃⌘J / ⇧⌃⌘K | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+cmd+j/k` | - | - |
| ⇧⌥⌘ | ⇧⌥⌘J / ⇧⌥⌘K | - | 📋 | Custom | Custom action | `Custom` | `shift+alt+cmd+j/k` | - | - |
| ⌃⌥⌘ | ⌃⌥⌘J / ⌃⌥⌘K | - | 📋 | Custom | Custom action | `Custom` | `ctrl+alt+cmd+j/k` | - | - |
| ⇧⌃⌥⌘ | ⇧⌃⌥⌘J / ⇧⌃⌥⌘K | - | 📋 | Custom | Custom action | `Custom` | `shift+ctrl+alt+cmd+j/k` | - | - |
| ✱ | ✱J / ✱K | K | ✅ | Navigation | Move down/up one line | `down_arrow/up_arrow` | `right_shift+right_ctrl+right_alt+right_cmd+j/k` | - | karabiner.json:L107 |
| ✱⇧ | ✱⇧J / ✱⇧K | K | 📋 | Navigation | App switching | `AppSwitcher` | - | - | - |
| ✱⌃ | ✱⌃J / ✱⌃K | K | 📋 | Desktop | Focus/expose | `MissionControl` | - | - | - |
| ✱⌥ | ✱⌥J / ✱⌥K | K | 📋 | Mouse | Mouse move | `mouse_move` | - | - | - |
| ✱⌘ | ✱⌘J / ✱⌘K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⇧⌃ | ✱⇧⌃J / ✱⇧⌃K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⇧⌥ | ✱⇧⌥J / ✱⇧⌥K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⇧⌘ | ✱⇧⌘J / ✱⇧⌘K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⌃⌥ | ✱⌃⌥J / ✱⌃⌥K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⌃⌘ | ✱⌃⌘J / ✱⌃⌘K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⌥⌘ | ✱⌥⌘J / ✱⌥⌘K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⇧⌃⌥ | ✱⇧⌃⌥J / ✱⇧⌃⌥K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⇧⌃⌘ | ✱⇧⌃⌘J / ✱⇧⌃⌘K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⇧⌥⌘ | ✱⇧⌥⌘J / ✱⇧⌥⌘K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⌃⌥⌘ | ✱⌃⌥⌘J / ✱⌃⌥⌘K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| ✱⇧⌃⌥⌘ | ✱⇧⌃⌥⌘J / ✱⇧⌃⌥⌘K | - | 📋 | Custom | Custom action | `Custom` | - | - | - |
| G | GJ / GK | I | ✅ | Navigation | Navigate prev/next method | `MethodUp/MethodDown` | - | `[m/]m` | .ideavimrc:L123 |

---
