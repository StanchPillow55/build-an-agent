"""
Tests for the content sanitizer module.

Tests profanity filtering, PII redaction, and constraint enforcement
on curriculum plans.
"""

import sys
import os

# Add the code directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

from educator_agent.sanitizer import (
    clean_text,
    enforce_constraints,
    ContentSanitizer,
)  # noqa: E402


class TestContentSanitizer:
    """Test suite for ContentSanitizer class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.sanitizer = ContentSanitizer()

    def test_clean_text_profanity(self):
        """Test profanity filtering."""
        # Test basic profanity filtering
        dirty_text = "This is damn difficult to understand"
        cleaned = self.sanitizer.clean_text(dirty_text)
        assert "damn" not in cleaned
        assert "*" in cleaned or "****" in cleaned  # better-profanity uses asterisks

        # Test that clean text passes through unchanged
        clean_text_input = "This is a perfectly normal educational sentence"
        cleaned = self.sanitizer.clean_text(clean_text_input)
        assert cleaned == clean_text_input

    def test_clean_text_names(self):
        """Test full name redaction."""
        text_with_names = (
            "John Smith will teach the class about Mary Johnson's research"
        )
        cleaned = self.sanitizer.clean_text(text_with_names)
        assert "John Smith" not in cleaned
        assert "Mary Johnson" not in cleaned
        assert "[REDACTED]" in cleaned

        # Should not redact single names or common words
        single_name = "John will teach the class"
        cleaned_single = self.sanitizer.clean_text(single_name)
        assert "John" in cleaned_single
        assert "[REDACTED]" not in cleaned_single

    def test_clean_text_phone_numbers(self):
        """Test phone number redaction."""
        text_with_phone = "Call me at (555) 123-4567 or 555.123.4567"
        cleaned = self.sanitizer.clean_text(text_with_phone)
        assert "(555) 123-4567" not in cleaned
        assert "555.123.4567" not in cleaned
        assert "[REDACTED]" in cleaned

    def test_clean_text_emails(self):
        """Test email redaction."""
        text_with_email = "Send questions to teacher@school.edu or admin@example.com"
        cleaned = self.sanitizer.clean_text(text_with_email)
        assert "teacher@school.edu" not in cleaned
        assert "admin@example.com" not in cleaned
        assert "[REDACTED]" in cleaned

    def test_clean_text_ssn(self):
        """Test SSN redaction."""
        text_with_ssn = "The SSN 123-45-6789 or 123456789 should be protected"
        cleaned = self.sanitizer.clean_text(text_with_ssn)
        assert "123-45-6789" not in cleaned
        assert "123456789" not in cleaned
        assert "[REDACTED]" in cleaned

    def test_clean_text_credit_cards(self):
        """Test credit card redaction."""
        text_with_cc = "Card number 1234 5678 9012 3456 or 1234-5678-9012-3456"
        cleaned = self.sanitizer.clean_text(text_with_cc)
        assert "1234 5678 9012 3456" not in cleaned
        assert "1234-5678-9012-3456" not in cleaned
        assert "[REDACTED]" in cleaned

    def test_clean_text_non_string(self):
        """Test that non-string inputs are returned unchanged."""
        assert self.sanitizer.clean_text(123) == 123
        assert self.sanitizer.clean_text(None) is None
        assert self.sanitizer.clean_text([1, 2, 3]) == [1, 2, 3]

    def test_clean_dict_recursively_simple(self):
        """Test recursive cleaning of simple dictionary."""
        dirty_dict = {
            "title": "John Smith's damn good lesson",
            "description": "Contact me at john@example.com",
        }

        cleaned = self.sanitizer._clean_dict_recursively(dirty_dict)

        assert "John Smith" not in cleaned["title"]
        assert "damn" not in cleaned["title"]
        assert "john@example.com" not in cleaned["description"]
        assert "[REDACTED]" in cleaned["title"]
        assert "[REDACTED]" in cleaned["description"]

    def test_clean_dict_recursively_nested(self):
        """Test recursive cleaning of nested structures."""
        nested_data = {
            "lesson": {
                "title": "Jane Doe's Research",
                "sections": [
                    {"name": "Introduction", "contact": "info@school.edu"},
                    {"name": "Methods", "phone": "Call (555) 987-6543"},
                ],
            },
            "metadata": {"numbers": [1, 2, 3], "author": "Bob Wilson"},
        }

        cleaned = self.sanitizer._clean_dict_recursively(nested_data)

        # Check that PII was redacted
        assert "Jane Doe" not in str(cleaned)
        assert "info@school.edu" not in str(cleaned)
        assert "(555) 987-6543" not in str(cleaned)
        assert "Bob Wilson" not in str(cleaned)
        assert "[REDACTED]" in str(cleaned)

        # Check that structure is preserved
        assert "lesson" in cleaned
        assert "sections" in cleaned["lesson"]
        assert len(cleaned["lesson"]["sections"]) == 2
        assert "metadata" in cleaned
        assert cleaned["metadata"]["numbers"] == [1, 2, 3]


class TestModuleFunctions:
    """Test module-level functions."""

    def test_clean_text_function(self):
        """Test module-level clean_text function."""
        dirty_text = "This is damn hard! Contact John Smith at john@email.com"
        cleaned = clean_text(dirty_text)

        assert "damn" not in cleaned
        assert "John Smith" not in cleaned
        assert "john@email.com" not in cleaned
        assert "[REDACTED]" in cleaned

    def test_enforce_constraints_curriculum(self):
        """Test enforce_constraints on curriculum plan structure."""
        curriculum_plan = {
            "lesson_title": "Jane Doe's damn good science lesson",
            "learning_objectives": [
                "Students will call (555) 123-4567 for more info",
                "Students will email teacher@school.edu with questions",
            ],
            "content_outline": [
                {
                    "title": "Introduction to John Smith's work",
                    "description": "Explore the research of Mary Johnson at mjohnson@university.edu",
                },
                {
                    "title": "Methods Section",
                    "description": "Contact the lab at (555) 987-6543 for damn good results",
                },
            ],
            "suggested_assessments": [
                "Email your SSN 123-45-6789 to verify identity",
                "Submit your credit card 1234-5678-9012-3456 for payment",
            ],
        }

        cleaned_plan = enforce_constraints(curriculum_plan)

        # Check that all PII and profanity was removed
        full_text = str(cleaned_plan)
        assert "Jane Doe" not in full_text
        assert "John Smith" not in full_text
        assert "Mary Johnson" not in full_text
        assert "damn" not in full_text
        assert "(555) 123-4567" not in full_text
        assert "(555) 987-6543" not in full_text
        assert "teacher@school.edu" not in full_text
        assert "mjohnson@university.edu" not in full_text
        assert "123-45-6789" not in full_text
        assert "1234-5678-9012-3456" not in full_text

        # Check that [REDACTED] placeholders are present
        assert "[REDACTED]" in full_text

        # Check that structure is preserved
        assert "lesson_title" in cleaned_plan
        assert "learning_objectives" in cleaned_plan
        assert "content_outline" in cleaned_plan
        assert "suggested_assessments" in cleaned_plan
        assert len(cleaned_plan["learning_objectives"]) == 2
        assert len(cleaned_plan["content_outline"]) == 2
        assert len(cleaned_plan["suggested_assessments"]) == 2

        # Each content outline item should have title and description
        for item in cleaned_plan["content_outline"]:
            assert "title" in item
            assert "description" in item

    def test_enforce_constraints_preserves_clean_content(self):
        """Test that clean educational content is preserved."""
        clean_curriculum = {
            "lesson_title": "Introduction to Photosynthesis",
            "learning_objectives": [
                "Students will understand the process of photosynthesis",
                "Students will identify the reactants and products",
            ],
            "content_outline": [
                {
                    "title": "What is Photosynthesis?",
                    "description": "Basic introduction to the process",
                }
            ],
            "suggested_assessments": [
                "Quiz on photosynthesis basics",
                "Lab report on leaf experiments",
            ],
        }

        cleaned_plan = enforce_constraints(clean_curriculum)

        # Clean content should be largely unchanged
        assert cleaned_plan["lesson_title"] == "Introduction to Photosynthesis"
        assert "photosynthesis" in cleaned_plan["learning_objectives"][0].lower()
        assert "What is Photosynthesis?" in cleaned_plan["content_outline"][0]["title"]
        assert "[REDACTED]" not in str(cleaned_plan)


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_strings(self):
        """Test handling of empty strings."""
        assert clean_text("") == ""
        assert clean_text("   ") == "   "

    def test_none_values(self):
        """Test handling of None values in data structures."""
        data_with_none = {
            "title": None,
            "description": "Valid content",
            "items": [None, "More content", None],
        }

        cleaned = enforce_constraints(data_with_none)
        assert cleaned["title"] is None
        assert cleaned["description"] == "Valid content"
        assert cleaned["items"][0] is None
        assert cleaned["items"][2] is None

    def test_mixed_data_types(self):
        """Test handling of mixed data types."""
        mixed_data = {
            "string": "John Doe at john@example.com",
            "number": 42,
            "boolean": True,
            "list": ["Bob Smith", 123, False],
            "nested": {"float": 3.14, "text": "Contact (555) 123-4567"},
        }

        cleaned = enforce_constraints(mixed_data)

        # Check types are preserved
        assert isinstance(cleaned["number"], int)
        assert isinstance(cleaned["boolean"], bool)
        assert isinstance(cleaned["nested"]["float"], float)

        # Check cleaning occurred on strings
        assert "John Doe" not in cleaned["string"]
        assert "john@example.com" not in cleaned["string"]
        assert "Bob Smith" not in str(cleaned["list"])
        assert "(555) 123-4567" not in cleaned["nested"]["text"]
