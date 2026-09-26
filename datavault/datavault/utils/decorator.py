"""_summary_
Decorators for logging stage execution and tagging CPU-bound jobs.
"""

import inspect
import logging
from collections.abc import Callable
from functools import wraps
from typing import Any

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")


def log_step(fn: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to log function execution for both sync and async tasks."""

    if inspect.iscoroutinefunction(fn):

        @wraps(fn)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = fn.__name__
            logging.info(f"Executing async stage: {func_name}")
            result = await fn(*args, **kwargs)
            logging.info(f"Stage '{func_name}' finished execution.")
            return result

        return async_wrapper

    else:

        @wraps(fn)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = fn.__name__
            logging.info(f"Executing sync stage: {func_name}")
            result = fn(*args, **kwargs)
            logging.info(f"Stage '{func_name}' finished execution.")
            return result

        return sync_wrapper
