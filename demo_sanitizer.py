#!/usr/bin/env python3
"""
Demo script showing the sanitizer functionality with intentionally problematic content.
"""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "code"))

from educator_agent.sanitizer import clean_text, enforce_constraints


def demo_clean_text():
    """Demonstrate text cleaning functionality."""
    print("🧹 Text Cleaning Demo")
    print("=" * 40)

    problematic_texts = [
        "Contact John Smith at john.smith@school.edu for damn good resources",
        "Call Mary Johnson at (555) 123-4567 if you have questions",
        "Submit your SSN 123-45-6789 and credit card 4532-1234-5678-9012 for verification",
        "This is a perfectly clean educational sentence about photosynthesis",
    ]

    for text in problematic_texts:
        cleaned = clean_text(text)
        print(f"Original: {text}")
        print(f"Cleaned:  {cleaned}")
        print("-" * 40)


def demo_curriculum_sanitization():
    """Demonstrate curriculum plan sanitization."""
    print("\n📚 Curriculum Plan Sanitization Demo")
    print("=" * 50)

    problematic_curriculum = {
        "lesson_title": "Bob Wilson's damn good science lesson on chemistry",
        "learning_objectives": [
            "Students will email professor@university.edu for extra help",
            "Students will call (555) 987-6543 to schedule lab time",
            "Students will understand basic chemistry principles",
        ],
        "content_outline": [
            {
                "title": "Introduction by Dr. Sarah Lee",
                "description": "Meet at sarah.lee@school.org or call (555) 111-2222",
            },
            {
                "title": "Chemistry Basics",
                "description": "Learn about atoms, molecules, and chemical reactions",
            },
            {
                "title": "Lab Safety with John Doe",
                "description": "Safety protocols - damn important for student welfare",
            },
        ],
        "suggested_assessments": [
            "Email your answers to teacher@school.edu",
            "Submit SSN 987-65-4321 for grade verification",
            "Quiz on basic chemistry concepts",
            "Lab report on molecular structure",
        ],
    }

    print("Original problematic curriculum:")
    print(json.dumps(problematic_curriculum, indent=2))

    print("\n" + "=" * 50)
    print("After sanitization:")

    cleaned_curriculum = enforce_constraints(problematic_curriculum)
    print(json.dumps(cleaned_curriculum, indent=2))

    print("\n✅ Notice how:")
    print("- Names like 'Bob Wilson', 'Dr. Sarah Lee', 'John Doe' → [REDACTED]")
    print("- Emails like 'professor@university.edu' → [REDACTED]")
    print("- Phone numbers like '(555) 987-6543' → [REDACTED]")
    print("- SSN like '987-65-4321' → [REDACTED]")
    print("- Profanity like 'damn' → censored with asterisks")
    print("- Clean educational content remains unchanged")


if __name__ == "__main__":
    demo_clean_text()
    demo_curriculum_sanitization()
