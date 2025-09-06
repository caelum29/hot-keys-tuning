#!/usr/bin/env python3
"""
Export keyboard binding data to CSV format for spreadsheet analysis.

This script converts YAML binding data to CSV format, making it easy to:
- Analyze bindings in Excel/Google Sheets
- Filter and sort by different criteria
- Perform bulk edits
- Generate reports and statistics
"""

import yaml
import csv
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple

def load_yaml_data(file_path: Path) -> Dict[str, Any]:
    """Load and parse YAML data from file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def flatten_binding_data(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Convert hierarchical YAML binding data to flat CSV-ready format."""
    flat_data = []
    
    navigation_type = data['navigation_type']
    keys = ', '.join(data['keys'])
    
    for binding_key, binding in data['bindings'].items():
        details = binding['details']
        
        row = {
            'navigation_type': navigation_type,
            'keys': keys,
            'binding_key': binding_key,
            'modifier': binding_key.replace('_', ' ').title() if binding_key != 'none' else 'None',
            'keystroke': binding['keystroke'],
            'system': binding['system'],
            'status': binding['status'],
            'category': binding['category'],
            'action': binding['action'],
            'ide_action_id': details['ide_action_id'],
            'karabiner_code': details['karabiner_code'],
            'ideavim_command': details['ideavim_command'],
            'config_reference': details['config_reference'],
            'notes': details.get('notes', ''),  # Optional field
            # New optional fields
            'timing_ms': details.get('timing_ms', ''),
            'sequence_type': details.get('sequence_type', ''),
            'chord_keys': ', '.join(details.get('chord_keys', [])) if details.get('chord_keys') else '',
            'press_type': details.get('press_type', '')
        }
        
        flat_data.append(row)
    
    return flat_data

def generate_combined_csv(h_data: Dict[str, Any], v_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Combine horizontal and vertical binding data into single CSV dataset."""
    combined_data = []
    
    # Add horizontal navigation data
    combined_data.extend(flatten_binding_data(h_data))
    
    # Add vertical navigation data  
    combined_data.extend(flatten_binding_data(v_data))
    
    return combined_data

def write_csv(data: List[Dict[str, Any]], output_file: Path, delimiter: str = ','):
    """Write data to CSV file with proper formatting."""
    if not data:
        raise ValueError("No data to write")
    
    # Define column order for consistent output
    fieldnames = [
        'navigation_type',
        'keys', 
        'binding_key',
        'modifier',
        'keystroke',
        'system',
        'status',
        'category',
        'action',
        'ide_action_id',
        'karabiner_code',
        'ideavim_command',
        'config_reference',
        'notes',
        # New optional fields
        'timing_ms',
        'sequence_type',
        'chord_keys',
        'press_type'
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter)
        
        # Write header
        writer.writeheader()
        
        # Write data rows
        for row in data:
            writer.writerow(row)

def generate_summary_csv(data: List[Dict[str, Any]], output_file: Path):
    """Generate summary statistics CSV."""
    summary_data = []
    
    # Count by status
    status_counts = {}
    system_counts = {}
    category_counts = {}
    sequence_type_counts = {}
    timing_counts = {}
    press_type_counts = {}
    
    for row in data:
        status = row['status']
        system = row['system'] 
        category = row['category']
        sequence_type = row['sequence_type']
        timing_ms = row['timing_ms']
        press_type = row['press_type']
        
        status_counts[status] = status_counts.get(status, 0) + 1
        system_counts[system] = system_counts.get(system, 0) + 1
        category_counts[category] = category_counts.get(category, 0) + 1
        
        if sequence_type:
            sequence_type_counts[sequence_type] = sequence_type_counts.get(sequence_type, 0) + 1
        if timing_ms:
            timing_counts[timing_ms] = timing_counts.get(timing_ms, 0) + 1
        if press_type:
            press_type_counts[press_type] = press_type_counts.get(press_type, 0) + 1
    
    total = len(data)
    
    # Status summary
    for status, count in sorted(status_counts.items()):
        summary_data.append({
            'metric': 'Status',
            'value': status,
            'count': count,
            'percentage': round(count / total * 100, 1)
        })
    
    # System summary
    for system, count in sorted(system_counts.items()):
        summary_data.append({
            'metric': 'System',
            'value': system,
            'count': count,
            'percentage': round(count / total * 100, 1)
        })
    
    # Category summary
    for category, count in sorted(category_counts.items()):
        summary_data.append({
            'metric': 'Category',
            'value': category,
            'count': count,
            'percentage': round(count / total * 100, 1)
        })
    
    # Sequence type summary
    if sequence_type_counts:
        for seq_type, count in sorted(sequence_type_counts.items()):
            summary_data.append({
                'metric': 'Sequence Type',
                'value': seq_type,
                'count': count,
                'percentage': round(count / total * 100, 1)
            })
    
    # Timing summary
    if timing_counts:
        for timing, count in sorted(timing_counts.items()):
            summary_data.append({
                'metric': 'Timing (ms)',
                'value': str(timing),
                'count': count,
                'percentage': round(count / total * 100, 1)
            })
    
    # Press type summary
    if press_type_counts:
        for press_type, count in sorted(press_type_counts.items()):
            summary_data.append({
                'metric': 'Press Type',
                'value': press_type,
                'count': count,
                'percentage': round(count / total * 100, 1)
            })
    
    # Write summary CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['metric', 'value', 'count', 'percentage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in summary_data:
            writer.writerow(row)

def generate_pivot_ready_csv(data: List[Dict[str, Any]], output_file: Path):
    """Generate CSV optimized for pivot table analysis."""
    pivot_data = []
    
    for row in data:
        # Create separate rows for easier pivot analysis
        pivot_row = {
            'Navigation': row['navigation_type'].title(),
            'Keys': row['keys'],
            'Binding': row['modifier'],
            'System': row['system'],
            'Status': row['status'].title(),
            'Category': row['category'].title(),
            'HasIdeAction': 'Yes' if row['ide_action_id'] != 'Custom' and row['ide_action_id'] != '-' else 'No',
            'HasKarabiner': 'Yes' if row['karabiner_code'] != '-' else 'No', 
            'HasIdeaVim': 'Yes' if row['ideavim_command'] != '-' else 'No',
            'IsImplemented': 'Yes' if row['status'] == 'implemented' else 'No',
            'ConfigFile': row['config_reference'].split(':')[0] if ':' in row['config_reference'] else row['config_reference']
        }
        
        pivot_data.append(pivot_row)
    
    # Write pivot CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = list(pivot_data[0].keys()) if pivot_data else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in pivot_data:
            writer.writerow(row)

def main():
    """Main script execution."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Input files
    h_file = project_root / 'data' / 'horizontal-navigation.yaml'
    v_file = project_root / 'data' / 'vertical-navigation.yaml'
    
    # Output directory
    output_dir = project_root / 'generated'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Output files
    main_csv = output_dir / 'bindings.csv'
    summary_csv = output_dir / 'bindings-summary.csv'
    pivot_csv = output_dir / 'bindings-pivot.csv'
    tsv_file = output_dir / 'bindings.tsv'  # Tab-separated for different tools
    
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
        
        # Generate combined dataset
        print("Processing binding data...")
        combined_data = generate_combined_csv(h_data, v_data)
        
        # Generate main CSV
        print(f"Generating {main_csv}...")
        write_csv(combined_data, main_csv)
        
        # Generate TSV version
        print(f"Generating {tsv_file}...")
        write_csv(combined_data, tsv_file, delimiter='\t')
        
        # Generate summary CSV
        print(f"Generating {summary_csv}...")
        generate_summary_csv(combined_data, summary_csv)
        
        # Generate pivot-ready CSV
        print(f"Generating {pivot_csv}...")
        generate_pivot_ready_csv(combined_data, pivot_csv)
        
        print("\nExport Summary:")
        print(f"  Main CSV: {main_csv} ({len(combined_data)} rows)")
        print(f"  TSV: {tsv_file} ({len(combined_data)} rows)")
        print(f"  Summary: {summary_csv}")
        print(f"  Pivot: {pivot_csv}")
        print(f"  Total bindings: {len(combined_data)}")
        
        # Show quick stats
        status_counts = {}
        for row in combined_data:
            status = row['status']
            status_counts[status] = status_counts.get(status, 0) + 1
        
        print(f"  Status breakdown:")
        for status, count in sorted(status_counts.items()):
            print(f"    {status}: {count}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()