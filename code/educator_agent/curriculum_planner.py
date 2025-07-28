"""
Curriculum planner module for generating educational plans.

Provides:
- generate_prompt: Generate an LLM prompt based on parameters.
- call_llm: Interact with OpenAI's LLM.
- validate_plan: Validate plan using a JSON schema.
- plan_curriculum: Wrap functionality in a high-level interface.

Requires OPENAI_API_KEY in the environment.
"""

import os
import json
from openai import OpenAI
from jsonschema import validate, ValidationError
from typing import Dict, Any
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from dotenv import load_dotenv

try:
    from .sanitizer import enforce_constraints
except ImportError:
    from sanitizer import enforce_constraints

# Load environment variables
load_dotenv()

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Curriculum JSON Schema - exactly as required
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

# Initialize OpenAI client (new SDK v1.x style)
client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
console = Console()


def generate_prompt(params: Dict[str, Any]) -> str:
    """Generate a comprehensive prompt for curriculum planning."""
    grade_level = params.get("grade_level", "Unknown Grade")
    subject = params.get("subject", "Unknown Subject")
    duration = params.get("duration", "45 minutes")
    constraints = params.get("constraints", [])

    constraints_text = ", ".join(constraints) if constraints else "None specified"

    return f"""Create a detailed curriculum plan for {grade_level} students studying {subject}.

Parameters:
- Grade Level: {grade_level}
- Subject: {subject}
- Duration: {duration}
- Constraints: {constraints_text}

Please respond with a JSON object containing exactly these fields:
- lesson_title: A clear, engaging title for the lesson
- learning_objectives: Array of specific, measurable learning objectives
- content_outline: Array of objects with "title" and "description" for each section
- suggested_assessments: Array of assessment methods and activities

Ensure the content is age-appropriate and educationally sound for {grade_level} level."""


def call_llm(prompt: str, model: str = "gpt-4o") -> Dict[str, Any]:
    """Call OpenAI LLM using new SDK v1.x style."""
    if not client:
        # Fallback demo response when no API key
        return {
            "lesson_title": "Introduction to Environmental Science",
            "learning_objectives": [
                "Students will define what an ecosystem is",
                "Students will identify biotic and abiotic factors",
                "Students will explain food chains and energy flow",
            ],
            "content_outline": [
                {
                    "title": "What is an Ecosystem?",
                    "description": "Introduce the concept of ecosystems using local examples",
                },
                {
                    "title": "Living vs Non-Living Components",
                    "description": "Explore biotic and abiotic factors through hands-on activities",
                },
                {
                    "title": "Energy Flow in Ecosystems",
                    "description": "Demonstrate food chains and energy transfer concepts",
                },
            ],
            "suggested_assessments": [
                "Ecosystem components identification worksheet",
                "Food chain construction activity",
                "Exit ticket with key vocabulary terms",
            ],
        }

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert curriculum designer. Always respond with valid JSON matching the requested schema.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=1500,
            temperature=0.7,
        )

        response_text = response.choices[0].message.content.strip()

        # Try to extract JSON from response
        if response_text.startswith("```json"):
            response_text = response_text[7:-3].strip()
        elif response_text.startswith("```"):
            response_text = response_text[3:-3].strip()

        return json.loads(response_text)

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON response from LLM: {e}")
    except Exception as e:
        raise ValueError(f"LLM API error: {e}")


def validate_plan(plan: Dict[str, Any]) -> None:
    """Validate a curriculum plan against the schema."""
    try:
        validate(instance=plan, schema=CURRICULUM_SCHEMA)
    except ValidationError as e:
        raise ValueError(f"Validation error: {e.message}")


def plan_curriculum(params: Dict[str, Any]) -> Dict[str, Any]:
    """Plan a curriculum given the input parameters."""
    prompt = generate_prompt(params)
    plan = call_llm(prompt)
    validate_plan(plan)
    # Apply content sanitization as final step
    plan = enforce_constraints(plan)
    return plan


def main():
    """Execute rich-printed CLI demo."""
    console.print(
        Panel(
            "[bold green]🎓 Curriculum Planner Demo[/bold green]\n"
            "Task 2: Advanced curriculum planning with JSON validation",
            title="Educator Agent",
            border_style="green",
        )
    )

    demo_params = {
        "grade_level": "8th Grade",
        "subject": "Environmental Science",
        "constraints": ["age-appropriate", "privacy-protecting"],
        "duration": "45 minutes",
    }

    # Display input parameters
    console.print("\n[bold blue]📝 Input Parameters:[/bold blue]")
    params_table = Table(show_header=True, header_style="bold magenta")
    params_table.add_column("Parameter", style="cyan")
    params_table.add_column("Value", style="yellow")

    for key, value in demo_params.items():
        if isinstance(value, list):
            value = ", ".join(value)
        params_table.add_row(key.replace("_", " ").title(), str(value))

    console.print(params_table)

    try:
        console.print("\n[bold yellow]🔄 Generating curriculum plan...[/bold yellow]")
        plan = plan_curriculum(demo_params)

        console.print(
            "\n[bold green]✅ Plan generated and validated successfully![/bold green]"
        )

        # Display lesson title
        console.print(
            Panel(
                f"[bold white]{plan['lesson_title']}[/bold white]",
                title="Lesson Title",
                border_style="blue",
            )
        )

        # Display learning objectives
        console.print("\n[bold blue]🎯 Learning Objectives:[/bold blue]")
        for i, obj in enumerate(plan["learning_objectives"], 1):
            console.print(f"  {i}. {obj}")

        # Display content outline
        console.print("\n[bold blue]📖 Content Outline:[/bold blue]")
        content_table = Table(show_header=True, header_style="bold cyan")
        content_table.add_column("Section", style="green")
        content_table.add_column("Description", style="white")

        for section in plan["content_outline"]:
            content_table.add_row(section["title"], section["description"])

        console.print(content_table)

        # Display assessments
        console.print("\n[bold blue]📝 Suggested Assessments:[/bold blue]")
        for i, assessment in enumerate(plan["suggested_assessments"], 1):
            console.print(f"  {i}. {assessment}")

        # Show JSON output
        if OPENAI_API_KEY:
            console.print("\n[dim]💡 Full JSON output:[/dim]")
        else:
            console.print(
                "\n[dim]💡 Demo JSON output (set OPENAI_API_KEY for AI generation):[/dim]"
            )

        console.print(
            Panel(
                json.dumps(plan, indent=2),
                title="JSON Schema Validated Output",
                border_style="dim",
            )
        )

        console.print(
            "\n[bold green]🎉 Task 2 Complete: Curriculum planner module working![/bold green]"
        )

    except Exception as e:
        console.print(f"\n[bold red]❌ Error: {e}[/bold red]")


if __name__ == "__main__":
    main()
