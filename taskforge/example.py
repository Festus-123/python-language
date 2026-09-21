"""_summary_
Project — TaskForge
A Concurrent Job Processing Engine

Recives several jobs or tasks and executes them with certain approach
to reuce execution time and make concurrency straight forward

1. asyncio
2. blocking i/0 (threads)
3. multiprocessing (CPU heavy tasks)

the objective - the bigger picture:
    Respect the event loop. Bypass the GIL when necessary.

prompt: okay so now we are ready in week thre project

it is called taskforge and the mottor is
respect the event loop bypass the GIL

The program is to recieve certain amount of jobs and determine the current process to use to execute them and execute them profoundly

basically asyncio, threading and multiprocessing
"""

# writing an sync function in puthon

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


# async operations
async def fetch_data(id: int, delay: int) -> str:
    print(f"[Async] Task {id} starting...")
    await asyncio.sleep(delay)
    print(f"[Async] Task {id} completed after {delay}s")
    return f"result {id}"


async def async_main() -> None:
    start_time = time.perf_counter()

    # Schedule all 3 coroutines concurrently on a single event loop thread
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 3), fetch_data(3, 1))

    elapsed = time.perf_counter() - start_time
    print(f"All tasks done in {elapsed:.2f}s: {results}")


# Threading calls


def download_file(task_id: int, delay: int) -> str:
    print(f"[Thread] Worker {task_id} starting...")
    # Blocking call: GIL is released while waiting on I/O operations
    time.sleep(delay)
    print(f"[Thread] Worker {task_id} done after {delay}s")
    return f"File {task_id}"


def thread_main() -> None:
    start_time = time.perf_counter()
    tasks = [(1, 2), (2, 3), (3, 1)]

    # Spin up 3 OS threads inside a pool context manager
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download_file, tid, d) for tid, d in tasks]
        results = [f.result() for f in futures]

    elapsed = time.perf_counter() - start_time
    print(f"All threads finished in {elapsed:.2f}s: {results}")


# Multiprocessing. CPU bound tasks, heavy computational works
def compute_heavy_task(task_id: int, target_number: int) -> int:
    print(f"[Process] Process {task_id} starting CPU compute...")
    # True CPU-bound work executed across separate CPU cores
    total = sum(i * i for i in range(target_number))
    print(f"[Process] Process {task_id} finished compute.")
    return total


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


if __name__ == "__main__":
    first_time = time.perf_counter()
    asyncio.run(async_main())
    thread_main()
    process_main()
    last_time = time.perf_counter()
    diff = last_time - first_time
    print(f'[Execution] All proces completed execution in {diff:.2f}s')


"""_summary_
Script to dynamically generate tasks.py containing 30 decorated functions.
"""

import random


def generate_tasks_file(filename: str = "tasks.py", count_per_type: int = 10) -> None:
    code_lines = [
        '"""Auto-generated tasks file."""',
        "import asyncio",
        "import time",
        "from utils.decorator import log_step, cpu_bound\n",
    ]

    # Generate 10 Async tasks
    for i in range(1, count_per_type + 1):
        delay = round(random.uniform(0.5, 2.0), 2)
        code_lines.append(
            f"@log_step\nasync def async_job_{i}():\n"
            f'    print("[Async] Task {i} starting...")\n'
            f"    await asyncio.sleep({delay})\n"
            f'    return "async_{i}_done_after_{delay}s"\n'
        )

    # Generate 10 Thread tasks
    for i in range(1, count_per_type + 1):
        delay = round(random.uniform(0.5, 2.0), 2)
        code_lines.append(
            f"@log_step\ndef thread_job_{i}():\n"
            f'    print("[Thread] Task {i} starting...")\n'
            f"    time.sleep({delay})\n"
            f'    return "thread_{i}_done_after_{delay}s"\n'
        )

    # Generate 10 Process tasks
    for i in range(1, count_per_type + 1):
        n = random.randint(5_000_000, 10_000_000)
        code_lines.append(
            f"@log_step\n@cpu_bound\ndef process_job_{i}():\n"
            f'    print("[Process] Task {i} computing...")\n'
            f"    return sum(x * x for x in range({n}))\n"
        )

    with open(filename, "w") as f:
        f.write("\n".join(code_lines))

    print(f"[Generator] Wrote 30 decorated task functions to {filename}")