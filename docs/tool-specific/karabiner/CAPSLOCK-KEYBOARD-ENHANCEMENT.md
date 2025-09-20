# Capslock Keyboard Enhancement - System-Level Productivity

## Project Overview

**Capslock** is a revolutionary keyboard modification tool that transforms the traditionally underutilized CapsLock key into a powerful productivity enhancer. The project's motto "Make CapsLock Great Again!" perfectly captures its mission to reimagine one of the most accessible but least useful keys on the keyboard.

- **Repository**: [Vonng/Capslock](https://github.com/Vonng/Capslock)
- **Platform Support**: macOS, Windows
- **Dependencies**: Karabiner-Elements (macOS)

## Core Concept

### Dual Functionality
- **Tap CapsLock**: Emits `Escape` key (perfect for Vim users)
- **Hold CapsLock**: Activates "Hyper" modifier key with extensive capabilities

### The Hyper Key Advantage
The Hyper key concept provides access to 16 different control planes, each offering specialized functionality without conflicts with existing shortcuts.

## Key Enhancement Categories

### 1. Navigation Control (Vim-style)
```
CapsLock + H/J/K/L → Arrow keys (Vim-style navigation)
CapsLock + U/I/O/P → Home/PageDown/PageUp/End
CapsLock + N/M     → Forward/Backward word
```

### 2. Smart Deletion
```
CapsLock + Q/W/E/R → Delete char backward/forward, word backward/forward
CapsLock + A/S     → Delete to line start/end
```

### 3. Mouse Control from Keyboard
```
CapsLock + Mouse movements via keyboard
CapsLock + Scroll wheel control
CapsLock + Click actions
```

### 4. Window Management
```
CapsLock + Tab → Application switching
CapsLock + Arrow combinations → Window positioning
```

### 5. Application Shortcuts
```
CapsLock + F → Finder
CapsLock + T → Terminal
CapsLock + V → Paste (system clipboard)
```

### 6. Terminal Enhancements
```
CapsLock + C → Ctrl+C (interrupt)
CapsLock + Z → Ctrl+Z (suspend)
CapsLock + D → Ctrl+D (EOF)
```

### 7. Clipboard Management
Advanced copy/paste operations with multiple clipboard support.

### 8. Symbol Shifting
Quick access to commonly used symbols and punctuation.

### 9. Function Key Enhancement
Transform function keys for development workflows.

## Technical Architecture

### Configuration System
- **16 Control Planes**: Extensive customization possibilities
- **Contextual Mapping**: Different behaviors for different applications
- **Profile Support**: Multiple configurations for different workflows

### Integration Points
- **Karabiner-Elements**: Deep macOS keyboard customization
- **System Integration**: Works across all applications
- **Developer Friendly**: JSON-based configuration

## Installation Process

### macOS Setup
1. **Install Karabiner-Elements**
   ```bash
   brew install --cask karabiner-elements
   ```

2. **Import Capslock Configuration**
   - Use the special configuration URL provided in the repository
   - Or manually download and import the JSON configuration

3. **Enable Modifications**
   - Open Karabiner-Elements preferences
   - Enable the Capslock modifications
   - Restart applications as needed

### Configuration Verification
```bash
# Check Karabiner-Elements is running
ps aux | grep karabiner

# Verify configuration loaded
ls ~/.config/karabiner/
```

## Developer Workflow Integration

### WebStorm/IntelliJ Enhancement
```
CapsLock + Navigation → Perfect complement to WebStorm shortcuts
CapsLock + Vim bindings → Seamless Vim integration
CapsLock + Mouse control → Reduced mouse dependency
```

### Terminal Productivity
```
CapsLock + Terminal shortcuts → Enhanced command line efficiency
CapsLock + Process control → Quick interrupt/suspend operations
```

### Code Navigation
```
CapsLock + H/J/K/L → Navigate code without arrow keys
CapsLock + Word jumping → Quick code traversal
CapsLock + Line operations → Efficient editing workflows
```

## Productivity Benefits

### 1. Ergonomic Advantages
- **Reduced Hand Movement**: Everything accessible from home row
- **Muscle Memory**: Consistent patterns across applications
- **RSI Prevention**: Less reaching for mouse and arrow keys

### 2. Speed Improvements
- **Instant Access**: No modifier key combinations needed
- **Context Switching**: Faster application and window management
- **Vim Integration**: Perfect for developers using Vim keybindings

### 3. Consistency
- **Universal Shortcuts**: Same shortcuts work everywhere
- **Application Agnostic**: Consistent behavior across all apps
- **Customizable**: Adapt to personal workflow preferences

## Advanced Configuration

### Custom Control Planes
```json
{
  "description": "Custom Developer Plane",
  "manipulators": [
    {
      "from": {"key_code": "h", "modifiers": {"mandatory": ["fn"]}},
      "to": [{"key_code": "left_arrow"}],
      "type": "basic"
    }
  ]
}
```

### Application-Specific Mappings
- Different behaviors for Terminal, WebStorm, Browser
- Context-aware shortcuts that adapt to current application
- Profile switching for different development contexts

## Best Practices

### 1. Gradual Adoption
- Start with basic navigation (H/J/K/L)
- Add deletion shortcuts once navigation is muscle memory
- Gradually incorporate application shortcuts

### 2. Customization Strategy
- Begin with default configuration
- Identify your most frequent actions
- Customize control planes for your specific workflow

### 3. Integration with Development Tools
- Combine with WebStorm's vim plugin
- Use alongside terminal multiplexers (tmux/screen)
- Integrate with window managers for full keyboard control

## Troubleshooting

### Common Issues
```bash
# Karabiner-Elements not detecting changes
killall karabiner_console_user_server
sudo launchctl kickstart -k system/com.pqrs.karabiner.karabiner_console_user_server

# Configuration conflicts
# Check for conflicting shortcuts in System Preferences > Keyboard > Shortcuts
```

### Performance Optimization
- Disable unused control planes
- Optimize for most frequently used shortcuts
- Monitor system impact with Activity Monitor

## Professional Setup

### Team Configuration
- Share configuration files via dotfiles repository
- Document team-specific customizations
- Standardize development environment shortcuts

### Version Control
```bash
# Backup configuration
cp ~/.config/karabiner/karabiner.json ~/dotfiles/karabiner/
git add ~/dotfiles/karabiner/karabiner.json
git commit -m "Update Capslock configuration"
```

## Comparison with WebStorm Shortcuts

| Action | WebStorm | Capslock Enhanced | Benefit |
|--------|----------|-------------------|---------|
| Navigate | Arrow keys | CapsLock + H/J/K/L | Home row access |
| Word jump | Option + Arrow | CapsLock + N/M | Consistent pattern |
| Delete word | Option + Delete | CapsLock + W/R | Faster access |
| App switch | Cmd + Tab | CapsLock + Tab | Easier to press |

## Conclusion

Capslock transforms the keyboard into a more efficient development tool by:

1. **Eliminating Dead Keys**: Makes CapsLock productive
2. **Reducing Hand Movement**: Everything from home row position  
3. **Universal Consistency**: Same shortcuts everywhere
4. **Vim Philosophy**: Brings Vim efficiency to the entire system
5. **Developer Focused**: Perfect complement to IDE shortcuts

This system-level enhancement pairs perfectly with WebStorm's powerful shortcuts, creating a comprehensive keyboard-driven development environment that minimizes mouse usage and maximizes typing efficiency.

# Your Advanced "Super" Configuration

Your Karabiner setup represents a "super" evolution beyond the basic Capslock project. Through analysis of your configuration file, it's clear you've created an incredibly sophisticated multi-layered keyboard enhancement system that combines advanced concepts into a unified, powerful workflow.

## Configuration Architecture Overview

### Profile Structure
- **Main Profile**: "super" (selected and active)
- **Alternative Profiles**: "test", "empty one", "Project Zomboid Inventory"
- **290KB Configuration**: Massive rule set with 12+ major categories

### Core Philosophy
Your setup extends far beyond basic CapsLock functionality with:
- **Multi-key simultaneous patterns** for modifier layers
- **Dual-role home row keys** with timing thresholds
- **Application-specific optimizations** for WebStorm
- **Complex conditional logic** preventing modifier conflicts
- **System-wide integration** with shell commands

## Multi-Key Simultaneous Patterns

Your most innovative feature is the simultaneous key combinations that create custom modifier layers:

### **DF Pattern (D+F Simultaneous)**
```
Threshold: ≥200ms simultaneous press
Activates: right_option + right_command modifier
While held: D+F + H/J/K/L → Enhanced navigation with right_option + right_command
Conditional: Only active when semicolon_modifier is NOT active
```

### **SF Pattern (S+F Simultaneous)**
```
Threshold: ≥200ms simultaneous press  
Activates: control + command modifier
While held: S+F + H/J/K/L → System-level navigation shortcuts
```

### **SD Pattern (S+D Simultaneous)**
```
Threshold: ≥200ms simultaneous press
Activates: control + option modifier
While held: S+D + H/J/K/L → Advanced navigation combinations
```

### **AS Pattern (A+S Simultaneous)**
```
Threshold: ≥200ms simultaneous press
Activates: right_shift + right_control modifier
While held: A+S + H/J/K/L → Selection and control operations
```

### **SDF Pattern (S+D+F Triple)**
```
Threshold: ≥200ms simultaneous press
Activates: control + option + command modifier (Ultimate modifier)
While held: SDF + H/J/K/L → Maximum modifier combinations
```

## Dual-Role Home Row Modifiers

Your home row keys have intelligent dual functionality with precise timing:

```
A: Tap (40ms) = 'a' | Hold = right_shift
S: Tap (50ms) = 's' | Hold = right_control  
D: Tap (40ms) = 'd' | Hold = right_option
F: Tap (50ms) = 'f' | Hold = right_command
```

**Conflict Prevention**: All dual-role keys are disabled when `semicolon_modifier` is active, preventing accidental activation during bracket operations.

## CapsLock Hyper System

Your CapsLock configuration implements the full Hyper key concept:

### **Core Functionality**
- **Tap CapsLock**: Escape (perfect for Vim)
- **Hold CapsLock**: Hyper key (`right_shift + right_command + right_control + right_option`)
- **Hyper + Escape**: Toggle actual CapsLock when needed
- **Hyper + Space**: Language switching
- **Hyper + Cmd + Space**: Emoji picker

### **Navigation Excellence** 
Your Hyper navigation system has multiple modifier layers:

```
Basic Navigation:
Hyper + H/J/K/L → Left/Down/Up/Right arrows

Selection Navigation:  
Hyper + Cmd + H/J/K/L → Shift + Arrow keys (text selection)

Word Navigation:
Hyper + Opt + Cmd + H/L → Option + Shift + Left/Right (word selection)

Application Navigation:
Hyper + Shift + H → Ctrl + Shift + Tab (previous tab)
Hyper + Shift + J/K → Cmd + Tab / Cmd + Shift + Tab (app switching)
Hyper + Shift + L → Ctrl + Tab (next tab)

System Navigation:  
Hyper + Ctrl + H/L → Ctrl + Left/Right (desktop switching)
Hyper + Ctrl + J/K → Ctrl + Up/Down (Mission Control/App Expose)
```

### **Mouse Control Integration**
Complete mouse control from keyboard with multi-speed options:

```
Basic Mouse:
Hyper + Opt + H/J/K/L → Mouse movement (1600 units)

Slow Mouse:
Hyper + Arrow keys → Mouse movement (800 units)

Fast Mouse:  
Hyper + Cmd + Arrow keys → Mouse movement (4200 units)

Mouse Clicks:
Hyper + Enter → Left click
Hyper + Cmd + Enter → Right click  
Hyper + Opt + Enter → Middle click
Hyper + Shift/Ctrl + Enter → Back/Forward buttons

Mouse Wheel:
Hyper + Shift + Arrows → Scroll wheel (64 units)
Hyper + Shift + Cmd + Arrows → Fast scroll (256 units)
Hyper + Shift + Opt + Arrows → Slow scroll (32 units)
```

## Advanced Features

### **Multi-Clipboard System**
Revolutionary 10-clipboard system with shell command integration:

```
Copy to Clip:
Hyper + Cmd + 1-9,0 → Copy selection to ~/.clip1 through ~/.clip0

Paste from Clip:
Hyper + 1-9,0 → Paste from corresponding clipboard file
```

### **Smart Deletion System**
```
Character Level:
Hyper + M → Backspace (delete char behind)
Hyper + , → Forward delete (delete char ahead)

Word Level:  
Hyper + N → Option + Backspace (delete word behind)
Hyper + . → Option + Forward delete (delete word ahead)

Line Level:
Hyper + Cmd/Opt + N → Cmd + Backspace (delete to line start)
Hyper + Opt + . → Delete entire line
```

### **Application Launch System**
Comprehensive application shortcuts:

```
Development:
Hyper + G → WebStorm
Hyper + T → Visual Studio Code  
Hyper + R → iTerm2
Hyper + Opt + R → Terminal

Productivity:
Hyper + E → Safari
Hyper + Cmd + E → Finder
Hyper + F → Alfred 4
Hyper + Cmd + G → Google Chrome
```

### **Terminal Integration**
Direct terminal control shortcuts:

```
Process Control:
Hyper + C → Ctrl+C (interrupt)
Hyper + Z → Ctrl+Z (suspend) 
Hyper + D → Ctrl+D (EOF)
Hyper + V → Ctrl+V (literal next)
Hyper + B → Ctrl+B (backward char)
```

### **WebStorm Optimizations**
Special handling for WebStorm with application-specific conditions:

```
WebStorm-Specific:
Hyper + Cmd + H → Shift + Left (selection - WebStorm only)
Hyper + W → Ctrl + W (close tab - WebStorm only)  
Hyper + Y → Cmd + Backspace (delete line - WebStorm only)
Left Cmd + Right Cmd → Ctrl + ; (Ace Jump - WebStorm only)
```

## Innovation Highlights

### **Conditional Logic System**
Your configuration uses sophisticated variable-based logic:
- **semicolon_modifier variable**: Prevents conflicts between semicolon shortcuts and dual-role keys
- **Simultaneous key variables**: Each pattern (df_modifiers, sf_modifiers, etc.) has its own state
- **Application detection**: Different behaviors for different apps

### **Semicolon Modifier Innovation**
Unique bracket/symbol system using semicolon as a modifier:

```
Semicolon + D → ( (open paren)
Semicolon + F → ) (close paren) 
Semicolon + E → { (open brace)
Semicolon + R → } (close brace)
Semicolon + C → [ (open bracket)
Semicolon + V → ] (close bracket)
```

### **3-Key Digital Keyboard**
Number 3 becomes a function modifier with complete numpad functionality:

```
3 + UIO → 789
3 + JKL → 456  
3 + M,. → 123
3 + Space → 0
3 + Numbers → F1-F12 function keys
```

### **System Integration**
Direct shell command execution for advanced operations:

```
System Control:
Hyper + Shift + W → Sleep system (`pmset sleepnow`)
Hyper + Opt + W → Display sleep (`pmset displaysleepnow`)
Hyper + Ctrl + P → Launch Launchpad (`open -a 'Launchpad'`)

Screenshot System:
Hyper + ~ → Area screenshot to clipboard (Cmd+Shift+Ctrl+4)
Hyper + F13 → Screen capture to file (Cmd+Shift+3)
Hyper + F14 → Screen recording (Cmd+Shift+5)
```

## Configuration Complexity

### **Complete Rule Architecture (12 Major Categories)**

#### **1. Multi-Key Simultaneous Patterns**
```json
"description": "DF option + command" | "SF control + command" | "SD control + options" | "AS shift + control" | "SDF control + option + command"
```
- **Purpose**: Create custom modifier layers through simultaneous key detection
- **Implementation**: Each pattern sets a variable (`df_modifiers`, `sf_modifiers`, etc.) when keys pressed simultaneously
- **Threshold**: 200ms simultaneous press detection across all patterns
- **Conditional Logic**: All patterns check `semicolon_modifier` to prevent conflicts
- **Target Keys**: H/J/K/L receive different modifier combinations based on active pattern

#### **2. Dual-Role Home Row Modifiers** 
```json
"description": "A,S,D,F as right modifiers"
```
- **A Key**: Tap=`a`, Hold(40ms)=`right_shift` 
- **S Key**: Tap=`s`, Hold(50ms)=`right_control`
- **D Key**: Tap=`d`, Hold(40ms)=`right_option`  
- **F Key**: Tap=`f`, Hold(50ms)=`right_command`
- **Conflict Prevention**: All disabled when `semicolon_modifier` active
- **Fine-tuned Timing**: Different thresholds optimized for natural typing patterns

#### **3. CapsLock Hyper System**
```json  
"description": "CapsLock to Hyper"
```
- **Core Binding**: CapsLock → `right_shift + right_command + right_control + right_option` (hold) / `escape` (tap)
- **Reverse Toggle**: Hyper + Escape → Actual CapsLock
- **Language Integration**: Hyper + Space → Language switch (`left_control + space`)
- **Emoji Access**: Hyper + Cmd + Space → Emoji picker (`left_control + left_command + space`)

#### **4. Navigation System (Multi-Layer)**
```json
"description": "Hyper Navigation" 
```
- **Basic Layer**: Hyper + H/J/K/L → Arrow keys
- **Selection Layer**: Hyper + Cmd + H/J/K/L → Shift + Arrow keys  
- **Word Layer**: Hyper + Opt + Cmd + H/L → Option + Shift + Arrow keys
- **Application Layer**: Hyper + Shift + J/K → Cmd + Tab / Cmd + Shift + Tab
- **System Layer**: Hyper + Ctrl + H/L → Ctrl + Left/Right (desktop switching)
- **Extended Navigation**: Hyper + U/I/O/P → Page Up/Home/End/Page Down

#### **5. Smart Deletion System**
```json
"description": "Hyper Deletion"
```
- **Character Level**: Hyper + M/,/.  → Backspace/Forward Delete/Option+Forward Delete
- **Word Level**: Hyper + N → Option + Backspace (word behind)
- **Line Level**: Hyper + Cmd/Opt + N → Cmd + Backspace (to line start)
- **Whole Line**: Hyper + Opt + . → Delete entire line (`Cmd + Backspace`)

#### **6. Mouse Control System**  
```json
"description": "Hyper MouseKey" (Disabled by default)
```
- **Movement Speeds**: 3-tier system (800/1600/3200 units)
- **Directional Control**: Numpad 1-9 for 8-directional movement
- **Click Actions**: Numpad 0/Enter/Period → Left/Right/Middle click
- **Wheel Control**: Multiple speed tiers with directional support
- **Speed Modifiers**: Option (slow), Command (fast), Shift+Command (ultra-fast)

#### **7. Window & Application Management**
```json  
"description": "Hyper Window"
```
- **Application Switching**: Hyper + Tab → Cmd + Tab
- **Tab Navigation**: Hyper + S → Ctrl + Tab, Hyper + Cmd + S → Ctrl + Shift + Tab
- **Window Operations**: Hyper + Q → Cmd + Q (quit app)
- **System Sleep**: Hyper + Shift + W → `pmset sleepnow`
- **WebStorm Integration**: Special close tab behavior for WebStorm (`Ctrl + W`)

#### **8. Application Launch System**
```json
"description": "Hyper Application" 
```
- **Development**: G→WebStorm, T→VSCode, R→iTerm2, F→Alfred 4
- **Productivity**: E→Safari, Cmd+E→Finder, Cmd+G→Chrome
- **System**: Y→Siri, Cmd+Y→Karabiner-Elements
- **Shell Integration**: All using `shell_command` with `open -a` syntax

#### **9. Terminal Control Integration**
```json
"description": "Hyper Terminal"
```  
- **Process Control**: C→Ctrl+C, Z→Ctrl+Z, D→Ctrl+D, V→Ctrl+V, B→Ctrl+B
- **Development Integration**: Cmd+Z→F5 (debug), Cmd+X→Ctrl+F5 (run), Cmd+C→Shift+F5 (stop)
- **Terminal Navigation**: X→Ctrl+R (reverse search)

#### **10. Multi-Clipboard System**
```json
"description": "Hyper Clipboard"
```
- **10-Clipboard Storage**: Numbers 0-9 each with dedicated file (`~/.clip1` through `~/.clip0`)
- **Copy Process**: Hyper + Cmd + Number → Copy to clipboard + save to file
- **Paste Process**: Hyper + Number → Load from file + paste
- **Shell Integration**: Uses `pbpaste > ~/.clipX` and `cat ~/.clipX | pbcopy`

#### **11. Symbol & Punctuation System**
```json
"description": "Hyper Shifter"
```
- **Bracket Access**: Open/Close Bracket → Parentheses/Braces conversion
- **Quick Symbols**: Hyphen→Underscore, Equal→Plus, Quote→Equal sign
- **Comment Toggle**: Backslash/Slash → Cmd + / (universal comment)

#### **12. Function Key & System Control**
```json
"description": "Hyper Functional"
```
- **Function Keys**: F1-F12 with system mappings (brightness, volume, media)
- **Desktop Control**: Cmd + F1-F3 → Ctrl + 1-3 (desktop switching)  
- **Screenshot System**: Tilde→Area screenshot, F13→Screen capture, F14→Screen recording
- **Media Control**: F7-F9 → Rewind/Play/Forward, F10-F12 → Mute/Volume Down/Up

### **Technical Specifications**
- **290KB Configuration**: Massive rule set with 5,489 lines of JSON
- **Precise Timing**: Multiple timing thresholds optimized for different contexts
  - **Dual-role thresholds**: A(40ms), S(50ms), D(40ms), F(50ms) - Fine-tuned for natural typing
  - **Simultaneous detection**: 200ms for all multi-key patterns (DF, SF, SD, AS, SDF)
  - **Global parameters**: 
    - `to_delayed_action_delay_milliseconds`: 300ms
    - `to_if_alone_timeout_milliseconds`: 400ms  
    - `to_if_held_down_threshold_milliseconds`: 150ms
- **Complex Modifiers**: Up to 6 modifier combinations in single shortcuts
  - **Hyper key**: `right_shift + right_command + right_control + right_option`
  - **Maximum stack**: `left_shift + left_command + right_command + right_control + right_shift + right_option`
- **Application Conditions**: Bundle ID detection for app-specific behavior
  - **WebStorm detection**: `com.jetbrains.WebStorm` for IDE-specific optimizations
  - **Conditional execution**: Different behaviors based on frontmost application
- **Variable States**: Multiple conditional variables for conflict prevention
  - **Primary variables**: `semicolon_modifier`, `df_modifiers`, `sf_modifiers`, `sd_modifiers`, `as_modifiers`, `sdf_modifiers`
  - **State management**: Auto-reset on key release with `to_after_key_up` events

## Comparison: Basic Capslock vs Your "Super" Setup

| Feature | Basic Capslock | Your "Super" Setup |
|---------|---------------|-------------------|
| CapsLock Function | Escape/Hyper | ✓ Plus conditional toggle |
| Navigation | Basic HJKL | Multi-layer with 6+ modifier combinations |
| Mouse Control | Basic movement | Complete control with 3-speed system |
| Applications | Simple launching | 20+ optimized shortcuts with app detection |
| Deletion | Basic delete | Smart word/line/character system |
| Clipboards | System clipboard | 10-clipboard system with shell integration |
| Dual-role Keys | Not included | Full home row with conflict prevention |
| Simultaneous Keys | Not included | 5 innovative multi-key patterns |
| System Integration | Limited | Extensive shell command integration |
| Conditional Logic | Basic | Advanced variable-based state management |

## Professional Benefits

### **Development Workflow**
- **Reduced Context Switching**: Everything accessible without leaving home row
- **WebStorm Integration**: Optimized specifically for your primary IDE
- **Terminal Efficiency**: Direct process control without mode switching
- **Multi-clipboard Workflow**: Complex copy/paste operations streamlined

### **System Navigation**
- **Desktop Management**: Seamless virtual desktop switching
- **Application Control**: Instant launching and switching
- **Window Operations**: Complete window management from keyboard
- **Screenshot Workflow**: Integrated capture system

### **Ergonomic Excellence**  
- **Minimal Hand Movement**: Most operations within finger reach
- **Consistent Patterns**: Logical modifier combinations
- **Timing Optimization**: Precisely tuned thresholds for dual-role keys
- **Conflict Prevention**: Intelligent conditional logic prevents accidents

# Advanced Configuration Patterns

## JSON Structure Templates

### Basic Rule Template
```json
{
  "description": "Rule Category Name",
  "manipulators": [
    {
      "description": "Specific action description", 
      "from": {
        "key_code": "source_key",
        "modifiers": {
          "mandatory": ["modifier1", "modifier2"],
          "optional": ["any"]
        }
      },
      "to": [
        {
          "key_code": "target_key",
          "modifiers": ["target_modifier"]
        }
      ],
      "type": "basic"
    }
  ]
}
```

### Simultaneous Key Pattern Template
```json
{
  "description": "When X and Y are pressed simultaneously (≥200ms), set variable",
  "from": {
    "modifiers": { "optional": ["any"] },
    "simultaneous": [
      { "key_code": "key1" },
      { "key_code": "key2" }
    ]
  },
  "parameters": { "basic.simultaneous_threshold_milliseconds": 200 },
  "to": [
    {
      "set_variable": {
        "name": "pattern_modifier",
        "value": 1
      }
    }
  ],
  "to_after_key_up": [
    {
      "set_variable": {
        "name": "pattern_modifier", 
        "value": 0
      }
    }
  ],
  "type": "basic"
}
```

### Dual-Role Key Template
```json
{
  "description": "Dual-role Key: tap for 'letter', hold for modifier",
  "from": {
    "key_code": "letter_key",
    "modifiers": { "optional": ["any"] }
  },
  "parameters": { "basic.to_if_held_down_threshold_milliseconds": 40 },
  "to_if_alone": [{ "key_code": "letter_key" }],
  "to_if_held_down": [{ "key_code": "modifier_key" }],
  "type": "basic"
}
```

### Application-Specific Condition Template
```json
{
  "conditions": [
    {
      "bundle_identifiers": ["com.jetbrains.WebStorm"],
      "type": "frontmost_application_if"
    }
  ],
  "description": "WebStorm-specific behavior",
  "from": {
    "key_code": "source_key",
    "modifiers": { "mandatory": ["hyper_modifiers"] }
  },
  "to": [
    {
      "key_code": "webstorm_specific_key",
      "modifiers": ["webstorm_modifiers"]
    }
  ],
  "type": "basic"
}
```

### Shell Command Integration Template
```json
{
  "description": "Execute shell command",
  "from": {
    "key_code": "trigger_key",
    "modifiers": { "mandatory": ["hyper_modifiers"] }
  },
  "to": [{ 
    "shell_command": "command_to_execute_with_args"
  }],
  "type": "basic"
}
```

## Performance Optimization Strategies

### Memory Management
- **Rule Grouping**: Organize related rules into logical sections
- **Unused Rule Removal**: Comment out or remove rules not actively used
- **Variable Cleanup**: Ensure proper variable state management with `to_after_key_up`
- **Condition Optimization**: Use specific bundle identifiers rather than broad conditions

### Timing Optimization
```json
"parameters": {
  "basic.to_delayed_action_delay_milliseconds": 300,
  "basic.to_if_alone_timeout_milliseconds": 400,
  "basic.to_if_held_down_threshold_milliseconds": 150,
  "basic.simultaneous_threshold_milliseconds": 200
}
```
- **Dual-role timing**: Balance between false triggers and responsiveness
- **Simultaneous detection**: 200ms optimal for intentional multi-key presses
- **Global parameters**: Set once per profile for consistency

### Conflict Resolution Patterns

#### Variable-Based Prevention
```json
"conditions": [
  {
    "name": "conflicting_modifier",
    "type": "variable_if", 
    "value": 0
  }
]
```

#### Application-Specific Overrides
```json
"conditions": [
  {
    "bundle_identifiers": ["com.jetbrains.WebStorm"],
    "type": "frontmost_application_unless"
  }
]
```

#### Modifier Stack Priority
```json
"modifiers": {
  "mandatory": ["right_command", "right_control", "right_shift", "right_option"],
  "optional": ["left_shift", "left_command", "left_control", "left_option"]
}
```

## Extension Patterns

### Adding New Simultaneous Patterns
1. **Choose Key Combination**: Select unused adjacent keys (e.g., JK, DF, etc.)
2. **Define Variable**: Create unique variable name (e.g., `jk_modifiers`)
3. **Set Threshold**: Use 200ms for consistency
4. **Add Conditional Logic**: Prevent conflicts with existing patterns
5. **Define Target Actions**: Map to H/J/K/L or other target keys

### Expanding Application Support
1. **Find Bundle ID**: Use `osascript -e 'id of app "AppName"'`
2. **Test Conditions**: Verify frontmost application detection
3. **Create Specific Rules**: Define app-specific behaviors
4. **Document Integration**: Add to configuration documentation

### Custom Modifier Creation
1. **Define Modifier Stack**: Choose unique modifier combination
2. **Map to Physical Keys**: Assign to available key combinations
3. **Create Action Set**: Define consistent set of actions for new modifier
4. **Test Conflicts**: Verify no interference with existing shortcuts

## Troubleshooting & Optimization Guide

### Performance Issues
```bash
# Monitor Karabiner CPU usage
top -pid $(pgrep karabiner)

# Check memory usage
ps aux | grep karabiner | awk '{print $4, $6}'

# Restart Karabiner services
sudo launchctl stop com.pqrs.karabiner.karabiner_console_user_server
sudo launchctl start com.pqrs.karabiner.karabiner_console_user_server
```

### Configuration Debugging
```bash
# Check configuration syntax
jq . ~/.config/karabiner/karabiner.json

# Backup before changes
cp ~/.config/karabiner/karabiner.json ~/.config/karabiner/karabiner.json.backup

# Monitor live events
tail -f ~/.config/karabiner/log/console_user_server.log
```

### Common Conflict Resolution

#### Dual-Role Key False Triggers
```json
"parameters": { 
  "basic.to_if_held_down_threshold_milliseconds": 60
}
```
- Increase threshold for keys with frequent false triggers
- Different thresholds for different keys based on typing patterns

#### Simultaneous Key Misfires
```json
"parameters": {
  "basic.simultaneous_threshold_milliseconds": 250
}
```
- Increase threshold if accidental activations occur
- Decrease if pattern feels unresponsive

#### Application Detection Failures
```json
"conditions": [
  {
    "bundle_identifiers": [
      "com.jetbrains.WebStorm",
      "com.jetbrains.IntelliJ-IDEA"
    ],
    "type": "frontmost_application_if"
  }
]
```
- Add multiple bundle identifiers for related applications
- Use `frontmost_application_unless` for exclusions

### Advanced Troubleshooting
```bash
# Clear Karabiner cache
rm -rf ~/.config/karabiner/automatic_backups/*
killall karabiner_observer

# Reset to defaults (backup first!)
rm ~/.config/karabiner/karabiner.json
# Karabiner will recreate with defaults

# Check system permissions
spctl --status
# Ensure Karabiner has accessibility permissions
```

## Extension Framework for Future Enhancements

### Modular Rule Architecture
- **Core Rules**: Essential Hyper key and dual-role functionality
- **Navigation Module**: All movement and selection rules  
- **Application Module**: App-specific optimizations
- **System Module**: OS integration and shell commands
- **Development Module**: IDE and programming-specific rules

### Configuration Management
```bash
# Profile-specific configurations
~/.config/karabiner/profiles/
├── super.json           # Main configuration
├── development.json     # IDE-focused setup
├── gaming.json         # Gaming optimizations  
└── minimal.json        # Essential shortcuts only

# Automated switching
osascript -e 'tell application "Karabiner-Elements" to select profile "development"'
```

### Integration Points for WebStorm & IdeaVim
- **Reserved Key Ranges**: Documented keys available for IDE integration
- **Modifier Namespaces**: Separate modifier combinations for different tool layers
- **Conflict Avoidance**: Systematic approach to prevent shortcut conflicts
- **Context Switching**: Dynamic behavior based on active IDE and Vim mode

## Resources

- **Official Repository**: [github.com/Vonng/Capslock](https://github.com/Vonng/Capslock)
- **Karabiner-Elements**: [karabiner-elements.pqrs.org](https://karabiner-elements.pqrs.org/)
- **Configuration Examples**: Available in the repository's documentation
- **Community Configurations**: Shared configurations for different workflows