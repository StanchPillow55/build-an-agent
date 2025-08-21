#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

async function buildCatalog() {
    const distDir = path.join(__dirname, '../dist');
    const pdfDir = path.join(distDir, 'pdf');
    const htmlDir = path.join(distDir, 'html');
    const notesDir = path.join(__dirname, '../notes');

    // Ensure directories exist
    if (!fs.existsSync(pdfDir)) {
        console.warn('PDF directory not found, creating empty catalog');
        return;
    }

    // Get all PDF files and sort them
    const pdfFiles = fs.readdirSync(pdfDir)
        .filter(f => f.endsWith('.pdf'))
        .sort();

    const weeks = pdfFiles.map(pdfFile => {
        const name = pdfFile.replace('.pdf', '');
        const weekMatch = name.match(/week(\d+)/);
        const week = weekMatch ? parseInt(weekMatch[1]) : 0;

        // Clean up title
        let title = name.replace(/week\d+-/, '').replace(/-/g, ' ');
        title = title.charAt(0).toUpperCase() + title.slice(1);

        const htmlFile = pdfFile.replace('.pdf', '.html');
        const notesFile = name + '-speaker-notes.md';

        return {
            name,
            week,
            title,
            pdf: pdfFile,
            html: htmlFile,
            notes: notesFile,
            hasHtml: fs.existsSync(path.join(htmlDir, htmlFile)),
            hasNotes: fs.existsSync(path.join(notesDir, notesFile))
        };
    });

    // Generate HTML catalog
    const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SJSU Hoplite Club - SWE Interview Master Plan</title>
    <style>
        :root {
            --primary: #0055A2;
            --secondary: #FFB81C;
            --text: #2C3E50;
            --light: #F8F9FA;
            --border: #E9ECEF;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: var(--text);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }

        .header h1 {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 0.5rem;
        }

        .header h2 {
            font-size: 1.5rem;
            color: var(--text);
            font-weight: 400;
            margin-bottom: 0.5rem;
        }

        .header p {
            color: #666;
            font-size: 1.1rem;
        }

        .week-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .week-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .week-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 25px rgba(0, 0, 0, 0.15);
        }

        .week-number {
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
        }

        .week-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--text);
            margin-bottom: 1rem;
            line-height: 1.4;
        }

        .week-links {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
        }

        .week-links a {
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            padding: 0.5rem 1rem;
            background: var(--light);
            color: var(--primary);
            text-decoration: none;
            border-radius: 6px;
            font-size: 0.9rem;
            font-weight: 500;
            transition: all 0.2s ease;
            border: 1px solid var(--border);
        }

        .week-links a:hover {
            background: var(--primary);
            color: white;
            transform: translateY(-1px);
        }

        .week-links a.disabled {
            opacity: 0.5;
            pointer-events: none;
        }

        .footer {
            text-align: center;
            margin-top: 3rem;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 12px;
            backdrop-filter: blur(10px);
        }

        .footer p {
            margin-bottom: 0.5rem;
            color: #666;
        }

        .footer a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
        }

        .footer a:hover {
            text-decoration: underline;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .stat {
            text-align: center;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: 700;
            color: var(--primary);
            display: block;
        }

        .stat-label {
            font-size: 0.9rem;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 SWE Interview Master Plan</h1>
            <h2>Fall 2025 Workshop Slides</h2>
            <p>SJSU Hoplite Club • 12-Week Technical Interview Preparation Program</p>

            <div class="stats">
                <div class="stat">
                    <span class="stat-number">${weeks.length}</span>
                    <span class="stat-label">Workshop Sessions</span>
                </div>
                <div class="stat">
                    <span class="stat-number">90</span>
                    <span class="stat-label">Minutes Each</span>
                </div>
                <div class="stat">
                    <span class="stat-number">2</span>
                    <span class="stat-label">Special Events</span>
                </div>
            </div>
        </div>

        <div class="week-grid">
            ${weeks.map(w => `
                <div class="week-card">
                    <div class="week-number">Week ${w.week}</div>
                    <div class="week-title">${w.title}</div>
                    <div class="week-links">
                        <a href="pdf/${w.pdf}">📄 PDF Slides</a>
                        <a href="html/${w.html}" ${!w.hasHtml ? 'class="disabled"' : ''}>🌐 HTML View</a>
                        <a href="../notes/${w.notes}" ${!w.hasNotes ? 'class="disabled"' : ''}>📋 Speaker Notes</a>
                    </div>
                </div>
            `).join('')}
        </div>

        <div class="footer">
            <p>Generated on ${new Date().toLocaleDateString('en-US', {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            })}</p>
            <p><a href="https://github.com/StanchPillow55/build-an-agent">📂 Source Repository</a> |
               <a href="https://algorithm-visualizer.org/">🔗 Algorithm Visualizer</a> |
               <a href="https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/">📚 MIT OCW 6.006</a></p>
        </div>
    </div>
</body>
</html>`;

    // Write the catalog file
    const catalogPath = path.join(distDir, 'index.html');
    fs.writeFileSync(catalogPath, html);

    console.log(`✅ Generated slide catalog with ${weeks.length} sessions`);
    console.log(`📁 Catalog saved to: ${catalogPath}`);
}

if (require.main === module) {
    buildCatalog().catch(console.error);
}

module.exports = { buildCatalog };
