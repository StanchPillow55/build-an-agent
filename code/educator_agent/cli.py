"""
Interactive CLI wizard for educator_agent using Typer.

Provides a user-friendly interactive experience for curriculum planning
with prompts for all required inputs and optional outputs.
"""

import json
import tempfile
from pathlib import Path
from typing import List, Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm, Prompt
from rich.table import Table

from .curriculum_planner import plan_curriculum
from .slide_generator import create_deck
from .speaker_notes import generate_notes, save_notes_to_markdown
from .packager import package_outputs
from .copilot_pptx import export_to_copilot, CopilotPowerPointError
from .oer_resource_finder import suggest_oer

app = typer.Typer(
    name="educator-agent",
    help="AI-powered curriculum planning with constraint enforcement",
    no_args_is_help=True,
    rich_markup_mode="rich",
)

console = Console()


def parse_constraints(constraints_str: str) -> List[str]:
    """Parse comma-separated constraints string into list."""
    if not constraints_str:
        return []
    return [c.strip() for c in constraints_str.split(",") if c.strip()]


def display_welcome():
    """Display welcome message and introduction."""
    console.print(
        Panel(
            "[bold green]🎓 Educator Agent CLI Wizard[/bold green]\n"
            "AI-powered curriculum planning with constraint enforcement\n\n"
            "This wizard will guide you through creating a comprehensive lesson plan\n"
            "with optional PowerPoint slides, speaker notes, and OER resources.",
            title="Welcome",
            border_style="green",
        )
    )


def collect_basic_inputs() -> dict:
    """Collect basic curriculum planning inputs from user."""
    console.print("\n[bold blue]📝 Let's start with the basics...[/bold blue]\n")

    # Grade level
    grade = Prompt.ask("What grade level are you teaching?", default="5th Grade")

    # Subject
    subject = Prompt.ask(
        "What subject or topic will you cover?", default="Environmental Science"
    )

    # Baseline knowledge
    baseline = Prompt.ask(
        "What's the students' baseline knowledge level?",
        default="grade-appropriate prior knowledge",
    )

    # Duration
    duration = Prompt.ask("How long is the lesson?", default="45 minutes")

    # Constraints
    constraints_str = Prompt.ask(
        "Any specific constraints? (comma-separated)",
        default="age-appropriate,privacy-protecting",
    )

    # Model selection
    model = Prompt.ask(
        "Which AI model would you like to use?",
        default="gpt-4o",
        choices=["gpt-4o", "gpt-4", "gpt-3.5-turbo"],
    )

    return {
        "grade_level": grade,
        "subject": subject,
        "audience_baseline": baseline,
        "duration": duration,
        "constraints": parse_constraints(constraints_str),
        "model": model,
    }


def collect_output_preferences() -> dict:
    """Collect user preferences for output formats."""
    console.print(
        "\n[bold blue]📊 What outputs would you like to generate?[/bold blue]\n"
    )

    outputs = {}

    # PowerPoint presentation
    if Confirm.ask("Generate PowerPoint presentation?", default=True):
        pptx_path = Prompt.ask(
            "PowerPoint file path", default="lesson_presentation.pptx"
        )
        outputs["pptx"] = Path(pptx_path)

    # Speaker notes
    outputs["notes"] = Confirm.ask("Generate speaker notes?", default=True)

    # OER resources
    if Confirm.ask("Include OER Commons resources?", default=True):
        oer_count = typer.prompt(
            "How many OER resources to fetch?", type=int, default=3
        )
        outputs["oer"] = oer_count

    # ZIP package
    if Confirm.ask("Package all outputs into a ZIP file?", default=False):
        zip_path = Prompt.ask("ZIP file path", default="lesson_package.zip")
        outputs["zip"] = Path(zip_path)

    # Microsoft Copilot export
    outputs["copilot"] = Confirm.ask(
        "Export to Microsoft 365 OneDrive with Copilot?", default=False
    )

    return outputs


def display_curriculum_plan(plan: dict) -> None:
    """Display the curriculum plan with rich formatting."""
    console.print(
        "\n[bold green]✅ Curriculum Plan Generated Successfully![/bold green]"
    )

    # Display lesson title
    console.print(
        Panel(
            f"[bold white]{plan['lesson_title']}[/bold white]",
            title="📚 Lesson Title",
            border_style="blue",
        )
    )

    # Display learning objectives
    console.print("\n[bold blue]🎯 Learning Objectives:[/bold blue]")
    for i, objective in enumerate(plan["learning_objectives"], 1):
        console.print(f"  {i}. {objective}")

    # Display content outline
    console.print("\n[bold blue]📖 Content Outline:[/bold blue]")
    content_table = Table(show_header=True, header_style="bold cyan")
    content_table.add_column("Section Title", style="green", width=25)
    content_table.add_column("Description", style="white")

    for section in plan["content_outline"]:
        content_table.add_row(section["title"], section["description"])

    console.print(content_table)

    # Display suggested assessments
    console.print("\n[bold blue]📝 Suggested Assessments:[/bold blue]")
    for i, assessment in enumerate(plan["suggested_assessments"], 1):
        console.print(f"  {i}. {assessment}")


def display_parameters(params: dict) -> None:
    """Display input parameters in a formatted table."""
    console.print("\n[bold blue]📋 Review Your Inputs:[/bold blue]")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Parameter", style="cyan", width=15)
    table.add_column("Value", style="yellow")

    display_params = {
        "Grade Level": params.get("grade_level", ""),
        "Subject": params.get("subject", ""),
        "Baseline": params.get("audience_baseline", ""),
        "Duration": params.get("duration", ""),
        "Constraints": ", ".join(params.get("constraints", [])),
        "Model": params.get("model", "gpt-4o"),
    }

    for key, value in display_params.items():
        table.add_row(key, str(value))

    console.print(table)


@app.command()
def wizard(
    non_interactive: bool = typer.Option(
        False,
        "--non-interactive",
        help="Skip interactive wizard and use provided flags",
    ),
    grade: Optional[str] = typer.Option(None, "--grade", help="Target grade level"),
    subject: Optional[str] = typer.Option(None, "--subject", help="Subject or topic"),
    baseline: Optional[str] = typer.Option(
        None, "--baseline", help="Audience knowledge baseline"
    ),
    constraints: Optional[str] = typer.Option(
        None, "--constraints", help="Comma-separated constraints"
    ),
    model: str = typer.Option("gpt-4o", "--model", help="OpenAI model to use"),
    duration: str = typer.Option("45 minutes", "--duration", help="Lesson duration"),
    pptx: Optional[str] = typer.Option(
        None, "--pptx", help="Generate PowerPoint at path"
    ),
    notes: bool = typer.Option(False, "--notes", help="Generate speaker notes"),
    oer: Optional[int] = typer.Option(
        None, "--oer", help="Number of OER resources to fetch"
    ),
    zip_path: Optional[str] = typer.Option(
        None, "--zip", help="Package outputs into ZIP"
    ),
    copilot: bool = typer.Option(
        False, "--copilot", help="Export to Microsoft Copilot"
    ),
    json_only: bool = typer.Option(False, "--json-only", help="Output only raw JSON"),
    quiet: bool = typer.Option(
        False, "--quiet", "-q", help="Suppress progress messages"
    ),
):
    """
    Generate curriculum plans with AI assistance.

    Run without arguments for interactive wizard mode, or use flags for direct execution.
    """
    try:
        if not non_interactive and not any([grade, subject]):
            # Interactive wizard mode
            display_welcome()

            # Collect inputs interactively
            params = collect_basic_inputs()
            outputs = collect_output_preferences()

            # Display review
            display_parameters(params)

            if not Confirm.ask(
                "\n[bold yellow]Proceed with curriculum generation?[/bold yellow]",
                default=True,
            ):
                console.print("[yellow]Operation cancelled.[/yellow]")
                raise typer.Exit(1)

        else:
            # Non-interactive mode using flags
            if not grade or not subject:
                console.print(
                    "[red]Error: --grade and --subject are required in non-interactive mode[/red]"
                )
                raise typer.Exit(1)

            params = {
                "grade_level": grade,
                "subject": subject,
                "audience_baseline": baseline or "grade-appropriate prior knowledge",
                "constraints": parse_constraints(
                    constraints or "age-appropriate,privacy-protecting"
                ),
                "duration": duration,
                "model": model,
            }

            outputs = {
                "pptx": Path(pptx) if pptx else None,
                "notes": notes,
                "oer": oer,
                "zip": Path(zip_path) if zip_path else None,
                "copilot": copilot,
            }

        # Generate curriculum plan
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            task = progress.add_task(
                f"Generating curriculum plan using {params['model']}...", total=None
            )
            plan = plan_curriculum(params)
            progress.update(task, completed=100)

        # Display results unless quiet or json-only
        if json_only:
            print(json.dumps(plan, indent=2))
            return
        elif not quiet:
            display_curriculum_plan(plan)

        # Handle OER resources
        oer_resources = []
        if outputs.get("oer"):
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                task = progress.add_task(
                    f"Fetching {outputs['oer']} OER Commons resources for '{params['subject']}'...",
                    total=None,
                )
                oer_resources = suggest_oer(params["subject"], count=outputs["oer"])
                progress.update(task, completed=100)

            if oer_resources and not quiet:
                console.print("\n[bold blue]📚 OER Commons Resources:[/bold blue]")
                for i, url in enumerate(oer_resources, 1):
                    console.print(f"  {i}. {url}")
            elif not oer_resources and not quiet:
                console.print(
                    "\n[yellow]⚠️  No OER resources found for this topic[/yellow]"
                )

        # Track generated files
        generated_files = {"pptx_path": None, "notes_path": None}

        # Generate PowerPoint if requested
        if outputs.get("pptx"):
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                task = progress.add_task(
                    "Generating PowerPoint presentation...", total=None
                )
                create_deck(plan, outputs["pptx"])
                generated_files["pptx_path"] = outputs["pptx"]
                progress.update(task, completed=100)

            if not quiet:
                console.print(
                    f"[bold green]✅ Deck saved to {outputs['pptx']}[/bold green]"
                )

        # Generate speaker notes if requested
        if outputs.get("notes"):
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                task = progress.add_task("Generating speaker notes...", total=None)
                notes = generate_notes(plan, model=params["model"])
                md_path = save_notes_to_markdown(
                    notes, plan["lesson_title"], oer_resources=oer_resources
                )
                generated_files["notes_path"] = Path(md_path)
                progress.update(task, completed=100)

            if not quiet:
                console.print(
                    f"[bold green]✅ Speaker notes saved to {md_path}[/bold green]"
                )

        # Package outputs into ZIP if requested
        if outputs.get("zip"):
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                task = progress.add_task(
                    "Packaging outputs into ZIP file...", total=None
                )

                # Create temporary JSON file for the plan
                temp_json = None
                with tempfile.NamedTemporaryFile(
                    mode="w", suffix=".json", delete=False
                ) as f:
                    json.dump(plan, f, indent=2)
                    temp_json = Path(f.name)

                try:
                    package_path = package_outputs(
                        plan_json_path=temp_json,
                        pptx_path=generated_files["pptx_path"],
                        notes_path=generated_files["notes_path"],
                        out_zip=outputs["zip"],
                        plan_data=plan,
                    )
                    progress.update(task, completed=100)

                    if not quiet:
                        console.print(
                            f"[bold green]✅ Package saved to {package_path}[/bold green]"
                        )

                finally:
                    # Clean up temporary JSON file
                    if temp_json and temp_json.exists():
                        temp_json.unlink()

        # Export to Microsoft Copilot if requested
        if outputs.get("copilot"):
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                task = progress.add_task(
                    "Exporting to Microsoft 365 OneDrive with Copilot...", total=None
                )
                share_url = export_to_copilot(plan)
                progress.update(task, completed=100)

                if not quiet:
                    console.print(
                        "[bold green]✅ Presentation exported to OneDrive[/bold green]"
                    )
                    console.print(f"[bold blue]🔗 Share URL: {share_url}[/bold blue]")

        if not quiet:
            console.print("\n[bold green]🎉 Task completed successfully![/bold green]")

    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Operation cancelled by user[/yellow]")
        raise typer.Exit(1)

    except CopilotPowerPointError as e:
        console.print(f"\n[bold red]❌ Copilot export failed: {e}[/bold red]")
        raise typer.Exit(1)

    except Exception as e:
        console.print(f"\n[bold red]❌ Error: {e}[/bold red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
