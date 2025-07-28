"""
Smoke test for curriculum planner module.

Tests the core functionality by mocking OpenAI responses and validating
that the JSON schema validation passes correctly.
"""

import json
import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add the code directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from educator_agent.curriculum_planner import (
    generate_prompt,
    call_llm,
    validate_plan,
    plan_curriculum,
    CURRICULUM_SCHEMA
)


class TestCurriculumPlanner:
    """Test suite for curriculum planner functionality."""
    
    def test_generate_prompt(self):
        """Test prompt generation with various parameters."""
        params = {
            "grade_level": "8th Grade",
            "subject": "Environmental Science",
            "constraints": ["age-appropriate", "privacy-protecting"],
            "duration": "45 minutes"
        }
        
        prompt = generate_prompt(params)
        
        # Assert key elements are in the prompt
        assert "8th Grade" in prompt
        assert "Environmental Science" in prompt
        assert "45 minutes" in prompt
        assert "age-appropriate" in prompt
        assert "JSON object" in prompt
        assert "lesson_title" in prompt
        assert "learning_objectives" in prompt
        assert "content_outline" in prompt
        assert "suggested_assessments" in prompt
    
    def test_validate_plan_valid_schema(self):
        """Test validation passes with valid curriculum plan."""
        valid_plan = {
            "lesson_title": "Introduction to Ecosystems",
            "learning_objectives": [
                "Students will define what an ecosystem is",
                "Students will identify biotic and abiotic factors"
            ],
            "content_outline": [
                {
                    "title": "What is an Ecosystem?",
                    "description": "Introduce ecosystem concepts"
                },
                {
                    "title": "Components of Ecosystems",
                    "description": "Explore living and non-living parts"
                }
            ],
            "suggested_assessments": [
                "Ecosystem identification worksheet",
                "Food chain construction activity"
            ]
        }
        
        # Should not raise any exception
        validate_plan(valid_plan)
    
    def test_validate_plan_invalid_schema(self):
        """Test validation fails with invalid curriculum plan."""
        invalid_plan = {
            "lesson_title": "Test Lesson",
            # Missing required fields: learning_objectives, content_outline, suggested_assessments
        }
        
        # Should raise ValueError due to missing required fields
        with pytest.raises(ValueError, match="Validation error"):
            validate_plan(invalid_plan)
    
    def test_validate_plan_invalid_content_outline(self):
        """Test validation fails with malformed content_outline."""
        invalid_plan = {
            "lesson_title": "Test Lesson",
            "learning_objectives": ["Test objective"],
            "content_outline": [
                {
                    "title": "Section 1",
                    # Missing required "description" field
                }
            ],
            "suggested_assessments": ["Test assessment"]
        }
        
        with pytest.raises(ValueError, match="Validation error"):
            validate_plan(invalid_plan)
    
    @patch('educator_agent.curriculum_planner.client')
    def test_call_llm_with_mock(self, mock_client):
        """Test LLM call with mocked OpenAI client."""
        # Mock the OpenAI response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = json.dumps({
            "lesson_title": "Mocked Lesson",
            "learning_objectives": ["Mock objective 1", "Mock objective 2"],
            "content_outline": [
                {"title": "Mock Section", "description": "Mock description"}
            ],
            "suggested_assessments": ["Mock assessment"]
        })
        
        mock_client.chat.completions.create.return_value = mock_response
        
        # Test the function
        prompt = "Test prompt"
        result = call_llm(prompt)
        
        # Assert the mocked response is returned correctly
        assert result["lesson_title"] == "Mocked Lesson"
        assert len(result["learning_objectives"]) == 2
        assert len(result["content_outline"]) == 1
        assert result["content_outline"][0]["title"] == "Mock Section"
        assert len(result["suggested_assessments"]) == 1
        
        # Verify the client was called correctly
        mock_client.chat.completions.create.assert_called_once()
        call_args = mock_client.chat.completions.create.call_args
        assert call_args[1]["model"] == "gpt-4o"
        assert len(call_args[1]["messages"]) == 2
        assert call_args[1]["messages"][1]["content"] == prompt
    
    @patch('educator_agent.curriculum_planner.client')
    def test_plan_curriculum_end_to_end(self, mock_client):
        """Test the complete plan_curriculum workflow with mocked OpenAI."""
        # Setup mock response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = json.dumps({
            "lesson_title": "Environmental Science: Ecosystem Basics",
            "learning_objectives": [
                "Students will define ecosystems and their components",
                "Students will identify relationships between organisms",
                "Students will analyze human impact on ecosystems"
            ],
            "content_outline": [
                {
                    "title": "Introduction to Ecosystems",
                    "description": "Define ecosystems and provide examples from local environment"
                },
                {
                    "title": "Ecosystem Components",
                    "description": "Explore biotic and abiotic factors through interactive activities"
                },
                {
                    "title": "Interactions and Relationships",
                    "description": "Examine predator-prey relationships and food webs"
                }
            ],
            "suggested_assessments": [
                "Ecosystem mapping activity",
                "Biotic vs abiotic sorting exercise",
                "Food web construction project",
                "Exit ticket with vocabulary terms"
            ]
        })
        
        mock_client.chat.completions.create.return_value = mock_response
        
        # Test parameters
        params = {
            "grade_level": "8th Grade",
            "subject": "Environmental Science",
            "constraints": ["age-appropriate", "privacy-protecting"],
            "duration": "45 minutes"
        }
        
        # Execute the full workflow
        result = plan_curriculum(params)
        
        # Validate the result structure and content
        assert isinstance(result, dict)
        assert "lesson_title" in result
        assert "learning_objectives" in result
        assert "content_outline" in result
        assert "suggested_assessments" in result
        
        # Validate content
        assert result["lesson_title"] == "Environmental Science: Ecosystem Basics"
        assert len(result["learning_objectives"]) == 3
        assert len(result["content_outline"]) == 3
        assert len(result["suggested_assessments"]) == 4
        
        # Validate content_outline structure
        for section in result["content_outline"]:
            assert "title" in section
            assert "description" in section
            assert isinstance(section["title"], str)
            assert isinstance(section["description"], str)
        
        # Validate the plan passes schema validation (this is the key test)
        validate_plan(result)  # Should not raise any exception
        
        # Verify OpenAI client was called
        mock_client.chat.completions.create.assert_called_once()
    
    def test_fallback_mode_no_client(self):
        """Test fallback mode when no OpenAI client is available."""
        # Temporarily patch the client to None
        with patch('educator_agent.curriculum_planner.client', None):
            prompt = "Test prompt for fallback"
            result = call_llm(prompt)
            
            # Validate fallback response structure
            assert isinstance(result, dict)
            assert "lesson_title" in result
            assert "learning_objectives" in result
            assert "content_outline" in result
            assert "suggested_assessments" in result
            
            # Validate the fallback plan passes schema validation
            validate_plan(result)  # Should not raise any exception
    
    def test_schema_compliance(self):
        """Test that the CURRICULUM_SCHEMA is properly defined."""
        # Verify required fields
        required_fields = CURRICULUM_SCHEMA["required"]
        expected_fields = ["lesson_title", "learning_objectives", "content_outline", "suggested_assessments"]
        
        assert set(required_fields) == set(expected_fields)
        
        # Verify properties structure
        properties = CURRICULUM_SCHEMA["properties"]
        assert "lesson_title" in properties
        assert "learning_objectives" in properties
        assert "content_outline" in properties
        assert "suggested_assessments" in properties
        
        # Verify content_outline has proper nested structure
        content_outline_items = properties["content_outline"]["items"]
        assert content_outline_items["type"] == "object"
        assert "title" in content_outline_items["required"]
        assert "description" in content_outline_items["required"]
