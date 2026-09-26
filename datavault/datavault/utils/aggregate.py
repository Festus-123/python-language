from typing import Any, Self


class Aggregate:
    def __init__(self: Any, dataset: Any, usable_data: Any) -> None:
        self.dataset = dataset
        self.usable_data = usable_data

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        pass

    def __call__(self: Any, stream: Any | None = None) -> Any:
        total_records = 0
        if hasattr(self.dataset, "shape"):
            total_records = int(self.dataset.shape[0])
        elif hasattr(self.dataset, "store_content_size"):
            total_records = int(self.dataset.store_content_size)
        elif self.dataset is not None:
            try:
                total_records = len(self.dataset)
            except TypeError:
                total_records = 0

        usable_records = 0
        if hasattr(self.usable_data, "shape"):
            usable_records = int(self.usable_data.shape[0])
        elif self.usable_data is not None:
            try:
                usable_records = len(self.usable_data)
            except TypeError:
                usable_records = 0

        corrupted_data_in_store = max(0, total_records - usable_records)

        print(
            f"""
    GATA VAULT ANALYTICS
    _________________________________________
    
    Records:                   {total_records:,}
    
    Aggregate records:
    
        Uncorrupted data       {usable_records:,} 
        Corrupted data          {corrupted_data_in_store:,}
                    
    Programm Execution Completed...
            """
        )
        return stream
