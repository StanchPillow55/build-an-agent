# Build An Agent Hackathon

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

The Educator Agent can be used via command-line interface:

#### Basic Usage
```bash
# Generate a curriculum for 8th Grade Environmental Science
cd code
python -m educator_agent --grade "8th Grade" --subject "Environmental Science"
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

#### Example Output

The CLI generates comprehensive curriculum plans with:
- **📚 Lesson Title** - Clear, engaging lesson titles
- **🎯 Learning Objectives** - Specific, measurable goals
- **📖 Content Outline** - Structured lesson sections with descriptions
- **📝 Suggested Assessments** - Multiple assessment methods
- **💾 JSON Schema** - Validated output for integration

### Features

- ✅ **OpenAI Integration** - Uses GPT-4o by default with SDK v1.x
- ✅ **JSON Schema Validation** - Ensures consistent, reliable output
- ✅ **Rich CLI Interface** - Beautiful terminal output with tables and panels
- ✅ **Constraint Enforcement** - Built-in privacy protection and age-appropriate content
- ✅ **Fallback Mode** - Works without API key for testing
- ✅ **Comprehensive Testing** - Full test coverage with mocked responses
- ✅ **PowerPoint Generation** - Automatic .pptx slide creation with images

### Testing

```bash
# Run the test suite
pip install -r requirements-dev.txt
pytest -q

# Run specific tests
pytest tests/test_planner.py -v
```
