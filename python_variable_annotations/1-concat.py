#!/usr/bin/env python3
"""
This module contains a type-annotated function that handles
string concatenation operations.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the resulting string.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The combined string consisting of str1 followed by str2.
    """
    return str1 + str2
