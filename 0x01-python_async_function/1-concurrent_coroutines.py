#!/usr/bin/env python3
""" multiple coroutines at the same time with async """
from typing import List
import asyncio
wait_rand = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ returns the list of all the delays """
    futs = [wait_rand(max_delay) for _ in range(n)]
    futs = asyncio.as_completed(futs)
    delay = [await fut for fut in futs]
    return delay
