"""
CLI entry-point for educator_agent module.

Usage: python -m educator_agent [options]

Provides command-line interface for curriculum planning with customizable
parameters and rich-formatted JSON output.
"""

import argparse
import json
import sys
from typing import List

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

from .curriculum_planner import plan_curriculum

console = Console()


def parse_constraints(constraints_str: str) -> List[str]:
    """Parse comma-separated constraints string into list."""
    if not constraints_str:
        return []
    return [c.strip() for c in constraints_str.split(',') if c.strip()]


def create_cli_parser() -> argparse.ArgumentParser:
    """Create and configure the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog='educator_agent',
        description='AI-powered curriculum planning tool with constraint enforcement',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m educator_agent --grade "8th Grade" --subject "Environmental Science"
  python -m educator_agent --grade "5th Grade" --subject "Math" --baseline "basic arithmetic" --model gpt-4
  python -m educator_agent --grade "10th Grade" --subject "Biology" --constraints "age-appropriate,privacy-protecting"
        """
    )
    
    parser.add_argument(
        '--grade',
        type=str,
        required=True,
        help='Target grade level (e.g., "8th Grade", "5th Grade")'
    )
    
    parser.add_argument(
        '--subject',
        type=str,
        required=True,
        help='Subject or topic (e.g., "Environmental Science", "Mathematics")'
    )
    
    parser.add_argument(
        '--baseline',
        type=str,
        default='grade-appropriate prior knowledge',
        help='Audience knowledge baseline (default: "grade-appropriate prior knowledge")'
    )
    
    parser.add_argument(
        '--constraints',
        type=str,
        default='age-appropriate,privacy-protecting',
        help='Comma-separated list of constraints (default: "age-appropriate,privacy-protecting")'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default='gpt-4o',
        help='OpenAI model to use (default: gpt-4o)'
    )
    
    parser.add_argument(
        '--duration',
        type=str,
        default='45 minutes',
        help='Lesson duration (default: "45 minutes")'
    )
    
    parser.add_argument(
        '--json-only',
        action='store_true',
        help='Output only raw JSON without rich formatting'
    )
    
    parser.add_argument(
        '--quiet',
        '-q',
        action='store_true',
        help='Suppress progress messages and headers'
    )
    
    return parser


def display_parameters(params: dict, quiet: bool = False) -> None:
    """Display input parameters in a formatted table."""
    if quiet:
        return
        
    console.print("\n[bold blue]📝 Input Parameters:[/bold blue]")
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Parameter", style="cyan", width=15)
    table.add_column("Value", style="yellow")
    
    # Display parameters in a nice format
    display_params = {
        "Grade Level": params.get('grade_level', ''),
        "Subject": params.get('subject', ''),
        "Baseline": params.get('audience_baseline', ''),
        "Duration": params.get('duration', ''),
        "Constraints": ', '.join(params.get('constraints', [])),
        "Model": params.get('model', 'gpt-4o')
    }
    
    for key, value in display_params.items():
        table.add_row(key, str(value))
    
    console.print(table)


def display_curriculum_plan(plan: dict, json_only: bool = False, quiet: bool = False) -> None:
    """Display the curriculum plan with rich formatting."""
    if json_only:
        # Output raw JSON for programmatic use
        print(json.dumps(plan, indent=2))
        return
    
    if not quiet:
        console.print("\n[bold green]✅ Curriculum Plan Generated Successfully![/bold green]")
    
    # Display lesson title
    console.print(Panel(
        f"[bold white]{plan['lesson_title']}[/bold white]",
        title="📚 Lesson Title",
        border_style="blue"
    ))
    
    # Display learning objectives
    console.print("\n[bold blue]🎯 Learning Objectives:[/bold blue]")
    for i, objective in enumerate(plan['learning_objectives'], 1):
        console.print(f"  {i}. {objective}")
    
    # Display content outline
    console.print("\n[bold blue]📖 Content Outline:[/bold blue]")
    content_table = Table(show_header=True, header_style="bold cyan")
    content_table.add_column("Section Title", style="green", width=25)
    content_table.add_column("Description", style="white")
    
    for section in plan['content_outline']:
        content_table.add_row(section['title'], section['description'])
    
    console.print(content_table)
    
    # Display suggested assessments
    console.print("\n[bold blue]📝 Suggested Assessments:[/bold blue]")
    for i, assessment in enumerate(plan['suggested_assessments'], 1):
        console.print(f"  {i}. {assessment}")
    
    # Display JSON output
    if not quiet:
        console.print("\n[dim]💾 JSON Output:[/dim]")
        json_str = json.dumps(plan, indent=2)
        syntax = Syntax(json_str, "json", theme="monokai", line_numbers=False)
        console.print(Panel(syntax, title="Schema-Validated JSON", border_style="dim"))


def main() -> int:
    """Main CLI entry-point."""
    parser = create_cli_parser()
    args = parser.parse_args()
    
    try:
        # Parse constraints
        constraints_list = parse_constraints(args.constraints)
        
        # Build parameters dictionary
        params = {
            'grade_level': args.grade,
            'subject': args.subject,
            'audience_baseline': args.baseline,
            'constraints': constraints_list,
            'duration': args.duration,
            'model': args.model
        }
        
        # Display header and parameters
        if not args.quiet and not args.json_only:
            console.print(Panel(
                "[bold green]🎓 Educator Agent CLI[/bold green]\n"
                "AI-powered curriculum planning with constraint enforcement",
                title="Curriculum Planner",
                border_style="green"
            ))
            display_parameters(params, args.quiet)
            console.print(f"\n[bold yellow]🔄 Generating curriculum plan using {args.model}...[/bold yellow]")
        
        # Generate curriculum plan
        plan = plan_curriculum(params)
        
        # Display results
        display_curriculum_plan(plan, args.json_only, args.quiet)
        
        if not args.quiet and not args.json_only:
            console.print("\n[bold green]🎉 Task completed successfully![/bold green]")
        
        return 0
        
    except KeyboardInterrupt:
        if not args.quiet:
            console.print("\n[yellow]⚠️  Operation cancelled by user[/yellow]")
        return 1
        
    except Exception as e:
        console.print(f"\n[bold red]❌ Error: {e}[/bold red]")
        return 1


if __name__ == '__main__':
    sys.exit(main())
