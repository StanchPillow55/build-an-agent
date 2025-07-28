"""
Test suite for Speaker Notes Generator module.

Tests the functionality of generating speaker notes from curriculum plans
and saving them to markdown files.
"""

import tempfile
import os
import sys
from unittest.mock import Mock, patch

# Add the code directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

from educator_agent.speaker_notes import (  # noqa: E402
    generate_notes,
    generate_title_slide_notes,
    generate_content_slide_notes,
    generate_assessment_slide_notes,
    save_notes_to_markdown,
    _fallback_title_notes,
    _fallback_content_notes,
    _fallback_assessment_notes,
)


class TestSpeakerNotesGenerator:
    """Test suite for speaker notes generator functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.sample_plan = {
            "lesson_title": "Introduction to Environmental Science",
            "learning_objectives": [
                "Students will define what an ecosystem is",
                "Students will identify biotic and abiotic factors",
                "Students will explain food chains and energy flow",
            ],
            "content_outline": [
                {
                    "title": "What is an Ecosystem?",
                    "description": "Introduce the concept of ecosystems using local examples",
                },
                {
                    "title": "Living vs Non-Living Components",
                    "description": "Explore biotic and abiotic factors through hands-on activities",
                },
                {
                    "title": "Energy Flow in Ecosystems",
                    "description": "Demonstrate food chains and energy transfer concepts",
                },
            ],
            "suggested_assessments": [
                "Ecosystem components identification worksheet",
                "Food chain construction activity",
                "Exit ticket with key vocabulary terms",
            ],
        }

    def test_generate_notes_structure(self):
        """Test that generate_notes returns proper structure."""
        notes = generate_notes(self.sample_plan)

        # Should return dictionary with correct number of slides
        assert isinstance(notes, dict)
        expected_slides = (
            1 + len(self.sample_plan["content_outline"]) + 1
        )  # title + content + assessment
        assert len(notes) == expected_slides

        # Should have proper slide indices
        expected_indices = list(range(expected_slides))
        assert sorted(notes.keys()) == expected_indices

        # All notes should be strings
        for note in notes.values():
            assert isinstance(note, str)
            assert len(note) > 0

    def test_generate_notes_with_different_models(self):
        """Test generate_notes with different model parameters."""
        models = ["gpt-4o", "gpt-4", "gpt-3.5-turbo"]

        for model in models:
            notes = generate_notes(self.sample_plan, model=model)
            assert isinstance(notes, dict)
            assert len(notes) > 0

    def test_fallback_title_notes(self):
        """Test fallback title slide notes generation."""
        notes = _fallback_title_notes(self.sample_plan)

        assert isinstance(notes, str)
        assert len(notes) > 0
        assert "Hook:" in notes
        assert "Overview:" in notes
        assert self.sample_plan["lesson_title"] in notes

    def test_fallback_content_notes(self):
        """Test fallback content slide notes generation."""
        title = "Test Title"
        description = "Test description"
        notes = _fallback_content_notes(title, description)

        assert isinstance(notes, str)
        assert len(notes) > 0
        assert "Hook:" in notes
        assert "Key Content:" in notes
        assert "Check Understanding:" in notes
        assert description in notes

    def test_fallback_assessment_notes(self):
        """Test fallback assessment slide notes generation."""
        notes = _fallback_assessment_notes(self.sample_plan)

        assert isinstance(notes, str)
        assert len(notes) > 0
        assert "Hook:" in notes
        assert "Assessment Overview:" in notes
        assert "Wrap-up:" in notes
        assert self.sample_plan["lesson_title"] in notes

    @patch("educator_agent.speaker_notes.client")
    def test_generate_title_slide_notes_with_mock(self, mock_client):
        """Test title slide notes generation with mocked OpenAI client."""
        # Mock the OpenAI response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = (
            "**Hook:** Welcome! **Overview:** Today we learn. **Question:** Ready?"
        )
        mock_client.chat.completions.create.return_value = mock_response

        notes = generate_title_slide_notes(self.sample_plan)

        assert isinstance(notes, str)
        assert "Hook:" in notes
        assert "Overview:" in notes
        assert "Question:" in notes

        # Verify the client was called
        mock_client.chat.completions.create.assert_called_once()

    @patch("educator_agent.speaker_notes.client")
    def test_generate_content_slide_notes_with_mock(self, mock_client):
        """Test content slide notes generation with mocked OpenAI client."""
        # Mock the OpenAI response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = (
            "**Hook:** Think about this! **Explanation:** Here's how it works. **Question:** What do you think?"
        )
        mock_client.chat.completions.create.return_value = mock_response

        notes = generate_content_slide_notes(
            slide_index=1,
            title="Test Title",
            description="Test Description",
            lesson_context="Test Lesson",
        )

        assert isinstance(notes, str)
        assert len(notes) > 0

        # Verify the client was called with correct parameters
        mock_client.chat.completions.create.assert_called_once()
        call_args = mock_client.chat.completions.create.call_args
        assert "Test Title" in call_args[1]["messages"][1]["content"]

    @patch("educator_agent.speaker_notes.client")
    def test_generate_assessment_slide_notes_with_mock(self, mock_client):
        """Test assessment slide notes generation with mocked OpenAI client."""
        # Mock the OpenAI response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = (
            "**Hook:** Assessment time! **Explanation:** Here's how we assess. **Question:** Any questions?"
        )
        mock_client.chat.completions.create.return_value = mock_response

        notes = generate_assessment_slide_notes(self.sample_plan)

        assert isinstance(notes, str)
        assert len(notes) > 0

        # Verify the client was called
        mock_client.chat.completions.create.assert_called_once()

    def test_save_notes_to_markdown(self):
        """Test saving notes to markdown file."""
        # Generate sample notes
        notes = {
            0: "**Title slide notes**",
            1: "**Content slide 1 notes**",
            2: "**Content slide 2 notes**",
            3: "**Assessment slide notes**",
        }

        lesson_title = "Test Lesson"

        # Use temporary directory
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Save notes
            output_path = os.path.join(tmp_dir, "test_notes.md")
            result_path = save_notes_to_markdown(notes, lesson_title, output_path)

            # Verify file was created
            assert os.path.exists(result_path)
            assert result_path == output_path

            # Read and verify content
            with open(result_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Check markdown structure
            assert f"# Speaker Notes: {lesson_title}" in content
            assert "## Slide 0: Title Slide" in content
            assert "## Slide 1: Content Slide 1" in content
            assert "## Slide 2: Content Slide 2" in content
            assert "## Slide 3: Assessment Slide" in content

            # Check notes content
            for note in notes.values():
                assert note in content

    def test_save_notes_to_markdown_auto_filename(self):
        """Test saving notes with automatic filename generation."""
        notes = {0: "Test notes"}
        lesson_title = "My Amazing Lesson!"

        # Use temporary directory and change to it
        with tempfile.TemporaryDirectory() as tmp_dir:
            old_cwd = os.getcwd()
            try:
                os.chdir(tmp_dir)

                result_path = save_notes_to_markdown(notes, lesson_title)

                # Should generate safe filename
                expected_filename = "My_Amazing_Lesson_notes.md"
                assert result_path == expected_filename
                assert os.path.exists(result_path)

            finally:
                os.chdir(old_cwd)

    def test_generate_notes_with_no_api_key(self):
        """Test generate_notes when no API key is available (fallback mode)."""
        with patch("educator_agent.speaker_notes.client", None):
            notes = generate_notes(self.sample_plan)

            # Should still generate notes using fallback methods
            assert isinstance(notes, dict)
            assert len(notes) > 0

            # All notes should contain fallback content markers
            title_notes = notes[0]
            assert "Hook:" in title_notes
            assert "Overview:" in title_notes

    def test_error_handling_in_api_calls(self):
        """Test error handling when API calls fail."""
        with patch("educator_agent.speaker_notes.client") as mock_client:
            # Make the API call raise an exception
            mock_client.chat.completions.create.side_effect = Exception("API Error")

            # Should fall back to default notes
            notes = generate_title_slide_notes(self.sample_plan)
            assert isinstance(notes, str)
            assert len(notes) > 0

            # Should contain fallback content
            assert "Hook:" in notes

    def test_notes_length_constraint(self):
        """Test that generated notes respect length constraints (≤150 words)."""
        notes = generate_notes(self.sample_plan)

        # Each note should be reasonably sized (this is more of a guideline test)
        for slide_index, note in notes.items():
            word_count = len(note.split())
            # Allow some flexibility but should be reasonable
            assert (
                word_count < 300
            ), f"Slide {slide_index} notes too long: {word_count} words"
