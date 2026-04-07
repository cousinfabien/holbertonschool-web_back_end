#!/usr/bin/env python3
"""
This module provides a function that calculates the length of elements
within an iterable object, demonstrating advanced type annotations.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains the sequence and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence objects.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple is
        (sequence, length_of_sequence).
    """
    return [(i, len(i)) for i in lst]
