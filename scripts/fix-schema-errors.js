#!/usr/bin/env node

/**
 * Fix schema validation errors in curriculum files
 */

const fs = require('fs');
const path = require('path');

// Helper function to update style sections
function fixStyleSection(content) {
  return content
    .replace(/theme: "hoplite"/g, 'theme: "academic"')
    .replace(/callouts: \["do", "dont"\]/g, 'callouts: ["do-dont", "tip"]')
    .replace(/activity: "Wrap"/g, 'activity: "Wrap up session"');
}

// List of files to fix
const filesToFix = [
  'week00-setup.yml',
  'week01-recursion.yml',
  'week02-sorting.yml',
  'week03-hashing.yml',
  'week05-industry-mixer.yml',
  'week09-system-design.yml'
];

filesToFix.forEach(filename => {
  const filePath = path.join(__dirname, '../curriculum/weeks', filename);
  if (fs.existsSync(filePath)) {
    let content = fs.readFileSync(filePath, 'utf8');

    // Fix style issues
    content = fixStyleSection(content);

    // Fix specific issues per file
    if (filename === 'week05-industry-mixer.yml') {
      // Fix activity time_minutes to be <= 45
      content = content.replace(/time_minutes: 65/g, 'time_minutes: 45');
    }

    fs.writeFileSync(filePath, content);
    console.log(`Fixed ${filename}`);
  }
});

console.log('All schema errors fixed!');
