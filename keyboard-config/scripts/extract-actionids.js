#!/usr/bin/env node

/**
 * Generic ActionID Extractor for IntelliJ/WebStorm Keymaps
 *
 * Extracts ActionIDs from keymap XML files based on specified keys and modifiers.
 * Supports multiple output formats (Markdown, CSV, JSON) and keymap comparison.
 *
 * Usage:
 *   node extract-actionids.js --keys H,J,K,L --file $default.xml
 *   node extract-actionids.js --keys UP,DOWN --modifier ctrl --format csv
 */

const fs = require('fs');
const path = require('path');
const { XMLParser } = require('fast-xml-parser');

// Parse command line arguments
function parseArgs() {
  const args = process.argv.slice(2);
  const config = {
    keys: [],
    modifiers: [],
    files: [],
    format: 'markdown',
    compare: false,
    output: null,
  };

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case '--keys':
      case '-k':
        config.keys = args[++i].split(',').map(k => k.trim().toUpperCase());
        break;
      case '--modifier':
      case '-m':
        config.modifiers = args[++i].split(',').map(m => m.trim().toLowerCase());
        break;
      case '--file':
      case '-f':
        config.files = args[++i].split(',').map(f => f.trim());
        break;
      case '--format':
        config.format = args[++i].toLowerCase();
        break;
      case '--compare':
      case '-c':
        config.compare = true;
        break;
      case '--output':
      case '-o':
        config.output = args[++i];
        break;
      case '--help':
      case '-h':
        showHelp();
        process.exit(0);
      default:
        // Assume it's a file if no flag
        if (!args[i].startsWith('--') && !args[i].startsWith('-')) {
          config.files.push(args[i]);
        }
    }
  }

  return config;
}

function showHelp() {
  console.log(`
Generic ActionID Extractor for IntelliJ/WebStorm Keymaps

Usage:
  extract-actionids.js [options]

Options:
  --keys, -k <keys>          Comma-separated list of keys to search (e.g., H,J,K,L or UP,DOWN,LEFT,RIGHT)
  --modifier, -m <mods>      Filter by modifiers: ctrl, shift, alt, meta (comma-separated)
  --file, -f <files>         Keymap XML file(s) to parse (comma-separated for comparison)
  --format <format>          Output format: markdown, csv, json (default: markdown)
  --compare, -c              Compare bindings across multiple files
  --output, -o <file>        Output file path (default: stdout)
  --help, -h                 Show this help message

Examples:
  # Extract arrow keys from default keymap
  extract-actionids.js --keys UP,DOWN,LEFT,RIGHT --file $default.xml

  # Extract HJKL with ctrl modifier
  extract-actionids.js --keys H,J,K,L --modifier ctrl --file $default.xml

  # Extract and compare across multiple keymaps
  extract-actionids.js --keys H,J,K,L --file "$default.xml,Mac OS X 10.5+.xml" --compare

  # Export to CSV
  extract-actionids.js --keys A,B,C --modifier "ctrl,shift" --format csv --output bindings.csv
`);
}

// Parse XML keymap file
function parseKeymapFile(filePath) {
  const parser = new XMLParser({
    ignoreAttributes: false,
    attributeNamePrefix: '@_',
  });

  const xmlContent = fs.readFileSync(filePath, 'utf8');
  const result = parser.parse(xmlContent);

  return result.keymap || {};
}

// Extract bindings for specified keys
function extractBindings(keymap, keys, modifiers) {
  const bindings = [];
  const actions = Array.isArray(keymap.action) ? keymap.action : [keymap.action];

  actions.forEach(action => {
    if (!action || !action['@_id']) return;

    const shortcuts = action['keyboard-shortcut'];
    if (!shortcuts) return;

    const shortcutArray = Array.isArray(shortcuts) ? shortcuts : [shortcuts];

    shortcutArray.forEach(shortcut => {
      if (!shortcut || !shortcut['@_first-keystroke']) return;

      const keystroke = shortcut['@_first-keystroke'];
      const keystrokeParts = keystroke.split(' ');
      const key = keystrokeParts[keystrokeParts.length - 1];

      // Check if this keystroke matches any of our target keys
      if (keys.length === 0 || keys.includes(key.toUpperCase())) {
        // Extract modifiers from keystroke
        const keystrokeModifiers = keystrokeParts.slice(0, -1).map(m => m.toLowerCase());

        // Filter by modifiers if specified
        if (modifiers.length > 0) {
          const hasAllModifiers = modifiers.every(mod =>
            keystrokeModifiers.includes(mod) ||
            (mod === 'meta' && keystrokeModifiers.includes('cmd'))
          );

          if (!hasAllModifiers) return;
        }

        bindings.push({
          actionId: action['@_id'],
          keystroke: keystroke,
          key: key.toUpperCase(),
          modifiers: keystrokeModifiers,
        });
      }
    });
  });

  return bindings;
}

// Format output as Markdown table
function formatMarkdown(bindings, groupByKey = true) {
  if (bindings.length === 0) {
    return 'No bindings found for the specified keys and modifiers.';
  }

  let output = '';

  if (groupByKey) {
    // Group by key
    const grouped = {};
    bindings.forEach(b => {
      if (!grouped[b.key]) grouped[b.key] = [];
      grouped[b.key].push(b);
    });

    Object.keys(grouped).sort().forEach(key => {
      output += `\n### ${key} Key (${grouped[key].length} bindings)\n\n`;
      output += '| ActionID | Keystroke | Modifiers |\n';
      output += '|----------|-----------|----------|\n';

      grouped[key].forEach(b => {
        const mods = b.modifiers.length > 0 ? b.modifiers.join(', ') : 'none';
        output += `| \`${b.actionId}\` | \`${b.keystroke}\` | ${mods} |\n`;
      });
    });
  } else {
    output += '| ActionID | Keystroke | Key | Modifiers |\n';
    output += '|----------|-----------|-----|----------|\n';

    bindings.forEach(b => {
      const mods = b.modifiers.length > 0 ? b.modifiers.join(', ') : 'none';
      output += `| \`${b.actionId}\` | \`${b.keystroke}\` | ${b.key} | ${mods} |\n`;
    });
  }

  return output;
}

// Format output as CSV
function formatCSV(bindings) {
  let output = 'ActionID,Keystroke,Key,Modifiers\n';

  bindings.forEach(b => {
    const mods = b.modifiers.join(';');
    output += `"${b.actionId}","${b.keystroke}","${b.key}","${mods}"\n`;
  });

  return output;
}

// Format output as JSON
function formatJSON(bindings) {
  return JSON.stringify(bindings, null, 2);
}

// Compare bindings across multiple keymaps
function compareKeymaps(fileBindings) {
  const allActionIds = new Set();

  Object.values(fileBindings).forEach(bindings => {
    bindings.forEach(b => allActionIds.add(b.actionId));
  });

  const comparison = [];

  allActionIds.forEach(actionId => {
    const row = { actionId };

    Object.entries(fileBindings).forEach(([file, bindings]) => {
      const binding = bindings.find(b => b.actionId === actionId);
      row[file] = binding ? binding.keystroke : '—';
    });

    comparison.push(row);
  });

  return comparison;
}

// Format comparison as Markdown
function formatComparisonMarkdown(comparison, files) {
  let output = '# Keymap Comparison\n\n';
  output += '| ActionID | ' + files.map(f => path.basename(f)).join(' | ') + ' |\n';
  output += '|----------|' + files.map(() => '----------').join('|') + '|\n';

  comparison.forEach(row => {
    output += `| \`${row.actionId}\` |`;
    files.forEach(file => {
      output += ` ${row[file]} |`;
    });
    output += '\n';
  });

  return output;
}

// Main execution
function main() {
  const config = parseArgs();

  if (config.files.length === 0) {
    console.error('Error: No keymap files specified. Use --file or -f flag.');
    console.error('Run with --help for usage information.');
    process.exit(1);
  }

  // Resolve file paths
  const baseDir = path.join(__dirname, '../../configs/webstorm/examples-from-the-web');
  const resolvedFiles = config.files.map(f => {
    if (path.isAbsolute(f)) return f;
    if (fs.existsSync(f)) return f;

    const tryPath = path.join(baseDir, f);
    if (fs.existsSync(tryPath)) return tryPath;

    console.error(`Error: File not found: ${f}`);
    process.exit(1);
  });

  console.error(`Searching for keys: ${config.keys.length > 0 ? config.keys.join(', ') : 'ALL'}`);
  if (config.modifiers.length > 0) {
    console.error(`Filtering by modifiers: ${config.modifiers.join(', ')}`);
  }
  console.error('');

  // Extract bindings from all files
  const fileBindings = {};
  resolvedFiles.forEach(file => {
    console.error(`Parsing: ${path.basename(file)}`);
    const keymap = parseKeymapFile(file);
    fileBindings[file] = extractBindings(keymap, config.keys, config.modifiers);
    console.error(`  Found ${fileBindings[file].length} bindings`);
  });
  console.error('');

  // Generate output
  let output;

  if (config.compare && resolvedFiles.length > 1) {
    const comparison = compareKeymaps(fileBindings);

    switch (config.format) {
      case 'markdown':
      case 'md':
        output = formatComparisonMarkdown(comparison, resolvedFiles);
        break;
      case 'json':
        output = JSON.stringify(comparison, null, 2);
        break;
      case 'csv':
        output = 'ActionID,' + resolvedFiles.map(f => path.basename(f)).join(',') + '\n';
        comparison.forEach(row => {
          output += `"${row.actionId}",` + resolvedFiles.map(f => `"${row[f]}"`).join(',') + '\n';
        });
        break;
      default:
        output = formatComparisonMarkdown(comparison, resolvedFiles);
    }
  } else {
    // Single file or merged output
    const allBindings = Object.values(fileBindings).flat();

    switch (config.format) {
      case 'markdown':
      case 'md':
        output = formatMarkdown(allBindings);
        break;
      case 'csv':
        output = formatCSV(allBindings);
        break;
      case 'json':
        output = formatJSON(allBindings);
        break;
      default:
        output = formatMarkdown(allBindings);
    }
  }

  // Write output
  if (config.output) {
    fs.writeFileSync(config.output, output);
    console.error(`Output written to: ${config.output}`);
  } else {
    console.log(output);
  }
}

// Run if called directly
if (require.main === module) {
  main();
}

module.exports = { parseKeymapFile, extractBindings, formatMarkdown, formatCSV, formatJSON };
