"""_summary_
Crete the huge datasetto use in the vectorised algorithm
"""

import time
from typing import Any, Self

import numpy as np

from utils import log_step


class DatasetGenerator:
    def __init__(self: Any, store_name: str, store_content_size: int) -> None:
        self.store_name = store_name
        self.store_content_size = store_content_size

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        pass

    @log_step
    def create_data_store_and_load_store_data(self: Any) -> None:
        # Create an array of 100,000 random 3D coordinates (float32)
        coordinates = np.random.randn(self.store_content_size, 3).astype(np.float32)

        start = time.perf_counter()

        # Save directly to binary format
        coordinates.tofile(self.store_name)

        # Read binary back into NumPy instantly
        loaded_coords = np.fromfile(self.store_name, dtype=np.float32).reshape(-1, 3)
        transformed_np = loaded_coords * 1.5
        transformed_np[:, 2] += 10.0

        duration = time.perf_counter() - start
        print(f"\n {' ' * 10} NumPy Vectorized time: {duration:.4f} seconds \n")

    def __call__(self) -> Any:
        self.create_data_store_and_load_store_data()
