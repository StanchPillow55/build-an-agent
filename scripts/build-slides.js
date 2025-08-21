#!/usr/bin/env node

const fs = require('fs-extra');
const path = require('path');
const yaml = require('yaml');
const Handlebars = require('handlebars');
const { execSync } = require('child_process');
const chalk = require('chalk');

// Register Handlebars helpers
Handlebars.registerHelper('formatDate', function(dateStr) {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
});

Handlebars.registerHelper('formatTime', function(timeStr) {
    if (!timeStr) return '';
    const [hours, minutes] = timeStr.split(':');
    const hour12 = parseInt(hours) % 12 || 12;
    const ampm = parseInt(hours) >= 12 ? 'PM' : 'AM';
    return `${hour12}:${minutes} ${ampm}`;
});

Handlebars.registerHelper('eq', function(a, b) {
    return a === b;
});

Handlebars.registerHelper('includes', function(array, value) {
    return array && array.includes(value);
});

Handlebars.registerHelper('join', function(array, separator) {
    return array ? array.join(separator || ', ') : '';
});

Handlebars.registerHelper('add', function(a, b) {
    return a + b;
});

Handlebars.registerHelper('gt', function(a, b) {
    return a > b;
});

Handlebars.registerHelper('lt', function(a, b) {
    return a < b;
});

Handlebars.registerHelper('addWeeks', function(dateStr, weeks) {
    if (!dateStr) return 'TBD';
    const date = new Date(dateStr);
    date.setDate(date.getDate() + (weeks * 7));
    return date.toLocaleDateString('en-US', {
        month: 'long',
        day: 'numeric'
    });
});

async function loadSchedule() {
    try {
        const schedulePath = path.join(__dirname, '../curriculum/schedule.fall25.yml');
        const scheduleContent = await fs.readFile(schedulePath, 'utf8');
        return yaml.parse(scheduleContent);
    } catch (error) {
        console.error(chalk.red('Failed to load schedule:'), error.message);
        return null;
    }
}

async function loadTemplate() {
    try {
        const templatePath = path.join(__dirname, '../slides/templates/week.hbs');
        const templateContent = await fs.readFile(templatePath, 'utf8');
        return Handlebars.compile(templateContent);
    } catch (error) {
        console.error(chalk.red('Failed to load template:'), error.message);
        throw error;
    }
}

async function mergeSessionWithSchedule(session, schedule) {
    const weekKey = `week${session.week.toString().padStart(2, '0')}`;
    const scheduleEntry = schedule?.schedule?.[weekKey];

    if (scheduleEntry) {
        return {
            ...session,
            date: scheduleEntry.date,
            time: scheduleEntry.time,
            location: scheduleEntry.location,
            delivery: scheduleEntry.delivery,
            schedule_notes: scheduleEntry.notes,
            is_special_event: scheduleEntry.type === 'special-event'
        };
    }

    return session;
}

async function generateSlide(sessionPath, template, schedule) {
    try {
        console.log(chalk.blue(`📝 Processing ${path.basename(sessionPath)}...`));

        const sessionContent = await fs.readFile(sessionPath, 'utf8');
        const session = yaml.parse(sessionContent);

        // Merge with schedule data
        const enrichedSession = await mergeSessionWithSchedule(session, schedule);

        // Generate Marp markdown
        const markdown = template(enrichedSession);

        // Write to slides directory
        const filename = path.basename(sessionPath, '.yml') + '.md';
        const outputPath = path.join(__dirname, '../slides', filename);
        await fs.writeFile(outputPath, markdown);

        // Generate speaker notes
        await generateSpeakerNotes(enrichedSession, filename);

        console.log(chalk.green(`  ✅ Generated ${filename}`));
        return outputPath;

    } catch (error) {
        console.error(chalk.red(`  ❌ Failed to process ${sessionPath}:`), error.message);
        throw error;
    }
}

async function generateSpeakerNotes(session, slideFilename) {
    const notesTemplate = `# Speaker Notes: ${session.title}

**Date:** ${session.date || 'TBD'}
**Duration:** ${session.duration}
**Week:** ${session.week}

## Session Overview
- **Objectives:** ${session.objectives ? session.objectives.length : 0} learning objectives
- **Activities:** ${session.activities ? session.activities.length : 0} hands-on activities
- **Assessment:** ${session.assessment ? session.assessment.length : 0} assessment items

## Timing & Agenda
${session.agenda ? session.agenda.map(item =>
    `- **${item.time}** (${item.duration || '?'} min): ${item.activity}`
).join('\\n') : 'No agenda provided'}

## Speaker Beats
${session.speaker_notes?.beats ? session.speaker_notes.beats.map((beat, i) =>
    `${i + 1}. ${beat}`
).join('\\n') : 'No speaker notes provided'}

## Demo Steps
${session.speaker_notes?.demo_steps ? session.speaker_notes.demo_steps.map((step, i) =>
    `${i + 1}. ${step}`
).join('\\n') : 'No demo steps provided'}

## Time Cues
${session.speaker_notes?.time_cues ? session.speaker_notes.time_cues.map(cue =>
    `- **Minute ${cue.minute}:** ${cue.note}`
).join('\\n') : 'No time cues provided'}

## FAQ Preparation
${session.speaker_notes?.faq ? session.speaker_notes.faq.map(qa =>
    `**Q:** ${qa.question}\\n**A:** ${qa.answer}\\n`
).join('\\n') : 'No FAQ provided'}

## Resources for Reference
${session.resources?.core ? session.resources.core.map(resource =>
    `- [${resource.title}](${resource.url}) - ${resource.why}`
).join('\\n') : 'No core resources'}

## Assessment Details
${session.assessment ? session.assessment.map(assess => {
    if (assess.type === 'leetcode') {
        return `- **LeetCode Problems:** ${assess.ids ? assess.ids.join(', ') : 'None specified'}\\n  Instructions: ${assess.instructions || 'Standard approach'}`;
    }
    return `- **${assess.type}:** ${assess.instructions || assess.project_description || 'See session materials'}`;
}).join('\\n') : 'No assessment details'}

---
*Generated from ${slideFilename}*
`;

    const notesPath = path.join(__dirname, '../notes', slideFilename.replace('.md', '-speaker-notes.md'));
    await fs.writeFile(notesPath, notesTemplate);
}

async function generateMarpPDF(markdownPath) {
    try {
        const filename = path.basename(markdownPath, '.md');
        const pdfPath = path.join(__dirname, '../dist/pdf', filename + '.pdf');
        const htmlPath = path.join(__dirname, '../dist/html', filename + '.html');

        console.log(chalk.blue(`  📊 Generating PDF for ${filename}...`));

        // Use marp-cli to generate PDF and HTML
        execSync(
            `npx @marp-team/marp-cli "${markdownPath}" --pdf --output "${pdfPath}" --theme "${path.join(__dirname, '../slides/theme/academic.css')}" --allow-local-files`,
            { stdio: 'pipe' }
        );

        execSync(
            `npx @marp-team/marp-cli "${markdownPath}" --html --output "${htmlPath}" --theme "${path.join(__dirname, '../slides/theme/academic.css')}" --allow-local-files`,
            { stdio: 'pipe' }
        );

        console.log(chalk.green(`    ✅ Generated ${filename}.pdf and ${filename}.html`));

    } catch (error) {
        console.error(chalk.red(`    ❌ Failed to generate PDF for ${markdownPath}:`), error.message);
    }
}

async function main() {
    console.log(chalk.blue('🚀 Building workshop slides...\n'));

    // Load schedule and template
    const schedule = await loadSchedule();
    const template = await loadTemplate();

    // Find all session YAML files
    const weeksDir = path.join(__dirname, '../curriculum/weeks');

    if (!await fs.pathExists(weeksDir)) {
        console.error(chalk.red(`Weeks directory not found: ${weeksDir}`));
        process.exit(1);
    }

    const files = await fs.readdir(weeksDir);
    const yamlFiles = files.filter(f => f.endsWith('.yml') || f.endsWith('.yaml'));

    if (yamlFiles.length === 0) {
        console.warn(chalk.yellow('No session files found to process'));
        process.exit(0);
    }

    // Ensure output directories exist
    await fs.ensureDir(path.join(__dirname, '../slides'));
    await fs.ensureDir(path.join(__dirname, '../notes'));
    await fs.ensureDir(path.join(__dirname, '../dist/pdf'));
    await fs.ensureDir(path.join(__dirname, '../dist/html'));

    const generatedSlides = [];

    // Process each session file
    for (const file of yamlFiles.sort()) {
        const sessionPath = path.join(weeksDir, file);
        try {
            const slidePath = await generateSlide(sessionPath, template, schedule);
            generatedSlides.push(slidePath);
        } catch (error) {
            console.error(chalk.red(`Failed to process ${file}:`, error.message));
        }
    }

    console.log(chalk.blue('\\n📊 Generating PDFs and HTML...'));

    // Generate PDFs for all slides
    for (const slidePath of generatedSlides) {
        await generateMarpPDF(slidePath);
    }

    console.log(chalk.green(`\\n🎉 Successfully generated ${generatedSlides.length} slide decks!`));
    console.log(chalk.blue('Output locations:'));
    console.log(`  📁 Markdown slides: slides/`);
    console.log(`  📋 Speaker notes: notes/`);
    console.log(`  📄 PDF slides: dist/pdf/`);
    console.log(`  🌐 HTML slides: dist/html/`);
}

if (require.main === module) {
    main().catch(error => {
        console.error(chalk.red('Build script failed:'), error);
        process.exit(1);
    });
}

module.exports = { generateSlide, mergeSessionWithSchedule };
