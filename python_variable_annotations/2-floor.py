#!/usr/bin/env python3
"""
This module contains a type-annotated function that calculates
the floor of a given floating-point number.
"""


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number as an integer.

    The floor of a number is the largest integer less than or equal to n.

    Args:
        n (float): The floating-point number to process.

    Returns:
        int: The floor value of the input.
    """
    return int(n) if n >= 0 else int(n) - 1
