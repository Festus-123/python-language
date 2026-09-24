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
from utils import log_step, DatasetGenerator


class Datavault:
    def __init__(self: Any, steps: list) -> None:
        self.steps = steps

    def __enter__(self) -> Self:
        return self

    def __exit__(self: Any, exc_type, exc, tb) -> None:
        pass

    def __call__(self: Any, stream: list) -> Any:
        for step in stream:
            step()



if __name__ == "__main__":
    print(f"\n {' ' * 10} DATAVAULT")
    print("_" * 50)
    print()
    print("\n Programme starting successfully...")

