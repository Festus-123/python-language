"""
Read and Parse the logs file
"""

import random
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import TracebackType

from utils import Any, Iterator, Self
from utils.decorators import log_step


class CleanText:
    """_summary_

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
    """

    # Regex pattern matching each part of the log format
    LOG_PATTERN = re.compile(
        r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+"
        r"(?P<level>[A-Z]+)\s+"
        r"\[(?P<service>[\w_]+)\]\s+"
        r"User (?P<user_id>\d+) (?P<message>.+?)"
        r"(?: \(Timeout after (?P<latency_ms>\d+)ms\))?$"
    )

    def __init__(self, file_path: str | Path = "logs/logs.txt") -> None:
        self.file_path = Path(file_path)
        self.levels = ["ERROR", "INFO", "WARN"]
        self.services = ["auth_service", "payment_service", "user_service"]
        
    def __enter__ (self) -> Self :
        """Directory existence check before running pipeline."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        return self
    
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        pass  # Propagate exceptions if any occurred

    def generate_random_user_logs(self) -> None:
        """_summary_
        Function to create the user logs that would be used
        in this pipeline test
        """
        print("Running logs services... \n ")
        print(f"checking {self.file_path}... >>>")
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        date = datetime.now(tz=timezone.utc)

        with open(self.file_path, "w") as file:
            for i in range(1, 1001):
                level = random.choice(self.levels)
                service = random.choice(self.services)
                user_id = random.randint(1, 1000)

                start_time = date - timedelta(minutes=random.randint(1, 60))
                latency_ms = random.randint(100, 5000)

                timestamp = start_time.strftime("%Y-%m-%d %H:%M:%S")
                file.writelines(
                    f"{timestamp} {level} [{service}] User {user_id} requested action (Timeout after {latency_ms}ms) \n"
                )

    def read_user_logs_per_line(self) -> Iterator[str]:
        """_summary_
        Function to read the logs into a store
        before outline and passing items
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"Log file not found at {self.file_path}")

        with open(self.file_path, "r", encoding="utf8") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    yield clean_line

    def parse_log_line(self, line: str) -> dict[str, Any] | None:
        """Parses a single log string into a structured dictionary."""
        match = self.LOG_PATTERN.match(line.strip())
        if not match:
            return None  # Returns None for invalid or unparseable lines

        data = match.groupdict()

        # Cast fields into proper Python types
        return {
            "timestamp": datetime.strptime(
                data["timestamp"], "%Y-%m-%d %H:%M:%S"
            ).replace(tzinfo=timezone.utc),
            "level": data["level"],
            "service": data["service"],
            "user_id": int(data["user_id"]),
            "message": data["message"],
            "latency_ms": int(data["latency_ms"]) if data["latency_ms"] else None,
        }

    @log_step
    def __call__(
        self, stream: Any =None, generate_mock_data: bool = True
    ) -> Iterator[dict[str, Any]] :
        """Pipeline execution entry point. Yields parsed records downstream."""
        if generate_mock_data:
            self.generate_random_user_logs()

        if not self.file_path.exists():
            raise FileNotFoundError(f"Log file not found at {self.file_path}")

        print("\n Parsed log streams..")
        for line in self.read_user_logs_per_line():
            parsed_record = self.parse_log_line(line)
            if parsed_record:
                yield parsed_record


# def write_tool(name: str, item: dict):

#     """_summary_

#     Args:
#         name (str): _description_
#         items (dict): _description_

#     Safely creates target directory and appends
#     formatted dictionary logs.
#     """
#     target_dir = Path(f"{name}-folder")
#     target_dir.mkdir(parents=True, exist_ok=True)
#     new_file_path = target_dir / f"{name}.json"

#     serializable_item = item.copy()
#     if isinstance(serializable_item.get("timestamp"), datetime):
#         serializable_item["timestamp"] = serializable_item["timestamp"].isoformat()

#     with open(new_file_path, "a", encoding='utf-8') as file:
#         file.write(json.dumps(serializable_item) + "\n")
#         # file.writelines(f"{item}\n")
#         # for i in items :
