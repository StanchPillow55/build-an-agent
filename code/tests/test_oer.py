"""
Tests for the OER resource finder module.
"""

import unittest
import responses
import requests
from unittest.mock import patch
from educator_agent.oer_resource_finder import suggest_oer, _make_oer_request


class TestOERResourceFinder(unittest.TestCase):
    """Test cases for OER Commons API integration."""

    @responses.activate
    def test_suggest_oer_success(self):
        """Test successful OER Commons API response."""
        # Mock API response
        mock_response = {
            "results": [
                {
                    "url": "https://www.oercommons.org/courses/biology-basics",
                    "title": "Biology Basics",
                },
                {
                    "url": "http://www.oercommons.org/courses/chemistry-intro",
                    "title": "Chemistry Introduction",
                },
                {
                    "url": "/courses/physics-fundamentals",
                    "title": "Physics Fundamentals",
                },
            ]
        }

        responses.add(
            responses.GET,
            "https://oercommons.org/api/v1/search",
            json=mock_response,
            status=200,
        )

        # Test the function
        urls = suggest_oer("science", count=3)

        # Verify results
        expected_urls = [
            "https://www.oercommons.org/courses/biology-basics",
            "https://www.oercommons.org/courses/chemistry-intro",  # http -> https
            "https://www.oercommons.org/courses/physics-fundamentals",  # relative -> absolute
        ]

        self.assertEqual(urls, expected_urls)
        self.assertEqual(len(responses.calls), 1)

        # Verify API call parameters
        call = responses.calls[0]
        self.assertIn("search=science", call.request.url)
        self.assertIn("per_page=3", call.request.url)
        self.assertIn("only=resource", call.request.url)

    @responses.activate
    def test_suggest_oer_empty_results(self):
        """Test OER Commons API with empty results."""
        mock_response = {"results": []}

        responses.add(
            responses.GET,
            "https://oercommons.org/api/v1/search",
            json=mock_response,
            status=200,
        )

        urls = suggest_oer("nonexistent-topic")

        self.assertEqual(urls, [])

    @responses.activate
    def test_suggest_oer_missing_results_key(self):
        """Test OER Commons API response without results key."""
        mock_response = {"message": "No results found"}

        responses.add(
            responses.GET,
            "https://oercommons.org/api/v1/search",
            json=mock_response,
            status=200,
        )

        urls = suggest_oer("test-topic")

        self.assertEqual(urls, [])

    @responses.activate
    def test_suggest_oer_count_limit(self):
        """Test that count parameter limits results correctly."""
        mock_response = {
            "results": [
                {"url": "https://www.oercommons.org/course1", "title": "Course 1"},
                {"url": "https://www.oercommons.org/course2", "title": "Course 2"},
                {"url": "https://www.oercommons.org/course3", "title": "Course 3"},
                {"url": "https://www.oercommons.org/course4", "title": "Course 4"},
                {"url": "https://www.oercommons.org/course5", "title": "Course 5"},
            ]
        }

        responses.add(
            responses.GET,
            "https://oercommons.org/api/v1/search",
            json=mock_response,
            status=200,
        )

        urls = suggest_oer("mathematics", count=2)

        self.assertEqual(len(urls), 2)
        self.assertEqual(urls[0], "https://www.oercommons.org/course1")
        self.assertEqual(urls[1], "https://www.oercommons.org/course2")

    @responses.activate
    def test_suggest_oer_4xx_error(self):
        """Test handling of 4xx HTTP errors (no retry)."""
        responses.add(responses.GET, "https://oercommons.org/api/v1/search", status=404)

        urls = suggest_oer("test-topic")

        # Should return fallback URLs instead of empty list
        self.assertEqual(len(urls), 5)  # Default count
        self.assertTrue(all(url.startswith("https://oercommons.org/search?q=test-topic") for url in urls))
        self.assertEqual(len(responses.calls), 1)  # Should not retry on 4xx

    @responses.activate
    def test_suggest_oer_5xx_error_with_retry(self):
        """Test handling of 5xx HTTP errors (with retry)."""
        # First two calls return 500, third succeeds
        responses.add(responses.GET, "https://oercommons.org/api/v1/search", status=500)
        responses.add(responses.GET, "https://oercommons.org/api/v1/search", status=500)
        responses.add(
            responses.GET,
            "https://oercommons.org/api/v1/search",
            json={
                "results": [
                    {"url": "https://www.oercommons.org/success", "title": "Success"}
                ]
            },
            status=200,
        )

        urls = suggest_oer("test-topic")

        self.assertEqual(urls, ["https://www.oercommons.org/success"])
        self.assertEqual(len(responses.calls), 3)  # Should retry on 5xx

    @responses.activate
    def test_suggest_oer_malformed_urls(self):
        """Test handling of results with missing or malformed URLs."""
        mock_response = {
            "results": [
                {"title": "Course without URL"},  # Missing URL
                {
                    "url": "https://www.oercommons.org/valid-course",
                    "title": "Valid Course",
                },
                {"url": "", "title": "Empty URL"},  # Empty URL
            ]
        }

        responses.add(
            responses.GET,
            "https://oercommons.org/api/v1/search",
            json=mock_response,
            status=200,
        )

        urls = suggest_oer("test-topic")

        # Should only return the valid URL
        self.assertEqual(urls, ["https://www.oercommons.org/valid-course"])

    def test_url_conversion(self):
        """Test URL conversion logic with various URL formats."""
        with responses.RequestsMock() as rsps:
            test_cases = [
                (
                    "https://www.oercommons.org/course",
                    "https://www.oercommons.org/course",
                ),
                (
                    "http://www.oercommons.org/course",
                    "https://www.oercommons.org/course",
                ),
                (
                    "/courses/relative-path",
                    "https://www.oercommons.org/courses/relative-path",
                ),
            ]

            for input_url, expected_url in test_cases:
                rsps.reset()
                mock_response = {
                    "results": [{"url": input_url, "title": "Test Course"}]
                }

                rsps.add(
                    responses.GET,
                    "https://oercommons.org/api/v1/search",
                    json=mock_response,
                    status=200,
                )

                urls = suggest_oer("test")
                self.assertEqual(
                    urls, [expected_url], f"Failed for input URL: {input_url}"
                )


if __name__ == "__main__":
    unittest.main()
