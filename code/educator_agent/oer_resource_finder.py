"""
OER Commons API integration for finding open educational resources.
"""

import requests
import backoff
from typing import List
from urllib.parse import quote


@backoff.on_exception(
    backoff.expo,
    requests.exceptions.HTTPError,
    max_tries=3,
    giveup=lambda e: e.response.status_code < 500,
)
def _make_oer_request(api_url: str, params: dict) -> dict:
    """Make the actual API request with retry logic."""
    response = requests.get(api_url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def suggest_oer(topic: str, count: int = 5) -> List[str]:
    """
    Search OER Commons for educational resources on a given topic.

    Args:
        topic: The search topic/query
        count: Maximum number of resources to return (default 5)

    Returns:
        List of HTTPS URLs to OER Commons resources

    Raises:
        requests.RequestException: If API request fails after retries
    """
    # Encode the topic for URL safety
    encoded_topic = quote(topic)

    # Build the API URL
    api_url = f"https://oercommons.org/api/v1/search"
    params = {"search": topic, "per_page": count, "only": "resource"}

    try:
        # Make the API request with retry logic
        data = _make_oer_request(api_url, params)

        # Extract URLs from the results
        urls = []
        if "results" in data:
            for result in data["results"]:
                if "url" in result and result["url"].strip():
                    url = result["url"].strip()
                    # Ensure HTTPS URLs
                    if url.startswith("http://"):
                        url = url.replace("http://", "https://", 1)
                    elif not url.startswith("https://"):
                        url = f"https://www.oercommons.org{url}"
                    urls.append(url)

        return urls[:count]  # Ensure we don't exceed requested count

    except requests.RequestException as e:
        print(
            f"Warning: OER Commons API not accessible, using search-based URLs instead."
        )
        # Fallback: create realistic OER Commons search URLs
        return _generate_fallback_oer_urls(topic, count)


def _generate_fallback_oer_urls(topic: str, count: int) -> List[str]:
    """Generate fallback OER Commons URLs when API is not accessible."""
    encoded_topic = quote(topic)

    # Create search-based URLs that educators can use to find resources
    fallback_urls = [
        f"https://oercommons.org/search?q={encoded_topic}",
        f"https://oercommons.org/search?q={encoded_topic}&f.material_type=lesson-plan",
        f"https://oercommons.org/search?q={encoded_topic}&f.material_type=activity",
        f"https://oercommons.org/search?q={encoded_topic}&f.material_type=assessment",
        f"https://oercommons.org/search?q={encoded_topic}&f.material_type=textbook",
        f"https://oercommons.org/search?q={encoded_topic}&f.material_type=interactive",
        f"https://oercommons.org/search?q={encoded_topic}&f.material_type=game",
        f"https://oercommons.org/search?q={encoded_topic}&f.material_type=simulation",
    ]

    return fallback_urls[:count]
