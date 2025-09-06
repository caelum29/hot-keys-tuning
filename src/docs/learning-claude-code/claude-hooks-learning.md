# Learning Claude Code: Subagents and Hooks

A hands-on guide using the keyboard configuration project to master Claude Code's most powerful features.

## Table of Contents
- [Hooks Fundamentals](#hooks-fundamentals)
- [Practical Hook Examples](#practical-hook-examples) 
- [Subagents Deep Dive](#subagents-deep-dive)
- [Integration & Workflows](#integration--workflows)
- [Security & Best Practices](#security--best-practices)
- [Troubleshooting](#troubleshooting)

## Hooks Fundamentals

### What Are Hooks?

Hooks are automated commands that execute at specific points in Claude Code's workflow. They allow you to:
- Automatically validate files before/after edits
- Log operations for audit trails
- Generate documentation when configs change
- Prevent dangerous operations
- Integrate with external tools

### Hook Events

Claude Code provides 5 hook trigger points:

1. **PreToolUse**: Runs BEFORE tool execution (can block tools)
2. **PostToolUse**: Runs AFTER tool execution completes  
3. **UserPromptSubmit**: Runs when you submit a prompt
4. **SubagentStop**: Runs when subagent tasks complete
5. **Notification**: Runs when Claude sends notifications

### Configuration Structure

Hooks are configured in `~/.claude/hooks/` JSON files:

```json
{
  "description": "My custom hooks",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command", 
            "command": "your-shell-command-here"
          }
        ]
      }
    ]
  }
}
```

## Practical Hook Examples

### 1. File Edit Logging Hook

**Location**: `~/.claude/hooks/keyboard-config-hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"[$(date '+%H:%M:%S')] About to edit: $(echo '$TOOL_INPUT' | jq -r '.file_path // \"unknown\"')\" >> ~/.claude/hooks/edit-log.txt"
          }
        ]
      }
    ]
  }
}
```

**What it does**: Logs every file edit attempt with timestamp to `edit-log.txt`

**Key concepts**:
- `$TOOL_INPUT`: Contains the tool parameters as JSON
- `jq`: Parses JSON to extract specific fields
- Append operator `>>`: Prevents overwriting previous logs

### 2. Auto-Documentation Generator Hook

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "FILE_PATH=$(echo '$TOOL_INPUT' | jq -r '.file_path // \"\"); if [[ \"$FILE_PATH\" == *\".yaml\" ]] && [[ \"$FILE_PATH\" == *\"keyboard-config/data\"* ]]; then cd \"$CLAUDE_PROJECT_DIR/keyboard-config\" && source venv/bin/activate && python scripts/generate-docs.py; fi"
          }
        ]
      }
    ]
  }
}
```

**What it does**: Automatically regenerates documentation when YAML config files are edited

**Key concepts**:
- `$CLAUDE_PROJECT_DIR`: Environment variable with project path
- Conditional execution: Only runs for specific file patterns
- Chain commands: `&&` ensures each step succeeds before continuing

### 3. Validation Hook with Scripts

**Script**: `keyboard-config/hooks/validate-yaml.sh`

```bash
#!/bin/bash
set -e

YAML_FILE="$1"
LOG_FILE="$HOME/.claude/hooks/yaml-validation.log"

# Validate YAML syntax
python3 -c "
import yaml
try:
    with open('$YAML_FILE', 'r') as f:
        yaml.safe_load(f)
    print('✓ YAML syntax valid')
except yaml.YAMLError as e:
    print(f'✗ YAML error: {e}', file=sys.stderr)
    sys.exit(1)
" >> "$LOG_FILE" 2>&1
```

**Hook configuration**:
```json
{
  "matcher": "MultiEdit",
  "hooks": [
    {
      "type": "command",
      "command": "if echo '$TOOL_INPUT' | jq -r '.file_path' | grep -q '\\.yaml$'; then ~/path/to/validate-yaml.sh \"$(echo '$TOOL_INPUT' | jq -r '.file_path')\"; fi"
    }
  ]
}
```

### 4. Backup Hook

**Script**: `keyboard-config/hooks/backup-changes.sh`

Creates timestamped backups and maintains only the 10 most recent versions:

```bash
#!/bin/bash
FILE_PATH="$1"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
BACKUP_DIR="$HOME/.claude/hooks/backups"
BASENAME=$(basename "$FILE_PATH")
BACKUP_PATH="$BACKUP_DIR/${BASENAME}_${TIMESTAMP}.bak"

mkdir -p "$BACKUP_DIR"
cp "$FILE_PATH" "$BACKUP_PATH"

# Keep only last 10 backups
find "$BACKUP_DIR" -name "${BASENAME}_*.bak" -type f | sort -r | tail -n +11 | xargs -r rm -f
```

## Subagents Deep Dive

### What Are Subagents?

Subagents are specialized AI agents that handle complex, multi-step tasks autonomously. They're perfect for:
- Research and analysis tasks
- Multi-file operations  
- Complex reasoning that requires multiple steps
- Tasks that need specialized expertise

### Available Subagent Types

1. **general-purpose**: Research, file operations, multi-step tasks
2. **code-reviewer**: Comprehensive code analysis
3. **statusline-setup**: Configure status line settings
4. **output-style-setup**: Create output styles

### Subagent Example: Keyboard Binding Analysis

Here's a real example from our learning session:

```markdown
Task: Analyze all keyboard bindings in this project

Subagent type: general-purpose
Description: "Analyze keyboard bindings" 
Prompt: "Please analyze all keyboard bindings in this project and provide a comprehensive report.

Specifically:
1. Read all YAML files in keyboard-config/data/
2. Check src/karabiner/ for JSON configurations
3. Look for .ideavimrc files for Vim mappings
4. Create statistical breakdown by key usage, modifier patterns, status
5. Generate specific recommendations

Return structured analysis with data points and actionable recommendations."
```

**Results**: The subagent autonomously:
- Read 3 different config file formats (YAML, JSON, Vim script)
- Analyzed 48 total bindings across multiple systems
- Generated statistical breakdowns and conflict analysis
- Provided prioritized implementation recommendations

### Context Sharing Challenge

**Important limitation**: Subagents have context isolation - they can't see files created by other subagents or the parent conversation.

**Workarounds**:
1. **Explicit file references**: Tell subagents exactly which files to read
2. **Structured handoffs**: Save subagent results to files for other agents
3. **Parent agent synthesis**: Have main agent summarize cross-subagent findings

### Best Practices for Subagents

1. **Be specific**: Detailed prompts get better results
2. **Define deliverables**: Specify exactly what format you want back
3. **Use for appropriate complexity**: Don't use subagents for simple tasks
4. **Chain strategically**: Design handoffs between multiple subagents

## Integration & Workflows

### Setting Up Project-Specific Hooks

1. **Create project directory structure**:
```bash
mkdir -p ~/.claude/hooks/scripts
mkdir -p keyboard-config/hooks
```

2. **Environment variables available**:
- `$CLAUDE_PROJECT_DIR`: Current project directory
- `$TOOL_INPUT`: Tool parameters as JSON
- `$USER_PROMPT`: User's submitted prompt
- `$SUBAGENT_RESULT`: Results from completed subagent

3. **Hook matchers for tools**:
- `Task`: Subagent executions
- `Bash`: Shell commands  
- `Read`: File reading
- `Edit`, `MultiEdit`: File modifications
- `Write`: File creation
- `WebFetch`, `WebSearch`: Web operations

### Workflow Example: YAML → Documentation Pipeline

1. **User edits YAML** → PreToolUse backup hook creates safety copy
2. **Edit completes** → PostToolUse hook validates YAML syntax  
3. **Validation passes** → Hook regenerates documentation
4. **Documentation updated** → Notification hook alerts completion

### MCP Tool Integration

Hooks work with MCP (Model Context Protocol) tools:

```json
{
  "matcher": "mcp__jetbrains__replace_text_in_file",
  "hooks": [
    {
      "type": "command",
      "command": "echo 'JetBrains file modified' >> ~/.claude/mcp-log.txt"
    }
  ]
}
```

## Security & Best Practices

### Critical Security Rules

1. **Always quote variables**:
```bash
# WRONG (vulnerable)
cp $TOOL_INPUT /tmp/backup

# RIGHT (safe)  
cp "$TOOL_INPUT" "/tmp/backup"
```

2. **Validate inputs**:
```bash
if [[ -z "$FILE_PATH" ]] || [[ ! -f "$FILE_PATH" ]]; then
    echo "Invalid file path"
    exit 1
fi
```

3. **Use absolute paths**:
```bash
# WRONG (context dependent)
./scripts/validate.py

# RIGHT (explicit)  
"$CLAUDE_PROJECT_DIR/scripts/validate.py"
```

4. **Set strict error handling**:
```bash
#!/bin/bash
set -e  # Exit on any error
set -u  # Exit on undefined variables
set -o pipefail  # Exit on pipe failures
```

### Performance Considerations

1. **Timeout management**: Long-running hooks can block operations
2. **Log rotation**: Prevent log files from growing too large
3. **Conditional execution**: Use guards to avoid unnecessary work
4. **Background processes**: Use `&` for non-blocking operations

## Troubleshooting

### Common Hook Issues

#### 1. Hook Not Running
- **Check**: Hook configuration syntax with `cat ~/.claude/hooks/config.json | jq`
- **Check**: File permissions on hook scripts with `ls -la`
- **Check**: Hook logs for error messages

#### 2. Command Failures
- **Test commands manually**: Run the exact command in terminal
- **Check environment variables**: `echo $CLAUDE_PROJECT_DIR`  
- **Validate JSON parsing**: `echo '$TOOL_INPUT' | jq`

#### 3. Permission Errors
```bash
chmod +x ~/path/to/hook-script.sh
```

#### 4. Path Issues
```bash
# Debug path resolution
echo "PWD: $PWD" >> debug.log
echo "PROJECT: $CLAUDE_PROJECT_DIR" >> debug.log
echo "PATH: $PATH" >> debug.log
```

### Debugging Strategies

1. **Start simple**: Test with basic `echo` commands first
2. **Add logging**: Liberal use of log files during development  
3. **Test components**: Verify each part of complex command chains
4. **Use error codes**: Proper exit codes for hook failure detection

### Hook Performance Testing

Create a test hook to measure execution times:

```json
{
  "matcher": "Read",
  "hooks": [
    {
      "type": "command",
      "command": "START=$(date +%s%N); echo 'Hook executed' > /dev/null; END=$(date +%s%N); echo \"Hook duration: $((($END - $START)/1000000))ms\" >> ~/.claude/hooks/perf.log"
    }
  ]
}
```

## Advanced Examples

### Multi-System Conflict Detection Hook

Combining hooks with our conflict detection script:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "if echo '$TOOL_INPUT' | jq -r '.file_path' | grep -qE '\\.(yaml|json|ideavimrc)$'; then \"$CLAUDE_PROJECT_DIR/keyboard-config/hooks/check-conflicts.py\" >> ~/.claude/hooks/conflicts.log 2>&1; fi"
          }
        ]
      }
    ]
  }
}
```

### Conditional Subagent Triggers

Hook that launches subagents based on file patterns:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "MultiEdit", 
        "hooks": [
          {
            "type": "command",
            "command": "CHANGES=$(echo '$TOOL_INPUT' | jq -r '.edits | length'); if [[ $CHANGES -gt 5 ]]; then echo 'Large change detected - consider code review subagent' >> ~/.claude/hooks/review-suggestions.log; fi"
          }
        ]
      }
    ]
  }
}
```

---

## Learning Path Recommendations

### Beginner (Week 1)
- Set up basic logging hooks
- Create simple validation scripts  
- Experiment with PreToolUse/PostToolUse events

### Intermediate (Week 2)
- Build project-specific hook workflows
- Use subagents for analysis tasks
- Integrate hooks with existing project scripts

### Advanced (Week 3+)
- Complex multi-step hook pipelines
- Custom subagent chaining workflows
- Performance optimization and security hardening

### Practice Projects
1. **Config Management**: Auto-validate and backup configuration files
2. **Documentation Sync**: Keep docs updated with code changes  
3. **Quality Gates**: Prevent commits without proper formatting/tests
4. **Workflow Integration**: Connect Claude Code to existing CI/CD pipelines

---

*This guide demonstrates Claude Code's advanced features using real project examples. Start with simple hooks and gradually build more sophisticated workflows as you become comfortable with the concepts.*