# Conflict Resolution: [Conflict Name]

---
created: {{date:YYYY-MM-DD}}
modified: {{date:YYYY-MM-DD}}
tags: [#status/conflicted, #learning/troubleshooting, #keyboard/, #binding/]
aliases: []
---

## Conflict Overview

**Conflicting Systems:**
- System 1: [e.g., Karabiner Elements]
- System 2: [e.g., IdeaVim]

**Key Combination:** [e.g., ⌘+H]
**Discovery Date:** [Date when conflict was found]
**Resolution Date:** [Date when resolved]

## Conflict Details

### System 1 Behavior
**Tool:** [Karabiner/IdeaVim/WebStorm/etc.]
**Expected Action:** [What should happen]
**Actual Behavior:** [What actually happens]
**Configuration Location:** `[file path]`

### System 2 Behavior
**Tool:** [Tool name]
**Expected Action:** [What should happen]
**Actual Behavior:** [What actually happens]
**Configuration Location:** `[file path]`

### Impact Assessment
**Severity:** [Low/Medium/High]
**Frequency:** [How often encountered]
**Workflow Disruption:** [Description of impact]

## Investigation Process

### Steps Taken
1. [Investigation step 1]
2. [Investigation step 2]
3. [Investigation step 3]

### Tools Used
- [ ] Karabiner Elements Event Viewer
- [ ] System keyboard preferences
- [ ] Application-specific settings
- [ ] Terminal/CLI tools
- [ ] [[ConflictDetection]] scripts

### Findings
[What was discovered during investigation]

## Resolution Strategy

### Chosen Approach
[Description of resolution method]

**Priority System:** [Which system takes precedence and why]

### Implementation Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Configuration Changes

#### Karabiner Elements
```json
[Configuration snippet if applicable]
```
**File:** `src/karabiner/karabiner.json`
**Section:** [Specific section modified]

#### IdeaVim
```vim
[Configuration snippet if applicable]
```
**File:** `src/idea-vim/.ideavimrc`
**Line:** [Line numbers]

#### WebStorm Keymap
**ActionID:** `[ActionID if applicable]`
**Key:** `[Key combination]`
**File:** `src/webstorm-keymap/macOS copy.xml`

#### Default Key Binding
```
[Configuration snippet if applicable]
```
**File:** `src/macOs/DefaultKeyBinding.dict`

### YAML Documentation Update
**File:** `keyboard-config/data/[relevant-file].yaml`
**Changes:** [What was updated in YAML]

## Testing and Validation

### Test Cases
- [ ] Original System 1 workflow works
- [ ] Original System 2 workflow works
- [ ] No new conflicts introduced
- [ ] Consistent behavior across applications

### Validation Results
[Results of testing the resolution]

## Alternative Solutions Considered

### Option 1: [Alternative approach]
**Pros:** [Benefits]
**Cons:** [Drawbacks]
**Why not chosen:** [Reason]

### Option 2: [Alternative approach]
**Pros:** [Benefits]
**Cons:** [Drawbacks]
**Why not chosen:** [Reason]

## Related Conflicts

### Similar Issues
- [[ConflictResolution/SimilarConflict1]]
- [[ConflictResolution/SimilarConflict2]]

### Prevention Strategy
[How to avoid similar conflicts in the future]

## Learning Outcomes

### Key Insights
- [Insight 1]
- [Insight 2]
- [Insight 3]

### Process Improvements
[How this experience improves future conflict resolution]

### Documentation Updates
- [ ] Updated [[TAGS.md]] if needed
- [ ] Updated [[WikiLinks.md]] patterns
- [ ] Updated conflict detection scripts
- [ ] Updated prevention guidelines

## Links and References

### Related Bindings
- [[BindingName1]] - Affected by this conflict
- [[BindingName2]] - Related binding

### Configuration Files
- [[KarabinerConfig]]
- [[IdeaVimConfig]]
- [[WebStormKeymap]]
- [[DefaultKeyBindingConfig]]

### Documentation
- [[ConflictDetection]] - Prevention and detection
- [[TroubleshootingHub]] - General troubleshooting

## Notes

[Additional observations, edge cases, or future considerations]

---

**Status:** [Resolved/Ongoing/Deferred]
**Last Updated:** {{date:YYYY-MM-DD}}
**Confidence Level:** [How confident in the resolution]