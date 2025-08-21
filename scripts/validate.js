#!/usr/bin/env node

const fs = require('fs-extra');
const path = require('path');
const yaml = require('yaml');
const Ajv = require('ajv');
const addFormats = require('ajv-formats');
const chalk = require('chalk');

// Initialize AJV with formats
const ajv = new Ajv({ allErrors: true, strict: false });
addFormats(ajv);

async function loadSchema() {
    try {
        const schemaPath = path.join(__dirname, '../curriculum/schema/session.schema.yml');
        const schemaContent = await fs.readFile(schemaPath, 'utf8');
        const schema = yaml.parse(schemaContent);
        return ajv.compile(schema);
    } catch (error) {
        console.error(chalk.red('Failed to load schema:'), error.message);
        process.exit(1);
    }
}

async function validateSession(filePath, validate) {
    try {
        const content = await fs.readFile(filePath, 'utf8');
        const session = yaml.parse(content);

        const valid = validate(session);

        if (!valid) {
            console.error(chalk.red(`❌ Validation failed for ${filePath}:`));
            validate.errors.forEach(error => {
                console.error(chalk.red(`  • ${error.instancePath || 'root'}: ${error.message}`));
                if (error.data !== undefined) {
                    console.error(chalk.gray(`    Current value: ${JSON.stringify(error.data)}`));
                }
            });
            return false;
        } else {
            console.log(chalk.green(`✅ ${path.basename(filePath)} is valid`));
            return true;
        }
    } catch (error) {
        console.error(chalk.red(`❌ Error parsing ${filePath}:`), error.message);
        return false;
    }
}

async function validateRubric(session, filePath) {
    const errors = [];

    // Check that agenda times sum to roughly 90 minutes
    if (session.agenda && Array.isArray(session.agenda)) {
        const totalMinutes = session.agenda.reduce((sum, item) => {
            return sum + (item.duration || 0);
        }, 0);

        if (totalMinutes < 80 || totalMinutes > 100) {
            errors.push(`Agenda duration (${totalMinutes} min) should be 80-100 minutes`);
        }
    }

    // Check for required resources based on topics
    if (session.topics && session.topics.includes('DSA') || session.topics.includes('ML')) {
        const coreResources = session.resources?.core || [];
        const hasOCW = coreResources.some(r => r.url.includes('ocw.mit.edu'));
        const hasAlgoViz = coreResources.some(r => r.url.includes('algorithm-visualizer'));

        if (!hasOCW && session.topics.includes('DSA')) {
            errors.push('DSA topics should include at least one MIT OCW resource');
        }

        if (!hasAlgoViz && session.topics.includes('DSA')) {
            errors.push('DSA topics should include Algorithm Visualizer link');
        }
    }

    // Check objectives are measurable (start with action verbs)
    const actionVerbs = [
        'analyze', 'apply', 'build', 'classify', 'compare', 'compute', 'containerize', 'create', 'define',
        'demonstrate', 'deploy', 'design', 'describe', 'evaluate', 'explain', 'identify', 'implement',
        'instrument', 'justify', 'measure', 'model', 'optimize', 'plan', 'present', 'prove', 'refactor',
        'set', 'simulate', 'solve', 'test', 'trace', 'transform'
    ];

    if (session.objectives) {
        session.objectives.forEach((objective, i) => {
            const firstWord = objective.toLowerCase().split(' ')[0];
            if (!actionVerbs.includes(firstWord)) {
                errors.push(`Objective ${i + 1} should start with measurable action verb, got: "${firstWord}"`);
            }
        });
    }

    if (errors.length > 0) {
        console.warn(chalk.yellow(`⚠️  Rubric warnings for ${path.basename(filePath)}:`));
        errors.forEach(error => {
            console.warn(chalk.yellow(`  • ${error}`));
        });
        return false;
    }

    return true;
}

async function main() {
    console.log(chalk.blue('🔍 Validating workshop session files...\n'));

    const validate = await loadSchema();
    const weeksDir = path.join(__dirname, '../curriculum/weeks');

    if (!await fs.pathExists(weeksDir)) {
        console.error(chalk.red(`Weeks directory not found: ${weeksDir}`));
        process.exit(1);
    }

    const files = await fs.readdir(weeksDir);
    const yamlFiles = files.filter(f => f.endsWith('.yml') || f.endsWith('.yaml'));

    if (yamlFiles.length === 0) {
        console.warn(chalk.yellow('No YAML files found to validate'));
        process.exit(0);
    }

    let validCount = 0;
    let rubricPassCount = 0;

    for (const file of yamlFiles) {
        const filePath = path.join(weeksDir, file);
        const isValid = await validateSession(filePath, validate);

        if (isValid) {
            validCount++;
            // Run additional rubric checks
            try {
                const content = await fs.readFile(filePath, 'utf8');
                const session = yaml.parse(content);
                const rubricPass = await validateRubric(session, filePath);
                if (rubricPass) {
                    rubricPassCount++;
                }
            } catch (error) {
                console.error(chalk.red(`Error in rubric check for ${file}:`), error.message);
            }
        }

        console.log(''); // Add spacing
    }

    console.log(chalk.blue('📊 Validation Summary:'));
    console.log(`  Schema valid: ${validCount}/${yamlFiles.length}`);
    console.log(`  Rubric compliant: ${rubricPassCount}/${yamlFiles.length}`);

    if (validCount === yamlFiles.length && rubricPassCount === yamlFiles.length) {
        console.log(chalk.green('🎉 All files pass validation and rubric checks!'));
        process.exit(0);
    } else {
        console.log(chalk.red('❌ Some files failed validation or rubric checks'));
        process.exit(1);
    }
}

if (require.main === module) {
    main().catch(error => {
        console.error(chalk.red('Validation script failed:'), error);
        process.exit(1);
    });
}
