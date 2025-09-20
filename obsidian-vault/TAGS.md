# Keyboard Productivity Tagging System

This document defines the standardized tagging hierarchy for maintaining consistency across all Obsidian notes in this keyboard productivity vault.

## Tag Categories

### Keyboard Tools
- `#keyboard/karabiner` - Karabiner Elements configurations and modifications
- `#keyboard/ideavim` - IdeaVim settings and mappings
- `#keyboard/webstorm` - WebStorm keymap configurations
- `#keyboard/homerow` - Homerow navigation tool setup
- `#keyboard/defaultkeybinding` - macOS DefaultKeyBinding.dict configurations
- `#keyboard/obsidian` - Obsidian-specific keyboard shortcuts and workflows

### Binding Types
- `#binding/hjkl` - HJKL navigation mappings
- `#binding/hyper` - Hyper key combinations (⌘⌥⌃⇧)
- `#binding/modifier` - Modifier key combinations (⇧⌃⌥⌘)
- `#binding/dual-role` - Dual-role key configurations
- `#binding/leader` - Leader key sequences
- `#binding/chord` - Chord combinations
- `#binding/long-press` - Long press variations
- `#binding/double-tap` - Double tap sequences

### Workflow Categories
- `#workflow/navigation` - Movement and cursor positioning
- `#workflow/editing` - Text editing and manipulation
- `#workflow/selection` - Text selection patterns
- `#workflow/window-management` - Window and pane control
- `#workflow/application-switching` - App navigation
- `#workflow/desktop-management` - Virtual desktop control
- `#workflow/mouse-replacement` - Mouse-free operations

### Learning & Progress
- `#learning/discovery` - New binding discoveries
- `#learning/practice` - Practice sessions and logs
- `#learning/muscle-memory` - Muscle memory development
- `#learning/optimization` - Workflow optimization insights
- `#learning/troubleshooting` - Problem solving and debugging

### Configuration Status
- `#status/implemented` - Successfully configured bindings
- `#status/planned` - Future binding implementations
- `#status/testing` - Currently testing configurations
- `#status/deprecated` - Obsolete or replaced bindings
- `#status/conflicted` - Binding conflicts requiring resolution

### Documentation Types
- `#docs/reference` - Reference documentation
- `#docs/tutorial` - Step-by-step guides
- `#docs/example` - Usage examples
- `#docs/troubleshooting` - Problem resolution guides
- `#docs/philosophy` - Design principles and concepts

### System Layers
- `#layer/macos-text` - Layer -1: macOS Text System
- `#layer/system-ui` - Layer 0: Full Keyboard Access
- `#layer/hardware` - Layer 1: Karabiner Elements
- `#layer/application` - Layer 2: Application configs
- `#layer/editor` - Layer 3: Editor configurations

### ActionID Integration
- `#actionid/verified` - Verified IntelliJ ActionIDs
- `#actionid/navigation` - Navigation-specific ActionIDs
- `#actionid/editing` - Text editing ActionIDs
- `#actionid/refactoring` - Code refactoring ActionIDs
- `#actionid/debugging` - Debugging-related ActionIDs

## Tagging Guidelines

### Multi-tagging Rules
- Always use the most specific tag available
- Combine multiple categories when relevant (e.g., `#keyboard/karabiner #binding/hjkl #workflow/navigation`)
- Include status tags for tracking implementation progress
- Add learning tags for personal development tracking

### Naming Conventions
- Use lowercase for all tags
- Separate words with hyphens (kebab-case)
- Keep tag names concise but descriptive
- Maintain consistency with existing tag structure

### Tag Evolution
- Add new tags to this document when needed
- Deprecate unused tags by moving to archive section
- Update existing notes when tag structure changes
- Maintain backward compatibility when possible

## Common Tag Combinations

### For New Binding Documentation
```
#keyboard/[tool] #binding/[type] #workflow/[category] #status/[current-status]
```

### For Learning Progress
```
#learning/[type] #workflow/[category] #keyboard/[tool]
```

### For Conflict Resolution
```
#status/conflicted #keyboard/[tool1] #keyboard/[tool2] #learning/troubleshooting
```

### For ActionID Integration
```
#actionid/[type] #keyboard/webstorm #workflow/[category]
```

## Archive (Deprecated Tags)

*No deprecated tags yet*

---

*This tagging system should be referenced in CLAUDE.md and maintained as the single source of truth for all tag usage in this vault.*