# Vault Organization System

This document defines the organizational structure and rules for maintaining a clean, discoverable knowledge base within this keyboard productivity Obsidian vault.

## Folder Structure

### `/notes/` - Daily Logs and General Observations
**Purpose:** Personal logs, daily practice sessions, and informal observations

**Naming Convention:**
- Daily logs: `DailyLog-YYYY-MM-DD.md`
- Weekly summaries: `WeeklyReview-YYYY-WW.md`
- Monthly progress: `MonthlyProgress-YYYY-MM.md`
- General notes: `CamelCaseDescriptiveName.md`

**Content Types:**
- Practice session logs
- Binding discovery notes
- Workflow improvement observations
- Personal insights and reflections

### `/research/` - Keyboard Research and Experiments
**Purpose:** Formal research into keyboard tools, techniques, and optimizations

**Naming Convention:**
- Research topics: `Research-TopicName.md`
- Tool evaluations: `ToolEvaluation-ToolName.md`
- Experiments: `Experiment-ExperimentName.md`
- Comparisons: `Comparison-ToolA-vs-ToolB.md`

**Content Types:**
- Tool research and evaluations
- Binding possibility explorations
- Performance optimization studies
- Integration investigations

### `/templates/` - Reusable Note Structures
**Purpose:** Templates for consistent note creation

**Existing Templates:**
- `BINDING_TEMPLATE.md` - For documenting new bindings
- `CONFLICT_RESOLUTION.md` - For resolving binding conflicts
- `DAILY_LOG.md` - For daily practice logs
- `RESEARCH_NOTE.md` - For formal research

**Guidelines:**
- Keep templates general and reusable
- Use placeholder text with clear instructions
- Include all relevant frontmatter fields
- Maintain consistent structure across similar templates

### `/archive/` - Old Configurations and Deprecated Content
**Purpose:** Historical configurations and obsolete content

**Naming Convention:**
- Archived configs: `Archived-ConfigName-YYYY-MM-DD.md`
- Deprecated bindings: `Deprecated-BindingName-YYYY-MM-DD.md`
- Old research: `Archive-ResearchTopic-YYYY-MM-DD.md`

**Guidelines:**
- Move obsolete content here instead of deleting
- Include reason for archiving in frontmatter
- Maintain links from current content to archived versions
- Review quarterly for permanent deletion

## File Naming Conventions

### General Rules
- Use CamelCase for all markdown files
- No spaces in file names
- Include dates in format YYYY-MM-DD when relevant
- Keep names descriptive but concise
- Use hyphens for compound concepts (e.g., `ConflictResolution`)

### Specific Patterns

#### Configuration Documentation
- `KarabinerConfig.md` - Main config documentation
- `IdeaVimConfig.md` - IdeaVim setup notes
- `WebStormKeymap.md` - WebStorm configuration
- `DefaultKeyBindingConfig.md` - macOS text system config

#### Binding Documentation
- `HJKLNavigation.md` - Core navigation bindings
- `HyperKeyMappings.md` - Hyper key combinations
- `ModifierCombinations.md` - Standard modifier patterns
- `[SpecificBinding]Binding.md` - Individual binding docs

#### Workflow Documentation
- `NavigationWorkflows.md` - Movement patterns
- `EditingWorkflows.md` - Text manipulation
- `WindowManagement.md` - Window/pane control
- `ApplicationSwitching.md` - App navigation

## Frontmatter Standards

### Required Fields
```yaml
---
created: YYYY-MM-DD
modified: YYYY-MM-DD
tags: [#category/subcategory, #status/current]
aliases: []
---
```

### Optional Fields
```yaml
---
author: [for shared content]
version: [for versioned content]
related: [related file references]
status: [implementation status]
priority: [High/Medium/Low]
reviewed: [last review date]
---
```

### Tag Guidelines
- Reference [[TAGS.md]] for official tag hierarchy
- Use 2-4 tags per note maximum
- Include at least one status tag
- Include category and workflow tags when relevant

## Linking Strategy

### Hub Notes
Create central hub notes for major topics:
- `KeyboardProductivityHub.md` - Central overview
- `ConfigurationHub.md` - All configuration links
- `WorkflowHub.md` - All workflow patterns
- `LearningHub.md` - Progress tracking hub
- `TechnicalHub.md` - Reference materials hub

### Link Naming Consistency
- Use full file names without extensions: `[[FileName]]`
- Use aliases for readability: `[[LongFileName|Short Name]]`
- Reference sections: `[[FileName#Section Name]]`
- Embed content: `![[FileName]]` or `![[FileName#Section]]`

### Bidirectional Linking
- Create links in both directions for related concepts
- Use backlinks panel to identify missing connections
- Regular review of backlink graphs for optimization

## Content Organization Rules

### Note Length Guidelines
- Daily logs: Flexible length based on activity
- Binding documentation: Comprehensive but focused
- Research notes: As detailed as needed for completeness
- Configuration docs: Complete but well-structured

### Section Structure
Use consistent heading hierarchy:
```markdown
# Main Title
## Major Sections
### Subsections
#### Details
```

### Code and Configuration Snippets
- Use appropriate language tags for syntax highlighting
- Include file paths and line numbers when relevant
- Link to source files in the repository
- Explain context and purpose of code blocks

## Maintenance Procedures

### Daily Maintenance
- Create daily log if practicing bindings
- Update modified dates in frontmatter
- Check for broken links in edited notes

### Weekly Maintenance
- Review and organize new notes
- Update hub notes with new links
- Check tag consistency
- Archive completed research

### Monthly Maintenance
- Review folder organization
- Clean up duplicate or redundant content
- Update templates based on usage patterns
- Audit tag usage and consolidate if needed

### Quarterly Maintenance
- Major reorganization if needed
- Archive old daily logs
- Review and update organizational rules
- Prune unnecessary archived content

## Search and Discovery

### Search Strategies
- Use tags for categorical searches
- Use Obsidian search for content across notes
- Leverage graph view for relationship discovery
- Use backlinks for reverse discovery

### Discovery Aids
- Maintain index notes for major topics
- Use consistent naming for easy browsing
- Create topic-based note collections
- Regular review of unlinked mentions

## Integration with Repository

### Sync with Configuration Files
- Link documentation to actual config files
- Reference specific file paths and line numbers
- Update docs when configurations change
- Maintain version correlation

### YAML Integration
- Link to YAML sources: `keyboard-config/data/`
- Reference ActionIDs and technical details
- Connect planning docs with implementation
- Track status through both systems

### Hook Integration
- Document hook behavior and triggers
- Link to automation results
- Track generated content
- Maintain automation logs

## Version Control Considerations

### Git Integration
- Include vault in version control
- Exclude temporary Obsidian files
- Track documentation changes with configs
- Use meaningful commit messages for note changes

### Backup Strategy
- Regular git commits
- Export important notes periodically
- Maintain links to external backups
- Document recovery procedures

---

*This organization system should evolve with usage patterns and be updated regularly to maintain effectiveness.*