#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of a mixed list
containing both integers and floating-point numbers.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of numbers (int or float).

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    return float(sum(mxd_lst))
