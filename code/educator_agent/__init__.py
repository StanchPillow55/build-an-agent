"""
Educator Agent Package

Advanced curriculum planning and educational content generation with:
- OpenAI integration using SDK v1.x
- JSON schema validation
- Rich CLI interface
- Constraint enforcement
"""

from .curriculum_planner import (
    generate_prompt,
    call_llm,
    validate_plan,
    plan_curriculum,
    CURRICULUM_SCHEMA,
)
from .slide_generator import create_deck

__all__ = [
    "generate_prompt",
    "call_llm",
    "validate_plan",
    "plan_curriculum",
    "CURRICULUM_SCHEMA",
    "create_deck",
]
