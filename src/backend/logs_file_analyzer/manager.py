from os.path import exists
from typing import List

from ...api.models import log as log_model
from . import extractor
from . import transformer


def get_is_file(logs_path: str) -> log_model.LogFile:
    return log_model.LogFile(
        is_file=exists(logs_path),
        path=logs_path,
    )


def get_remote_addrs_count_from_file(logs_path: str) -> List[log_model.RemoteAddrCount]:
    logs = extractor.extract(logs_path)
    return transformer.get_remote_addrs_count(logs)
