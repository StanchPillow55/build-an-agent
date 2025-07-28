# API Reference

This page provides comprehensive API documentation for the Build An Agent project, with a focus on the Educator Agent modules.

## Educator Agent

The Educator Agent is the main component for curriculum planning and educational content generation.

### Curriculum Planner

Core curriculum planning functionality with OpenAI integration.

::: code.educator_agent.curriculum_planner

### Content Sanitizer

Content sanitization and PII detection for safe educational content.

::: code.educator_agent.sanitizer

### Slide Generator

PowerPoint presentation generation from curriculum plans.

::: code.educator_agent.slide_generator

### Speaker Notes

Speaker notes generation for educators.

::: code.educator_agent.speaker_notes

### OER Resource Finder

Open Educational Resource discovery and integration.

::: code.educator_agent.oer_resource_finder

### Packager

Package generation for complete educational materials.

::: code.educator_agent.packager

### Microsoft Copilot Integration

Microsoft Graph API integration for OneDrive export.

::: code.educator_agent.copilot_pptx

## Document Generation Agent

Example agent for research and document writing tasks.

### Main Agent

::: code.docgen_agent.agent

### Research Tools

::: code.docgen_agent.researcher

### Author Tools

::: code.docgen_agent.author

### Available Tools

::: code.docgen_agent.tools

## Curriculum Agent

Core curriculum agent implementation.

### Main Agent

::: code.curriculum_agent.curriculum_agent

### Data Models

::: code.curriculum_agent.models

## Utility Functions

### Schema Definitions

The Educator Agent uses JSON schema validation to ensure consistent output:

```python
CURRICULUM_SCHEMA = {
    "type": "object",
    "properties": {
        "lesson_title": {"type": "string"},
        "learning_objectives": {"type": "array", "items": {"type": "string"}},
        "content_outline": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                },
                "required": ["title", "description"],
            },
        },
        "suggested_assessments": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "lesson_title",
        "learning_objectives",
        "content_outline",
        "suggested_assessments",
    ],
}
```

### Error Handling

All modules include comprehensive error handling:

- **API Errors**: Graceful handling of OpenAI API failures
- **Validation Errors**: Clear messages for schema validation failures
- **File Operations**: Robust file handling with proper cleanup
- **Network Issues**: Retry logic and fallback mechanisms

### Testing

The project includes comprehensive test coverage:

- **Unit Tests**: Individual function testing with mocks
- **Integration Tests**: End-to-end workflow testing
- **Schema Validation**: Extensive schema compliance testing
- **Error Scenarios**: Edge case and error condition testing

Run tests with:
```bash
pytest tests/ -v
```

## Type Definitions

### Common Types

```python
from typing import Dict, Any, List, Optional

# Curriculum plan structure
CurriculumPlan = Dict[str, Any]

# Parameters for curriculum generation
PlanningParams = Dict[str, Any]

# Slide generation options
SlideOptions = Dict[str, Any]
```

### Function Signatures

Key function signatures for type checking:

```python
def plan_curriculum(params: Dict[str, Any]) -> Dict[str, Any]: ...

def generate_prompt(params: Dict[str, Any]) -> str: ...

def validate_plan(plan: Dict[str, Any]) -> None: ...

def clean_text(text: str) -> str: ...

def enforce_constraints(plan: Dict[str, Any]) -> Dict[str, Any]: ...
```

## Configuration

### Environment Variables

Required and optional environment variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | OpenAI API key for LLM features |
| `MS_CLIENT_ID` | No | Azure app client ID for Copilot |
| `MS_TENANT_ID` | No | Azure tenant ID for Copilot |
| `MS_CLIENT_SECRET` | No | Azure app secret for Copilot |

### Default Settings

```python
DEFAULT_SETTINGS = {
    "model": "gpt-4o",
    "duration": "45 minutes",
    "constraints": ["age-appropriate", "privacy-protecting"],
    "baseline": "grade-appropriate prior knowledge"
}
```

## Examples

### Basic Usage

```python
from code.educator_agent import plan_curriculum

# Generate a curriculum plan
params = {
    "grade_level": "8th Grade",
    "subject": "Environmental Science",
    "duration": "45 minutes"
}

curriculum = plan_curriculum(params)
print(f"Title: {curriculum['lesson_title']}")
```

### With Content Sanitization

```python
from code.educator_agent.sanitizer import enforce_constraints

# Sanitize curriculum content
sanitized_curriculum = enforce_constraints(curriculum)
```

### PowerPoint Generation

```python
from code.educator_agent.slide_generator import create_deck

# Generate PowerPoint presentation
create_deck(curriculum, "lesson.pptx")
```

For more detailed examples, see the [Examples](examples/curriculum.md) section.
