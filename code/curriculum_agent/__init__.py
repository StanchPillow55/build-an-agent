"""
Curriculum Ideation & Constraint Enforcement Agent

This module provides AI-powered curriculum generation with built-in constraint
enforcement for educational content creation.
"""

from .curriculum_agent import CurriculumAgent
from .models import LessonPlanInput, LessonPlanOutput, Constraint

__all__ = ["CurriculumAgent", "LessonPlanInput", "LessonPlanOutput", "Constraint"]
