"""
Content sanitizer module for filtering profanity and PII.

Provides:
- clean_text: Remove profanity and replace PII with [REDACTED]
- enforce_constraints: Apply cleaning to all user-visible strings in curriculum JSON

Uses better-profanity for profanity filtering and regex for PII detection.
"""

import re
from typing import Dict, Any, Union
from better_profanity import profanity


class ContentSanitizer:
    """Content sanitizer for educational materials."""

    def __init__(self):
        """Initialize the sanitizer with profanity filter."""
        # Initialize profanity filter
        profanity.load_censor_words()

        # PII detection patterns
        self.patterns = {
            # Full names (first + last name pattern)
            "names": re.compile(r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b"),
            # Phone numbers (various formats)
            "phones": re.compile(
                r"(\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})"
            ),
            # Email addresses
            "emails": re.compile(
                r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            ),
            # Social Security Numbers
            "ssn": re.compile(r"\b\d{3}-?\d{2}-?\d{4}\b"),
            # Credit card numbers (basic pattern)
            "credit_cards": re.compile(r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b"),
        }

    def clean_text(self, text: str) -> str:
        """
        Clean text by removing profanity and replacing PII with [REDACTED].

        Args:
            text: Input text to clean

        Returns:
            Cleaned text with profanity censored and PII redacted
        """
        if not isinstance(text, str):
            return text

        # First, remove profanity
        cleaned_text = profanity.censor(text)

        # Then replace PII patterns with [REDACTED]
        for pattern_name, pattern in self.patterns.items():
            cleaned_text = pattern.sub("[REDACTED]", cleaned_text)

        return cleaned_text

    def _clean_dict_recursively(
        self, data: Union[Dict, list, str, Any]
    ) -> Union[Dict, list, str, Any]:
        """
        Recursively clean all string values in a dictionary or list structure.

        Args:
            data: Data structure to clean

        Returns:
            Cleaned data structure
        """
        if isinstance(data, dict):
            return {
                key: self._clean_dict_recursively(value) for key, value in data.items()
            }
        elif isinstance(data, list):
            return [self._clean_dict_recursively(item) for item in data]
        elif isinstance(data, str):
            return self.clean_text(data)
        else:
            return data

    def enforce_constraints(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enforce content constraints on a curriculum plan.

        Runs clean_text on every user-visible string in the curriculum JSON.

        Args:
            plan: Curriculum plan dictionary

        Returns:
            Cleaned curriculum plan
        """
        return self._clean_dict_recursively(plan)


# Global sanitizer instance
_sanitizer = ContentSanitizer()


def clean_text(text: str) -> str:
    """
    Clean text by removing profanity and replacing PII with [REDACTED].

    Args:
        text: Input text to clean

    Returns:
        Cleaned text with profanity censored and PII redacted
    """
    return _sanitizer.clean_text(text)


def enforce_constraints(plan: Dict[str, Any]) -> Dict[str, Any]:
    """
    Enforce content constraints on a curriculum plan.

    Runs clean_text on every user-visible string in the curriculum JSON.

    Args:
        plan: Curriculum plan dictionary

    Returns:
        Cleaned curriculum plan
    """
    return _sanitizer.enforce_constraints(plan)
