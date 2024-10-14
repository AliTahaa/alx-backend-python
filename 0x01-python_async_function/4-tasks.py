#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
task_wait_rand = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ returns the list of all the delays """
    futs = [task_wait_rand(max_delay) for _ in range(n)]
    futs = asyncio.as_completed(futs)
    delay = [await fut for fut in futs]
    return delay
