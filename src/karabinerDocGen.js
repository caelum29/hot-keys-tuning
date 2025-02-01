#!/usr/bin/env node
/**
 * karabinerDocGen.js
 *
 * This script reads a Karabiner‑Elements configuration JSON file and generates
 * Markdown documentation describing its contents. It also accepts an optional
 * filter for key definitions by key_code.
 *
 * Usage:
 *   node karabinerDocGen.js path/to/karabiner.json [filterKeyCode]
 *
 * Example:
 *   node karabinerDocGen.js ./karabiner.json spacebar
 */

const fs = require('fs');
const path = require('path');

// Key mapper to substitute key_code strings (e.g., "comma" becomes ",")
const keyMapper = {
  comma: ',',
  // Add additional mappings as needed:
  period: '.',
  semicolon: ';',
  left_arrow: '<-',
  left_command: '⌘',
  left_control: '⌃',
  left_shift: '  ⇧ ',
  left_option: '⌥'
  // etc.
};

const hyperModifiers = ['right_command', 'right_control', 'right_shift', 'right_option'];

/**
 * Substitutes a key code using the keyMapper and returns the key wrapped in <kbd> tags.
 *
 * @param {string} keyCode - The original key code.
 * @returns {string} - The substituted key wrapped in <kbd>...</kbd>.
 */
function substituteKeyCode(keyCode) {
  let displayKey = keyCode;
  if (keyMapper[displayKey]) {
    displayKey = keyMapper[displayKey];
  }
  return `<kbd>${displayKey}</kbd>`;
}

// Check command-line arguments
if (process.argv.length < 3) {
  console.error('Usage: node karabinerDocGen.js <path to karabiner.json> [filterKeyCode]');
  process.exit(1);
}

const inputPath = process.argv[2];
// Optional filter: a key_code to filter by (e.g., "spacebar")
const filterKeyCode = process.argv[3] || null;

// Read the Karabiner JSON file
fs.readFile(inputPath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    process.exit(1);
  }

  let karabinerData;
  try {
    karabinerData = JSON.parse(data);
  } catch (parseErr) {
    console.error('Error parsing JSON:', parseErr);
    process.exit(1);
  }

  // Generate the Markdown documentation
  const markdown = generateMarkdown(karabinerData, filterKeyCode);

  // Write the Markdown to an output file in the current directory
  const outputPath = path.join(process.cwd(), 'karabiner_documentation.md');
  fs.writeFile(outputPath, markdown, (err) => {
    if (err) {
      console.error('Error writing markdown file:', err);
      process.exit(1);
    }
    console.log('Markdown documentation generated:', outputPath);
  });
});

/**
 * Generates Markdown documentation from the Karabiner JSON data.
 *
 * @param {Object} data - The parsed Karabiner JSON data.
 * @param {string|null} filterKey - Optional key_code filter.
 * @returns {string} - The generated Markdown string.
 */
function generateMarkdown(data, filterKey) {
  let md = `# Karabiner‑Elements Configuration Documentation\n\n`;
  md += `**Generated on:** ${new Date().toLocaleString()}\n\n`;
  if (filterKey) {
    md += `**Filter applied:** Only manipulators matching key_code \`${filterKey}\` are included.\n\n`;
  }

  if (data.profiles && Array.isArray(data.profiles)) {
    data.profiles.forEach((profile, profileIndex) => {
      md += `## Profile ${profileIndex + 1}: ${profile.name || 'Unnamed Profile'}\n\n`;

      // Simple modifications
      if (profile.simple_modifications && Object.keys(profile.simple_modifications).length > 0) {
        md += `### Simple Modifications\n\n`;
        md += `| From Key | To Key |\n| --- | --- |\n`;
        Object.entries(profile.simple_modifications).forEach(([fromKey, toKey]) => {
          md += `| ${fromKey} | ${toKey} |\n`;
        });
        md += `\n`;
      }

      // Complex modifications (rules)
      if (profile.complex_modifications && profile.complex_modifications.rules && profile.complex_modifications.rules.length > 0) {
        md += `### Complex Modifications\n\n`;
        profile.complex_modifications.rules.forEach((rule, ruleIndex) => {
          // Collect matching manipulators (if a filter is set)
          let matchingManipulators = [];
          if (rule.manipulators && Array.isArray(rule.manipulators)) {
            rule.manipulators.forEach((manipulator) => {
              if (!filterKey || manipulatorMatchesFilter(manipulator, filterKey)) {
                matchingManipulators.push(manipulator);
              }
            });
          }
          if (matchingManipulators.length > 0) {
            md += `#### Rule ${ruleIndex + 1}: ${rule.description || 'No Description'}\n\n`;
            matchingManipulators.forEach((manipulator, manipIndex) => {
              md += `##### ${manipIndex + 1}: `;
              if (manipulator.description) {
                md += `description: ${manipulator.description}\n`;
              }
              // "from" field
              if (manipulator.from) {
                md += `- **From:** ${formatKeyDefinition(manipulator.from)}\n`;
              }
              // "to" field
              if (manipulator.to) {
                md += `- **To:** `;
                if (Array.isArray(manipulator.to)) {
                  md += manipulator.to.map(formatKeyDefinition).join(', ');
                } else {
                  md += formatKeyDefinition(manipulator.to);
                }
                md += `\n`;
              }
              // Optional: include conditions if they exist
              if (manipulator.conditions && Array.isArray(manipulator.conditions)) {
                md += `- **Conditions:**\n`;
                manipulator.conditions.forEach(condition => {
                  md += `  - ${JSON.stringify(condition)}\n`;
                });
              }
              md += `\n`;
            });
          }
        });
      }
      md += `\n`;
    });
  } else {
    md += `No profiles found in the configuration.\n`;
  }

  return md;
}

/**
 * Checks if a manipulator matches the given filter key_code.
 *
 * @param {Object} manipulator - The manipulator object.
 * @param {string} filterKey - The key_code to filter by.
 * @returns {boolean} - True if the manipulator's "from" or "to" contains the filter key_code.
 */
function manipulatorMatchesFilter(manipulator, filterKey) {
  // Check the "from" definition
  if (manipulator.from && manipulator.from.key_code && manipulator.from.key_code === filterKey) {
    return true;
  }
  // Check the "to" definition: could be an array or an object
  if (manipulator.to) {
    if (Array.isArray(manipulator.to)) {
      for (let toDef of manipulator.to) {
        if (toDef.key_code && toDef.key_code === filterKey) {
          return true;
        }
      }
    } else if (manipulator.to.key_code && manipulator.to.key_code === filterKey) {
      return true;
    }
  }
  return false;
}

/**
 * Formats a key definition (from or to) into a human-readable string.
 *
 * If keyDef.modifiers.mandatory (or keyDef.modifiers as an array) contains any of:
 *   ["right_command", "right_control", "right_shift", "right_option"]
 * they are substituted by <kbd>✱</kbd>. Any additional modifiers are appended.
 *
 * Additionally, keyMapper is used to substitute key codes (e.g., "comma" is replaced by ",").
 *
 * @param {Object} keyDef - The key definition object.
 * @returns {string} - A formatted string representation.
 */
function formatKeyDefinition(keyDef) {
  let str = '';

  // Use the separate function for key code substitution
  if (keyDef.key_code) {
    str += substituteKeyCode(keyDef.key_code);
  }
  if (keyDef.modifiers) {
    // Process modifiers provided as an object with mandatory/optional
    if (typeof keyDef.modifiers === 'object' && !Array.isArray(keyDef.modifiers)) {
      if (keyDef.modifiers.mandatory) {
        const mods = keyDef.modifiers.mandatory;
        // Separate hyper modifiers from any others
        const hyperUsed = mods.filter(m => hyperModifiers.includes(m));
        const otherMods = mods.filter(m => !hyperModifiers.includes(m));
        let modStr = '';
        // If all hyper modifiers are used, substitute with <kbd>✱</kbd>
        const sortedHyperUsed = hyperUsed.slice().sort();
        const sortedHyper = hyperModifiers.slice().sort();
        if (JSON.stringify(sortedHyperUsed) === JSON.stringify(sortedHyper)) {
          modStr += `<kbd>✱</kbd>`;
        } else if (hyperUsed.length > 0) {
          modStr += `<kbd>✱</kbd>`;
        }
        if (otherMods.length > 0) {
          if (modStr) {
            modStr += ', ';
          }
          modStr += otherMods.map(m => `${substituteKeyCode(m)}`).join(', ');
        }
        str += ` + [${modStr}]`;
      }
      if (keyDef.modifiers.optional) {
        str += ` (optional: ${keyDef.modifiers.optional.join(', ')})`;
      }
    }
    // Process modifiers if provided as an array
    else if (Array.isArray(keyDef.modifiers)) {
      const mods = keyDef.modifiers;
      const hyperUsed = mods.filter(m => hyperModifiers.includes(m));
      const otherMods = mods.filter(m => !hyperModifiers.includes(m));
      let modStr = '';
      if (hyperUsed.length > 0) {
        modStr += `<kbd>✱</kbd>`;
      }
      if (otherMods.length > 0) {
        if (modStr) {
          modStr += ' , ';
        }
        modStr += otherMods.map(m => `${substituteKeyCode(m)}`).join(', ');
      }
      str += ` + [${modStr}]`;
    }
  }
  return str;
}
