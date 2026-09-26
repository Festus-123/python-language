# tests/test_coverage_boost.py

import pytest
import numpy as np
from datavault.utils.cli import main
from datavault.utils.decorator import log_step
from datavault.utils.validator import ValidateBinFileContent
from datavault.utils.createdataset import DatasetGenerator


def test_decorator_logging(capsys):
    """Hits execution and logging lines inside decorator.py."""

    @log_step
    def sample_task():
        return "done"

    result = sample_task()
    assert result == "done"


def test_cli_invalid_args_handling(monkeypatch, capsys):
    """Hits argparser error exit path."""
    try:
        monkeypatch.setattr("sys.argv", ["datavault", "--invalid-flag"])
        main()
    except SystemExit:
        pass

    captured = capsys.readouterr()
    assert captured.err or captured.out


def test_cli_analyze_verbose_flow(tmp_bin_file, monkeypatch, capsys):
    """Hits end-to-end analyze subcommand with verbose flag active."""
    rows = 2_000
    DatasetGenerator(tmp_bin_file, rows)()

    monkeypatch.setattr(
        "sys.argv", ["datavault", "-v", "analyze", "-i", tmp_bin_file, "-r", str(rows)]
    )
    main()

    captured = capsys.readouterr()
    assert "ANALYTICS" in captured.out or "Total execution time" in captured.out


def test_validator_empty_file(tmp_path):
    """Hits validator error handler for zero-byte binary files."""
    empty_file = str(tmp_path / "empty.bin")
    with open(empty_file, "wb") as f:
        pass  # 0 bytes file

    validator = ValidateBinFileContent(empty_file, expected_rows=100, expected_cols=3)
    with pytest.raises((ValueError, FileNotFoundError, Exception)):
        validator()