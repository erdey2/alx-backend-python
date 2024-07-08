#!/usr/bin/env python3
""" Asyncronous execution module """
import random
import asyncio


async def wait_random(max_delay: int = 10):
    """Runs after delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
