#!/usr/bin/env python3
"""
Generate comprehensive markdown documentation from YAML keyboard binding data.

This script converts the structured YAML binding data into formatted markdown tables
that are both human-readable and LLM-friendly.
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, List, Any

def load_yaml_data(file_path: Path) -> Dict[str, Any]:
    """Load and parse YAML data from file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def status_to_emoji(status: str) -> str:
    """Convert status string to emoji representation."""
    status_map = {
        'implemented': '✅',
        'planned': '📋', 
        'needs_attention': '⚠️',
        'disabled': '❌',
        'conflict': '⚡'
    }
    return status_map.get(status, '❓')

def category_to_emoji(category: str) -> str:
    """Convert category string to emoji representation."""
    category_map = {
        'timing': '⏱️',
        'chord': '🎹',
        'leader': '👑',
        'sequence': '🔗',
        'navigation': '🧭',
        'selection': '✏️',
        'text_edit': '📝',
        'window': '🪟',
        'desktop': '🖥️',
        'action': '⚙️',
        'custom': '🎛️',
        'mouse': '🖱️'
    }
    return category_map.get(category, '📂')

def format_table_row(binding_key: str, binding: Dict[str, Any]) -> str:
    """Format a single binding as a markdown table row."""
    details = binding['details']
    
    # Format each column with proper escaping
    modifier = binding_key.replace('_', ' ').title() if binding_key != 'none' else 'None'
    keystroke = binding['keystroke']
    system = binding['system']
    status = status_to_emoji(binding['status'])
    category = binding['category'].replace('_', ' ').title()
    category_icon = category_to_emoji(binding['category'])
    action = binding['action']
    ide_action = f"`{details['ide_action_id']}`"
    karabiner = f"`{details['karabiner_code']}`"
    ideavim = f"`{details['ideavim_command']}`" if details['ideavim_command'] != '-' else '-'
    config_ref = details['config_reference']
    
    # Add optional field indicators
    optional_info = []
    if 'timing_ms' in details:
        optional_info.append(f"⏱️{details['timing_ms']}ms")
    if 'sequence_type' in details:
        optional_info.append(f"🔗{details['sequence_type']}")
    if 'chord_keys' in details and details['chord_keys']:
        chord_str = '+'.join(details['chord_keys'])
        optional_info.append(f"🎹{chord_str}")
    if 'press_type' in details:
        optional_info.append(f"👆{details['press_type']}")
    
    optional_suffix = f" {' '.join(optional_info)}" if optional_info else ""
    
    return f"| {modifier} | {keystroke} | {system} | {status} | {category_icon} {category} | {action}{optional_suffix} | {ide_action} | {karabiner} | {ideavim} | {config_ref} |"

def generate_navigation_table(data: Dict[str, Any]) -> List[str]:
    """Generate markdown table for navigation bindings."""
    lines = []
    
    # Table header
    lines.append("| Modifier | Keystroke | System | Status | Category | Action | **IDE Action ID** | Karabiner Code | IdeaVim Command | Config Reference |")
    lines.append("|----------|-----------|---------|---------|----------|---------|-------------------|----------------|-----------------|------------------|")
    
    # Sort bindings for consistent output
    binding_order = [
        # Standard modifier combinations
        'none', 'shift', 'ctrl', 'alt', 'cmd',
        'shift_ctrl', 'shift_alt', 'shift_cmd', 'ctrl_alt', 'ctrl_cmd', 'alt_cmd',
        'shift_ctrl_alt', 'shift_ctrl_cmd', 'shift_alt_cmd', 'ctrl_alt_cmd',
        'shift_ctrl_alt_cmd',
        # Hyper key combinations
        'hyper', 'hyper_shift', 'hyper_ctrl', 'hyper_alt', 'hyper_cmd',
        # Double tap combinations
        'double_tap', 'shift_double_tap', 'ctrl_double_tap', 'alt_double_tap', 'cmd_double_tap',
        # Leader key sequences
        'leader', 'leader_shift', 'leader_ctrl', 'leader_alt', 'leader_cmd', 'double_leader',
        # Long press variations
        'long_press', 'tap_hold',
        # Chord combinations
        'chord_vertical', 'chord_horizontal', 'chord_mouse', 'chord_scroll',
        # Vim-specific bindings
        'g_prefix', 'change_camel', 'delete_camel', 'inner_camel', 'scroll_horizontal', 'scroll_vertical',
        # Additional Vim sequences
        'yank_horizontal', 'yank_vertical', 'visual_horizontal', 'visual_vertical',
        'mark_horizontal', 'mark_vertical', 'jump_mark', 'jump_mark_vertical',
        'register_horizontal', 'register_vertical', 'backslash_leader', 'backslash_leader_vertical',
        'bracket_prev', 'bracket_next'
    ]
    
    # Add bindings in order, then any remaining ones
    added_keys = set()
    for key in binding_order:
        if key in data['bindings']:
            lines.append(format_table_row(key, data['bindings'][key]))
            added_keys.add(key)
    
    # Add any remaining bindings not in the predefined order
    for key in sorted(data['bindings'].keys()):
        if key not in added_keys:
            lines.append(format_table_row(key, data['bindings'][key]))
    
    return lines

def generate_summary_stats(h_data: Dict[str, Any], v_data: Dict[str, Any]) -> List[str]:
    """Generate summary statistics section."""
    lines = []
    
    # Count bindings by status
    all_bindings = list(h_data['bindings'].values()) + list(v_data['bindings'].values())
    status_counts = {}
    system_counts = {}
    category_counts = {}
    
    sequence_type_counts = {}
    timing_bindings = []
    chord_bindings = []
    
    for binding in all_bindings:
        status = binding['status']
        system = binding['system']
        category = binding['category']
        details = binding['details']
        
        status_counts[status] = status_counts.get(status, 0) + 1
        system_counts[system] = system_counts.get(system, 0) + 1
        category_counts[category] = category_counts.get(category, 0) + 1
        
        # Count new binding types
        if 'sequence_type' in details:
            seq_type = details['sequence_type']
            sequence_type_counts[seq_type] = sequence_type_counts.get(seq_type, 0) + 1
            
        if 'timing_ms' in details:
            timing_bindings.append(binding)
            
        if 'chord_keys' in details and details['chord_keys']:
            chord_bindings.append(binding)
    
    lines.append("## Implementation Summary")
    lines.append("")
    
    # Status breakdown
    lines.append("### Status Overview")
    lines.append("| Status | Count | Percentage |")
    lines.append("|--------|-------|------------|")
    
    total = len(all_bindings)
    for status, count in sorted(status_counts.items()):
        emoji = status_to_emoji(status)
        percentage = round(count / total * 100, 1)
        lines.append(f"| {emoji} {status.title()} | {count} | {percentage}% |")
    
    lines.append("")
    
    # System breakdown
    lines.append("### System Distribution")
    lines.append("| System | Count | Description |")
    lines.append("|--------|-------|-------------|")
    
    system_names = {
        'I': 'IdeaVim only',
        'W': 'WebStorm only', 
        'K': 'Karabiner only',
        'W+I': 'WebStorm + IdeaVim',
        'K+W': 'Karabiner + WebStorm',
        'K+I': 'Karabiner + IdeaVim',
        'K+W+I': 'All systems',
        '-': 'Not implemented'
    }
    
    for system, count in sorted(system_counts.items()):
        desc = system_names.get(system, 'Unknown')
        lines.append(f"| {system} | {count} | {desc} |")
    
    # Add new binding type statistics
    if sequence_type_counts:
        lines.append("")
        lines.append("### Sequence Types")
        lines.append("| Type | Count | Description |")
        lines.append("|------|-------|-------------|")
        
        type_descriptions = {
            'double_tap': 'Double key press within timeout',
            'long_press': 'Hold key for extended period',
            'tap_hold': 'Different actions for tap vs hold',
            'leader': 'Leader key prefix sequences',
            'vim_prefix': 'Vim-style prefix commands',
            'text_object': 'Vim text object operations',
            'chord': 'Multiple keys pressed together'
        }
        
        for seq_type, count in sorted(sequence_type_counts.items()):
            desc = type_descriptions.get(seq_type, 'Custom sequence type')
            lines.append(f"| {seq_type} | {count} | {desc} |")
    
    if timing_bindings:
        lines.append("")
        lines.append("### Timing-Based Bindings")
        lines.append(f"**{len(timing_bindings)} bindings** use timing patterns:")
        timing_stats = {}
        for binding in timing_bindings:
            timing = binding['details']['timing_ms']
            timing_stats[timing] = timing_stats.get(timing, 0) + 1
        
        for timing, count in sorted(timing_stats.items()):
            lines.append(f"- {timing}ms timeout: {count} bindings")
    
    if chord_bindings:
        lines.append("")
        lines.append("### Chord Combinations")
        lines.append(f"**{len(chord_bindings)} bindings** use chord patterns:")
        chord_stats = {}
        for binding in chord_bindings:
            chord_keys = '+'.join(binding['details']['chord_keys'])
            chord_stats[chord_keys] = chord_stats.get(chord_keys, 0) + 1
        
        for chord, count in sorted(chord_stats.items()):
            lines.append(f"- {chord}: {count} bindings")

    lines.append("")
    return lines

def generate_full_markdown(h_data: Dict[str, Any], v_data: Dict[str, Any]) -> str:
    """Generate complete markdown document."""
    lines = []
    
    # Header
    lines.extend([
        "# Keyboard Navigation Configuration",
        "",
        "Generated from YAML configuration data. **DO NOT EDIT MANUALLY** - changes will be overwritten.",
        "",
        "This document provides comprehensive keyboard binding documentation for the unified productivity system.",
        "",
        "- For **horizontal navigation**, **H** corresponds to moving left and **L** corresponds to moving right.",
        "- For **vertical navigation**, **J** corresponds to moving down and **K** corresponds to moving up.",
        "",
        "## Legend",
        "",
        "### Systems",
        "- **I**: IdeaVim (editor-level vim emulation)",
        "- **W**: WebStorm (IDE-level keymaps)", 
        "- **K**: Karabiner Elements (system-wide key modifications)",
        "- Combinations indicate multi-system bindings",
        "",
        "### Status Icons",
        "- ✅ **Implemented**: Fully configured and working",
        "- 📋 **Planned**: Identified for future implementation",
        "- ⚠️ **Needs Attention**: Requires fixes or remapping",
        "- ❌ **Disabled**: Intentionally disabled",
        "- ⚡ **Conflict**: Conflicts with other bindings",
        "",
        "### Category Icons",
        "- ⏱️ **Timing**: Double tap, long press, tap/hold patterns",
        "- 🎹 **Chord**: Multiple keys pressed simultaneously",
        "- 👑 **Leader**: Leader key prefix sequences",
        "- 🔗 **Sequence**: Multi-step key sequences",
        "- 🧭 **Navigation**: Movement and positioning",
        "- ✏️ **Selection**: Text and object selection",
        "- 📝 **Text Edit**: Text manipulation and editing",
        "- 🪟 **Window**: Window and pane management",
        "- 🖥️ **Desktop**: Desktop and workspace control",
        "- ⚙️ **Action**: IDE actions and commands",
        "- 🎛️ **Custom**: Custom or unspecified actions",
        "- 🖱️ **Mouse**: Mouse-related operations",
        "",
        "### Field Indicators",
        "- ⏱️500ms: Timing window (double tap/long press)",
        "- 🔗double_tap: Sequence type",
        "- 🎹H+J: Chord keys combination",
        "- 👆hold: Press type requirement",
        "",
        "---",
        ""
    ])
    
    # Summary stats
    lines.extend(generate_summary_stats(h_data, v_data))
    
    # Horizontal navigation table
    lines.extend([
        "## Horizontal Navigation Key Bindings (H / L)",
        "",
        f"**Navigation Type**: {h_data['navigation_type'].title()}  ",
        f"**Keys**: {', '.join(h_data['keys'])}  ",
        f"**Description**: {h_data['description']}",
        ""
    ])
    lines.extend(generate_navigation_table(h_data))
    lines.append("")
    
    # Vertical navigation table  
    lines.extend([
        "## Vertical Navigation Key Bindings (J / K)",
        "",
        f"**Navigation Type**: {v_data['navigation_type'].title()}  ",
        f"**Keys**: {', '.join(v_data['keys'])}  ", 
        f"**Description**: {v_data['description']}",
        ""
    ])
    lines.extend(generate_navigation_table(v_data))
    lines.extend([
        "",
        "---",
        "",
        "*Generated automatically from YAML configuration data.*",
        f"*Source files: `horizontal-navigation.yaml`, `vertical-navigation.yaml`*"
    ])
    
    return '\n'.join(lines)

def generate_multi_config_markdown(all_data: List[Dict[str, Any]]) -> str:
    """Generate markdown document for multiple configuration files."""
    lines = []
    
    # Header
    lines.extend([
        "# Keyboard Configuration System",
        "",
        "Generated from YAML configuration data. **DO NOT EDIT MANUALLY** - changes will be overwritten.",
        "",
        "This document provides comprehensive keyboard binding documentation for all configured keys in the unified productivity system.",
        "",
        "## Legend",
        "",
        "### Systems",
        "- **I**: IdeaVim (editor-level vim emulation)",
        "- **W**: WebStorm (IDE-level keymaps)", 
        "- **K**: Karabiner Elements (system-wide key modifications)",
        "- Combinations indicate multi-system bindings",
        "",
        "### Status Icons",
        "- ✅ **Implemented**: Fully configured and working",
        "- 📋 **Planned**: Identified for future implementation",
        "- ⚠️ **Needs Attention**: Requires fixes or remapping",
        "- ❌ **Disabled**: Intentionally disabled",
        "- ⚡ **Conflict**: Conflicts with other bindings",
        "",
        "### Category Icons",
        "- ⏱️ **Timing**: Double tap, long press, tap/hold patterns",
        "- 🎹 **Chord**: Multiple keys pressed simultaneously",
        "- 👑 **Leader**: Leader key prefix sequences",
        "- 🔗 **Sequence**: Multi-step key sequences",
        "- 🧭 **Navigation**: Movement and positioning",
        "- ✏️ **Selection**: Text and object selection",
        "- 📝 **Text Edit**: Text manipulation and editing",
        "- 🪟 **Window**: Window and pane management",
        "- 🖥️ **Desktop**: Desktop and workspace control",
        "- ⚙️ **Action**: IDE actions and commands",
        "- 🎛️ **Custom**: Custom or unspecified actions",
        "- 🖱️ **Mouse**: Mouse-related operations",
        "",
        "### Field Indicators",
        "- ⏱️500ms: Timing window (double tap/long press)",
        "- 🔗double_tap: Sequence type",
        "- 🎹H+J: Chord keys combination",
        "- 👆hold: Press type requirement",
        "",
        "---",
        ""
    ])
    
    # Generate overall summary statistics
    lines.extend(generate_multi_config_summary_stats(all_data))
    
    # Generate section for each configuration
    source_files = []
    for data in all_data:
        nav_type = data['navigation_type']
        keys_str = ', '.join(data['keys'])
        
        # Create friendly section title based on navigation type and keys
        if nav_type == 'horizontal':
            section_title = f"Horizontal Navigation Key Bindings ({keys_str})"
        elif nav_type == 'vertical':
            section_title = f"Vertical Navigation Key Bindings ({keys_str})"
        elif nav_type == 'bracket':
            section_title = f"Bracket Navigation Key Bindings ({keys_str})"
        elif nav_type == 'individual':
            section_title = f"Individual Key Bindings ({keys_str})"
        else:
            section_title = f"{nav_type.title()} Key Bindings ({keys_str})"
        
        lines.extend([
            f"## {section_title}",
            "",
            f"**Navigation Type**: {nav_type.title()}  ",
            f"**Keys**: {keys_str}  ",
            f"**Description**: {data['description']}",
            ""
        ])
        lines.extend(generate_navigation_table(data))
        lines.append("")
        
        # Track source file names for footer
        source_files.append(f"{nav_type}-navigation.yaml")
    
    lines.extend([
        "---",
        "",
        "*Generated automatically from YAML configuration data.*",
        f"*Source files: {', '.join(f'`{f}`' for f in source_files)}*"
    ])
    
    return '\n'.join(lines)

def generate_multi_config_summary_stats(all_data: List[Dict[str, Any]]) -> List[str]:
    """Generate summary statistics for multiple configuration files."""
    lines = []
    
    # Collect all bindings
    all_bindings = []
    config_counts = {}
    navigation_type_counts = {}
    
    for data in all_data:
        nav_type = data['navigation_type']
        bindings = list(data['bindings'].values())
        all_bindings.extend(bindings)
        config_counts[nav_type] = len(bindings)
        navigation_type_counts[nav_type] = navigation_type_counts.get(nav_type, 0) + 1
    
    # Count bindings by status, system, category
    status_counts = {}
    system_counts = {}
    category_counts = {}
    sequence_type_counts = {}
    timing_bindings = []
    chord_bindings = []
    
    for binding in all_bindings:
        status = binding['status']
        system = binding['system']
        category = binding['category']
        details = binding['details']
        
        status_counts[status] = status_counts.get(status, 0) + 1
        system_counts[system] = system_counts.get(system, 0) + 1
        category_counts[category] = category_counts.get(category, 0) + 1
        
        if 'sequence_type' in details:
            seq_type = details['sequence_type']
            sequence_type_counts[seq_type] = sequence_type_counts.get(seq_type, 0) + 1
            
        if 'timing_ms' in details:
            timing_bindings.append(binding)
            
        if 'chord_keys' in details and details['chord_keys']:
            chord_bindings.append(binding)
    
    lines.append("## Implementation Summary")
    lines.append("")
    
    # Configuration overview
    lines.append("### Configuration Overview")
    lines.append("| Navigation Type | Bindings | Description |")
    lines.append("|----------------|----------|-------------|")
    
    type_descriptions = {
        'horizontal': 'Left/right navigation (H/L keys)',
        'vertical': 'Up/down navigation (J/K keys)', 
        'bracket': 'Previous/next navigation with brackets',
        'individual': 'Single key bindings',
        'custom': 'Custom key pair combinations',
        'pair': 'Two-key combinations'
    }
    
    for nav_type, count in sorted(config_counts.items()):
        desc = type_descriptions.get(nav_type, 'Custom navigation type')
        lines.append(f"| {nav_type.title()} | {count} | {desc} |")
    
    lines.append("")
    
    # Status breakdown
    lines.append("### Status Overview")
    lines.append("| Status | Count | Percentage |")
    lines.append("|--------|-------|------------|")
    
    total = len(all_bindings)
    for status, count in sorted(status_counts.items()):
        emoji = status_to_emoji(status)
        percentage = round(count / total * 100, 1)
        lines.append(f"| {emoji} {status.title()} | {count} | {percentage}% |")
    
    lines.append("")
    
    # System breakdown
    lines.append("### System Distribution")
    lines.append("| System | Count | Description |")
    lines.append("|--------|-------|-------------|")
    
    system_names = {
        'I': 'IdeaVim only',
        'W': 'WebStorm only', 
        'K': 'Karabiner only',
        'W+I': 'WebStorm + IdeaVim',
        'K+W': 'Karabiner + WebStorm',
        'K+I': 'Karabiner + IdeaVim',
        'K+W+I': 'All systems',
        '-': 'Not implemented'
    }
    
    for system, count in sorted(system_counts.items()):
        desc = system_names.get(system, 'Unknown')
        lines.append(f"| {system} | {count} | {desc} |")
    
    # Additional statistics similar to the original function
    if sequence_type_counts:
        lines.append("")
        lines.append("### Sequence Types")
        lines.append("| Type | Count | Description |")
        lines.append("|------|-------|-------------|")
        
        type_descriptions = {
            'double_tap': 'Double key press within timeout',
            'long_press': 'Hold key for extended period',
            'tap_hold': 'Different actions for tap vs hold',
            'leader': 'Leader key prefix sequences',
            'vim_prefix': 'Vim-style prefix commands',
            'text_object': 'Vim text object operations',
            'chord': 'Multiple keys pressed together'
        }
        
        for seq_type, count in sorted(sequence_type_counts.items()):
            desc = type_descriptions.get(seq_type, 'Custom sequence type')
            lines.append(f"| {seq_type} | {count} | {desc} |")

    lines.append("")
    return lines

def discover_yaml_files(data_dir: Path) -> List[Path]:
    """Discover all YAML configuration files in the data directory."""
    yaml_files = []
    for file_path in data_dir.glob('*.yaml'):
        # Skip schema files
        if 'schema' not in file_path.name.lower():
            yaml_files.append(file_path)
    return sorted(yaml_files)

def main():
    """Main script execution."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    data_dir = project_root / 'data'
    
    # Output file
    output_file = project_root / 'generated' / 'KEY-MAP.md'
    
    # Discover all YAML files
    yaml_files = discover_yaml_files(data_dir)
    
    if not yaml_files:
        print(f"Error: No YAML configuration files found in {data_dir}", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Load all YAML data
        all_data = []
        total_bindings = 0
        
        for yaml_file in yaml_files:
            print(f"Loading {yaml_file}...")
            data = load_yaml_data(yaml_file)
            all_data.append(data)
            total_bindings += len(data['bindings'])
        
        # Generate markdown
        print("Generating markdown documentation...")
        markdown = generate_multi_config_markdown(all_data)
        
        # Ensure output directory exists
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"Generated: {output_file}")
        print(f"Total configuration files processed: {len(all_data)}")
        print(f"Total bindings processed: {total_bindings}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()