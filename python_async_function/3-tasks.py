#!/usr/bin/env python3
"""
This module provides a regular function that creates and returns
an asyncio.Task object using a coroutine.
"""
import asyncio


# Importing wait_random from the 0-basic_async_syntax file
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task from the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the coroutine.

    Returns:
        asyncio.Task: A task object wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
