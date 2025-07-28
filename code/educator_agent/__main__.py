"""
Thin shell for invoking the Typer-based CLI wizard.
"""

import sys
from .cli import app

if __name__ == "__main__":
    sys.exit(app())
