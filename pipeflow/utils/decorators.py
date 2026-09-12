"""_summary_
Hold the functions to call functtions making the system more lazy
"""

import logging
from collections.abc import Generator
from functools import wraps

from utils import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")


def log_step(fn: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to log stage initialization and output count."""

    @wraps(fn)
    def wrapper(self: Any, stream: Any = None, *args: Any, **kwargs: Any) -> Any:
        stage_name = self.__class__.__name__
        logging.info(f"Executing pipeline stage: {stage_name}")

        count = 0

        for item in fn(self, stream, *args, **kwargs):
            count += 1
            yield item
        logging.info(f"Stage '{stage_name}' emitted {count} items.")

    return wrapper


def validate_input(
    schema: dict[str, type],
) -> Callable[[Callable[..., Any]], Callable[..., Generator[Any, None, None]]]:
    """Decorator to enforce dictionary type schemas on yield items."""

    def decorator(fn: Callable[..., Any]) -> Callable[..., Generator[Any, None, None]]:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Generator[Any, None, None]:
            for item in fn(*args, **kwargs):
                if isinstance(item, dict):
                    for key, expected_type in schema.items():
                        if key in item and not isinstance(item[key], expected_type):
                            raise TypeError(
                                f"Field '{key}' must be {expected_type.__name__}, got {type(item[key]).__name__}"
                            )
                yield item

        return wrapper

    return decorator
