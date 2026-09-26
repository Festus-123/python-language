import os

import numpy as np

from datavault.utils.aggregate import Aggregate
from datavault.utils.createdataset import DatasetGenerator
from datavault.utils.validator import ValidateBinFileContent


def test_dataset_generation(tmp_bin_file):
    """Tests if DatasetGenerator creates the file with the expected byte size."""
    count = 10_000
    generator = DatasetGenerator(tmp_bin_file, count)
    generator()

    assert os.path.exists(tmp_bin_file)
    # File size should include header overhead + 10,000 * 3 float32s (12 bytes per row)
    assert os.path.getsize(tmp_bin_file) > (count * 3 * 4)


def test_validation_success(tmp_bin_file):
    """Tests validation on a valid binary file."""
    count = 5_000
    DatasetGenerator(tmp_bin_file, count)()

    validator = ValidateBinFileContent(
        tmp_bin_file, expected_rows=count, expected_cols=3
    )
    validated_data = validator()

    assert isinstance(validated_data, np.ndarray)
    assert validated_data.shape == (count, 3)


def test_validation_row_mismatch_uses_header_row_count(tmp_bin_file):
    """Accepts a differing row override and uses the file header row count."""
    count = 5_000
    DatasetGenerator(tmp_bin_file, count)()

    validator = ValidateBinFileContent(
        tmp_bin_file, expected_rows=10_000, expected_cols=3
    )

    validated_data = validator()

    assert validator.expected_rows == count
    assert validated_data.shape == (count, 3)


def test_aggregation(tmp_bin_file):
    """Tests processing pipeline through Aggregate."""
    count = 1_000
    DatasetGenerator(tmp_bin_file, count)()

    validated_data = ValidateBinFileContent(
        tmp_bin_file, expected_rows=count, expected_cols=3
    )()
    aggregator = Aggregate(dataset=validated_data, usable_data=validated_data)

    # Ensure pipeline completes without error
    aggregator()
