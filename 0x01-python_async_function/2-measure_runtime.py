#!/usr/bin/env python3
""" total execution time for wait_n """
import asyncio
import time
wait_n_var = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Returns total_time """
    start_time = time.perf_counter()
    asyncio.run(wait_n_var(n, max_delay))
    end_t = time.perf_counter()
    return (end_t - start_time) / n
