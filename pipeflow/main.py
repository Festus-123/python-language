"""_summary_
Project: PipeFlow — A Mini Data Processing Framework

Objectives:
    - build a framwework for processing data accessible to people amd projects
    steps:
    - Raw data (inputs)
    - filter (sorts out data aviding go through massive sets)
    - transform
    - validate (type check for consistency )
    - save

OOP, dunder methods, decorators, generators, context managers, type hints,
mypy, and pytest.

## use case tools
    - Use __getitem__
    - Use __call__
    - Generator
    - Decorator
    - Context Manager
    - Pipeline statistics
    - Type Hints
    - mypy
    - pytest ---- meet up with the tes
    
    
Version 2 of this project PipeFlow v2
────────────────────────
□ User-defined input file
□ User-defined output path
□ Automatic format detection
□ Regex generation from sample data
□ Automatic schema inference
□ CLI interface
□ Better error reporting
□ More comprehensive tests
"""

from utils import CleanText, Filter, Pipeline, Transform, Validator, Callable, Any

condition_to_filte : Callable[[dict[str, Any]], bool] = ( lambda item: item["level"] == "ERROR")

if __name__ == "__main__":
    print("Pipeflow data processing framework Initialised >>>")

    log_schema: dict[str, type] = {"level": str, "user_id": int, "service": str}
    
    pipeline = Pipeline(
        [
        CleanText(file_path="logs/logs.txt"), 
        Validator(
            schema=log_schema,
            predicate=condition_to_filte,
            ),
        Filter(predicate=condition_to_filte, key="user_id"),
        Transform(output_name='refined-errors')
        ]
    )
    count = 0
    # for record in pipeline() or ():
    #     count += 1
        
    # print(f"Final Record Passed: {count} logs")
    with pipeline as runner :
        for record in runner() :
            count += 1
        print(f"[INFO] stage Final Output Passed: {count} logs \n")
            
