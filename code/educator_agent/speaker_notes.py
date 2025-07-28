"""
Speaker notes generator module for converting curriculum plans to speaker notes.

Generates detailed speaker notes with hooks, explanations, and closing questions
for each slide in a curriculum presentation.
"""

import os
from typing import Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load OpenAI API key
client = (
    OpenAI(api_key=os.getenv("OPENAI_API_KEY")) if os.getenv("OPENAI_API_KEY") else None
)


def generate_notes(plan: Dict[str, Any], model: str = "gpt-4o") -> Dict[int, str]:
    """
    Generate speaker notes for all slides based on a curriculum plan.

    Args:
        plan: Curriculum plan dictionary from curriculum_planner
        model: OpenAI model to use for generation

    Returns:
        Dictionary mapping slide index (0-based) to speaker notes markdown
    """
    notes = {}

    # Generate notes for title slide (slide 0)
    notes[0] = generate_title_slide_notes(plan, model)

    # Generate notes for each content slide (slides 1 to n)
    for i, section in enumerate(plan["content_outline"], 1):
        notes[i] = generate_content_slide_notes(
            slide_index=i,
            title=section["title"],
            description=section["description"],
            lesson_context=plan["lesson_title"],
            model=model,
        )

    # Generate notes for assessment slide (final slide)
    assessment_slide_index = len(plan["content_outline"]) + 1
    notes[assessment_slide_index] = generate_assessment_slide_notes(plan, model)

    return notes


def generate_title_slide_notes(plan: Dict[str, Any], model: str = "gpt-4o") -> str:
    """Generate speaker notes for the title slide."""
    if not client:
        return _fallback_title_notes(plan)

    prompt = f"""For the title slide of a lesson titled "{plan['lesson_title']}", draft concise speaker notes ≤150 words.

Learning Objectives:
{chr(10).join(f'• {obj}' for obj in plan['learning_objectives'])}

Include:
- An engaging hook or analogy to open the lesson
- Brief overview of what students will learn
- A closing question to generate interest

Format as markdown."""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert educator creating engaging speaker notes. Keep notes concise, practical, and under 150 words.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Warning: Failed to generate title slide notes: {e}")
        return _fallback_title_notes(plan)


def generate_content_slide_notes(
    slide_index: int,
    title: str,
    description: str,
    lesson_context: str,
    model: str = "gpt-4o",
) -> str:
    """Generate speaker notes for a content slide."""
    if not client:
        return _fallback_content_notes(title, description)

    prompt = f"""For slide {slide_index} titled "{title}", draft concise speaker notes ≤150 words.

Slide Content: {description}
Lesson Context: {lesson_context}

Include:
- Engaging hook or analogy relevant to the topic
- Key explanation of the content
- Closing question to check understanding or transition

Format as markdown."""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert educator creating engaging speaker notes. Keep notes concise, practical, and under 150 words.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Warning: Failed to generate notes for slide {slide_index}: {e}")
        return _fallback_content_notes(title, description)


def generate_assessment_slide_notes(plan: Dict[str, Any], model: str = "gpt-4o") -> str:
    """Generate speaker notes for the assessment slide."""
    if not client:
        return _fallback_assessment_notes(plan)

    assessments_text = "\n".join(
        f"• {assessment}" for assessment in plan["suggested_assessments"]
    )

    prompt = f"""For the final assessment slide of "{plan['lesson_title']}", draft concise speaker notes ≤150 words.

Suggested Assessments:
{assessments_text}

Include:
- Engaging hook or analogy about the importance of assessment
- Key explanation of how these assessments work
- Closing question to wrap up the lesson

Format as markdown."""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert educator creating engaging speaker notes. Keep notes concise, practical, and under 150 words.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Warning: Failed to generate assessment slide notes: {e}")
        return _fallback_assessment_notes(plan)


def save_notes_to_markdown(
    notes: Dict[int, str], lesson_title: str, output_path: str = None
) -> str:
    """
    Save speaker notes to a markdown file.

    Args:
        notes: Dictionary of slide index to speaker notes
        lesson_title: Title of the lesson for filename
        output_path: Optional custom output path

    Returns:
        Path to the saved markdown file
    """
    # Generate filename from lesson title
    if output_path is None:
        safe_title = "".join(
            c for c in lesson_title if c.isalnum() or c in " -_"
        ).strip()
        safe_title = "_".join(safe_title.split())
        output_path = f"{safe_title}_notes.md"

    # Build markdown content
    markdown_content = f"# Speaker Notes: {lesson_title}\n\n"

    for slide_index in sorted(notes.keys()):
        if slide_index == 0:
            slide_title = "Title Slide"
        elif slide_index == max(notes.keys()):
            slide_title = "Assessment Slide"
        else:
            slide_title = f"Content Slide {slide_index}"

        markdown_content += f"## Slide {slide_index}: {slide_title}\n\n"
        markdown_content += notes[slide_index] + "\n\n"

    # Write to file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    return output_path


# Fallback methods for when API is unavailable
def _fallback_title_notes(plan: Dict[str, Any]) -> str:
    """Fallback speaker notes for title slide when no API key."""
    return f"""**Hook:** Welcome to our exploration of {plan['lesson_title']}! Think of this lesson as a journey where each step builds your understanding.

**Overview:** Today we'll master several key concepts that will transform how you think about this subject. By the end, you'll have practical skills you can apply immediately.

**Transition:** Before we dive in, who can share what they already know about this topic? Let's see what foundation we're building on."""


def _fallback_content_notes(title: str, description: str) -> str:
    """Fallback speaker notes for content slide when no API key."""
    return f"""**Hook:** Imagine trying to {title.lower()} without understanding the fundamentals—it would be like building a house without a foundation!

**Key Content:** {description} This concept is crucial because it connects to everything else we'll learn today.

**Check Understanding:** Can someone explain this concept in their own words? What questions do you have before we move forward?"""


def _fallback_assessment_notes(plan: Dict[str, Any]) -> str:
    """Fallback speaker notes for assessment slide when no API key."""
    return f"""**Hook:** Assessment isn't about testing—it's about celebrating what you've learned and identifying where to grow next!

**Assessment Overview:** These activities will help you demonstrate your mastery of {plan['lesson_title']} concepts while giving me insight into your learning journey.

**Wrap-up:** What's one key insight you're taking away from today's lesson? How will you apply this knowledge moving forward?"""
