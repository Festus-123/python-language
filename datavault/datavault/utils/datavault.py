import time
from collections.abc import Generator, Iterable
from types import TracebackType
from typing import Any, Self


class Datavault:
    def __init__(self: Any, steps: list[Any]) -> None:
        self.steps = steps

    def __enter__(self) -> Self:
        """Tracks pipeline execution start time and enters child context steps."""
        self.start_time = time.perf_counter()
        print("[DataVault] Context session opened. Starting pipeline run...")
        for step in self.steps:
            if hasattr(step, "__enter__"):
                step.__enter__()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        session processing in DataVault framwork
        """
        for step in reversed(self.steps):
            if hasattr(step, "__exit__"):
                step.__exit__(exc_type, exc_val, exc_tb)

        if self.start_time:
            elapsed = time.perf_counter() - self.start_time
            print(f"[DataVault] Run completed in {elapsed:.4f}s.")

    def __call__(
        self: Any, initial_input: Iterable[Any] | None = None
    ) -> Generator[Any, Any, Any]:
        stream: Any = initial_input
        for step in self.steps:
            if stream is None:
                try:
                    stream = step()
                except TypeError:
                    stream = step(None)
            else:
                try:
                    stream = step(stream)
                except TypeError:
                    stream = step()

        if stream is None:
            return

        yield from stream
