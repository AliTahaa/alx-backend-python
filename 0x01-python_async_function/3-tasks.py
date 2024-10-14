#!/usr/bin/env python3
""" Create a task """
import asyncio
wait_rand = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Return a task """
    return asyncio.create_task(wait_rand(max_delay))
