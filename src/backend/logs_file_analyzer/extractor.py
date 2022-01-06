from typing import List

from ..logs_file_parser import manager as logs_file_parser_manager
from ...api.models import log as log_model


def extract(file: str) -> List[log_model.Log]:
    return logs_file_parser_manager.get_logs_from_file(file)
