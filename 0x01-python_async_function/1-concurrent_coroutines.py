#!/usr/bin/env python3
""" concurrent execution function
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Execute multiple coroutines at the same time with asyncronous
    """
    resolves = await asyncio.gather(
        *(wait_random(max_delay) for i in range(n)))
    return sorted(resolves)
