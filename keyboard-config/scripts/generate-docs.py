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

def format_table_row(binding_key: str, binding: Dict[str, Any]) -> str:
    """Format a single binding as a markdown table row."""
    details = binding['details']
    
    # Format each column with proper escaping
    modifier = binding_key.replace('_', ' ').title() if binding_key != 'none' else 'None'
    keystroke = binding['keystroke']
    system = binding['system']
    status = status_to_emoji(binding['status'])
    category = binding['category'].replace('_', ' ').title()
    action = binding['action']
    ide_action = f"`{details['ide_action_id']}`"
    karabiner = f"`{details['karabiner_code']}`"
    ideavim = f"`{details['ideavim_command']}`" if details['ideavim_command'] != '-' else '-'
    config_ref = details['config_reference']
    
    return f"| {modifier} | {keystroke} | {system} | {status} | {category} | {action} | {ide_action} | {karabiner} | {ideavim} | {config_ref} |"

def generate_navigation_table(data: Dict[str, Any]) -> List[str]:
    """Generate markdown table for navigation bindings."""
    lines = []
    
    # Table header
    lines.append("| Modifier | Keystroke | System | Status | Category | Action | IDE Action ID | Karabiner Code | IdeaVim Command | Config Reference |")
    lines.append("|----------|-----------|---------|---------|----------|---------|---------------|----------------|-----------------|------------------|")
    
    # Sort bindings for consistent output
    binding_order = [
        'none', 'shift', 'ctrl', 'alt', 'cmd',
        'shift_ctrl', 'shift_alt', 'shift_cmd', 'ctrl_alt', 'ctrl_cmd', 'alt_cmd',
        'shift_ctrl_alt', 'shift_ctrl_cmd', 'shift_alt_cmd', 'ctrl_alt_cmd',
        'shift_ctrl_alt_cmd',
        'hyper', 'hyper_shift', 'hyper_ctrl', 'hyper_alt', 'hyper_cmd',
        'g_prefix', 'change_camel', 'delete_camel', 'inner_camel', 'scroll_horizontal'
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
    
    for binding in all_bindings:
        status = binding['status']
        system = binding['system']
        category = binding['category']
        
        status_counts[status] = status_counts.get(status, 0) + 1
        system_counts[system] = system_counts.get(system, 0) + 1
        category_counts[category] = category_counts.get(category, 0) + 1
    
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

def main():
    """Main script execution."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Input files
    h_file = project_root / 'data' / 'horizontal-navigation.yaml'
    v_file = project_root / 'data' / 'vertical-navigation.yaml'
    
    # Output file
    output_file = project_root / 'generated' / 'KEY-MAP.md'
    
    # Ensure input files exist
    if not h_file.exists():
        print(f"Error: {h_file} not found", file=sys.stderr)
        sys.exit(1)
    if not v_file.exists():
        print(f"Error: {v_file} not found", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Load YAML data
        print(f"Loading {h_file}...")
        h_data = load_yaml_data(h_file)
        
        print(f"Loading {v_file}...")  
        v_data = load_yaml_data(v_file)
        
        # Generate markdown
        print("Generating markdown documentation...")
        markdown = generate_full_markdown(h_data, v_data)
        
        # Ensure output directory exists
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"Generated: {output_file}")
        print(f"Total bindings processed: {len(h_data['bindings']) + len(v_data['bindings'])}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()