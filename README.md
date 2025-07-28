# Build An Agent Hackathon

[![CI](https://github.com/StanchPillow55/build-an-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/StanchPillow55/build-an-agent/actions/workflows/ci.yml)

Welcome to the **Build An Agent Hackathon**! This hands-on workshop teaches you how to create intelligent AI agents that can perform complex tasks using Large Language Models (LLMs) and tools. You'll build a **Document Generation Agent** - an intelligent system that can research any topic, create comprehensive outlines, write detailed sections, and compile professional reports automatically. Unlike simple workflows, agents are intelligent programs that can adapt to changing requirements, choose tools dynamically, and perform complex reasoning and planning.

## What You'll Learn

By the end of this hackathon, you'll know how to create an agent that can:
- **Use tools** to perform actions like web searches, API calls, and data processing
- **Maintain conversation context** across multiple interactions
- **Make decisions** about next steps based on available information
- **Handle complex multi-step workflows** autonomously

## Educator Agent CLI

This project includes an **Educator Agent** - an AI-powered curriculum planning tool with constraint enforcement and rich CLI interface.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/StanchPillow55/build-an-agent.git
   cd build-an-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**
   ```bash
   # Add to .env file
   echo "OPENAI_API_KEY=your_api_key_here" >> .env
   ```

### Usage

The Educator Agent provides two modes of operation:

#### Interactive Wizard Mode (Recommended)

Run without arguments to launch the interactive wizard:

```bash
cd code
python -m educator_agent
```

The wizard will guide you through:
- 📝 **Basic inputs**: Grade level, subject, baseline knowledge, duration, constraints, AI model
- 📊 **Output preferences**: PowerPoint generation, speaker notes, OER resources, ZIP packaging, Microsoft Copilot export
- 📋 **Review**: Confirm your choices before generation
- ⚡ **Progress tracking**: Real-time progress indicators for each step

#### Non-Interactive Mode

For automation or when you know exactly what you want:

```bash
# Generate a curriculum for 8th Grade Environmental Science
python -m educator_agent --non-interactive --grade "8th Grade" --subject "Environmental Science"
```

#### Advanced Usage
```bash
# Specify baseline knowledge and custom constraints
python -m educator_agent \
  --grade "5th Grade" \
  --subject "Mathematics" \
  --baseline "basic arithmetic and counting" \
  --constraints "age-appropriate,hands-on-activities,no-calculators" \
  --model "gpt-4"
```

#### JSON Output Only
```bash
# Output raw JSON for programmatic use
python -m educator_agent \
  --grade "10th Grade" \
  --subject "Biology" \
  --json-only
```

#### PowerPoint Generation
```bash
# Generate both curriculum plan and PowerPoint presentation
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --pptx "ecosystem_lesson.pptx"

# Generate presentation with custom parameters
python -m educator_agent \
  --grade "5th Grade" \
  --subject "Mathematics" \
  --baseline "basic arithmetic" \
  --constraints "hands-on-activities,visual-learning" \
  --pptx "math_lesson.pptx"
```

#### Speaker Notes Generation
```bash
# Generate speaker notes along with the curriculum plan
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --notes
```

#### Complete Package Generation
```bash
# Generate everything: curriculum, PowerPoint, notes, and package into ZIP
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --baseline "No prior knowledge of ecosystems" \
  --constraints "PII-safe, simple language" \
  --pptx "lesson.pptx" \
  --notes \
  --zip "complete_package.zip"
```

#### Microsoft Copilot / Graph PowerPoint Export (Beta)
```bash
# Export presentation directly to OneDrive using Microsoft Graph API
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --copilot
```

**Prerequisites for Copilot Export:**
1. Microsoft 365 EDU account with appropriate permissions
2. Registered Azure app with Graph API permissions:
   - `Files.ReadWrite.All`
   - `Sites.ReadWrite.All`
3. Environment variables set in `.env`:
   ```bash
   MS_CLIENT_ID=your_azure_app_client_id
   MS_TENANT_ID=your_azure_tenant_id
   MS_CLIENT_SECRET=your_azure_app_client_secret
   ```

#### Available Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--grade` | ✅ | - | Target grade level (e.g., "8th Grade") |
| `--subject` | ✅ | - | Subject or topic (e.g., "Environmental Science") |
| `--baseline` | ❌ | "grade-appropriate prior knowledge" | Audience knowledge baseline |
| `--constraints` | ❌ | "age-appropriate,privacy-protecting" | Comma-separated constraints |
| `--model` | ❌ | "gpt-4o" | OpenAI model to use |
| `--duration` | ❌ | "45 minutes" | Lesson duration |
| `--json-only` | ❌ | `false` | Output only raw JSON |
| `--quiet, -q` | ❌ | `false` | Suppress progress messages |
| `--pptx` | ❌ | - | Generate PowerPoint presentation (specify output path) |
| `--notes` | ❌ | `false` | Generate speaker notes in Markdown format |
| `--oer` | ❌ | - | Include OER Commons resources (specify number to fetch) |
| `--zip` | ❌ | - | Package all outputs into a ZIP file (specify output path) |
| `--copilot` | ❌ | `false` | Export presentation to Microsoft 365 OneDrive using Copilot |

#### Example Output

The CLI generates comprehensive curriculum plans with:
- **📚 Lesson Title** - Clear, engaging lesson titles
- **🎯 Learning Objectives** - Specific, measurable goals
- **📖 Content Outline** - Structured lesson sections with descriptions
- **📝 Suggested Assessments** - Multiple assessment methods
- **💾 JSON Schema** - Validated output for integration

### Features

- ✅ **Interactive CLI Wizard** - User-friendly guided setup with Typer prompts and rich progress indicators
- ✅ **OpenAI Integration** - Uses GPT-4o by default with SDK v1.x
- ✅ **JSON Schema Validation** - Ensures consistent, reliable output
- ✅ **Rich CLI Interface** - Beautiful terminal output with tables and panels
- ✅ **Constraint Enforcement** - Built-in privacy protection and age-appropriate content
- ✅ **Fallback Mode** - Works without API key for testing
- ✅ **Comprehensive Testing** - Full test coverage with mocked responses
- ✅ **PowerPoint Generation** - Automatic .pptx slide creation with images
- ✅ **Speaker Notes** - Markdown-formatted notes for educators
- ✅ **OER Commons Integration** - Live search and integration of Open Educational Resources
- ✅ **Package Generation** - Complete ZIP packages with all materials
- ✅ **Microsoft Copilot Integration** - Direct export to OneDrive using Graph API (beta)

### End-to-End Demo

Try the complete educator agent experience with our demo script:

```bash
# Run the comprehensive demo
bash scripts/demo_end_to_end.sh
```

This demo will:
- Generate a complete curriculum plan for 8th Grade Environmental Science
- Create a PowerPoint presentation with images
- Generate speaker notes in Markdown format
- Package everything into a convenient ZIP file
- Demonstrate all major features in one command

### Testing

```bash
# Run the test suite
pip install -r requirements-dev.txt
pytest -q

# Run specific tests
pytest tests/test_planner.py -v
```
