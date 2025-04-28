#!/usr/bin/env python3
"""module containing max_delay function"""

import random
import asyncio


async def wait_random(max_delay=10):
    """wait for a random time and return time"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
