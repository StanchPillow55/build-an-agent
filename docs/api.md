# API Reference

This page provides comprehensive API documentation for the Build An Agent project, with a focus on the Educator Agent modules.

!!! note "Auto-Generated Documentation"
    This page contains auto-generated API documentation. For live documentation with interactive examples, run `make docs` to start the development server.

## Educator Agent Modules

The Educator Agent consists of several key modules that work together to provide comprehensive curriculum planning capabilities.

### Core Functions

#### Curriculum Planning

**Module:** `code.educator_agent.curriculum_planner`

Core functions for curriculum generation and validation:

```python
def plan_curriculum(params: Dict[str, Any]) -> Dict[str, Any]:
    """Plan a curriculum given the input parameters.
    
    Args:
        params: Dictionary containing:
            - grade_level: Target grade level (e.g., "8th Grade")
            - subject: Subject or topic
            - baseline: Prior knowledge assumption
            - constraints: List of constraints
            - duration: Lesson duration
    
    Returns:
        Validated curriculum plan dictionary
    """

def generate_prompt(params: Dict[str, Any]) -> str:
    """Generate a comprehensive prompt for curriculum planning."""

def call_llm(prompt: str, model: str = "gpt-4o") -> Dict[str, Any]:
    """Call OpenAI LLM using new SDK v1.x style."""

def validate_plan(plan: Dict[str, Any]) -> None:
    """Validate a curriculum plan against the schema."""
```

#### Content Sanitization

**Module:** `code.educator_agent.sanitizer`

Content safety and PII protection:

```python
def clean_text(text: str) -> str:
    """Clean text by removing profanity and replacing PII with [REDACTED].
    
    Args:
        text: Input text to clean
        
    Returns:
        Cleaned text with profanity censored and PII redacted
    """

def enforce_constraints(plan: Dict[str, Any]) -> Dict[str, Any]:
    """Enforce content constraints on a curriculum plan.
    
    Runs clean_text on every user-visible string in the curriculum JSON.
    
    Args:
        plan: Curriculum plan dictionary
        
    Returns:
        Cleaned curriculum plan
    """

class ContentSanitizer:
    """Content sanitizer for educational materials.
    
    Features:
    - Profanity filtering using better-profanity
    - PII detection for names, emails, phone numbers, SSNs, credit cards
    - Recursive cleaning of nested data structures
    - Type preservation for non-string data
    """
```

#### Slide Generation

**Module:** `code.educator_agent.slide_generator`

PowerPoint presentation generation:

```python
def create_deck(curriculum_plan: Dict[str, Any], output_file: str) -> None:
    """Create a PowerPoint presentation from curriculum plan.
    
    Args:
        curriculum_plan: Validated curriculum dictionary
        output_file: Output .pptx file path
        
    Features:
    - Automatic slide generation from curriculum sections
    - Image integration with educational content
    - Professional slide layouts and design
    """
```

#### Speaker Notes

**Module:** `code.educator_agent.speaker_notes`

Generate detailed speaker notes for educators:

```python
def generate_speaker_notes(curriculum_plan: Dict[str, Any]) -> str:
    """Generate comprehensive speaker notes in Markdown format.
    
    Args:
        curriculum_plan: Curriculum dictionary
        
    Returns:
        Formatted Markdown speaker notes
    """
```

#### Package Generation

**Module:** `code.educator_agent.packager`

Bundle complete educational materials:

```python
def create_package(curriculum_plan: Dict[str, Any], 
                  output_zip: str, 
                  include_pptx: bool = False,
                  include_notes: bool = False) -> None:
    """Create a complete educational package.
    
    Args:
        curriculum_plan: Curriculum dictionary
        output_zip: Output ZIP file path
        include_pptx: Include PowerPoint presentation
        include_notes: Include speaker notes
    """
```

### Microsoft Integration

#### Copilot Export

**Module:** `code.educator_agent.copilot_pptx`

Microsoft Graph API integration:

```python
def export_to_onedrive(pptx_path: str, title: str) -> Dict[str, str]:
    """Export presentation to Microsoft OneDrive.
    
    Args:
        pptx_path: Local PowerPoint file path
        title: Presentation title
        
    Returns:
        Dictionary with share_url and file_id
        
    Prerequisites:
    - Microsoft 365 EDU account
    - Azure app with Graph API permissions
    - Environment variables: MS_CLIENT_ID, MS_TENANT_ID, MS_CLIENT_SECRET
    """
```

### CLI Interface

**Module:** `code.educator_agent.__main__`

Command-line interface with argument parsing and rich output formatting.

**Usage:**
```bash
python -m educator_agent --grade "8th Grade" --subject "Environmental Science"
```

**Available Arguments:**
- `--grade`: Target grade level (required)
- `--subject`: Subject or topic (required) 
- `--baseline`: Prior knowledge baseline
- `--constraints`: Comma-separated constraints
- `--model`: OpenAI model to use
- `--duration`: Lesson duration
- `--pptx`: Generate PowerPoint presentation
- `--notes`: Generate speaker notes
- `--zip`: Create complete package
- `--copilot`: Export to Microsoft OneDrive
- `--json-only`: Output raw JSON only
- `--quiet`: Suppress progress messages

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
