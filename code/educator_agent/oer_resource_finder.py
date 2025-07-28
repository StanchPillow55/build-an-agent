"""
OER Resource Finder Module

This module provides functionality to suggest Open Educational Resources (OER)
for educational topics using OER Commons.
"""

from typing import List


def suggest_oer(topic: str, count: int = 5) -> List[str]:
    """
    Suggest Open Educational Resources (OER) for a given topic.

    Args:
        topic (str): The educational topic to find resources for
        count (int): Number of resources to return (default: 5)

    Returns:
        List[str]: List of OER Commons URLs for the topic

    TODO: Implement real OER Commons search integration
    Currently returns hard-coded sample URLs for testing purposes.
    """
    # Hard-coded sample OER Commons URLs for testing
    sample_resources = [
        "https://www.oercommons.org/courses/introduction-to-biology",
        "https://www.oercommons.org/courses/environmental-science-fundamentals",
        "https://www.oercommons.org/courses/mathematics-grade-8",
        "https://www.oercommons.org/courses/chemistry-basics",
        "https://www.oercommons.org/courses/physics-concepts",
        "https://www.oercommons.org/courses/earth-science-exploration",
        "https://www.oercommons.org/courses/algebra-foundations",
        "https://www.oercommons.org/courses/geometry-essentials",
        "https://www.oercommons.org/courses/history-world-civilizations",
        "https://www.oercommons.org/courses/literature-appreciation",
    ]

    # Return the requested number of resources, cycling through if needed
    if count <= len(sample_resources):
        return sample_resources[:count]
    else:
        # If more resources requested than available, cycle through the list
        result = []
        for i in range(count):
            result.append(sample_resources[i % len(sample_resources)])
        return result
