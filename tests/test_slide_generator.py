"""
Tests for the slide generator module.

Tests the PowerPoint generation functionality with curriculum plan data.
"""

import tempfile
from pathlib import Path
from unittest.mock import patch, Mock
import sys
import os

# Add the code directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

from educator_agent.slide_generator import (  # noqa: E402
    sanitize_keyword,
    download_image,
    create_deck,
)


class TestSlideGenerator:
    """Test suite for slide generator functionality."""

    def test_sanitize_keyword(self):
        """Test keyword sanitization for image search."""
        # Test basic sanitization
        assert sanitize_keyword("Hello World") == "hello+world"

        # Test special character removal
        assert sanitize_keyword("Test@#$%") == "test"

        # Test multiple spaces
        assert sanitize_keyword("Multiple   Spaces") == "multiple+spaces"

        # Test empty string
        assert sanitize_keyword("") == ""

        # Test numbers and letters
        assert sanitize_keyword("Test 123 ABC") == "test+123+abc"

    @patch("educator_agent.slide_generator.requests.get")
    def test_download_image_success(self, mock_get):
        """Test successful image download."""
        # Mock successful response
        mock_response = Mock()
        mock_response.iter_content.return_value = [b"fake_image_data"]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Mock PIL Image
        with patch("educator_agent.slide_generator.Image.open") as mock_image_open:
            mock_img = Mock()
            mock_img.width = 1200
            mock_img.height = 800
            mock_img.resize.return_value = mock_img
            mock_img.save.return_value = None
            mock_image_open.return_value.__enter__.return_value = mock_img

            result = download_image("test keyword")

            # Should return a Path object
            assert result is not None
            assert isinstance(result, Path)

    @patch("educator_agent.slide_generator.requests.get")
    def test_download_image_failure(self, mock_get):
        """Test image download failure handling."""
        # Mock failed response
        mock_get.side_effect = Exception("Network error")

        result = download_image("test keyword")

        # Should return None on failure
        assert result is None

    def test_create_deck_basic(self):
        """Test basic PowerPoint deck creation."""
        # Sample curriculum plan data
        sample_plan = {
            "lesson_title": "Test Lesson",
            "learning_objectives": [
                "Students will understand concept A",
                "Students will demonstrate skill B",
            ],
            "content_outline": [
                {
                    "title": "Introduction",
                    "description": "Basic introduction to the topic",
                },
                {
                    "title": "Main Content",
                    "description": "Detailed exploration of key concepts",
                },
            ],
            "suggested_assessments": ["Quiz on basic concepts", "Hands-on activity"],
        }

        # Create temporary output file
        with tempfile.NamedTemporaryFile(suffix=".pptx", delete=False) as tmp_file:
            output_path = Path(tmp_file.name)

        try:
            # Mock image download to avoid network calls
            with patch(
                "educator_agent.slide_generator.download_image", return_value=None
            ):
                create_deck(sample_plan, output_path)

            # Verify file was created
            assert output_path.exists()
            assert output_path.stat().st_size > 0

        finally:
            # Clean up
            if output_path.exists():
                output_path.unlink()

    def test_create_deck_empty_plan(self):
        """Test deck creation with minimal plan data."""
        # Minimal plan data
        minimal_plan = {
            "lesson_title": "Empty Lesson",
            "learning_objectives": [],
            "content_outline": [],
            "suggested_assessments": [],
        }

        # Create temporary output file
        with tempfile.NamedTemporaryFile(suffix=".pptx", delete=False) as tmp_file:
            output_path = Path(tmp_file.name)

        try:
            create_deck(minimal_plan, output_path)

            # Should still create a valid file
            assert output_path.exists()
            assert output_path.stat().st_size > 0

        finally:
            # Clean up
            if output_path.exists():
                output_path.unlink()

    def test_create_deck_missing_fields(self):
        """Test deck creation with missing plan fields."""
        # Plan with missing fields
        incomplete_plan = {
            "lesson_title": "Incomplete Lesson"
            # Missing other required fields
        }

        # Create temporary output file
        with tempfile.NamedTemporaryFile(suffix=".pptx", delete=False) as tmp_file:
            output_path = Path(tmp_file.name)

        try:
            # Should handle missing fields gracefully
            create_deck(incomplete_plan, output_path)

            assert output_path.exists()
            assert output_path.stat().st_size > 0

        finally:
            # Clean up
            if output_path.exists():
                output_path.unlink()

    def test_create_deck_with_subdirectory(self):
        """Test deck creation in a subdirectory that doesn't exist."""
        sample_plan = {
            "lesson_title": "Directory Test",
            "learning_objectives": ["Test objective"],
            "content_outline": [{"title": "Test", "description": "Test content"}],
            "suggested_assessments": ["Test assessment"],
        }

        # Create path with non-existent subdirectory
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / "subdir" / "test.pptx"

            with patch(
                "educator_agent.slide_generator.download_image", return_value=None
            ):
                create_deck(sample_plan, output_path)

            # Should create directory and file
            assert output_path.exists()
            assert output_path.parent.exists()
            assert output_path.stat().st_size > 0
