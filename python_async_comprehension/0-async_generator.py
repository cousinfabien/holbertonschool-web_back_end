#!/usr/bin/env python3
"""
This module provides an asynchronous generator that yields random numbers.
Each number is yielded after an asynchronous delay of one second.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loop ten times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
