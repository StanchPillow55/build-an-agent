# Usage Guide

This guide covers how to use the Build An Agent project, focusing on the Educator Agent CLI and its various capabilities.

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (for AI-powered features)
- Optional: Microsoft 365 account (for Copilot integration)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/StanchPillow55/build-an-agent.git
   cd build-an-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   Create a `.env` file in the project root:
   ```bash
   # Required for AI features
   OPENAI_API_KEY=your_openai_api_key_here

   # Optional: For Microsoft Copilot integration
   MS_CLIENT_ID=your_azure_app_client_id
   MS_TENANT_ID=your_azure_tenant_id
   MS_CLIENT_SECRET=your_azure_app_client_secret
   ```

## Basic Usage

### Simple Curriculum Generation

Generate a basic curriculum plan:

```bash
cd code
python -m educator_agent --grade "8th Grade" --subject "Environmental Science"
```

This will create a comprehensive curriculum plan with:
- 📚 **Lesson Title** - Clear, engaging title
- 🎯 **Learning Objectives** - Specific, measurable goals
- 📖 **Content Outline** - Structured lesson sections
- 📝 **Suggested Assessments** - Multiple assessment methods

### With Custom Parameters

Specify additional parameters for more tailored content:

```bash
python -m educator_agent \
  --grade "5th Grade" \
  --subject "Mathematics" \
  --baseline "basic arithmetic and counting" \
  --constraints "age-appropriate,hands-on-activities,no-calculators" \
  --duration "60 minutes" \
  --model "gpt-4"
```

## Advanced Features

### PowerPoint Generation

Create a complete PowerPoint presentation alongside your curriculum:

```bash
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --pptx "ecosystem_lesson.pptx"
```

The generated presentation includes:
- Title slide with lesson information
- Learning objectives slide
- Content slides for each curriculum section
- Assessment slide with suggested activities
- Automatically sourced images for visual appeal

### Speaker Notes

Generate detailed speaker notes for educators:

```bash
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --notes
```

Speaker notes include:
- Detailed explanations for each curriculum section
- Teaching tips and guidance
- Time estimates for each activity
- Suggested discussion questions

### Complete Package Generation

Create a comprehensive educational package:

```bash
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --baseline "No prior knowledge of ecosystems" \
  --constraints "PII-safe,simple-language" \
  --pptx "lesson.pptx" \
  --notes \
  --zip "complete_package.zip"
```

The ZIP package contains:
- Curriculum plan (JSON format)
- PowerPoint presentation
- Speaker notes (Markdown format)
- Any additional resources

### Microsoft Copilot Integration (Beta)

Export presentations directly to OneDrive:

```bash
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --copilot
```

**Prerequisites for Copilot Export:**
1. Microsoft 365 EDU account
2. Registered Azure app with Graph API permissions:
   - `Files.ReadWrite.All`
   - `Sites.ReadWrite.All`
3. Environment variables configured (see Installation section)

## Command-Line Reference

### Required Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `--grade` | Target grade level | `"8th Grade"`, `"High School"`, `"College"` |
| `--subject` | Subject or topic | `"Environmental Science"`, `"Mathematics"` |

### Optional Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--baseline` | `"grade-appropriate prior knowledge"` | Audience knowledge baseline |
| `--constraints` | `"age-appropriate,privacy-protecting"` | Comma-separated constraints |
| `--model` | `"gpt-4o"` | OpenAI model to use |
| `--duration` | `"45 minutes"` | Lesson duration |
| `--json-only` | `false` | Output only raw JSON |
| `--quiet, -q` | `false` | Suppress progress messages |
| `--pptx` | - | Generate PowerPoint (specify output path) |
| `--notes` | `false` | Generate speaker notes |
| `--zip` | - | Package outputs into ZIP (specify path) |
| `--copilot` | `false` | Export to Microsoft 365 OneDrive |

### Output Formats

#### Standard Output
Rich terminal interface with formatted tables and panels.

#### JSON Only
```bash
python -m educator_agent \
  --grade "10th Grade" \
  --subject "Biology" \
  --json-only
```

Outputs raw JSON for programmatic use:
```json
{
  "lesson_title": "Introduction to Cell Biology",
  "learning_objectives": [...],
  "content_outline": [...],
  "suggested_assessments": [...]
}
```

#### Quiet Mode
```bash
python -m educator_agent \
  --grade "8th Grade" \
  --subject "Environmental Science" \
  --quiet
```

Suppresses progress messages for scripting.

## Content Sanitization

The Educator Agent includes built-in content sanitization:

### Automatic PII Detection
- **Names**: Full names (First Last) → `[REDACTED]`
- **Emails**: email@domain.com → `[REDACTED]`
- **Phone Numbers**: (555) 123-4567 → `[REDACTED]`
- **SSNs**: 123-45-6789 → `[REDACTED]`
- **Credit Cards**: 1234-5678-9012-3456 → `[REDACTED]`

### Profanity Filtering
- Inappropriate language is automatically censored
- Uses industry-standard profanity detection
- Maintains educational content integrity

### Custom Constraints

Specify additional constraints via the `--constraints` parameter:

```bash
--constraints "age-appropriate,hands-on-activities,visual-learning,no-technology"
```

Common constraint examples:
- `age-appropriate` - Content suitable for target grade
- `hands-on-activities` - Include interactive elements
- `visual-learning` - Emphasize visual aids
- `no-technology` - Avoid tech-dependent activities
- `PII-safe` - Extra PII protection
- `simple-language` - Use simpler vocabulary

## Error Handling

### Fallback Mode
If no OpenAI API key is provided, the system uses demo content:

```bash
# Works without API key for testing
python -m educator_agent --grade "8th Grade" --subject "Science"
```

### Common Issues

**Missing API Key**:
```
Error: OpenAI API key not found. Set OPENAI_API_KEY in .env file.
```

**Invalid Grade/Subject**:
```
Error: Grade level must be specified (e.g., "8th Grade")
```

**PowerPoint Generation Failure**:
```
Warning: PowerPoint generation failed. Curriculum plan created successfully.
```

## Testing

Run the test suite to verify functionality:

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest

# Run specific test modules
pytest tests/test_planner.py -v
pytest tests/test_sanitizer.py -v

# Run with coverage
pytest --cov=code
```

## Examples

See the [Examples](examples/curriculum.md) section for detailed walkthroughs and use cases.

## Integration

### Python API

Use the Educator Agent in your own Python code:

```python
from code.educator_agent import plan_curriculum

params = {
    "grade_level": "8th Grade",
    "subject": "Environmental Science",
    "constraints": ["age-appropriate", "hands-on-activities"],
    "duration": "45 minutes"
}

curriculum = plan_curriculum(params)
print(curriculum["lesson_title"])
```

### Batch Processing

Process multiple curricula:

```bash
#!/bin/bash
subjects=("Mathematics" "Science" "History" "Literature")

for subject in "${subjects[@]}"; do
    python -m educator_agent \
        --grade "8th Grade" \
        --subject "$subject" \
        --pptx "${subject,,}_lesson.pptx" \
        --quiet
done
```

## Next Steps

- Explore the [API Reference](api.md) for detailed function documentation
- Check out [curriculum examples](examples/curriculum.md) for specific use cases
- Learn about [PowerPoint generation](examples/powerpoint.md) features
- Understand [content sanitization](examples/sanitizer.md) capabilities
