#!/usr/bin/env python3
"""
This module demonstrates how to execute multiple coroutines at the same time
using asyncio and collect their results in the order they complete.
"""
import asyncio
from typing import List


# Importing wait_random from the previous file
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Results are collected as they complete, ensuring the list of delays
    is in ascending order without the need for an explicit sort() call.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = [
        asyncio.create_task(wait_random(max_delay)) for _ in range(n)
    ]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
