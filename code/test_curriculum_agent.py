#!/usr/bin/env python3
"""
Test script for the Curriculum Ideation & Constraint Enforcement module.

This script demonstrates the curriculum agent functionality with the
exact inputs specified in the requirements.
"""

import json
import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from curriculum_agent import CurriculumAgent, LessonPlanInput, Constraint  # noqa: E402


def main():
    """Test the curriculum agent with the specified inputs."""
    print("🎯 Testing Curriculum Ideation & Constraint Enforcement Module")
    print("=" * 60)

    # Create test input exactly as specified
    test_input = LessonPlanInput(
        grade_level="8th Grade",
        subject_topic="Environmental Science",
        audience_baseline="no prior knowledge of ecosystems",
        duration_minutes=45,
        constraints=[
            Constraint(
                name="Privacy Protection",
                description="No collection or use of personal student information",
                priority=5,
            ),
            Constraint(
                name="Age-Appropriate Language",
                description="Use classroom-appropriate language suitable for 8th grade",
                priority=5,
            ),
            Constraint(
                name="Simplified Vocabulary",
                description="Use vocabulary appropriate for 8th grade level",
                priority=4,
            ),
            Constraint(
                name="No Personal Information",
                description="Avoid requesting or referencing personal student information",
                priority=5,
            ),
        ],
    )

    # Display input parameters
    print("📝 Input Parameters:")
    print(f"   Grade Level: {test_input.grade_level}")
    print(f"   Subject/Topic: {test_input.subject_topic}")
    print(f"   Audience Baseline: {test_input.audience_baseline}")
    print(f"   Duration: {test_input.duration_minutes} minutes")
    print(f"   Constraints: {len(test_input.constraints)} applied")
    print()

    # Initialize the agent
    print("🤖 Initializing Curriculum Agent...")
    try:
        # Try with OpenAI first, fall back to demo mode if no API key
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            agent = CurriculumAgent(api_key=api_key)
            print("✅ Agent initialized with OpenAI API")
        else:
            agent = CurriculumAgent(use_fallback=True)
            print("✅ Agent initialized in fallback/demo mode")
            print("📝 Note: Using enhanced fallback mode for demonstration")
            print(
                "   For full AI capabilities, set OPENAI_API_KEY environment variable"
            )
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")
        return

    print()

    # Generate lesson plan
    print("🎓 Generating lesson plan...")
    try:
        lesson_plan = agent.generate_lesson_plan(test_input)
        print("✅ Lesson plan generated successfully")
        print()

        # Display results in JSON format
        print("📋 Generated Lesson Plan (JSON Format):")
        print("=" * 60)

        # Convert to dict for JSON serialization
        lesson_dict = lesson_plan.model_dump()

        # Pretty print JSON
        print(json.dumps(lesson_dict, indent=2, ensure_ascii=False))

        print("=" * 60)
        print(
            "✅ Task 1 Complete: Curriculum Ideation & Constraint Enforcement module working!"
        )

        # Summary statistics
        print()
        print("📊 Lesson Plan Summary:")
        print(f"   📚 Title: {lesson_plan.lesson_title}")
        print(f"   🎯 Learning Objectives: {len(lesson_plan.learning_objectives)}")
        print(f"   📖 Content Sections: {len(lesson_plan.content_breakdown)}")
        print(f"   📝 Assessments: {len(lesson_plan.assessments)}")
        print(f"   🔒 Constraints Applied: {len(lesson_plan.constraints_applied)}")
        print(f"   ✅ Compliance Verified: {lesson_plan.compliance_verified}")

    except Exception as e:
        print(f"❌ Error generating lesson plan: {e}")
        return

    print()
    print("🎉 Test completed successfully!")


if __name__ == "__main__":
    main()
