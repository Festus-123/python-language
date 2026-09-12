# PipeFlow

PipeFlow is a small Python log-processing project designed to teach stream-based data pipelines. It reads raw log lines, converts them into structured records, validates them, filters out unwanted data, and writes the final results to JSON output.

## What the project does

The project models a simple data processing flow where data moves through multiple stages, one item at a time. Instead of loading everything into a single list, each stage acts like a generator-based worker that accepts a stream and yields the next result.

This is useful for learning the core ideas behind real-world ETL-like processing, especially:

- generator-based pipelines
- reusable processing stages
- validation and filtering logic
- context-managed workflow execution
- file-based output sinks

## Pipeline stages

The current implementation is centered around these components:

- `CleanText`: reads a log file, parses each line, and turns it into a dictionary record.
- `Validator`: checks each item against a schema and optional predicate before continuing.
- `Filter`: removes unwanted items using a condition or unique identifier check.
- `Transform`: writes valid records to disk as JSON lines.
- `Pipeline`: connects each stage together and executes them in sequence.

A typical record looks like this:

```python
{
    "timestamp": "2026-09-12 10:00:00+00:00",
    "level": "ERROR",
    "service": "auth_service",
    "user_id": 123,
    "message": "User 123 requested action",
    "latency_ms": 450
}
```

## How the flow works

The project follows this pattern:

1. Read raw log text from a file such as `logs/logs.txt`
2. Parse each line into a structured dictionary
3. Validate the record against a required field schema
4. Apply a filter such as only `ERROR` records or unique user IDs
5. Save the accepted records to output JSON files
6. Report the number of items emitted at each stage

The main example in `main.py` builds a pipeline like this:

```python
pipeline = Pipeline([
    CleanText(file_path="logs/logs.txt"),
    Validator(schema=log_schema, predicate=condition_to_filter),
    Filter(predicate=condition_to_filter, key="user_id"),
    Transform(output_name="refined-errors")
])
```

The `Pipeline` object uses `__call__` and supports a context manager flow so each stage can initialize and clean up as needed.

## Recent additions and design changes

The project now includes a more practical pipeline structure with these improvements:

- `__enter__` and `__exit__` support in `Pipeline`, `CleanText`, and `Transform`
- logging decorators for stage execution tracking
- schema-based validation with type enforcement
- generator-based streaming between stages
- file output created automatically in a generated folder
- filter logic that prevents duplicate records based on a chosen key

This makes the project feel more like a mini framework rather than a single script.

## Project structure

```text
pipeflow/
├── main.py
├── example.py
├── README.md
├── logs/
│   └── logs.txt
├── refined-errors-folder/
│   └── refined-errors.json
└── utils/
    ├── __init__.py
    ├── clean_text.py
    ├── pipeline.py
    ├── filter.py
    ├── transform.py
    ├── validator.py
    └── decorators.py
```

## Run it

From the project folder, execute:

```bash
python main.py
```

This will generate log data if needed, process the records through the pipeline, and write the accepted entries to a JSON output folder.

## Notes

- This is an educational project focused on Python patterns such as generators, decorators, context managers, validation, and reusable pipeline components.
- It is intentionally lightweight and not meant to be a full production-grade framework.
- The output is designed to demonstrate how a simple processing system can transform raw input into structured, filtered, persistent data.
