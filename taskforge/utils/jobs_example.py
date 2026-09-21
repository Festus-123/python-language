"""_summary_
Contains the jobs to be executed by the programme
"""

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from .decorator import log_step


# async operations
@log_step
async def fetch_data(id: int, delay: int) -> str:
    print(f"[Async] Task {id} starting...")
    await asyncio.sleep(delay)
    print(f"\n [Async] Task {id} completed after {delay}s\n ")
    return f"result {id}"


@log_step
async def async_main() -> None:
    start_time = time.perf_counter()

    # Schedule all 3 coroutines concurrently on a single event loop thread
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 3), fetch_data(3, 1))

    elapsed = time.perf_counter() - start_time
    print(f"\n All tasks done in {elapsed:.2f}s: {results}\n ")


# Threading calls
@log_step
def download_file(task_id: int, delay: int) -> str:
    print(f"[Thread] Worker {task_id} starting...")
    # Blocking call: GIL is released while waiting on I/O operations
    time.sleep(delay)
    print(f"[Thread] Worker {task_id} done after {delay}s")
    return f"File {task_id}"


@log_step
def thread_main() -> None:
    start_time = time.perf_counter()
    tasks = [(1, 2), (2, 3), (3, 1)]

    # Spin up 3 OS threads inside a pool context manager
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download_file, tid, d) for tid, d in tasks]
        results = [f.result() for f in futures]

    elapsed = time.perf_counter() - start_time
    print(f"\n All threads finished in {elapsed:.2f}s: {results}\n ")
    

# Multiprocessing. CPU bound tasks, heavy computational works
@log_step
def compute_heavy_task(task_id: int, target_number: int) -> int:
    print(f"[Process] Process {task_id} starting CPU compute...")
    # True CPU-bound work executed across separate CPU cores
    total = sum(i * i for i in range(target_number))
    print(f"[Process] Process {task_id} finished compute.")
    return total

@log_step
def process_main() -> None:
    start_time = time.perf_counter()
    numbers = [(1, 10_000_000), (2, 12_000_000), (3, 8_000_000)]

    # Spawn separate OS processes across CPU cores
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(compute_heavy_task, tid, num) for tid, num in numbers
        ]
        results = [f.result() for f in futures]

    elapsed = time.perf_counter() - start_time
    print(f"All processes finished in {elapsed:.2f}s")
