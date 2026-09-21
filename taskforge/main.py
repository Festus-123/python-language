"""_summary_
Task fore executes task concurrently with the right concurrent approach
"""

import asyncio
import inspect
import time
from collections.abc import Callable
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from enum import Enum, auto
from types import TracebackType
from typing import Any, Self

from utils import get_async_jobs, get_process_jobs, get_thread_jobs


class TaskType(Enum):
    ASYNC_IO = auto()
    BLOCKING_IO = auto()
    CPU_BOUND = auto()


class TaskForge:
    def __init__(self: Any, sem_count: int=10, thread_pool: int = 20, proc_pool: int = 10) -> None:
        self.thread_pool = ThreadPoolExecutor(thread_pool)
        self.proc_pool = ProcessPoolExecutor(proc_pool)
        self.async_sem = asyncio.Semaphore(sem_count)

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.shutdown()

    # @cpu_bound
    def classify_task(
        self: Any, func: Callable[..., Any], is_cpu_bound: bool = False
    ) -> TaskType:
        # Unwrap any decorators to inspect the underlying original function
        unwrapped = inspect.unwrap(func)

        if inspect.iscoroutinefunction(func) or inspect.iscoroutinefunction(unwrapped):
            return TaskType.ASYNC_IO
        elif (
            is_cpu_bound
            or getattr(func, "__cpu_bound__", False)
            or getattr(unwrapped, "__cpu_bound__", False)
        ):
            return TaskType.CPU_BOUND
        return TaskType.BLOCKING_IO

    async def execute_job(
        self: Any,
        func: Callable[..., Any],
        args: tuple[Any, ...] = (),
        is_cpu_bound: bool = False,
    ) -> Any:
        task_type = self.classify_task(func, is_cpu_bound=is_cpu_bound)
        loop = asyncio.get_running_loop()

        if task_type == TaskType.ASYNC_IO:
            async with self.async_sem :
                return await func(*args)
        elif task_type == TaskType.BLOCKING_IO:
            return await loop.run_in_executor(self.thread_pool, func, *args)
        elif task_type == TaskType.CPU_BOUND:
            return await loop.run_in_executor(self.proc_pool, func, *args)

    # @log_step
    async def __call__(
        self, functions: list[tuple[Callable[..., Any], tuple[Any, ...]]]
    ) -> list[Any]:
        tasks = [self.execute_job(func=func, args=args) for func, args in functions]
        return await asyncio.gather(*tasks)

    def shutdown(self) -> None:
        self.thread_pool.shutdown()
        self.proc_pool.shutdown()


async def tast_forge_main() -> None:
    jobs_list = get_async_jobs(40) + get_thread_jobs(40) + get_process_jobs(40)
    print("[TaskForge] Process and job executor handler Starting... ")
    print("\n Starting system loop.... \n")
    first_time = time.perf_counter()

    with TaskForge(sem_count=15, thread_pool=15, proc_pool=10) as forge:
        results = await forge(jobs_list)

        print("\n <<< Completed Rsults >>> \n")
        for result in results[:5]:
            print(f"[Task Result]: {result}\n")
        print(f"... and {len(results) - 5} more results.")

    last_time = time.perf_counter()
    diff = last_time - first_time
    print(f"\n [Execution ended after {diff:.2f}s]")


if __name__ == "__main__":
    asyncio.run(tast_forge_main())


# Score from gpt.... 9/10
# score from gemini..9.2/10