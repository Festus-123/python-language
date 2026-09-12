import time
from types import TracebackType

from utils import Any, Iterable, Iterator, Self


class Pipeline:
    def __init__(self, steps: list[Any]) -> None:
        self.steps = steps
        self.start_time: float | None = None

    def __enter__(self) -> Self:
        """Tracks pipeline execution start time and enters child context steps."""
        self.start_time = time.perf_counter()
        print("[Pipeline] Context session opened. Starting pipeline run...")
        for step in self.steps:
            if hasattr(step, "__enter__"):
                step.__enter__()
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        """
        session processing in pipeflow framwork
        """
        for step in reversed(self.steps):
            if hasattr(step, "__exit__"):
                step.__exit__(exc_type, exc_val, exc_tb)

        if self.start_time:
            elapsed = time.perf_counter() - self.start_time
            print(f"[Pipeline] Run completed in {elapsed:.4f}s.")
        

    def __call__(
        self, initial_input: Iterable[dict[str, Any]] | None = None
    ) -> Iterator[dict[str, Any]]:
        stream: Any = initial_input
        for step in self.steps:
            if stream is None:
                try:
                    stream = step()
                except TypeError:
                    stream = step(None)
            else:
                stream = step(stream)
        yield from stream
