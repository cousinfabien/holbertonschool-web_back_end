#!/usr/bin/env python3
"""
This module provides a function to measure the average execution time
of the wait_n coroutine defined in the previous task.
"""
import time
import asyncio


# Importing wait_n from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and
    returns the average time per iteration.

    Args:
        n (int): The number of times to spawn the coroutine.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average time taken (total_time / n).
    """
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.perf_counter()
    total_time: float = end_time - start_time
    return total_time / n
