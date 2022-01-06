from typing import List

from ...api.models import log as log_model
from . import exception
from . import extractor
from . import transformer


def get_logs_from_file(logs_path: str) -> List[log_model.Log]:
    lines = extractor.extract(logs_path)
    result = []
    for line in lines:
        try:
            result.append(transformer.transform(line))
        except exception.LogInFileNotParsedError:
            print(f"[ERROR] Log not parsed: {line}")
    return result
