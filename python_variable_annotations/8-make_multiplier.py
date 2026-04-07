#!/usr/bin/env python3
"""
This module contains a higher-order function that creates
multiplier functions based on a given float.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the product of that float and the multiplier.
    """
    def multiplication_func(n: float) -> float:
        """ Multiplies a float by the outer multiplier. """
        return n * multiplier

    return multiplication_func
