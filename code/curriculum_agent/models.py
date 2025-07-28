"""
Data models for curriculum generation and constraint enforcement.
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from enum import Enum


class GradeLevel(str, Enum):
    """Supported grade levels"""
    KINDERGARTEN = "Kindergarten"
    FIRST_GRADE = "1st Grade"
    SECOND_GRADE = "2nd Grade"
    THIRD_GRADE = "3rd Grade"
    FOURTH_GRADE = "4th Grade"
    FIFTH_GRADE = "5th Grade"
    SIXTH_GRADE = "6th Grade"
    SEVENTH_GRADE = "7th Grade"
    EIGHTH_GRADE = "8th Grade"
    NINTH_GRADE = "9th Grade"
    TENTH_GRADE = "10th Grade"
    ELEVENTH_GRADE = "11th Grade"
    TWELFTH_GRADE = "12th Grade"


class Constraint(BaseModel):
    """Defines a constraint for curriculum generation"""
    name: str = Field(description="Name of the constraint")
    description: str = Field(description="Detailed description of the constraint")
    priority: int = Field(default=1, ge=1, le=5, description="Priority level (1=lowest, 5=highest)")


class LessonPlanInput(BaseModel):
    """Input parameters for curriculum generation"""
    grade_level: str = Field(description="Target grade level (e.g., '8th Grade')")
    subject_topic: str = Field(description="Subject or specific topic (e.g., 'Environmental Science')")
    audience_baseline: str = Field(description="Audience knowledge baseline (e.g., 'no prior knowledge of ecosystems')")
    duration_minutes: Optional[int] = Field(default=45, description="Lesson duration in minutes")
    constraints: List[Constraint] = Field(
        default_factory=lambda: [
            Constraint(
                name="Privacy Protection",
                description="No collection or use of personal student information",
                priority=5
            ),
            Constraint(
                name="Age-Appropriate Language",
                description="Use classroom-appropriate language suitable for the grade level",
                priority=5
            ),
            Constraint(
                name="Simplified Vocabulary",
                description="Use vocabulary appropriate for the specified grade level",
                priority=4
            ),
            Constraint(
                name="No Personal Information",
                description="Avoid requesting or referencing personal student information",
                priority=5
            )
        ]
    )


class LearningObjective(BaseModel):
    """A specific learning objective"""
    id: str = Field(description="Unique identifier for the objective")
    description: str = Field(description="Clear, measurable learning objective")
    bloom_level: str = Field(description="Bloom's taxonomy level (Remember, Understand, Apply, Analyze, Evaluate, Create)")


class ContentSection(BaseModel):
    """A section of lesson content"""
    title: str = Field(description="Section title")
    duration_minutes: int = Field(description="Estimated time for this section")
    content_type: str = Field(description="Type of content (introduction, explanation, activity, etc.)")
    description: str = Field(description="Detailed description of the content")
    materials_needed: List[str] = Field(default_factory=list, description="Required materials")


class Assessment(BaseModel):
    """An assessment method"""
    type: str = Field(description="Assessment type (formative, summative, etc.)")
    method: str = Field(description="Assessment method (quiz, discussion, project, etc.)")
    description: str = Field(description="Detailed description of the assessment")
    criteria: List[str] = Field(description="Assessment criteria or rubric points")


class LessonPlanOutput(BaseModel):
    """Complete lesson plan output"""
    lesson_title: str = Field(description="Title of the lesson")
    grade_level: str = Field(description="Target grade level")
    subject: str = Field(description="Subject area")
    duration_minutes: int = Field(description="Total lesson duration")
    
    # Core lesson components
    learning_objectives: List[LearningObjective] = Field(description="List of learning objectives")
    content_breakdown: List[ContentSection] = Field(description="Structured content sections")
    assessments: List[Assessment] = Field(description="Assessment methods")
    
    # Supporting information
    prerequisites: List[str] = Field(description="Required prior knowledge or skills")
    materials: List[str] = Field(description="All required materials and resources")
    vocabulary: List[Dict[str, str]] = Field(description="Key vocabulary terms with definitions")
    
    # Constraint compliance
    constraints_applied: List[str] = Field(description="List of constraints that were enforced")
    age_appropriateness_notes: str = Field(description="Notes on age-appropriate adaptations made")
    
    # Metadata
    created_timestamp: str = Field(description="When the lesson plan was created")
    compliance_verified: bool = Field(description="Whether constraint compliance was verified")
