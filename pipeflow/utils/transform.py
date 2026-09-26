import json
from datetime import datetime
from pathlib import Path
from types import TracebackType

from utils import Any, Iterable, Iterator, Self
from utils.decorators import log_step


class Transform:
    """Pipeline sink to append structured dictionary logs into JSON Lines files."""

    def __init__(self, output_name: str) -> None:
        self.output_name = output_name
        self.file_handle: Any = None

        if isinstance(output_name, str):
            self.target_dir = Path(f"{output_name}-folder")
            self.target_dir.mkdir(parents=True, exist_ok=True)
            self.file_path = self.target_dir / f"{output_name}.json"
        else:
            self.file_path = None

    def __enter__(self) -> Self:
        """Opens the output file handle when entering context."""
        if self.file_path is None:
            raise ValueError("Transform requires a valid output path.")
        self.file_handle = open(self.file_path, "a", encoding="utf-8")
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        """Ensures file handles are flushed and closed upon exit."""
        if self.file_handle:
            self.file_handle.close()
            self.file_handle = None
        # Propagate exceptions if any occurred

    @log_step
    def __call__(self, stream: Iterable[dict[str, Any]]) -> Iterator[dict[str, Any]]:
        for item in stream:
            if callable(self.output_name):
                record = self.output_name(item)
            else:
                record = item

            if self.file_path:
                serializable_item = item.copy()
                if isinstance(serializable_item.get("timestamp"), datetime):
                    serializable_item["timestamp"] = serializable_item[
                        "timestamp"
                    ].isoformat()

                if self.file_handle:
                    self.file_handle.write(json.dumps(serializable_item) + "\n")
                else:
                    with open(self.file_path, "a", encoding="utf-8") as file:
                        file.write(json.dumps(serializable_item) + "\n")
            yield record
