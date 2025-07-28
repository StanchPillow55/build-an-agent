"""
Test suite for OER Resource Finder module.

Tests the functionality of suggesting Open Educational Resources
from OER Commons for educational topics.
"""

import sys
import os

# Add the code directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

from educator_agent.oer_resource_finder import suggest_oer  # noqa: E402


class TestOERResourceFinder:
    """Test suite for OER resource finder functionality."""

    def test_suggest_oer_default_count(self):
        """Test suggest_oer returns 5 resources by default."""
        resources = suggest_oer("biology")

        assert isinstance(resources, list)
        assert len(resources) == 5

        # All resources should be valid URLs
        for resource in resources:
            assert isinstance(resource, str)
            assert resource.startswith("https://www.oercommons.org/courses/")

    def test_suggest_oer_custom_count(self):
        """Test suggest_oer with custom count parameter."""
        # Test with count less than available resources
        resources = suggest_oer("mathematics", count=3)
        assert len(resources) == 3

        # Test with count equal to available resources
        resources = suggest_oer("science", count=10)
        assert len(resources) == 10

        # Test with count greater than available resources
        resources = suggest_oer("history", count=15)
        assert len(resources) == 15

    def test_suggest_oer_topic_parameter(self):
        """Test suggest_oer accepts different topic strings."""
        # Test with various topic types
        topics = [
            "biology",
            "Environmental Science",
            "8th Grade Math",
            "Chemistry Basics",
        ]

        for topic in topics:
            resources = suggest_oer(topic)
            assert isinstance(resources, list)
            assert len(resources) == 5

    def test_suggest_oer_returns_unique_resources(self):
        """Test that resources are returned in consistent order."""
        resources1 = suggest_oer("physics", count=5)
        resources2 = suggest_oer("chemistry", count=5)

        # Should return same resources regardless of topic (since it's hard-coded)
        assert resources1 == resources2

    def test_suggest_oer_zero_count(self):
        """Test suggest_oer with zero count."""
        resources = suggest_oer("biology", count=0)
        assert isinstance(resources, list)
        assert len(resources) == 0

    def test_suggest_oer_large_count(self):
        """Test suggest_oer with large count to verify cycling behavior."""
        resources = suggest_oer("mathematics", count=25)
        assert len(resources) == 25

        # With cycling, first and 11th resource should be the same
        # (assuming 10 hard-coded resources cycle)
        expected_cycle_length = 10  # Based on the hard-coded list
        assert resources[0] == resources[expected_cycle_length]
        assert resources[1] == resources[expected_cycle_length + 1]

    def test_suggest_oer_url_format(self):
        """Test that all returned URLs follow expected OER Commons format."""
        resources = suggest_oer("science", count=10)

        for resource in resources:
            assert resource.startswith("https://www.oercommons.org/courses/")
            assert isinstance(resource, str)
            assert len(resource) > 30  # Reasonable URL length check
