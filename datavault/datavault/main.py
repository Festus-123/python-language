"""Datavault example runner."""

import time
from pathlib import Path

from datavault.utils import Aggregate, DatasetGenerator, ValidateBinFileContent, main

if __name__ == "__main__":
    main()
    bin_path = Path(__file__).with_name("data_store.bin")
    fixed_data_size = 1_000_000

    print(
        f"""
            \n DATAVAULT 
            {"_" * 40}
            
            Program starting...
        """
    )

    start_time = time.perf_counter()
    generated_data = DatasetGenerator(str(bin_path), fixed_data_size)()
    validated_data = ValidateBinFileContent(
        str(bin_path), expected_rows=fixed_data_size, expected_cols=3
    )()

    print(f"\n [INFO] Validated {validated_data.shape[0]} rows from {bin_path}\n")
    print("\n [INFO] Corruption check passed: header, size, and checksum are valid \n")

    Aggregate(dataset=generated_data, usable_data=validated_data)()

    print(f"Total execution time {(time.perf_counter() - start_time):.4f}s")
