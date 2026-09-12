"""
Filter recieved data by requirement or conditional function to
get value, without going through maasive set of data
"""

from types import TracebackType

from utils import Any, Callable, Iterable, Iterator, Self
from utils.decorators import log_step


class Filter:
    def __init__(self, predicate: Callable, key: Any | None = None) -> None:
        self.predicate = predicate
        self.key = key
        self.seen: set[Any] = set()
        
    def __enter__(self) -> Self:
        return self
    
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        pass

    @log_step
    def __call__(self, stream: Iterable[dict[str, Any]]) -> Iterator[dict[str, Any]]:
        for item in stream:
            identifier = item.get(self.key) if self.key else str(item)
            if identifier not in self.seen:
                self.seen.add(identifier)
                if self.predicate(item):
                    yield item
