#!/usr/bin/env python3
"""
This module provides a coroutine that measures the total execution time
of running multiple asynchronous comprehensions in parallel.
"""
import asyncio
import time


# Import the async_comprehension coroutine from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather.
    Measures the total execution time and returns the duration.

    Returns:
        float: The total elapsed time in seconds.
    """
    start_time: float = time.perf_counter()

    # asyncio.gather runs all four calls concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time: float = time.perf_counter()
    return end_time - start_time
