import pytest
from utils.validator import Validator


def test_validator_filters_correctly(sample_log_records):
    schema = {"level": str, "user_id": int}
    validator = Validator(
        schema=schema, predicate=lambda x: x["level"] == "ERROR"
    )

    results = list(validator(sample_log_records))

    assert len(results) == 2
    assert all(r["level"] == "ERROR" for r in results)


def test_validator_raises_type_error_on_invalid_schema():
    schema = {"user_id": int}
    validator = Validator(schema=schema, drop_invalid=False)
    corrupt_stream = [{"user_id": "invalid_string_id"}]

    with pytest.raises(TypeError) as exc_info:
        list(validator(corrupt_stream))

    assert "user_id" in str(exc_info.value)