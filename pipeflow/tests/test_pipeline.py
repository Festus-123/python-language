from utils.clean_text import CleanText
from utils.filter import Filter
from utils.pipeline import Pipeline
from utils.transform import Transform
from utils.validator import Validator


def test_full_pipeline_execution(tmp_path):
    log_path = tmp_path / "logs.txt"
    out_name = str(tmp_path / "test_out")

    pipeline = Pipeline([
        CleanText(file_path=log_path),
        Validator(
            schema={"level": str, "user_id": int},
            predicate=lambda item: item["level"] == "ERROR",
        ),
        Filter(predicate=lambda item: item["user_id"] > 0),
        Transform(output_name=out_name)
    ])

    with pipeline as runner:
        results = list(runner())

    assert len(results) > 0
    # assert clean_step.processed_count == 1000
    # assert filter_step.processed_count == len(results)
    # assert transform_step.processed_count == len(results)