#!/usr/bin/env node
/**
 * karabinerDocGen.js
 *
 * This script reads a Karabiner‑Elements configuration JSON file and generates
 * Markdown documentation describing its profiles, simple modifications, and
 * complex modifications (rules and manipulators).
 *
 * Usage:
 *   node karabinerDocGen.js path/to/karabiner.json
 */

const fs = require('fs');
const path = require('path');

// Check command-line arguments
if (process.argv.length < 3) {
  console.error('Usage: node karabinerDocGen.js <path to karabiner.json>');
  process.exit(1);
}

const inputPath = process.argv[2];

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
  const markdown = generateMarkdown(karabinerData);

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
 * @returns {string} - The generated Markdown string.
 */
function generateMarkdown(data) {
  let md = `# Karabiner‑Elements Configuration Documentation\n\n`;
  md += `**Generated on:** ${new Date().toLocaleString()}\n\n`;

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
          md += `#### Rule ${ruleIndex + 1}: ${rule.description || 'No Description'}\n\n`;
          if (rule.manipulators && Array.isArray(rule.manipulators)) {
            rule.manipulators.forEach((manipulator, manipIndex) => {
              md += `##### ${manipIndex + 1}:`;
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
          md += `\n`;
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
 * Formats a key definition (from or to) into a human-readable string.
 *
 * @param {Object} keyDef - The key definition object.
 * @returns {string} - A formatted string representation.
 */
function formatKeyDefinition(keyDef) {
  let str = '';
  if (keyDef.key_code) {
    str += keyDef.key_code;
  }
  if (keyDef.modifiers) {
    // modifiers can be an object (with mandatory/optional) or an array
    if (typeof keyDef.modifiers === 'object' && !Array.isArray(keyDef.modifiers)) {
      if (keyDef.modifiers.mandatory) {
        str += ` + [${keyDef.modifiers.mandatory.join(', ')}]`;
      }
      if (keyDef.modifiers.optional) {
        str += ` (optional: ${keyDef.modifiers.optional.join(', ')})`;
      }
    } else if (Array.isArray(keyDef.modifiers)) {
      str += ` + [${keyDef.modifiers.join(', ')}]`;
    }
  }
  return str;
}
