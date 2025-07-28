"""
Thin shell for invoking the Typer-based CLI wizard.
"""

import sys
from .cli import app

if __name__ == "__main__":
    sys.exit(app())
                    print(f"Copilot presentation URL: {share_url}")

            except CopilotPowerPointError as e:
                console.print(f"\n[bold red]❌ Copilot export failed: {e}[/bold red]")
                return 1
            except Exception as e:
                console.print(
                    f"\n[bold red]❌ Unexpected Copilot error: {e}[/bold red]"
                )
                return 1

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


if __name__ == "__main__":
    sys.exit(main())
