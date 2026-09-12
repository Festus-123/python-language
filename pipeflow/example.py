import time
from abc import ABC, abstractmethod


class PipelineStep(ABC):
    @abstractmethod
    def process(self, item):
        """Transform or filter a single item."""

    def __call__(self, stream):
        """Processes the stream item by item."""
        for item in stream:
            result = self.process(item)
            if result is not None:  # Drops items if process returns None
                yield result


class Filter(PipelineStep):
    def __init__(self, predicate):
        self.predicate = predicate

    def __call__(self, stream):
        for item in stream:
            if self.predicate(item):
                yield item


class Transform(PipelineStep):
    def __init__(self, fn):
        self.fn = fn

    def process(self, item):
        return self.fn(item)


class RemoveDuplicates(PipelineStep):
    def __init__(self, key=None):
        self.key = key
        self.seen = set()

    def __call__(self, stream):
        for item in stream:
            val = item[self.key] if self.key else item
            if val not in self.seen:
                self.seen.add(val)
                yield item


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def __call__(self, data):
        stream = data
        for step in self.steps:
            # Pass the output generator of step N as input stream to step N+1
            stream = step(stream)
        return stream


list = [1, 2, 3, 4, 5, 6]
users = ["dele", "kolade", "irawo", "wunmi", "tawosan"]

filter_item = Transform(lambda item: item == "wunmi")
print(f" Filtering item {filter_item(users)}")


pipelines = Pipeline([Filter, Transform, RemoveDuplicates])

# result = pipelines(users)


class DatabaseConnection:
    def __enter__(self):
        print("Connecting to DB...")
        time.sleep(3)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing DB connection...")


with DatabaseConnection():
    print("Querying data...")
    time.sleep(3)


class Dataset:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, index):
        return self._data[index]


ds = Dataset([10, 20, 30])
print(ds[1])  # Outputs: 20


# Lamda functions in python
# A lambda is a small, anonymous function defined inline
# on a single line. It can accept any number of arguments,
# but can only evaluate a single expression and implicitly
# return its result.#


# users = generate_one_million_users()

# from typing import Callable, Iterable, Iterator, TypeVar

# T = TypeVar("T")
# U = TypeVar("U")

# def transform(
#     items: Iterable[T],
#     function: Callable[[T], U]
# ) -> Iterator[U]:
#     ...
