#!/usr/bin/env python3
"""
This module provides a basic type-annotated function for addition.
It demonstrates the use of float annotations for both parameters and returns.
"""


def add(a: float, b: float) -> float:
    """
    Takes two floating-point numbers and returns their sum.

    Args:
        a (float): The first number to add.
        b (float): The second number to add.

    Returns:
        float: The sum of the two input numbers.
    """
    return a + b