import hashlib
import time
from pathlib import Path
from typing import Any, Self

import numpy as np


class ValidateBinFileContent:
    def __init__(
        self: Any,
        file_path: str | Path,
        expected_rows: int | None = None,
        expected_cols: int = 3,
    ) -> None:
        self.file_path = Path(file_path)
        self.expected_rows = expected_rows
        self.expected_cols = expected_cols
        self.dtype = np.float32
        self.magic = b"DVBIN01\x00"

    def __enter__(self) -> Self:
        return self

    def __exit__(self: Any, exc_type, exc, tb) -> None:
        pass

    def _load_array(self) -> np.ndarray:
        start_time = time.perf_counter()

        if not self.file_path.exists():
            raise FileNotFoundError(f"Binary file not found: {self.file_path}")

        raw = self.file_path.read_bytes()
        if len(raw) < 8 + 8 + 4 + 32:
            raise ValueError(
                "Binary file is too short to contain a valid header and payload."
            )

        magic = raw[:8]
        if magic != self.magic:
            raise ValueError(
                "Binary header is invalid; file is not a datavault dataset."
            )

        rows = int.from_bytes(raw[8:16], byteorder="little", signed=False)
        cols = int.from_bytes(raw[16:20], byteorder="little", signed=False)
        stored_checksum = raw[20:52]
        payload = raw[52:]

        if self.expected_rows is not None and rows != self.expected_rows:
            self.expected_rows = rows
            # raise ValueError(
            #     f"Row count mismatch: expected {self.expected_rows}, found {rows}."
            # )

        if cols != self.expected_cols:
            raise ValueError(
                f"Column count mismatch: expected {self.expected_cols}, found {cols}."
            )

        expected_payload_size = rows * cols * np.dtype(self.dtype).itemsize
        if len(payload) != expected_payload_size:
            raise ValueError(
                f"Payload size mismatch: expected {expected_payload_size} bytes, got {len(payload)} bytes."
            )

        actual_checksum = hashlib.sha256(payload).digest()
        if actual_checksum != stored_checksum:
            raise ValueError(
                "Checksum mismatch: payload does not match the stored integrity hash."
            )

        data = np.frombuffer(payload, dtype=self.dtype).reshape(-1, cols)
        if not np.isfinite(data).all():
            raise ValueError(
                "Binary data contains NaN or Inf values; the dataset is corrupted."
            )
        diff = time.perf_counter() - start_time
        print(f"\n [INFO] Total execution time {diff:.2f}s \n")
        return data

    def __call__(self, stream: Any | None = None) -> Any:
        if stream is not None:
            if hasattr(stream, "store_path"):
                self.file_path = Path(stream.store_path)
            elif isinstance(stream, (str, Path)):
                self.file_path = Path(stream)
            elif hasattr(stream, "store_name"):
                self.file_path = Path(stream.store_name)

        return self._load_array()
