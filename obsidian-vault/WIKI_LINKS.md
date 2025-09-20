# WikiLinks System for Keyboard Productivity Vault

This document establishes linking conventions for creating a connected knowledge base around keyboard productivity configurations and learning.

## Link Types and Conventions

### Configuration Cross-References
Link between different configuration files and their documentation:

- `[[KARABINER-CONFIG]]` - Main Karabiner Elements configuration
- `[[IDEAVIM-CONFIG]]` - IdeaVim configuration and mappings
- `[[WEBSTORM-KEYMAP]]` - WebStorm keymap configurations
- `[[DEFAULT-KEY-BINDING-CONFIG]]` - macOS text system bindings
- `[[HOMEROW-CONFIG]]` - Homerow navigation setup

### Key Binding Documentation
- `[[HJKL-NAVIGATION]]` - Core HJKL movement patterns
- `[[HYPER-KEY-MAPPINGS]]` - Hyper key combinations
- `[[MODIFIER-COMBINATIONS]]` - Standard modifier patterns
- `[[DUAL-ROLE-KEYS]]` - Dual-role key configurations
- `[[LEADER-SEQUENCES]]` - Leader key workflows

### Layer System Links
- `[[MACOS-TEXT-LAYER]]` - Layer -1: Text system bindings
- `[[SYSTEM-UI-LAYER]]` - Layer 0: Full Keyboard Access
- `[[HARDWARE-LAYER]]` - Layer 1: Karabiner modifications
- `[[APPLICATION-LAYER]]` - Layer 2: App-specific configs
- `[[EDITOR-LAYER]]` - Layer 3: Editor bindings

### Workflow Categories
- `[[NAVIGATION-WORKFLOWS]]` - Movement and positioning
- `[[EDITING-WORKFLOWS]]` - Text manipulation patterns
- `[[WINDOW-MANAGEMENT]]` - Window and pane control
- `[[APPLICATION-SWITCHING]]` - App navigation patterns
- `[[DESKTOP-MANAGEMENT]]` - Virtual desktop control

### Learning and Progress
- `[[BINDING-DISCOVERIES]]` - New binding findings
- `[[PRACTICE-SESSIONS]]` - Practice logs and progress
- `[[MUSCLE-MEMORY-DEVELOPMENT]]` - Skill building notes
- `[[CONFLICT-RESOLUTIONS]]` - Binding conflict solutions
- `[[OPTIMIZATION-INSIGHTS]]` - Workflow improvements

### Technical References
- `[[ACTIONID-REFERENCE]]` - IntelliJ ActionID mappings
- `[[YAML-CONFIGURATION]]` - YAML config system
- `[[HOOK-AUTOMATION]]` - Claude Code hooks
- `[[CONFLICT-DETECTION]]` - Binding conflict analysis

## Linking Patterns

### For New Binding Notes
When documenting a new binding, link to:
1. The configuration file where it's implemented
2. Related bindings in the same category
3. The workflow it supports
4. Any conflicts it resolves

Example:
```markdown
This [[HJKL-NAVIGATION]] binding is implemented in [[KARABINER-CONFIG]]
and works with [[IDEAVIM-CONFIG]] to provide consistent [[NAVIGATION-WORKFLOWS]]
across all [[LAYER-SYSTEM]] levels.
```

### For Configuration Changes
When updating configurations, link to:
1. Previous version or conflict
2. Related documentation
3. Testing notes
4. Implementation guide

### For Learning Progress
When tracking progress, link to:
1. Specific bindings being practiced
2. Related workflow improvements
3. Muscle memory development notes
4. Optimization discoveries

## Alias Conventions

Use aliases for frequently referenced concepts:

- Configuration files: `config`, `setup`, `mapping`
- Workflows: `flow`, `pattern`, `sequence`
- Learning: `practice`, `progress`, `development`
- Technical: `ref`, `guide`, `doc`

Example:
```markdown
[[KARABINER-CONFIG|main config]] - Links to KARABINER-CONFIG with alias "main config"
[[HJKL-NAVIGATION|HJKL]] - Links to HJKL-NAVIGATION with alias "HJKL"
```

## Embedding Guidelines

Use embeds for:
- Code snippets from configuration files
- Key sections of reference documents
- Examples from other notes

Examples:
```markdown
![[KARABINER-CONFIG#HJKL Section]] - Embeds specific section
![[BINDING_TEMPLATE]] - Embeds entire template
```

## Backlink Strategy

Maintain strong backlink networks by:
1. Linking bidirectionally between related concepts
2. Creating hub notes for major topics
3. Using consistent link naming
4. Regular backlink review and cleanup

## Link Maintenance

### Weekly Review
- Check for broken links
- Identify missing connections
- Update aliases for clarity
- Consolidate duplicate links

### Monthly Audit
- Review link structure effectiveness
- Identify knowledge gaps
- Plan new connection patterns
- Archive obsolete links

## Hub Notes (Central Connection Points)

Create hub notes for major topics:
- `[[KEYBOARD-PRODUCTIVITY-HUB]]` - Central overview
- `[[CONFIGURATION-HUB]]` - All config links
- `[[WORKFLOW-HUB]]` - All workflow patterns
- `[[LEARNING-HUB]]` - Progress tracking
- `[[TECHNICAL-HUB]]` - Reference materials

## Example Link Structures

### For a New Binding Discovery
```markdown
# New Binding: Hyper+H Window Left

Discovered in [[PRACTICE-SESSIONS/2024-01-15]] while working on [[WINDOW-MANAGEMENT]].

Implementation:
- [[KARABINER-CONFIG#Window Navigation]]
- [[WEBSTORM-KEYMAP#Window Actions]]

Related:
- [[HYPER-KEY-MAPPINGS]]
- [[NAVIGATION-WORKFLOWS]]
- [[APPLICATION-LAYER]]

Conflicts:
- Resolved [[CONFLICT-RESOLUTIONS/HyperH-IdeaVim]]

Tags: #binding/hyper #workflow/window-management #status/implemented
```

### For Configuration Documentation
```markdown
# Karabiner Elements Configuration

Main config: [[src/karabiner/karabiner.json]]

Key sections:
- [[HJKL-NAVIGATION]] implementation
- [[DUAL-ROLE-KEYS]] setup
- [[HYPER-KEY-MAPPINGS]] definitions

Integration with:
- [[IDEAVIM-CONFIG]]
- [[WEBSTORM-KEYMAP]]
- [[DEFAULT-KEY-BINDING-CONFIG]]

See also: [[CONFIGURATION-HUB]]
```

---

*This linking system creates a web of knowledge that makes configuration relationships and learning progress easily discoverable and maintainable.*