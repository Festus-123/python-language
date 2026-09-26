import os

from datavault.utils.cli import get_expected_rows, main, parse_args


def test_cli_parse_generate():
    """Tests parsing of 'generate' subcommand arguments."""
    args = parse_args(["generate", "--count", "50000", "-o", "custom.bin"])
    assert args.command == "generate"
    assert args.count == 50000
    assert args.output == "custom.bin"


def test_cli_parse_validate():
    """Tests parsing of 'validate' subcommand arguments."""
    args = parse_args(["validate", "-i", "data.bin", "-r", "1000"])
    assert args.command == "validate"
    assert args.input == "data.bin"
    assert args.rows == 1000


def test_get_expected_rows_uses_user_value(tmp_bin_file):
    """Uses the explicit row count when the caller provides one."""
    assert get_expected_rows(tmp_bin_file, user_rows=1000) == 1000


def test_get_expected_rows_infers_rows_from_file_size(tmp_bin_file):
    """Infers rows from a valid three-column float32 payload size."""
    row_count = 1000
    with open(tmp_bin_file, "wb") as dataset_file:
        dataset_file.write(b"0" * (row_count * 3 * 4))

    assert get_expected_rows(tmp_bin_file) == row_count


def test_cli_parse_analyze():
    """Tests parsing of 'analyze' subcommand with verbose flag."""
    args = parse_args(["-v", "analyze", "-i", "mesh.bin", "-r", "100000"])
    assert args.verbose is True
    assert args.command == "analyze"
    assert args.input == "mesh.bin"
    assert args.rows == 100000


def test_cli_end_to_end_flow(tmp_bin_file, monkeypatch):
    """Simulates running generate -> validate -> analyze via CLI entry point."""

    # 1. Test Generate Command
    monkeypatch.setattr(
        "sys.argv", ["datavault", "generate", "--count", "10000", "-o", tmp_bin_file]
    )
    main()
    assert os.path.exists(tmp_bin_file)

    # 2. Test Validate Command
    monkeypatch.setattr(
        "sys.argv", ["datavault", "validate", "-i", tmp_bin_file, "-r", "10000"]
    )
    main()

    # 3. Test Analyze Command
    monkeypatch.setattr(
        "sys.argv", ["datavault", "-v", "analyze", "-i", tmp_bin_file, "-r", "10000"]
    )
    main()
