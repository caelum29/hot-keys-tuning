# Karabiner‑Elements Configuration Documentation

**Generated on:** 2/2/2025, 3:30:39 AM

**Filter applied:** Only manipulators matching key_code `h` are included.

## Profile 1: super

### Complex Modifications

#### Rule 3: Hyper Navigation

________________________________________________________________
##### 1: description: command + h = shift + left
| From | To  | 
| --- | --- |
| <kbd>✱</kbd>, <kbd>⌘</kbd> + <kbd>h</kbd> |<kbd>  ⇧ </kbd> + <kbd><-</kbd>

________________________________________________________________
##### 2: description: option + command + h = option + shift + left (select word ahead)
| From | To  | 
| --- | --- |
| <kbd>✱</kbd>, <kbd>⌥</kbd>, <kbd>⌘</kbd> + <kbd>h</kbd> |<kbd>⌥</kbd>, <kbd>  ⇧ </kbd> + <kbd><-</kbd>

________________________________________________________________
##### 3: description: shift + h = ctrl + shift + tab (prev tab)
| From | To  | 
| --- | --- |
| <kbd>✱</kbd>, <kbd>  ⇧ </kbd> + <kbd>h</kbd> |<kbd>⌃</kbd>, <kbd>  ⇧ </kbd> + <kbd>tab</kbd>

________________________________________________________________
##### 4: description: control + h = ctrl + left (prev desktop)
| From | To  | 
| --- | --- |
| <kbd>✱</kbd>, <kbd>⌃</kbd> + <kbd>h</kbd> |<kbd>⌃</kbd> + <kbd><-</kbd>

________________________________________________________________
##### 5: description: option + h = mouse left
| From | To  | 
| --- | --- |
| <kbd>✱</kbd>, <kbd>⌥</kbd> + <kbd>h</kbd> |

________________________________________________________________
##### 6: description: shift + option + h = mouse left fast
| From | To  | 
| --- | --- |
| <kbd>✱</kbd>, <kbd>  ⇧ </kbd>, <kbd>⌥</kbd> + <kbd>h</kbd> |

________________________________________________________________
##### 7: description: shift + control + h = mouse wheel left
| From | To  | 
| --- | --- |
| <kbd>✱</kbd>, <kbd>  ⇧ </kbd>, <kbd>⌃</kbd> + <kbd>h</kbd> |

________________________________________________________________
##### 8: description: shift + command + h = mouse wheel left fast
| From | To  | 
| --- | --- |
| <kbd>✱</kbd>, <kbd>  ⇧ </kbd>, <kbd>⌘</kbd> + <kbd>h</kbd> |

________________________________________________________________
##### 9: description:  h = left
| From | To  | 
| --- | --- |
| <kbd>✱</kbd> + <kbd>h</kbd> | + <kbd><-</kbd>

________________________________________________________________
##### 10: description: control + i = command + h (hide current window)
| From | To  | 
| --- | --- |
| <kbd>✱</kbd>, <kbd>⌃</kbd> + <kbd>i</kbd> |<kbd>⌘</kbd> + <kbd>h</kbd>

#### Rule 15: 3 Awake Digital Keyboard

________________________________________________________________
##### 1: description: 3 + h = ,
| From | To  | 
| --- | --- |
| <kbd>✱</kbd>, <kbd>fn</kbd> + <kbd>h</kbd> | + <kbd>,</kbd>


## Profile 2: vim

### Complex Modifications

#### Rule 3: (Vim 3/11) visual mode + h,j,k,l,e,b,0,^,$,gg,G,{,} + d,y,c,x

________________________________________________________________
##### 1: | From | To  | 
| --- | --- |
| + <kbd>h</kbd> |<kbd>  ⇧ </kbd> + <kbd><-</kbd>
- **Conditions:**
  - {"bundle_identifiers":[],"type":"frontmost_application_unless"}
  - {"name":"visual_mode","type":"variable_if","value":1}

#### Rule 8: (Vim 8/11) h,j,k,l (+ control/option/command/shift),e,b,0,^,$,gg,G,{,}

________________________________________________________________
##### 1: | From | To  | 
| --- | --- |
| (optional: control, option, command, shift) + <kbd>h</kbd> | + <kbd><-</kbd>
- **Conditions:**
  - {"bundle_identifiers":[],"type":"frontmost_application_unless"}
  - {"name":"vim_mode","type":"variable_if","value":1}


