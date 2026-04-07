#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of a list of floats
using complex type annotations.
"""


def sum_list(input_list: list[float]) -> float:
    """
    Calculates the sum of all elements in a list of floating-point numbers.

    Args:
        input_list (list[float]): A list containing only float numbers.

    Returns:
        float: The total sum of the elements in the list.
    """
    return sum(input_list)
