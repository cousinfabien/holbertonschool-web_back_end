#!/usr/bin/env python3
"""
This module contains a coroutine that uses an asynchronous comprehension
to collect values from an asynchronous generator.
"""
from typing import List

# Import de la tâche précédente
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using an async
    comprehension and returns the list of these numbers.

    Returns:
        List[float]: A list of 10 floating-point numbers.
    """
    return [i async for i in async_generator()]
