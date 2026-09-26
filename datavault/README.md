# Datavault

Datavault is a small Python command-line project that demonstrates a binary data
pipeline with NumPy. It can generate a synthetic dataset, store it in a custom
binary format, validate the stored bytes, and report basic record statistics.

The generated dataset contains three `float32` values per row. The values are
created with `numpy.random.randn`, so each run produces different data unless
NumPy's random seed is set by the caller.

## What the project does

- `generate` creates a binary dataset with a header, checksum, and raw payload.
- `validate` reads the file and checks its header, dimensions, payload length,
    SHA-256 checksum, and numeric values.
- `analyze` validates the file and prints record, usable-record, and corrupted-
    record counts through the aggregation step.
- `run-e` runs generation, validation, and analysis as one example workflow.
- `dump` currently reports the requested input and format; export functionality
    is not implemented yet.

## Requirements

- Python 3.10 or newer
- NumPy 1.24 or newer

## Installation

Run this command from the repository root, the directory containing
`pyproject.toml`:

```bash
python -m pip install -e .
```

The installation registers the `datavault` command-line entry point.

## Command-line reference

Global options must appear before the subcommand:

```text
datavault [-v|--verbose] [-t|--threshold VALUE] COMMAND
```

The current implementation accepts these global options, but the analysis
pipeline does not yet use `--verbose` or `--threshold` to change its output.

### Generate

Generate a dataset. Defaults are one million rows and `data_store.bin`.

```bash
datavault generate --count 100000 -o data_store.bin
```

Options:

- `--count`: number of rows to create; default `1000000`.
- `-o`, `--output`: destination path; default `data_store.bin`.

### Validate

Validate an existing dataset. The input path is required. If `--rows` is
omitted, the validator uses the row count stored in the file header.

```bash
datavault validate -i data_store.bin
datavault validate -i data_store.bin --rows 100000
```

Options:

- `-i`, `--input`: binary file to validate; required.
- `-r`, `--rows`: optional expected row count.

Validation raises an error for a missing file, an invalid magic header, an
incorrect column count, a payload-size mismatch, a checksum mismatch, or
non-finite values such as `NaN` and `Inf`.

### Analyze

Validate a dataset and print the aggregation summary:

```bash
datavault analyze -i data_store.bin
datavault analyze -i data_store.bin -r 100000
```

The current aggregation compares the number of rows in the validated array
with the number of usable rows. Because both inputs are currently the same
validated array, a valid file normally reports zero corrupted records.

### Run the complete example

```bash
datavault run-e --count 100000 -o example.bin
```

This command generates `example.bin`, validates it using the requested row
count, analyzes it, and prints the total execution time. Its default output
path is `output.bin`.

### Dump

The command-line parser accepts `txt`, `json`, and `csv` formats:

```bash
datavault dump -i data_store.bin --format csv
```

At present this command only prints a status message. It does not create an
exported file.

## Binary file format

Each generated file is laid out as follows:

| Offset | Size | Content |
| ---: | ---: | --- |
| `0` | 8 bytes | Magic value `DVBIN01\x00` |
| `8` | 8 bytes | Row count, unsigned little-endian integer |
| `16` | 4 bytes | Column count, unsigned little-endian integer |
| `20` | 32 bytes | SHA-256 digest of the payload |
| `52` | Remaining bytes | Raw NumPy `float32` payload |

The payload contains `rows * columns` values and is expected to contain three
columns. The checksum covers only the payload, not the header.

## Python API

The main building blocks are available under `datavault.utils`:

```python
from datavault.utils import Aggregate, DatasetGenerator, ValidateBinFileContent

path = "data_store.bin"
generated = DatasetGenerator(path, 1000)()
validated = ValidateBinFileContent(path, expected_rows=1000, expected_cols=3)()
Aggregate(dataset=generated, usable_data=validated)()
```

`DatasetGenerator` returns a transformed in-memory array after writing the
file. The file itself contains the original generated values. The validator
returns the stored payload as a two-dimensional NumPy array with shape
`(rows, 3)`.

## Project layout

```text
datavault/
├── datavault/
│   ├── main.py
│   └── utils/
│       ├── aggregate.py       # Record-count summary
│       ├── cli.py             # argparse CLI and commands
│       ├── createdataset.py   # Dataset generation and serialization
│       ├── decorator.py       # Pipeline logging decorator
│       └── validator.py       # Binary integrity checks
├── tests/                     # CLI, pipeline, and error tests
├── pyproject.toml
└── README.md
```

## Development

Run the test suite from the repository root:

```bash
python -m pytest
```

This is a learning-focused example, not a production database or general
purpose storage format. It intentionally keeps the file format and processing
pipeline small enough to inspect and extend.
