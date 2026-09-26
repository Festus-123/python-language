"""Create a binary dataset file with an integrity header and checksum."""

import hashlib
import time
import types
from pathlib import Path
from typing import Any, Self

import numpy as np

from datavault.utils import log_step


class DatasetGenerator:
    def __init__(self: Any, store_name: str, store_content_size: int) -> None:
        self.store_name = str(store_name)
        self.store_path = Path(self.store_name)
        self.store_path.parent.mkdir(parents=True, exist_ok=True)
        self.store_content_size = store_content_size

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self: Any,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: types.TracebackType | None,
    ) -> None:
        pass

    @staticmethod
    def _build_binary_payload(matrix: np.ndarray) -> bytes:
        magic = b"DVBIN01\x00"
        rows = int(matrix.shape[0]).to_bytes(8, byteorder="little", signed=False)
        cols = int(matrix.shape[1]).to_bytes(4, byteorder="little", signed=False)
        payload = np.asarray(matrix, dtype=np.float32).tobytes()
        checksum = hashlib.sha256(payload).digest()
        return magic + rows + cols + checksum + payload

    @log_step
    def create_data_store_and_load_store_data(self: Any) -> np.ndarray:
        coordinates = np.random.randn(self.store_content_size, 3).astype(np.float32)
        start = time.perf_counter()

        self.store_path.write_bytes(self._build_binary_payload(coordinates))

        raw = self.store_path.read_bytes()
        payload = raw[52:]
        loaded_coords = np.frombuffer(payload, dtype=np.float32).reshape(-1, 3)
        transformed_np = loaded_coords * 1.5
        transformed_np[:, 2] += 10.0

        duration = time.perf_counter() - start
        print(f"\n {' ' * 10} NumPy Vectorized time: {duration:.4f} seconds \n")
        return transformed_np

    def __call__(self) -> Any:
        return self.create_data_store_and_load_store_data()
