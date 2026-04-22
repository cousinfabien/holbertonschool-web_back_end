#!/usr/bin/env python3
"""
This module provides a function to filter schools by a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection: A pymongo collection object.
        topic (str): The topic searched.

    Returns:
        A list of dictionaries (documents) containing the topic.
    """
    query = {"topics": topic}
    return list(mongo_collection.find(query))
