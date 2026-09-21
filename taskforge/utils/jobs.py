"""_summary_
Contains core worker functions and dynamic task list generators.
"""

import asyncio
import os
import random
import time
from collections.abc import Callable
from typing import Any

from .decorator import cpu_bound, log_step


# Core Operations
@log_step
async def fetch_data(task_id: int, delay: float) -> str:
    print(f"[Async] Task {task_id} starting (delay={delay:.2f}s)...")
    await asyncio.sleep(delay)
    return f"Async result {task_id} after {delay:.2f}s"


@log_step
def download_file(task_id: int, delay: float) -> str:
    print(f"[Thread] Task {task_id} starting (delay={delay:.2f}s)...")
    time.sleep(delay)
    return f"Thread result {task_id} after {delay:.2f}s"


@log_step
@cpu_bound
def compute_heavy_task(task_id: int, n: int) -> str:
    print(f"[Process-{os.getpid()}] Task {task_id} computing n={n}...")
    acc = 0
    for i in range(n):
        acc += i * i
    return f"Process result {task_id} computed sum to {n}"


# Batch Generators (Generate 10 tasks each using random args)
def get_async_jobs(count: int = 10) -> list[tuple[Callable[..., Any], tuple[Any, ...]]]:
    return [(fetch_data, (i + 1, round(random.uniform(0.5, 2.5), 2))) for i in range(count)]


def get_thread_jobs(count: int = 10) -> list[tuple[Callable[..., Any], tuple[Any, ...]]]:
    return [(download_file, (i + 1, round(random.uniform(0.5, 2.5), 2))) for i in range(count)]


def get_process_jobs(count: int = 10) -> list[tuple[Callable[..., Any], tuple[Any, ...]]]:
    return [(compute_heavy_task, (i + 1, random.randint(5_000_000, 15_000_000))) for i in range(count)]