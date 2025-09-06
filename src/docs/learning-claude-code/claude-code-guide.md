# Claude Code Complete Learning Guide

A comprehensive guide to mastering Claude Code through practical examples with the keyboard configuration project.

## Table of Contents
- [Core Concepts](#core-concepts)
- [Essential Tools](#essential-tools)
- [File Operations](#file-operations)
- [Search & Navigation](#search--navigation)
- [Advanced Features](#advanced-features)
- [Project-Specific Examples](#project-specific-examples)
- [Best Practices](#best-practices)
- [Workflow Integration](#workflow-integration)

## Core Concepts

### What is Claude Code?
Claude Code is an AI-powered CLI tool that helps with software engineering tasks. It can:
- Read, edit, and create files
- Search through codebases
- Execute shell commands
- Generate documentation
- Integrate with Git workflows
- Work with JetBrains IDEs

### Key Principles
1. **Context Awareness**: Uses project structure and CLAUDE.md for guidance
2. **Tool-Based**: Operates through specialized tools rather than general commands
3. **Safety First**: Plan mode allows exploration before making changes
4. **Parallelization**: Can execute multiple operations simultaneously

## Essential Tools

### File Operations
```markdown
# Read files
Read - View file contents with line numbers
Write - Create new files or overwrite existing ones
Edit - Make targeted replacements in existing files
MultiEdit - Multiple edits to the same file in one operation
```

### Search Tools
```markdown
# Finding files
Glob - Pattern matching for file paths (*.yaml, **/*.json)
mcp__jetbrains__find_files_by_name_keyword - Fast name-based search
mcp__jetbrains__find_files_by_glob - JetBrains IDE file search

# Content search
Grep - Regex pattern search in file contents
mcp__jetbrains__search_in_files_by_text - IDE-powered text search
mcp__jetbrains__search_in_files_by_regex - IDE-powered regex search
```

### Task Management
```markdown
TodoWrite - Track progress with structured todo lists
Task - Delegate complex tasks to specialized sub-agents
```

## File Operations

### Reading Files
```bash
# Read entire file
Read file_path="/Users/artem/.../keyboard-config/data/horizontal-navigation.yaml"

# Read with limits (for large files)
Read file_path="large-file.json" offset=100 limit=50
```

### Editing Files
```bash
# Single edit
Edit file_path="config.yaml" old_string="hjkl: false" new_string="hjkl: true"

# Multiple edits
MultiEdit file_path="config.yaml" edits=[
  {old_string: "version: 1.0", new_string: "version: 2.0"},
  {old_string: "debug: false", new_string: "debug: true"}
]
```

### Creating Files
```bash
# New file with content
Write file_path="new-config.yaml" content="# New configuration\nversion: 1.0"
```

## Search & Navigation

### File Pattern Matching
```bash
# Find all YAML files
Glob pattern="**/*.yaml"

# Find Karabiner configs
Glob pattern="src/karabiner/*.json"

# Find IdeaVim files
Glob pattern="**/.ideavimrc"
```

### Content Search
```bash
# Search for key combinations
Grep pattern="cmd.*shift.*h" output_mode="content"

# Find function definitions
Grep pattern="def generate_.*:" type="py" -n

# Search in specific directory
Grep pattern="hjkl" path="keyboard-config/data"
```

### JetBrains Integration
```bash
# Fast file search by name
mcp__jetbrains__find_files_by_name_keyword nameKeyword="horizontal"

# Search content with IDE
mcp__jetbrains__search_in_files_by_text searchText="hyper key" fileMask="*.md"
```

## Advanced Features

### Plan Mode
```markdown
Plan Mode allows safe exploration before making changes:
- Activated automatically for analysis tasks
- Prevents accidental modifications
- Shows comprehensive plan before execution
- User approval required to proceed
```

### Sub-Agents
```bash
# General purpose research
Task subagent_type="general-purpose" 
     description="Find keyboard shortcuts" 
     prompt="Search for all HJKL bindings and categorize by modifier keys"

# Code review
Task subagent_type="code-reviewer"
     description="Review configurations"
     prompt="Analyze Karabiner config for security issues and performance problems"
```

### Parallel Operations
```bash
# Execute multiple searches simultaneously
Grep pattern="cmd.*h" & 
Grep pattern="ctrl.*h" &
Grep pattern="opt.*h"
```

### Web Integration
```bash
# Fetch documentation
WebFetch url="https://docs.anthropic.com/en/docs/claude-code/intro" 
        prompt="Extract key features and capabilities"

# Search current topics
WebSearch query="Karabiner Elements 2025 best practices"
```

## Project-Specific Examples

### 1. Adding New Keyboard Binding

```yaml
# Step 1: Read current YAML structure
Read file_path="keyboard-config/data/horizontal-navigation.yaml"

# Step 2: Add new binding
Edit file_path="keyboard-config/data/horizontal-navigation.yaml"
     old_string="# End of bindings"
     new_string="- key: m
  modifiers: [cmd, shift]
  action: "Move window right"
  status: planned
# End of bindings"

# Step 3: Regenerate documentation
Bash command="cd keyboard-config && python scripts/generate-docs.py"
```

### 2. Finding Conflicting Key Combinations

```bash
# Search across all config files
Task subagent_type="general-purpose"
     description="Find key conflicts"
     prompt="Search all config files (Karabiner JSON, IdeaVim, WebStorm XML) for duplicate key combinations and report conflicts"
```

### 3. Analyzing Binding Statistics

```bash
# Generate CSV export
Bash command="cd keyboard-config && python scripts/export-csv.py"

# Read statistics
Read file_path="keyboard-config/generated/bindings-summary.csv"
```

### 4. Updating Documentation

```bash
# Find all markdown files needing updates
Grep pattern="TODO.*update" glob="**/*.md" output_mode="files_with_matches"

# Batch update using MultiEdit
MultiEdit file_path="README.md" edits=[
  {old_string: "Version 1.0", new_string: "Version 2.0"},
  {old_string: "48 total bindings", new_string: "52 total bindings"}
]
```

## Best Practices

### File Operations
1. **Always Read First**: Use Read before Edit to understand context
2. **Prefer Edit over Write**: Edit preserves file structure and comments
3. **Use MultiEdit**: For multiple changes to the same file
4. **Check Line Numbers**: Read provides line numbers for precise editing

### Search Strategy
1. **Start Broad**: Use Glob to find relevant files
2. **Narrow Down**: Use Grep for specific content
3. **Use Context**: Add -A/-B/-C flags for surrounding lines
4. **Leverage IDE**: JetBrains tools are faster for project-wide search

### Task Management
1. **Use TodoWrite**: Track complex multi-step operations
2. **Update Status**: Mark tasks as in_progress and completed
3. **Break Down**: Complex tasks into smaller, manageable steps

### Performance
1. **Parallel Execution**: Batch independent operations
2. **Appropriate Tools**: Use specialized tools for their strengths
3. **Limit Results**: Use head_limit for large search results

## Workflow Integration

### JetBrains IDE Features
```bash
# Get project structure
mcp__jetbrains__list_directory_tree directoryPath="." maxDepth=3

# Check for problems
mcp__jetbrains__get_project_problems

# Reformat files
mcp__jetbrains__reformat_file path="src/karabiner/karabiner.json"

# Open in editor
mcp__jetbrains__open_file_in_editor filePath="keyboard-config/data/vertical-navigation.yaml"
```

### Git Integration
```bash
# Check status
Bash command="git status"

# View changes
Bash command="git diff"

# Create commits
Bash command='git add . && git commit -m "Update keyboard bindings

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"'
```

### Testing & Validation
```bash
# Run Python scripts
Bash command="cd keyboard-config && source venv/bin/activate && python scripts/generate-docs.py"

# Validate YAML
Bash command="cd keyboard-config && python -c 'import yaml; yaml.safe_load(open(\"data/horizontal-navigation.yaml\"))'"

# Check schema compliance
Bash command="cd keyboard-config && python scripts/validate-schema.py"
```

### Documentation Generation
```bash
# Generate all docs
Bash command="cd keyboard-config && python scripts/generate-docs.py"

# Export data formats
Bash command="cd keyboard-config && python scripts/export-csv.py"

# Update statistics
Grep pattern="Statistics.*:" path="CLAUDE.md" -n
Edit file_path="CLAUDE.md" 
     old_string="**Current Statistics**: 48 total bindings"
     new_string="**Current Statistics**: 52 total bindings"
```

## Configuration Tips

### CLAUDE.md Setup
```markdown
# Essential sections for your CLAUDE.md:

## Development Workflow
- List build/test commands
- Define primary file types
- Specify generation scripts

## LLM-Friendly Workflow
- Prefer YAML over markdown editing
- Use schema validation
- Define data structure benefits

## Key Patterns  
- Maintain consistency across tools
- Follow established paradigms
- Test across all systems
```

### Command Shortcuts
```bash
# Create aliases for common operations
alias cc-docs="cd keyboard-config && python scripts/generate-docs.py"
alias cc-export="cd keyboard-config && python scripts/export-csv.py"
alias cc-validate="cd keyboard-config && python scripts/validate-schema.py"
```

## Troubleshooting

### Common Issues
1. **File Not Found**: Use absolute paths or check working directory
2. **Edit Failures**: Ensure old_string matches exactly (including whitespace)
3. **Tool Timeouts**: Increase timeout parameter for large operations
4. **Permission Errors**: Check file permissions and IDE access

### Debug Strategies
1. **Use Read First**: Understand file structure before editing
2. **Small Changes**: Make incremental edits and test
3. **Check Git Status**: Monitor what's actually being changed
4. **Validate Syntax**: Run parsers/linters after modifications

---

*This guide covers the essential Claude Code features. Practice with your keyboard configuration project to master these tools and workflows.*