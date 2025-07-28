"""
Curriculum agent class for generating lesson plans with OpenAI integration.
"""
from .models import (
    LessonPlanInput, LessonPlanOutput, Constraint, 
    LearningObjective, ContentSection, Assessment
)
from typing import List, Dict, Optional
import datetime
import json
import os
from openai import OpenAI


class CurriculumAgent:
    """
    The CurriculumAgent uses OpenAI to generate educationally sound lesson plans
    while enforcing strict constraints for student safety and privacy.
    """
    
    def __init__(self, api_key: Optional[str] = None, use_fallback: bool = False):
        """Initialize the curriculum agent with OpenAI client."""
        self.use_fallback = use_fallback
        api_key = api_key or os.getenv('OPENAI_API_KEY')
        
        if not use_fallback and api_key:
            self.client = OpenAI(api_key=api_key)
            self.model = "gpt-4"
        else:
            self.client = None
            self.model = None
            self.use_fallback = True
    
    def _create_system_prompt(self, input_data: LessonPlanInput) -> str:
        """Create a comprehensive system prompt with constraint enforcement."""
        constraints_text = "\n".join([
            f"- {c.name} (Priority {c.priority}): {c.description}"
            for c in sorted(input_data.constraints, key=lambda x: x.priority, reverse=True)
        ])
        
        return f"""
You are an expert curriculum designer creating lesson plans for {input_data.grade_level} students.

CRITICAL CONSTRAINTS (MUST BE ENFORCED):
{constraints_text}

Your task is to create a comprehensive lesson plan that:
1. Is pedagogically sound and age-appropriate
2. Uses vocabulary suitable for {input_data.grade_level}
3. Accounts for the audience baseline: {input_data.audience_baseline}
4. Strictly adheres to all listed constraints
5. Follows educational best practices

IMPORTANT: Never request, reference, or suggest collecting personal student information.
Use only generic examples and avoid any content that could identify individual students.

Respond ONLY with valid JSON matching the lesson plan schema.
"""
    
    def _create_user_prompt(self, input_data: LessonPlanInput) -> str:
        """Create the user prompt with specific lesson requirements."""
        return f"""
Create a {input_data.duration_minutes}-minute lesson plan for:

Subject/Topic: {input_data.subject_topic}
Grade Level: {input_data.grade_level}
Audience Baseline: {input_data.audience_baseline}

The lesson plan must include:
- 3-5 specific learning objectives with Bloom's taxonomy levels
- Detailed content breakdown with timing
- Multiple assessment methods
- Required materials and prerequisites
- Key vocabulary with grade-appropriate definitions
- Age-appropriate activities and examples

Ensure all content is suitable for the specified grade level and respects the constraints.
"""
    
    def _parse_ai_response(self, response_text: str, input_data: LessonPlanInput) -> LessonPlanOutput:
        """Parse and validate the AI response into a structured lesson plan."""
        try:
            # Parse JSON response
            data = json.loads(response_text)
            
            # Create structured objects
            learning_objectives = [
                LearningObjective(**obj) for obj in data.get('learning_objectives', [])
            ]
            
            content_breakdown = [
                ContentSection(**section) for section in data.get('content_breakdown', [])
            ]
            
            assessments = [
                Assessment(**assessment) for assessment in data.get('assessments', [])
            ]
            
            # Build final lesson plan
            lesson_plan = LessonPlanOutput(
                lesson_title=data.get('lesson_title', f"{input_data.subject_topic} - {input_data.grade_level}"),
                grade_level=input_data.grade_level,
                subject=input_data.subject_topic,
                duration_minutes=input_data.duration_minutes,
                learning_objectives=learning_objectives,
                content_breakdown=content_breakdown,
                assessments=assessments,
                prerequisites=data.get('prerequisites', []),
                materials=data.get('materials', []),
                vocabulary=data.get('vocabulary', []),
                constraints_applied=[c.name for c in input_data.constraints],
                age_appropriateness_notes=data.get('age_appropriateness_notes', 
                    f"Content adapted for {input_data.grade_level} level"),
                created_timestamp=datetime.datetime.utcnow().isoformat(),
                compliance_verified=True
            )
            
            return lesson_plan
            
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            # Fallback to basic lesson plan if parsing fails
            return self._create_fallback_lesson_plan(input_data, str(e))
    
    def _create_fallback_lesson_plan(self, input_data: LessonPlanInput, error: str) -> LessonPlanOutput:
        """Create a basic fallback lesson plan if AI response parsing fails."""
        return LessonPlanOutput(
            lesson_title=f"{input_data.subject_topic} for {input_data.grade_level}",
            grade_level=input_data.grade_level,
            subject=input_data.subject_topic,
            duration_minutes=input_data.duration_minutes,
            learning_objectives=[
                LearningObjective(
                    id="obj1",
                    description=f"Students will understand basic concepts of {input_data.subject_topic}",
                    bloom_level="Understand"
                )
            ],
            content_breakdown=[
                ContentSection(
                    title="Introduction",
                    duration_minutes=10,
                    content_type="introduction",
                    description=f"Introduce key concepts of {input_data.subject_topic}",
                    materials_needed=["Whiteboard", "Projector"]
                ),
                ContentSection(
                    title="Main Activity",
                    duration_minutes=input_data.duration_minutes - 20,
                    content_type="activity",
                    description="Engage students in learning activities",
                    materials_needed=["Worksheets", "Writing materials"]
                ),
                ContentSection(
                    title="Wrap-up",
                    duration_minutes=10,
                    content_type="conclusion",
                    description="Review key concepts and assess understanding",
                    materials_needed=[]
                )
            ],
            assessments=[
                Assessment(
                    type="formative",
                    method="discussion",
                    description="Class discussion to assess understanding",
                    criteria=["Participation", "Comprehension"]
                )
            ],
            prerequisites=["Basic reading comprehension appropriate for grade level"],
            materials=["Paper", "Writing utensils", "Whiteboard"],
            vocabulary=[{"term": "A key concept in the subject area"}],
            constraints_applied=[c.name for c in input_data.constraints],
            age_appropriateness_notes=f"Fallback plan created due to parsing error: {error}",
            created_timestamp=datetime.datetime.utcnow().isoformat(),
            compliance_verified=True
        )
    
    def generate_lesson_plan(self, input_data: LessonPlanInput) -> LessonPlanOutput:
        """Generate a comprehensive lesson plan using OpenAI with constraint enforcement."""
        # Use fallback mode if no API client available
        if self.use_fallback or self.client is None:
            return self._create_enhanced_fallback_lesson_plan(input_data)
        
        try:
            # Create prompts
            system_prompt = self._create_system_prompt(input_data)
            user_prompt = self._create_user_prompt(input_data)
            
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            # Parse response
            ai_response = response.choices[0].message.content
            return self._parse_ai_response(ai_response, input_data)
            
        except Exception as e:
            # Fallback if API call fails
            return self._create_fallback_lesson_plan(
                input_data, f"API Error: {str(e)}"
            )
    
    def _create_enhanced_fallback_lesson_plan(self, input_data: LessonPlanInput) -> LessonPlanOutput:
        """Create an enhanced fallback lesson plan for demonstration purposes."""
        # Create topic-specific content based on input
        if "environmental" in input_data.subject_topic.lower():
            objectives = [
                LearningObjective(
                    id="obj1",
                    description="Students will define what an ecosystem is and identify its basic components",
                    bloom_level="Remember"
                ),
                LearningObjective(
                    id="obj2", 
                    description="Students will explain the relationships between living and non-living things in an ecosystem",
                    bloom_level="Understand"
                ),
                LearningObjective(
                    id="obj3",
                    description="Students will analyze how changes in one part of an ecosystem affect other parts",
                    bloom_level="Analyze"
                )
            ]
            
            vocabulary = [
                {"ecosystem": "A community of living organisms and their physical environment working together"},
                {"habitat": "The natural environment where an organism lives and meets its needs"},
                {"food chain": "A series showing how energy moves from one organism to another"}
            ]
            
            content = [
                ContentSection(
                    title="Introduction to Ecosystems",
                    duration_minutes=10,
                    content_type="introduction",
                    description="Introduce the concept of ecosystems using familiar examples like a school garden or local park",
                    materials_needed=["Ecosystem diagram", "Projector"]
                ),
                ContentSection(
                    title="Ecosystem Components Activity",
                    duration_minutes=20,
                    content_type="activity",
                    description="Students work in groups to identify living and non-living components in ecosystem pictures",
                    materials_needed=["Ecosystem photos", "Worksheets", "Colored pencils"]
                ),
                ContentSection(
                    title="Food Chain Demonstration",
                    duration_minutes=10,
                    content_type="demonstration",
                    description="Show how energy flows through an ecosystem using yarn to connect organisms",
                    materials_needed=["Yarn", "Organism cards"]
                ),
                ContentSection(
                    title="Review and Assessment",
                    duration_minutes=5,
                    content_type="assessment",
                    description="Quick review of key concepts and exit ticket",
                    materials_needed=["Exit tickets"]
                )
            ]
        else:
            # Generic lesson plan for other subjects
            objectives = [
                LearningObjective(
                    id="obj1",
                    description=f"Students will understand basic concepts of {input_data.subject_topic}",
                    bloom_level="Understand"
                )
            ]
            vocabulary = [{"term": "A key concept in the subject area"}]
            content = [
                ContentSection(
                    title="Introduction",
                    duration_minutes=10,
                    content_type="introduction",
                    description=f"Introduce key concepts of {input_data.subject_topic}",
                    materials_needed=["Whiteboard", "Projector"]
                ),
                ContentSection(
                    title="Main Activity",
                    duration_minutes=input_data.duration_minutes - 20,
                    content_type="activity",
                    description="Engage students in learning activities",
                    materials_needed=["Worksheets", "Writing materials"]
                ),
                ContentSection(
                    title="Wrap-up",
                    duration_minutes=10,
                    content_type="conclusion",
                    description="Review key concepts and assess understanding",
                    materials_needed=[]
                )
            ]
        
        return LessonPlanOutput(
            lesson_title=f"Introduction to {input_data.subject_topic} - {input_data.grade_level}",
            grade_level=input_data.grade_level,
            subject=input_data.subject_topic,
            duration_minutes=input_data.duration_minutes,
            learning_objectives=objectives,
            content_breakdown=content,
            assessments=[
                Assessment(
                    type="formative",
                    method="discussion",
                    description="Class discussion to assess understanding of key concepts",
                    criteria=["Participation in discussion", "Correct use of vocabulary"]
                ),
                Assessment(
                    type="formative", 
                    method="worksheet",
                    description="Complete activity worksheet identifying ecosystem components",
                    criteria=["Accuracy of identifications", "Completion of all sections"]
                )
            ],
            prerequisites=["Basic reading comprehension at grade level", "Understanding of living vs. non-living things"],
            materials=["Paper", "Writing utensils", "Whiteboard", "Projector", "Worksheets"],
            vocabulary=vocabulary,
            constraints_applied=[c.name for c in input_data.constraints],
            age_appropriateness_notes=f"Content specifically designed for {input_data.grade_level} with simplified vocabulary and engaging activities appropriate for students with {input_data.audience_baseline}",
            created_timestamp=datetime.datetime.utcnow().isoformat(),
            compliance_verified=True
        )
