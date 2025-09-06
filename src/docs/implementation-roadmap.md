# Implementation Roadmap - Unified Keyboard Productivity System

*Step-by-step guide for safely implementing the integrated Karabiner-Elements + WebStorm + IdeaVim system*

## Overview

This roadmap provides a phased approach to implementing the unified keyboard productivity system with validation checkpoints and rollback procedures at each stage.

## Pre-Implementation Checklist

### **System Requirements**
- [ ] macOS (Karabiner-Elements requirement)
- [ ] WebStorm installed and licensed
- [ ] IdeaVim plugin installed in WebStorm
- [ ] Karabiner-Elements installed (current sophisticated setup)
- [ ] Backup system in place

### **Current State Documentation**
- [ ] Current Karabiner configuration backed up
- [ ] Current WebStorm keymap exported
- [ ] Current `.ideavimrc` backed up
- [ ] Performance baseline established (CPU/memory usage)

## Phase 1: Foundation Validation & Enhancement (Week 1)

### **Day 1-2: Current System Analysis**

#### **Step 1.1: Analyze Current Karabiner Setup**
```bash
# Validate current Karabiner configuration
echo "📊 Analyzing current Karabiner setup..."

# Check configuration size and complexity
KARABINER_SIZE=$(wc -c < ~/.config/karabiner/karabiner.json)
echo "Current configuration size: $KARABINER_SIZE bytes"

# Verify WebStorm bundle detection
grep -n "com.jetbrains.WebStorm" ~/.config/karabiner/karabiner.json || echo "⚠️  WebStorm bundle ID not found"

# Test current functionality
echo "✅ Testing current Hyper key functionality:"
echo "1. Press CapsLock+H/J/K/L → Should work as arrow keys"
echo "2. Press CapsLock+G → Should launch WebStorm"
echo "3. Verify all current shortcuts still work"
```

#### **Step 1.2: Backup & Version Control**
```bash
# Create comprehensive backup
echo "📦 Creating comprehensive backup..."

BACKUP_DIR="$HOME/keyboard-backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Backup Karabiner
cp -r ~/.config/karabiner "$BACKUP_DIR/karabiner-backup"
echo "✅ Karabiner backed up to $BACKUP_DIR"

# Backup WebStorm keymap
WEBSTORM_SUPPORT_DIR=$(find ~/Library/Application\ Support/JetBrains -name "WebStorm*" -type d | head -1)
if [[ -n "$WEBSTORM_SUPPORT_DIR" ]]; then
    cp -r "$WEBSTORM_SUPPORT_DIR/keymaps" "$BACKUP_DIR/webstorm-keymaps-backup" 2>/dev/null || true
    echo "✅ WebStorm keymap backed up"
fi

# Backup IdeaVim
cp ~/.ideavimrc "$BACKUP_DIR/ideavimrc-backup" 2>/dev/null || true
echo "✅ IdeaVim configuration backed up"

echo "🎯 All configurations backed up to: $BACKUP_DIR"
```

#### **Step 1.3: Performance Baseline**
```bash
# Establish performance baseline
echo "⚡ Establishing performance baseline..."

# Measure Karabiner CPU/Memory usage
echo "Karabiner Performance Baseline:" > "$BACKUP_DIR/performance-baseline.txt"
ps aux | grep karabiner_console_user_server | grep -v grep >> "$BACKUP_DIR/performance-baseline.txt"

# Test input latency (manual)
echo "🖱️  Manual Input Latency Test:"
echo "1. Press CapsLock+H 10 times rapidly"
echo "2. Note any lag or missed inputs"
echo "3. Record baseline response time feel"
```

### **Day 3-4: Enhanced Karabiner Integration**

#### **Step 1.4: Add WebStorm-Specific Rules**
Create `~/keyboard-setup/enhanced-webstorm-rules.json`:

```json
{
  "description": "Phase 1: Enhanced WebStorm Integration",
  "manipulators": [
    {
      "description": "Hyper + Semicolon → AceJump in WebStorm (Phase 1 Test)",
      "conditions": [
        {
          "bundle_identifiers": ["com.jetbrains.WebStorm"],
          "type": "frontmost_application_if"
        }
      ],
      "from": {
        "key_code": "semicolon",
        "modifiers": { "mandatory": ["right_shift", "right_command", "right_control", "right_option"] }
      },
      "to": [{ "key_code": "semicolon", "modifiers": ["control"] }],
      "type": "basic"
    }
  ]
}
```

#### **Step 1.5: Gradual Integration**
```bash
# Gradual integration approach
echo "🔧 Implementing enhanced WebStorm integration..."

# Add single rule first for testing
echo "1. Adding Hyper+; → Ctrl+; (AceJump) rule"
echo "2. Test in WebStorm: Press CapsLock+; → Should trigger AceJump"
echo "3. Verify no conflicts with existing shortcuts"

# If successful, add more rules one by one
echo "✅ Phase 1 enhancement ready for testing"
```

### **Day 5-7: Validation & Adjustment**

#### **Step 1.6: Integration Testing**
```bash
# Comprehensive Phase 1 testing
echo "🧪 Phase 1 Integration Testing..."

echo "Test 1: Basic Navigation (Should still work)"
echo "- CapsLock+H/J/K/L → Arrow movement"
echo "- All existing navigation shortcuts"

echo "Test 2: New WebStorm Integration"  
echo "- CapsLock+; in WebStorm → AceJump trigger"
echo "- Verify shortcut works only in WebStorm"

echo "Test 3: Performance Impact"
echo "- Check CPU usage hasn't increased significantly"
echo "- Verify input latency still feels instant"

echo "Test 4: Conflict Detection"
echo "- All existing shortcuts still work"
echo "- No unexpected behavior in other apps"
```

#### **Step 1.7: Phase 1 Validation Checkpoint**
```bash
# Phase 1 completion validation
echo "✅ Phase 1 Validation Checkpoint"

# Performance check
CURRENT_CPU=$(ps aux | grep karabiner_console_user_server | grep -v grep | awk '{print $3}')
echo "Current Karabiner CPU usage: ${CURRENT_CPU:-0}%"

# Functionality check
echo "✅ Validation checklist:"
echo "[ ] All existing shortcuts work"
echo "[ ] New WebStorm AceJump shortcut works"  
echo "[ ] No performance degradation"
echo "[ ] No conflicts detected"
echo "[ ] Ready for Phase 2"
```

## Phase 2: WebStorm Enhancement Implementation (Week 2)

### **Day 8-10: Priority 1 Shortcuts**

#### **Step 2.1: Git Integration Implementation**
```bash
# Implement Priority 1 Git shortcuts
echo "🔧 Implementing Git integration shortcuts..."

echo "WebStorm Keymap Changes (macOS copy1):"
echo "1. Check-in Project → Cmd+K"
echo "2. Git Push → Cmd+Shift+K" 
echo "3. Git Log → Cmd+9"
echo "4. Git Branches → Ctrl+Shift+\`"
echo "5. Show Changes → Cmd+Shift+Alt+D"
```

**Manual WebStorm Configuration Steps:**
1. Open WebStorm → Settings → Keymap
2. Select "macOS copy1" keymap
3. Add shortcuts one by one:
   - Search "Check-in Project" → Add `Cmd+K`
   - Search "Git Push" → Add `Cmd+Shift+K`
   - Search "Git Log" → Add `Cmd+9`
   - Search "Git Branches" → Add `Ctrl+Shift+\``
   - Search "Show Changes" → Add `Cmd+Shift+Alt+D`

#### **Step 2.2: Testing Workflow Integration** 
```bash
# Implement testing shortcuts
echo "🧪 Implementing testing workflow shortcuts..."

echo "WebStorm Testing Shortcuts:"
echo "1. Run Configuration → Cmd+R"
echo "2. Debug Configuration → Cmd+D"
echo "3. Run Class → Ctrl+R" 
echo "4. Debug Class → Ctrl+D"
echo "5. Run Coverage → Ctrl+Shift+R"
```

#### **Step 2.3: Code Generation Shortcuts**
```bash
# Implement code generation shortcuts
echo "⚡ Implementing code generation shortcuts..."

echo "WebStorm Code Generation:"
echo "1. Generate Menu → Cmd+N"
echo "2. Generate Constructor → Cmd+Shift+C"
echo "3. Generate Getter/Setter → Cmd+Shift+G"
echo "4. Generate toString → Cmd+Shift+T"
echo "5. Generate equals/hashCode → Cmd+Shift+E"
```

### **Day 11-12: Enhanced Karabiner Rules**

#### **Step 2.4: Advanced Karabiner Integration**
Add comprehensive WebStorm rules to Karabiner:

```bash
# Add advanced WebStorm integration rules
echo "🚀 Adding advanced Karabiner WebStorm integration..."

echo "New Karabiner Rules:"
echo "1. Hyper+Ctrl+G+C → Git Commit (Cmd+K)"
echo "2. Hyper+Ctrl+G+P → Git Push (Cmd+Shift+K)" 
echo "3. Hyper+Ctrl+T+R → Run Tests (Ctrl+R)"
echo "4. Hyper+Ctrl+T+D → Debug Tests (Ctrl+D)"
echo "5. Hyper+Ctrl+C+G → Generate Menu (Cmd+N)"
```

#### **Step 2.5: Window Management Simplification**
```bash
# Simplify complex window management shortcuts
echo "🪟 Simplifying window management..."

echo "Replacing complex shortcuts:"
echo "- Shift+Ctrl+Alt+K → Cmd+Alt+Up"
echo "- Shift+Ctrl+Alt+J → Cmd+Alt+Down"
echo "- Shift+Ctrl+Alt+H → Cmd+Alt+Left"  
echo "- Shift+Ctrl+Alt+L → Cmd+Alt+Right"
```

### **Day 13-14: Phase 2 Validation**

#### **Step 2.6: Enhanced Workflow Testing**
```bash
# Comprehensive Phase 2 testing
echo "🧪 Phase 2 Enhanced Workflow Testing..."

echo "Test 1: Git Workflow"
echo "1. Make file change → Press Cmd+K → Should open commit dialog"
echo "2. Commit change → Press Cmd+Shift+K → Should push"
echo "3. Press Cmd+9 → Should show Git log"

echo "Test 2: Testing Workflow"
echo "1. Press Cmd+R → Should run current configuration"
echo "2. Press Ctrl+R → Should run current class/test"
echo "3. Press Ctrl+Shift+R → Should run with coverage"

echo "Test 3: Code Generation"
echo "1. Press Cmd+N → Should show generate menu"
echo "2. Press Cmd+Shift+C → Should generate constructor"
echo "3. Verify all generation shortcuts work"
```

## Phase 3: IdeaVim Modern Integration (Week 3)

### **Day 15-17: Enhanced .ideavimrc Implementation**

#### **Step 3.1: Basic IdeaVim Enhancements**
```bash
# Implement enhanced IdeaVim configuration
echo "🎯 Implementing enhanced IdeaVim integration..."

# Backup current .ideavimrc
cp ~/.ideavimrc ~/.ideavimrc.backup.$(date +%Y%m%d)

echo "Enhanced .ideavimrc features:"
echo "1. System integration detection functions"
echo "2. Context-aware navigation mappings" 
echo "3. Git operation IdeaVim shortcuts"
echo "4. Testing workflow integration"
echo "5. Code generation IdeaVim shortcuts"
```

#### **Step 3.2: Expression Mappings Implementation**
Create enhanced `.ideavimrc` with expression mappings:

```vim
" === PHASE 3: ENHANCED IDEAVIM INTEGRATION ===

" System integration detection
function! HasKarabinerEnhancement()
  return system('pgrep karabiner_console_user_server') != ''
endfunction

function! IsWebStorm()
  return has('ide') && &ide =~? 'webstorm'
endfunction

" Context-aware navigation
map <expr> <leader>h IsWebStorm() ? ':action EditorLeft<CR>' : 'h'
map <expr> <leader>j IsWebStorm() ? ':action EditorDown<CR>' : 'j'  
map <expr> <leader>k IsWebStorm() ? ':action EditorUp<CR>' : 'k'
map <expr> <leader>l IsWebStorm() ? ':action EditorRight<CR>' : 'l'

" Git integration shortcuts
if IsWebStorm()
    map <leader>gs :action Vcs.Show.Local.Changes<CR>
    map <leader>gd :action Compare.SameVersion<CR>
    map <leader>gc :action CheckinProject<CR>
    map <leader>gp :action Vcs.Push<CR>
endif
```

#### **Step 3.3: Advanced Integration Features**
```bash
# Implement advanced IdeaVim features
echo "🚀 Implementing advanced IdeaVim features..."

echo "Advanced Features:"
echo "1. Smart paste behavior based on mode"
echo "2. Context-sensitive search actions"
echo "3. File-type specific behavior" 
echo "4. Intelligent comment toggling"
echo "5. Dynamic project-type detection"
```

### **Day 18-19: Integration Testing**

#### **Step 3.4: Three-System Integration Testing**
```bash
# Comprehensive three-system integration test
echo "🔄 Three-System Integration Testing..."

echo "Test 1: Navigation Hierarchy"
echo "1. CapsLock+H (Karabiner) → System arrow left"
echo "2. Space+h (IdeaVim) → WebStorm editor left action"
echo "3. H (Vim normal) → Character left in editor"
echo "4. All should work harmoniously"

echo "Test 2: Git Workflow Integration"  
echo "1. Space+gs (IdeaVim) → Show changes"
echo "2. Cmd+K (WebStorm) → Commit dialog"
echo "3. Cmd+Shift+K (WebStorm) → Push"
echo "4. Should feel like unified workflow"

echo "Test 3: Context Switching"
echo "1. Switch apps with CapsLock shortcuts"
echo "2. WebStorm-specific shortcuts work only in WebStorm"
echo "3. System shortcuts work everywhere"
echo "4. IdeaVim shortcuts work only in WebStorm"
```

### **Day 20-21: Phase 3 Optimization**

#### **Step 3.5: Performance Optimization**
```bash
# Optimize integrated system performance
echo "⚡ Optimizing integrated system performance..."

echo "Optimization Areas:"
echo "1. IdeaVim expression mapping performance"
echo "2. Karabiner rule complexity reduction"
echo "3. WebStorm shortcut conflict resolution"
echo "4. Input latency minimization"

# Performance monitoring
CURRENT_CPU=$(ps aux | grep karabiner_console_user_server | grep -v grep | awk '{print $3}')
echo "Current Karabiner CPU usage: ${CURRENT_CPU:-0}%"

echo "Performance targets:"
echo "- Karabiner CPU < 3%"
echo "- Input latency < 50ms perceived"
echo "- No missed keystrokes"
echo "- Smooth context switching"
```

## Phase 4: Final Optimization & Documentation (Week 4)

### **Day 22-24: System Optimization**

#### **Step 4.1: Timing Optimization**
```bash
# Fine-tune timing parameters
echo "⏱️  Fine-tuning system timing..."

echo "Timing optimizations:"
echo "1. Dual-role key thresholds"
echo "2. Simultaneous key detection timing" 
echo "3. IdeaVim expression mapping delays"
echo "4. WebStorm action response timing"
```

#### **Step 4.2: Conflict Resolution**
```bash
# Resolve any remaining conflicts
echo "🔧 Resolving remaining conflicts..."

echo "Conflict resolution areas:"
echo "1. Overlapping shortcut patterns"
echo "2. Context switching delays"
echo "3. Application detection reliability" 
echo "4. Modifier key conflicts"
```

### **Day 25-26: Comprehensive Testing**

#### **Step 4.3: End-to-End Workflow Testing**
```bash
# Complete workflow integration testing
echo "🎯 End-to-end workflow testing..."

echo "Workflow Test Scenarios:"
echo "1. Morning development setup routine"
echo "2. Code development flow (navigate → edit → refactor)"
echo "3. Git workflow (changes → commit → push)"
echo "4. Testing workflow (write → run → debug)"
echo "5. Multi-project switching workflow"
```

#### **Step 4.4: Stress Testing**
```bash
# System stress testing
echo "💪 System stress testing..."

echo "Stress Test Scenarios:"
echo "1. Rapid key combinations (CapsLock+combinations)"
echo "2. Fast context switching between apps"
echo "3. Simultaneous multi-key pattern usage"
echo "4. Heavy WebStorm usage with complex projects"
echo "5. Long development sessions (8+ hours)"
```

### **Day 27-28: Documentation & Validation**

#### **Step 4.5: Documentation Finalization**
```bash
# Finalize integration documentation
echo "📚 Finalizing integration documentation..."

echo "Documentation completion:"
echo "1. Final configuration files documented"
echo "2. Troubleshooting procedures tested"
echo "3. Rollback procedures validated"
echo "4. Performance benchmarks documented"
echo "5. User training materials created"
```

#### **Step 4.6: Final Validation Checkpoint**
```bash
# Final system validation
echo "✅ Final System Validation Checkpoint"

echo "Validation Criteria:"
echo "[ ] All three systems work harmoniously" 
echo "[ ] No performance degradation"
echo "[ ] All shortcuts work as designed"
echo "[ ] Context switching is seamless"
echo "[ ] Rollback procedures tested"
echo "[ ] Documentation complete"
echo "[ ] System ready for production use"

# Performance final check
FINAL_CPU=$(ps aux | grep karabiner_console_user_server | grep -v grep | awk '{print $3}')
echo "Final Karabiner CPU usage: ${FINAL_CPU:-0}%"

# Feature completeness check
echo "Feature Completeness:"
echo "✅ Karabiner system-level enhancement"
echo "✅ WebStorm IDE productivity features"
echo "✅ IdeaVim editing efficiency"
echo "✅ Integrated Git workflow"
echo "✅ Enhanced testing workflow"
echo "✅ Code generation shortcuts"
echo "✅ Context-aware behavior"
echo "✅ Performance optimization"

echo "🎉 Unified Keyboard Productivity System Implementation Complete!"
```

## Rollback Procedures

### **Emergency Rollback (If Critical Issues)**
```bash
#!/bin/bash
# Emergency rollback script

echo "🚨 Emergency rollback initiated..."

# Find most recent backup
LATEST_BACKUP=$(ls -t ~/keyboard-backups/ | head -1)
echo "Rolling back to: $LATEST_BACKUP"

# Restore Karabiner
cp -r ~/keyboard-backups/$LATEST_BACKUP/karabiner-backup/* ~/.config/karabiner/
sudo launchctl kickstart -k system/com.pqrs.karabiner.karabiner_console_user_server

# Restore IdeaVim
cp ~/keyboard-backups/$LATEST_BACKUP/ideavimrc-backup ~/.ideavimrc

# Restore WebStorm keymap (manual step required)
echo "⚠️  Manual step: Restore WebStorm keymap through Settings → Keymap → Import"
echo "   Backup location: ~/keyboard-backups/$LATEST_BACKUP/webstorm-keymaps-backup/"

echo "✅ Emergency rollback complete. System restored to previous state."
```

### **Selective Rollback (Per System)**
```bash
#!/bin/bash
# Selective rollback script

echo "🔧 Selective rollback options:"
echo "1. Rollback Karabiner only"
echo "2. Rollback IdeaVim only" 
echo "3. Rollback WebStorm keymap only"
echo "4. Rollback all systems"

read -p "Choose option (1-4): " option

LATEST_BACKUP=$(ls -t ~/keyboard-backups/ | head -1)

case $option in
    1)
        echo "Rolling back Karabiner..."
        cp -r ~/keyboard-backups/$LATEST_BACKUP/karabiner-backup/* ~/.config/karabiner/
        sudo launchctl kickstart -k system/com.pqrs.karabiner.karabiner_console_user_server
        ;;
    2)
        echo "Rolling back IdeaVim..."
        cp ~/keyboard-backups/$LATEST_BACKUP/ideavimrc-backup ~/.ideavimrc
        ;;
    3)
        echo "Rolling back WebStorm keymap..."
        echo "Manual step: Settings → Keymap → Import from ~/keyboard-backups/$LATEST_BACKUP/webstorm-keymaps-backup/"
        ;;
    4)
        echo "Rolling back all systems..."
        # Full rollback procedure here
        ;;
esac

echo "✅ Selective rollback complete."
```

## Success Metrics

### **Performance Metrics**
- **Input Latency**: < 50ms perceived response time
- **CPU Usage**: Karabiner < 3% CPU usage
- **Memory Usage**: No significant increase in system memory
- **Reliability**: 99.9% shortcut success rate

### **Functionality Metrics**  
- **Coverage**: All planned shortcuts implemented and working
- **Integration**: Seamless operation between all three systems
- **Context Awareness**: Correct behavior in different applications
- **Conflict Resolution**: No shortcut conflicts or unexpected behavior

### **User Experience Metrics**
- **Muscle Memory Transfer**: Shortcuts feel consistent across contexts  
- **Productivity Gain**: Measurable improvement in development workflow speed
- **Learning Curve**: Minimal disruption during implementation
- **Satisfaction**: Enhanced development experience vs. previous setup

## Maintenance Schedule

### **Weekly Maintenance**
- [ ] Check Karabiner CPU/memory usage
- [ ] Verify all critical shortcuts still work
- [ ] Update backup if configuration changes made

### **Monthly Maintenance** 
- [ ] Full system functionality test
- [ ] Performance benchmark comparison
- [ ] Configuration optimization review
- [ ] Documentation updates if needed

### **Quarterly Maintenance**
- [ ] Complete system backup refresh
- [ ] Review new WebStorm features for integration
- [ ] Update IdeaVim configuration with new best practices
- [ ] Evaluate new Karabiner community rules

---

This implementation roadmap provides a safe, systematic approach to achieving the unified keyboard productivity system while maintaining the ability to rollback at any stage if issues arise.