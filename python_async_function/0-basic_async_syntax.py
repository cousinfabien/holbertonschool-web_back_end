#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that demonstrates
the basics of the asyncio library and random delay execution.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds and eventually returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The amount of time waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
