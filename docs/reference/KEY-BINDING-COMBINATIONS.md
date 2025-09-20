# KEY-BINDING-COMBINATIONS

Complete reference guide for all possible key binding combinations for a single physical key in keyboard productivity systems.

## Overview

This document catalogs every possible way to bind functionality to a single key, from simple modifier combinations to complex multi-key sequences. The total number of unique combinations exceeds 57+ patterns per key.

## Standard Modifier Combinations (16)

Basic modifier key combinations using standard macOS modifiers:

| #  | Combination                     | Symbol | Example | Description         |
|----|---------------------------------|--------|---------|---------------------|
| 1  | Key                             | -      | `H`     | No modifier         |
| 2  | Shift + Key                     | ⇧      | `⇧H`    | Shift modifier      |
| 3  | Control + Key                   | ⌃      | `⌃H`    | Control modifier    |
| 4  | Alt + Key                       | ⌥      | `⌥H`    | Alt/Option modifier |
| 5  | Command + Key                   | ⌘      | `⌘H`    | Command modifier    |
| 6  | Shift + Control + Key           | ⇧⌃     | `⇧⌃H`   | Shift + Control     |
| 7  | Shift + Alt + Key               | ⇧⌥     | `⇧⌥H`   | Shift + Alt         |
| 8  | Shift + Command + Key           | ⇧⌘     | `⇧⌘H`   | Shift + Command     |
| 9  | Control + Alt + Key             | ⌃⌥     | `⌃⌥H`   | Control + Alt       |
| 10 | Control + Command + Key         | ⌃⌘     | `⌃⌘H`   | Control + Command   |
| 11 | Alt + Command + Key             | ⌥⌘     | `⌥⌘H`   | Alt + Command       |
| 12 | Shift + Control + Alt + Key     | ⇧⌃⌥    | `⇧⌃⌥H`  | Triple modifier     |
| 13 | Shift + Control + Command + Key | ⇧⌃⌘    | `⇧⌃⌘H`  | Triple modifier     |
| 14 | Shift + Alt + Command + Key     | ⇧⌥⌘    | `⇧⌥⌘H`  | Triple modifier     |
| 15 | Control + Alt + Command + Key   | ⌃⌥⌘    | `⌃⌥⌘H`  | Triple modifier     |
| 16 | All Modifiers + Key             | ⇧⌃⌥⌘   | `⇧⌃⌥⌘H` | Quad modifier       |

## Hyper Key Combinations (5)

Special "Hyper" key combinations using right-side modifiers as a unified layer:

| #  | Combination           | Symbol | Example | Description          |
|----|-----------------------|--------|---------|----------------------|
| 17 | Hyper + Key           | ✱      | `✱H`    | Right ⇧⌃⌥⌘ + Key     |
| 18 | Hyper + Shift + Key   | ✱⇧     | `✱⇧H`   | Hyper + left Shift   |
| 19 | Hyper + Control + Key | ✱⌃     | `✱⌃H`   | Hyper + left Control |
| 20 | Hyper + Alt + Key     | ✱⌥     | `✱⌥H`   | Hyper + left Alt     |
| 21 | Hyper + Command + Key | ✱⌘     | `✱⌘H`   | Hyper + left Command |

## Leader Key Combinations (18+)

Vim-style leader key sequences where a prefix key is pressed followed by the target key:

### Custom Leaders
| #  | Pattern             | Example             | Description          |
|----|---------------------|---------------------|----------------------|
| 22 | Leader + Key        | `<Leader>h`         | Space/Comma + h      |
| 23 | Leader + ⇧ + Key    | `<Leader>H`         | Leader + Shift + h   |
| 24 | Leader + ⌃ + Key    | `<Leader><C-h>`     | Leader + Control + h |
| 25 | Leader + ⌥ + Key    | `<Leader><A-h>`     | Leader + Alt + h     |
| 26 | Leader + ⌘ + Key    | `<Leader><D-h>`     | Leader + Command + h |
| 27 | Double Leader + Key | `<Leader><Leader>h` | Leader twice + h     |

### Vim Standard Prefixes
| #  | Pattern | Example | Description          |
|----|---------|---------|----------------------|
| 28 | g + Key | `gh`    | Go-to commands       |
| 29 | z + Key | `zh`    | Fold/scroll commands |
| 30 | [ + Key | `[h`    | Previous navigation  |
| 31 | ] + Key | `]h`    | Next navigation      |
| 32 | c + Key | `ch`    | Change commands      |
| 33 | d + Key | `dh`    | Delete commands      |
| 34 | y + Key | `yh`    | Yank commands        |
| 35 | v + Key | `vh`    | Visual commands      |
| 36 | m + Key | `mh`    | Mark commands        |
| 37 | ' + Key | `'h`    | Jump to mark         |
| 38 | " + Key | `"h`    | Register prefix      |
| 39 | \ + Key | `\h`    | Custom leader        |

## Double Tap Combinations (5)

Sequences activated by pressing the same key twice within a timeout window:

| #  | Pattern     | Example | Description          |
|----|-------------|---------|----------------------|
| 40 | Key Key     | `hh`    | Double tap           |
| 41 | ⇧ + Key Key | `⇧hh`   | Shift + double tap   |
| 42 | ⌃ + Key Key | `⌃hh`   | Control + double tap |
| 43 | ⌥ + Key Key | `⌥hh`   | Alt + double tap     |
| 44 | ⌘ + Key Key | `⌘hh`   | Command + double tap |

## Multi-Key Sequences (8+)

Vim-style operator + text object combinations:

### Text Objects
| #  | Pattern  | Example | Description   |
|----|----------|---------|---------------|
| 45 | ci + Key | `cih`   | Change inner  |
| 46 | di + Key | `dih`   | Delete inner  |
| 47 | yi + Key | `yih`   | Yank inner    |
| 48 | ca + Key | `cah`   | Change around |
| 49 | da + Key | `dah`   | Delete around |
| 50 | ya + Key | `yah`   | Yank around   |
| 51 | vi + Key | `vih`   | Visual inner  |
| 52 | va + Key | `vah`   | Visual around |

## Long Press Variations (2)

Time-based activation patterns:

| #  | Pattern        | Example       | Description                       |
|----|----------------|---------------|-----------------------------------|
| 53 | Key (hold)     | `h(hold)`     | Long press activation             |
| 54 | Key (tap-hold) | `h(tap/hold)` | Different actions for tap vs hold |

## Chord Combinations (3+)

Simultaneous multi-key or multi-device combinations:

| #  | Pattern      | Example    | Description               |
|----|--------------|------------|---------------------------|
| 55 | Key1 + Key2  | `h+j`      | Two keys pressed together |
| 56 | Key + Mouse  | `h+click`  | Key with mouse button     |
| 57 | Key + Scroll | `h+scroll` | Key with scroll wheel     |

## Implementation Notes

### Karabiner Elements
- Handles system-wide modifier combinations
- Supports complex modifications and dual-role keys
- Implements hyper key functionality
- Can detect key sequences and timing

### IdeaVim
- Implements Vim-style leader and operator combinations
- Supports custom key mappings with prefixes
- Handles text objects and motion combinations
- Modal editing context affects key behavior

### WebStorm Keymap
- Standard IDE modifier combinations
- Custom action assignments
- Context-sensitive bindings
- Multi-keystroke sequences

### YAML Configuration System
- Single source of truth for all bindings
- Schema validation prevents conflicts
- Structured data enables automated analysis
- Generation scripts create documentation

## Conflict Detection

With 57+ possible combinations per key, conflict detection becomes critical:

1. **Cross-system conflicts**: Same combination in different systems
2. **Modal conflicts**: Different behavior in different modes
3. **Context conflicts**: Application-specific overlaps
4. **Timing conflicts**: Double-tap vs hold conflicts

## Statistics

Based on current implementation:
- **Total theoretical combinations per key**: 57+
- **Currently implemented**: ~28 combinations per HJKL key
- **Available for assignment**: ~29+ combinations per key
- **Total keys in navigation set**: 4 (H, J, K, L)
- **Maximum possible bindings**: 228+ unique combinations

## Extension Possibilities

Additional combination types not yet catalogued:

### Triple Tap Patterns
- `hhh` - Triple tap
- `⇧hhh` - Shift + triple tap

### Sequence Chains
- `Key1 → Key2 → Key3` - Multi-step sequences
- `h → j → k` - Navigation chains

### Context-Aware Bindings
- Application-specific overrides
- Mode-dependent behavior
- File-type sensitive mappings

### Sticky Key Combinations
- Lock modifiers for subsequent keys
- Sequential modifier application

### Dead Key Sequences
- Compose key functionality
- International character input
- Symbol generation sequences

## Best Practices

1. **Consistency**: Maintain logical patterns across similar keys
2. **Ergonomics**: Prioritize comfortable combinations for frequent actions
3. **Memorability**: Use mnemonic patterns when possible
4. **Conflict Avoidance**: Always check for existing bindings
5. **Documentation**: Keep binding references up to date
6. **Testing**: Verify combinations work across all target systems

## References

- `keyboard-config/data/horizontal-navigation.yaml` - H/L key implementations
- `keyboard-config/data/vertical-navigation.yaml` - J/K key implementations
- `src/karabiner/karabiner.json` - System-wide configuration
- `src/idea-vim/.ideavimrc` - Vim emulation bindings
- `src/webstorm-keymap/macOS copy.xml` - IDE keymap configuration

---

*Last updated: 2025-09-06*
*Total documented combinations: 57+*
