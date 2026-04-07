#!/usr/bin/env python3
"""
This module provides a function that converts a string and a numerical
value into a tuple, with the numerical value being squared.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and the square of a number.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value to be squared.

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v as a float.
    """
    return (k, float(v**2))
