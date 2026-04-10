#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields random numbers.
It demonstrates the use of the async yield syntax in Python 3.9.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutines that loops ten times, waiting one second each time
    and yielding a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
