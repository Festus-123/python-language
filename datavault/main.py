"""_summary_
Motor....
'Vectorize your algorithimic thinking'

Objectives...
A High-Performance Binary Dataset Analyzer

Build a CLI tool that generates, stores, loads, and
analyzes large numerical datasets using NumPy and binary file I/O.

requirements :
    1. Generate large datasets
    2. stores large data set as binary (.bin)
    3. loads the stored large numerical datasets using numpy (the .bin file)
    4. carry out vectorised analysis
    5. generate a simplified report about analysis and results (Human readable format)

expectected outcome
    python datavault.py generate --rows 1000000 --output data.bin
    then
    python datavault.py analyze data.bin
    --- using argparser

    and expected output type

DATA VAULT ANALYSIS
────────────────────────────

Records:          1,000,000

Temperature
  Mean:             27.43
  Minimum:           8.21
  Maximum:          44.92

Pressure
  Mean:            101.82
  Minimum:          90.31
  Maximum:         112.74

Anomalies:             842

Processing time:      0.18s
"""

import time
from typing import Any, Self

import numpy as np
from utils import log_step


class Datavault:
    def __init__(self: Any) -> None:
        pass

    def __enter__(self) -> Self:
        return self

    def __exit__(self: Any, exc_type, exc, tb) -> None:
        pass

    @log_step
    def create_data_store_and_load_store_data(
        self: Any, store_name: str, store_content_size: int
    ) -> None:
        # Create an array of 100,000 random 3D coordinates (float32)
        coordinates = np.random.randn(store_content_size, 3).astype(np.float32)

        start = time.perf_counter()

        # Save directly to binary format
        coordinates.tofile(store_name)

        # Read binary back into NumPy instantly
        loaded_coords = np.fromfile(store_name, dtype=np.float32).reshape(-1, 3)
        transformed_np = loaded_coords * 1.5
        transformed_np[:, 2] += 10.0

        duration = time.perf_counter() - start
        print(f"\n {' ' * 10} NumPy Vectorized time: {duration:.4f} seconds \n")

    def __call__(self: Any, name: str, size: int) -> Any:
        print(f"\n {' ' * 10} DATAVAULT")
        print("_" * 50)
        print()
        self.create_data_store_and_load_store_data(
            store_name=name, store_content_size=size
        )
        print("\n Programme executed successfully...")


if __name__ == "__main__":
    datavault = Datavault()
    datavault("mesh_data.bin", 1_000_000)
