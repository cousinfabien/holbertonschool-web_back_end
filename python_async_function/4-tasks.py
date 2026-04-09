#!/usr/bin/env python3
"""
This module contains a function that spawns multiple tasks using
a task factory function and collects their results concurrently.
"""
import asyncio
from typing import List


# Importing task_wait_random from the previous task file
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    The function collects results as they are completed to maintain
    an ascending order of delays without using sort.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delays: List[float] = []
    # We call task_wait_random which returns an asyncio.Task immediately
    tasks: List[asyncio.Task] = [
        task_wait_random(max_delay) for _ in range(n)
    ]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
