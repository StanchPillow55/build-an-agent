# SWE Interview Master Plan - Slide Generation Pipeline

This repository contains a complete pipeline for generating workshop slides, speaker notes, and resources for SJSU Hoplite Club's 12-week Technical Interview Preparation Program.

## 🏗️ Architecture Overview

```
curriculum/
├── schema/session.schema.yml     # YAML validation schema
├── schedule.fall25.yml          # Master schedule with dates/events
├── weeks/                       # Weekly session content
│   ├── week00-setup.yml
│   ├── week01-recursion.yml
│   └── ...week12-devops.yml
└── events/                      # Special event configurations
    ├── industry-mixer.yml
    └── senior-work-day.yml

slides/
├── templates/week.hbs           # Handlebars template for slides
└── theme/academic.css           # Marp theme styling

scripts/
├── validate.js                  # YAML schema validation
├── build-slides.js             # Main slide generation
└── build-catalog.js            # Web catalog generation

dist/                           # Generated output
├── pdf/                        # PDF slides
├── html/                       # HTML presentations
├── index.html                  # Web catalog
└── notes/                      # Speaker notes
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- npm or yarn

### Setup
```bash
# Install dependencies
npm install

# Validate all session files
npm run validate:sessions

# Build all slides
npm run build:slides

# Generate PDFs and HTML
npm run export:pdf

# Build web catalog
npm run build:catalog

# Or do everything at once
npm run make
```

### Development
```bash
# Clean previous builds
npm run clean

# Development mode with file watching
npm run dev
```

## 📋 Content Creation Guide

### Adding a New Week

1. Create `curriculum/weeks/weekXX-topic.yml` following the schema
2. Include all required fields: objectives, agenda, topics, activities, assessment
3. Add speaker notes with beats, time cues, demo steps, and FAQ
4. Include industry tips referencing Success With SCE slides
5. Validate with `npm run validate:sessions`

### YAML Schema Requirements

Each session file must include:
- **id**: Unique identifier (e.g., "week01-recursion")
- **title**: Human-readable session title
- **week**: Numeric week (0-12)
- **objectives**: 4-6 measurable learning outcomes
- **agenda**: Time-boxed activity schedule
- **topics**: Tags for resource matching (DSA, Git, etc.)
- **activities**: Hands-on labs, demos, coding exercises
- **assessment**: LeetCode problems, projects, or reflections
- **resources**: Core and enrichment learning materials
- **speaker_notes**: Detailed facilitation guidance

### Style Guidelines

**Slides follow Success With SCE and Github 101 patterns:**
- Clear, step-by-step structure with short definitions
- Semi-professional tone with practical career guidance
- DO/DON'T callout blocks for key concepts
- Command sequence blocks for terminal workflows
- Industry relevance slides connecting to job search reality

**Academic Theme Features:**
- SJSU brand colors (Blue #0055A2, Gold #FFB81C)
- Generous whitespace and readable typography
- Callout boxes: `.do`, `.dont`, `.tip`, `.career`, `.industry`
- Two-column layouts and command sequence styling

## 🎯 Generated Outputs

### Slide Formats
- **PDF**: Print-ready presentations for offline use
- **HTML**: Interactive web presentations with navigation
- **Markdown**: Source files compatible with Marp and reveal.js

### Speaker Support Materials
- **Speaker Notes**: Detailed facilitation guides with timing cues
- **Demo Steps**: Step-by-step technical demonstrations
- **FAQ**: Common student questions with prepared answers
- **Time Cues**: Checkpoint reminders for pacing

### Web Catalog
- **Responsive Design**: Mobile-friendly slide browsing
- **Direct Links**: PDF, HTML, and speaker notes access
- **Search/Filter**: Find sessions by topic or week number
- **Resource Integration**: Links to Algorithm Visualizer, MIT OCW

## 🔧 Pipeline Features

### Validation & Quality Assurance
- JSON Schema validation for all YAML content
- Rubric enforcement (agenda timing, resource requirements)
- Measurable learning objective verification
- Link checking for external resources

### Build Automation
- GitHub Actions CI/CD pipeline
- Automatic PDF and HTML generation
- GitHub Pages deployment
- Build artifact preservation

### Theming & Customization
- Academic theme optimized for education
- SJSU branding and color scheme
- Print and web responsive layouts
- Accessibility considerations

## 📚 Special Events

### Industry Mixer (Week 5 - Virtual)
- **Format**: Zoom breakout rooms with industry professionals
- **Content**: Interview anxiety management + mock interviews
- **Deliverables**: Micro-deck, breakout facilitation guide
- **Follow-up**: LinkedIn connections and practice resources

### Senior Work Day (Week 11 - In-Person)
- **Format**: Career fair table with portfolio reviews
- **Content**: Technical interview practice + mentorship matching
- **Deliverables**: Table placard, practice prompts, review checklists
- **Materials**: QR codes linking to slide catalog and resources

## 🚢 Deployment

### GitHub Pages (Automatic)
- Triggers on push to `main` or `slides-automation` branches
- Builds and validates all content
- Deploys web catalog to GitHub Pages
- Available at: `https://stanchpillow55.github.io/build-an-agent/`

### Local Testing
```bash
# Serve locally for development
npx http-server dist/ -p 8080

# Or use Python
python -m http.server 8080 -d dist/
```

## 📊 Content Statistics

- **13 Sessions**: Week 0-12 covering full interview preparation
- **2 Special Events**: Virtual mixer + in-person career fair
- **90-minute Duration**: Consistent workshop timing
- **4-6 Learning Objectives**: Per session with measurable outcomes
- **100+ LeetCode Problems**: Curated and categorized by difficulty
- **25+ Resource Links**: Algorithm visualizers, MIT OCW, industry tools

## 🎨 Design Philosophy

**Inspired by Success With SCE:**
- One-page resume rule and XYZ bullet formatting
- LinkedIn networking strategies (500+ connections target)
- Project showcase over GPA emphasis
- Realistic expectations about referrals and applications

**Modeled after Github 101:**
- Clear vocabulary definitions and setup instructions
- Step-by-step command sequences with explanations
- Visual workflow diagrams before technical details
- Practical, hands-on learning approach

**Academic Best Practices:**
- Bloom's taxonomy for learning objective verbs
- Chunked content delivery with active learning
- Assessment aligned with objectives
- Scaffolded difficulty progression

---

## 🏆 Success Metrics

- **Validation**: 100% of YAML files pass schema validation
- **Build**: All 13 sessions generate PDF + HTML + speaker notes
- **Deployment**: Automatic GitHub Pages publishing
- **Quality**: Consistent styling and branding across all materials
- **Accessibility**: Mobile-responsive catalog with clear navigation

*Generated by SJSU Hoplite Club for Fall 2025 Technical Interview Preparation Program*
