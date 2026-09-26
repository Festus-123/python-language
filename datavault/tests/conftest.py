import pytest
from pathlib import Path

@pytest.fixture
def tmp_bin_file(tmp_path):
    """Provides a temporary binary file path for isolated test runs."""
    return str(tmp_path / "test_data.bin")