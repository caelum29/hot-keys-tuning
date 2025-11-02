# WEBSTORM-TERMINAL-AUTOCOMPLETE

---
created: 2025-11-02
modified: 2025-11-02
tags:
  - webstorm
  - terminal
  - autocomplete
  - zsh
  - oh-my-zsh
  - productivity
aliases:
  - Terminal Autocomplete
  - WebStorm Terminal Setup
---

## Overview

Complete setup guide for terminal autocomplete in WebStorm 2025 using Oh-My-Zsh, zsh-autosuggestions, fast-syntax-highlighting, and fzf. This configuration provides maximum autocomplete features while maintaining full compatibility with the **Reworked 2025 terminal engine**.

## Quick Reference

| Feature | Plugin | Keybinding |
|---------|--------|------------|
| History suggestions (gray text) | zsh-autosuggestions | Right Arrow / End to accept |
| Fuzzy history search | fzf | Ctrl+R |
| Fuzzy file search | fzf | Ctrl+T |
| Command syntax highlighting | fast-syntax-highlighting | Automatic |
| Directory jumping | z | `z <partial-name>` |
| Archive extraction | extract | `extract <file>` |

## Installation Summary

### What Was Installed

1. **Oh-My-Zsh** (v2025) - Framework for zsh configuration
2. **Powerlevel10k** - Modern, fast theme with git status and version info
3. **zsh-autosuggestions** - History-based cyan text suggestions
4. **fast-syntax-highlighting** - Real-time command validation (green/red highlighting)
5. **fzf** v0.66.1 - Fuzzy finder for enhanced search
6. **Productivity plugins** - node, npm, yarn, jsontools

### File Locations

```bash
~/.oh-my-zsh/                                    # Oh-My-Zsh installation
~/.oh-my-zsh/custom/plugins/zsh-autosuggestions/ # History suggestions
~/.oh-my-zsh/custom/plugins/fast-syntax-highlighting/ # Syntax highlighting
~/.zshrc                                         # Main configuration file
~/.zshrc.backup-YYYYMMDD-HHMMSS                  # Backup of original config
~/.zshrc.pre-oh-my-zsh                           # Oh-My-Zsh auto-backup
~/.fzf.zsh                                       # fzf keybindings and completion
/opt/homebrew/bin/fzf                            # fzf binary
```

## Configuration Details

### Enabled Plugins

The following plugins are active in `~/.zshrc`:

```bash
plugins=(
  git                      # Git aliases and completion
  docker                   # Docker command completion
  node                     # Node.js shortcuts and version info
  npm                      # npm command completion
  yarn                     # Yarn command completion
  jsontools                # JSON pretty-printing (pp_json)
  z                        # Directory jumping (tracks frequently used dirs)
  extract                  # Smart archive extraction
  fzf                      # Fuzzy finder integration
  zsh-autosuggestions      # History-based suggestions
  fast-syntax-highlighting # Real-time syntax highlighting
)
```

### Autocomplete Settings

```bash
# Suggestion visibility (gray color for dark backgrounds)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=8'

# History optimization (prevents WebStorm terminal conflicts)
setopt INC_APPEND_HISTORY    # Write immediately, not on exit
setopt SHARE_HISTORY         # Share between sessions
setopt HIST_IGNORE_DUPS      # No duplicate entries
setopt HIST_FIND_NO_DUPS     # No duplicates in search

# fzf integration
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
```

## WebStorm Terminal Configuration

### Required Settings

**Location**: WebStorm → Settings (Cmd+,) → **Tools → Terminal**

| Setting | Value | Notes |
|---------|-------|-------|
| Shell path | `/bin/zsh` | Use system zsh |
| Terminal engine | **Reworked 2025** | Default in 2025.2+ |
| Shell integration | ✓ Enabled | Loads `~/.zshrc` automatically |

### Verification

Open WebStorm terminal (Cmd+Option+F12 or Alt+F12) and test:

```bash
# Test autocomplete - type a command you've used before
git sta█  # should show gray suggestion "git status"

# Test syntax highlighting
echo "test"  # should be green (valid command)
echooo       # should be red (invalid command)

# Test fzf history search
# Press Ctrl+R and type to fuzzy search command history

# Test fzf file search
# Press Ctrl+T to fuzzy search files in current directory

# Test z directory jumping
z projects   # jumps to most frequent directory matching "projects"
```

## Feature Guide

### 1. zsh-autosuggestions

**What it does**: Shows gray text suggestions from command history as you type

**How to use**:
- Start typing: `git com`
- See suggestion: `git commit -m "fix bug"` (in gray)
- Accept full suggestion: **Right Arrow** or **End**
- Accept partial: **Ctrl+Right Arrow** (forward-word)

**Customization**:
```bash
# Change suggestion color (edit ~/.zshrc)
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=blue'  # blue suggestions
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=cyan'  # cyan suggestions
```

### 2. fast-syntax-highlighting

**What it does**: Colors commands green (valid) or red (invalid) in real-time

**Features**:
- ✅ Command validation before execution
- ✅ Variable highlighting in strings
- ✅ Bracket matching
- ✅ Command-specific parsing (git, docker, etc.)

**No configuration needed** - works automatically after installation

### 3. fzf Fuzzy Finder

**What it does**: Interactive fuzzy search for history and files

**Keybindings**:

| Key | Function | Example |
|-----|----------|---------|
| **Ctrl+R** | Search command history | Type "docker" to find all docker commands |
| **Ctrl+T** | Search files in current dir | Type "json" to find all JSON files |
| **Alt+C** | Change directory (cd) | Fuzzy search directories to navigate |

**Tips**:
- Use space to separate search terms: `git push origin`
- Use `'` for exact match: `'git push'`
- Use `^` for prefix: `^git` (starts with git)
- Use `$` for suffix: `.md$` (ends with .md)

### 4. z Directory Jumping

**What it does**: Tracks frequently used directories and lets you jump to them with partial names

**Usage**:
```bash
# Navigate to a directory a few times
cd ~/Projects/hot-keys-tuning
cd ~/Projects/my-app

# Later, jump to them from anywhere
z hot-keys    # jumps to ~/Projects/hot-keys-tuning
z my-app      # jumps to ~/Projects/my-app

# List tracked directories
z -l          # show all tracked paths with scores
```

### 5. extract Plugin

**What it does**: Universal archive extraction (no need to remember tar flags)

**Usage**:
```bash
extract file.tar.gz   # extracts .tar.gz
extract file.zip      # extracts .zip
extract file.rar      # extracts .rar
extract file.7z       # extracts .7z
# ... supports 20+ formats
```

## Troubleshooting

### Problem: Suggestions Not Visible

**Cause**: Suggestion color matches background

**Fix**: Edit `~/.zshrc` and change highlight color:
```bash
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=240'  # lighter gray
```

Then reload: `source ~/.zshrc`

### Problem: Syntax Highlighting Not Working

**Cause**: Plugin load order (must be last)

**Fix**: In `~/.zshrc`, ensure `fast-syntax-highlighting` is the **last plugin**:
```bash
plugins=(
  git
  docker
  zsh-autosuggestions
  fast-syntax-highlighting  # MUST BE LAST
)
```

### Problem: fzf Not Working (Ctrl+R does nothing)

**Cause**: fzf integration not sourced

**Fix**: Add to `~/.zshrc`:
```bash
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
```

Then reload: `source ~/.zshrc`

### Problem: History Conflicts Between Terminal and WebStorm

**Cause**: Both writing to history on exit

**Fix**: Already configured in `~/.zshrc`:
```bash
setopt INC_APPEND_HISTORY  # Write immediately
setopt SHARE_HISTORY       # Share between sessions
```

### Problem: Terminal Shortcuts Not Working (Ctrl+R, arrow keys)

**Cause**: Using "Classic" terminal engine instead of "Reworked 2025"

**Fix**:
1. Settings → Tools → Terminal
2. Terminal engine: **Reworked 2025**
3. Restart WebStorm

## Advanced Customization

### Change Theme

Oh-My-Zsh includes 140+ themes. To change:

```bash
# Edit ~/.zshrc
ZSH_THEME="agnoster"  # or "powerlevel10k", "spaceship", etc.

# List all themes
ls ~/.oh-my-zsh/themes/

# Preview themes
omz theme use <theme-name>
```

### Powerlevel10k Theme (Installed)

**Powerlevel10k** is now installed and configured in your setup. It provides:

- **Instant prompt** - Zero lag when opening terminal
- **Git status** - Branch, changes, ahead/behind info
- **Node version** - Current Node.js version display
- **Command timing** - Execution time for long commands
- **Highly customizable** - 50+ segments to choose from

#### Configuration

Run the configuration wizard anytime:
```bash
p10k configure
```

The wizard will guide you through:
1. **Visual style** - Lean, Classic, Rainbow, Powerline
2. **Icons** - Nerdfont icons vs ASCII
3. **Prompt elements** - Which segments to show
4. **Colors** - Color scheme preferences

#### Font Installation (Required)

For proper icon display, install **MesloLGS NF** font:

1. Download fonts from: https://github.com/romkatv/powerlevel10k#fonts
2. Install the 4 font files to your system:
   - MesloLGS NF Regular.ttf
   - MesloLGS NF Bold.ttf
   - MesloLGS NF Italic.ttf
   - MesloLGS NF Bold Italic.ttf
3. Configure WebStorm terminal to use "MesloLGS NF" font:
   - Settings → Tools → Terminal
   - Font: MesloLGS NF
   - Size: 12-14 (recommended)

Without this font, special characters will display as `?` or boxes.

#### Customization

Edit `~/.p10k.zsh` to customize:

```bash
# Show/hide segments
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status node_version time)

# Change colors
POWERLEVEL9K_DIR_BACKGROUND='blue'
POWERLEVEL9K_DIR_FOREGROUND='white'

# Transient prompt (simplify old prompts)
POWERLEVEL9K_TRANSIENT_PROMPT=always
```

Open config file: `webstorm ~/.p10k.zsh` or `p10k configure`

#### File Locations

```bash
~/.oh-my-zsh/custom/themes/powerlevel10k/  # Theme installation
~/.p10k.zsh                                # Your configuration
```

### Add More Plugins

Browse plugins: https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins

**Popular additions**:
```bash
plugins=(
  git
  docker
  node                 # Node.js shortcuts
  npm                  # npm completion
  yarn                 # yarn completion
  kubectl              # Kubernetes completion
  aws                  # AWS CLI completion
  terraform            # Terraform completion
  z
  extract
  fzf
  zsh-autosuggestions
  fast-syntax-highlighting
)
```

### Performance Optimization

If shell startup feels slow:

```bash
# Time your shell startup
time zsh -i -c exit

# Disable unused plugins
# Edit ~/.zshrc and remove plugins you don't use

# Use lazy loading for heavy plugins
# Example: Load nvm only when needed
nvm() {
  unset -f nvm
  export NVM_DIR="$HOME/.nvm"
  [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
  nvm "$@"
}
```

## Keyboard Shortcuts Reference

### zsh-autosuggestions

| Key | Action |
|-----|--------|
| Right Arrow / End | Accept full suggestion |
| Ctrl+Right Arrow | Accept one word |
| Ctrl+E | Accept full suggestion (alternative) |

### fzf

| Key | Action |
|-----|--------|
| **Ctrl+R** | Search command history |
| **Ctrl+T** | Search files |
| **Alt+C** | Search directories (cd) |
| Ctrl+J / Down | Next match |
| Ctrl+K / Up | Previous match |
| Enter | Select |
| Esc / Ctrl+C | Cancel |

### Terminal Navigation (Standard)

| Key | Action |
|-----|--------|
| Ctrl+A | Beginning of line |
| Ctrl+E | End of line |
| Ctrl+U | Clear line before cursor |
| Ctrl+K | Clear line after cursor |
| Ctrl+W | Delete word before cursor |
| Ctrl+L | Clear screen |
| Ctrl+C | Cancel current command |
| Ctrl+D | Exit terminal (if empty line) |

## Related Documentation

- [[WEBSTORM-DOCUMENTATION]] - Comprehensive WebStorm docs index
- [[WEBSTORM-KEYMAP]] - Custom WebStorm keymap configurations
- [[WEBSTORM-QUICK-LISTS]] - WebStorm quick lists reference
- [[HJKL-NAVIGATION]] - Vim-style navigation patterns
- [[KARABINER-CONFIG]] - System-wide keyboard modifications

## External Resources

### Official Documentation
- [Oh-My-Zsh Wiki](https://github.com/ohmyzsh/ohmyzsh/wiki)
- [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
- [fast-syntax-highlighting](https://github.com/zdharma-continuum/fast-syntax-highlighting)
- [fzf Documentation](https://github.com/junegunn/fzf)
- [WebStorm Terminal Docs](https://www.jetbrains.com/help/webstorm/terminal-emulator.html)

### JetBrains Blog
- [JetBrains Terminal: A New Architecture (2025)](https://blog.jetbrains.com/idea/2025/04/jetbrains-terminal-a-new-architecture/)
- [Reworked Terminal Default in 2025.2](https://blog.jetbrains.com/platform/2025/07/the-reworked-terminal-becomes-the-default-in-2025-2/)

## Maintenance

### Update Oh-My-Zsh

```bash
omz update  # Manual update
```

### Update Plugins

```bash
cd ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions && git pull
cd ~/.oh-my-zsh/custom/plugins/fast-syntax-highlighting && git pull
```

### Update fzf

```bash
brew upgrade fzf
/opt/homebrew/opt/fzf/install  # Re-run installer
```

### Backup Configuration

```bash
# Backup current config
cp ~/.zshrc ~/.zshrc.backup-$(date +%Y%m%d)

# Restore from backup
cp ~/.zshrc.backup-YYYYMMDD ~/.zshrc
source ~/.zshrc
```

---

**Last Updated**: 2025-11-02  
**WebStorm Version**: 2025.2+  
**Terminal Engine**: Reworked 2025  
**macOS Version**: Sequoia 24.6.0