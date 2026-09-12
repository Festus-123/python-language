from types import TracebackType

from utils import Any, Callable, Self
from utils.decorators import log_step


class Validator:
    """_summary_
    validate input before attempting to proces values to yield more
    effective resilts
    """

    def __init__(
        self,
        schema: dict[str, type] | None = None,
        predicate: Callable[[dict[str, Any]], bool] | None = None,
        drop_invalid: bool=True,
    ) -> None:
        self.schema = schema or {}
        self.predicate = predicate
        self.drop_invalid = drop_invalid

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        pass  # Propagate exceptions if any occurred

    def _validate_item(self, item: dict[str, Any]) -> bool:
        if not isinstance(item, dict):
            if not self.drop_invalid:
                raise TypeError(f"Expected dict record, got {type(item).__name__}")
            return False

        for field, expected_type in self.schema.items():
            if field not in item or not isinstance(item[field], expected_type):
                if not self.drop_invalid:
                    actual_type = type(item.get(field)).__name__
                    raise TypeError(
                        f"Field '{field}' must be {expected_type.__name__}, got {actual_type}"
                    )
                return False

        if self.predicate and not self.predicate(item):
            if not self.drop_invalid:
                raise ValueError(f"Predicate validation failed for record: {item}")
            return False

        return True

    @log_step
    def __call__(self, stream: Any) -> Any:
        for item in stream:
            if self._validate_item(item):
                yield item

