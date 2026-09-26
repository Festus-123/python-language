# tests/test_errors.py

import pytest

from datavault.utils.aggregate import Aggregate
from datavault.utils.cli import main
from datavault.utils.validator import ValidateBinFileContent


def test_cli_dump_command(monkeypatch, capsys):
    """Hits the dump command branch in CLI."""
    monkeypatch.setattr(
        "sys.argv", ["datavault", "dump", "-i", "data_store.bin", "-f", "txt"]
    )
    main()
    captured = capsys.readouterr()
    assert "[INFO] Dumping contents" in captured.out


def test_cli_missing_input_file(monkeypatch):
    """Ensures validation propagates a missing input file error."""
    monkeypatch.setattr("sys.argv", ["datavault", "validate", "-i", "missing.bin"])
    with pytest.raises(FileNotFoundError, match="Binary file not found"):
        main()


def test_validator_file_not_found():
    """Hits missing file check in ValidateBinFileContent directly."""
    validator = ValidateBinFileContent(
        "non_existent.bin", expected_rows=100, expected_cols=3
    )
    with pytest.raises(FileNotFoundError):
        validator()


def test_validator_row_mismatch_uses_header_row_count(tmp_bin_file):
    """Uses the row count stored in the file when an override differs."""
    from datavault.utils.createdataset import DatasetGenerator

    generated_rows = 5_000
    expected_mismatched_rows = 10_000

    # Generate binary dataset
    DatasetGenerator(tmp_bin_file, generated_rows)()

    # Validate with mismatched row count expectation
    validator = ValidateBinFileContent(
        tmp_bin_file, expected_rows=expected_mismatched_rows, expected_cols=3
    )

    validated_data = validator()

    assert validator.expected_rows == generated_rows
    assert validated_data.shape == (generated_rows, 3)


def test_aggregate_direct_invocation(tmp_bin_file):
    """Tests direct Aggregate processing flow with valid dataset array."""
    from datavault.utils.createdataset import DatasetGenerator

    rows = 1_000
    DatasetGenerator(tmp_bin_file, rows)()

    validator = ValidateBinFileContent(
        tmp_bin_file, expected_rows=rows, expected_cols=3
    )
    validated_data = validator()

    # Pass matching data to Aggregate
    aggregator = Aggregate(dataset=validated_data, usable_data=validated_data)

    # Should execute without throwing errors
    aggregator()
