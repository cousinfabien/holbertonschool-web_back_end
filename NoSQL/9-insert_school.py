#!/usr/bin/env python3
"""
This module provides a function to insert a document in a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Arbitrary keyword arguments representing the document fields.

    Returns:
        The _id of the newly created document.
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
