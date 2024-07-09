#!/usr/bin/env python3
"""
asynchronous execution
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure runtime
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    return (end - start)
