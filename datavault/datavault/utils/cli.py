# datavault/utils/cli.py
import argparse
import os
import time

from .aggregate import Aggregate
from .createdataset import DatasetGenerator
from .validator import ValidateBinFileContent


def get_expected_rows(
    file_path: str, user_rows: int | None = None, cols: int = 3, dtype_size: int = 4
) -> int:
    """Returns user-provided row count or infers it dynamically from file size."""
    if user_rows is not None:
        return user_rows

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Binary file not found: {file_path}")

    total_bytes = os.path.getsize(file_path)
    bytes_per_row = cols * dtype_size

    if total_bytes == 0:
        raise ValueError(f"File '{file_path}' is empty.")

    if total_bytes % bytes_per_row != 0:
        raise ValueError(
            f"Corrupt binary file: {total_bytes} bytes is not divisible by row size ({bytes_per_row} bytes)."
        )

    return total_bytes // bytes_per_row


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        prog="datavault",
        description="A standard CLI tool for vectorized processing operations using NumPy on large datasets.",
        epilog=r"""
        Example: datavault generate --count 1000000 -o data_store.bin,
                 datavault run-e -c 1000000 -o output.bin
                """,
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=float,
        default=0.5,
        help="Filtering threshold value (default: 0.5)",
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available subcommands"
    )

    # --- Subcommand 1: Generate ---
    parser_gen = subparsers.add_parser(
        "generate", help="Generate synthetic binary data"
    )
    parser_gen.add_argument(
        "--count", type=int, default=1000000, help="Number of samples to generate"
    )
    parser_gen.add_argument(
        "-o",
        "--output",
        type=str,
        default="data_store.bin",
        help="Output binary file path",
    )

    # --- Subcommand 2: Validate ---
    parser_validator = subparsers.add_parser(
        "validate", help="Run validation process on binary data"
    )
    parser_validator.add_argument(
        "-i", "--input", type=str, required=True, help="Input binary file path"
    )
    parser_validator.add_argument(
        "-r",
        "--rows",
        type=int,
        default=None,
        help="Optional expected row count override",
    )

    # --- Subcommand 3: Analyze ---
    parser_analyze = subparsers.add_parser(
        "analyze", help="Run vectorized analysis on binary dataset"
    )
    parser_analyze.add_argument(
        "-i", "--input", type=str, required=True, help="Input binary file path"
    )
    parser_analyze.add_argument(
        "-r",
        "--rows",
        type=int,
        default=None,
        help="Optional expected row count override",
    )

    # --- Subcommand 4: Dump
    parser_dump = subparsers.add_parser("dump", help="dump content into .txt file")
    parser_dump.add_argument(
        "-i",
        "--input",
        type=str,
        default="data_store.bin",
        help="input file path to dump from",
    )
    parser_dump.add_argument(
        "-f",
        "--format",
        type=str,
        default="txt",
        choices=["txt", "json", "csv"],
        help="Export format",
    )

    #  --- Subcommand 5: Run_example ---
    parser_run_e = subparsers.add_parser("run-e", help="Run a full program example")
    parser_run_e.add_argument(
        "-c", "--count", type=int, default=1000000, help="Number of samples to generate"
    )
    parser_run_e.add_argument(
        "-o", "--output", type=str, default="output.bin", help="output binary file path"
    )

    return parser.parse_args(args)



done = r"""
    _____         _________     __          ________    
    |     \       |       |     |  \    |   |           |
    |       \     |       |     |   \   |   |______     |
    |        /    |       |     |    \  |   |           |
    |______ /     |_______|     |     \ |   |_______    .
    """


def main():
    args = parse_args()

    if args.command == "generate":
        generated_data = DatasetGenerator(args.output, args.count)
        print(f"[INFO] Generating {args.count:,} items -> {args.output}")
        generated_data()
        print(done)
        return

    if args.command == "validate":
        validator = ValidateBinFileContent(
            args.input, expected_rows=args.rows, expected_cols=3
        )
        print(f"\n [INFO] Validating file: {args.input} \n")
        validated_data = validator()
        print(f"\n [SUCCESS] Validated {validated_data.shape[0]:,} rows.\n")
        print(done)
        return

    if args.command == "analyze":
        validator = ValidateBinFileContent(
            args.input, expected_rows=args.rows, expected_cols=3
        )
        print(f"\n [INFO] Analyzing binary file: {args.input}")
        start_time = time.perf_counter()
        validated_data = validator()
        Aggregate(dataset=validated_data, usable_data=validated_data)()
        print(f"Total execution time {(time.perf_counter() - start_time):.4f}s")
        print(done)
        return

    if args.command == "dump":
        print(f"[INFO] Dumping contents from {args.input} to {args.format}")
        print(done)
        return

    if args.command == "run-e":
        # timer
        start_time = time.perf_counter()

        # generates data
        generated_data = DatasetGenerator(args.output, args.count)
        print(f"\n [INFO] Generating {args.count:,} items -> {args.output}")
        generated_data()

        # validate contents
        validator = ValidateBinFileContent(
            args.output, expected_rows=args.count, expected_cols=3
        )
        print(f"\n [INFO] Validating file: {args.output}")
        validated_data = validator()
        print(f"[SUCCESS] Validated {validated_data.shape[0]:,} rows.")

        # aggregate content
        print(f"\n [INFO] Analyzing binary file: {args.output}")
        Aggregate(dataset=validated_data, usable_data=validated_data)()

        print(
            f"Total execution time for example program {(time.perf_counter() - start_time):.4f}s"
        )
        print(done)
        return

    print(f"[ERROR] Unsupported command: {args.command}")
    

if __name__ == "__main__":
    main()


# 90 / 100 A Gemini
# 87 / 100 A Gpt