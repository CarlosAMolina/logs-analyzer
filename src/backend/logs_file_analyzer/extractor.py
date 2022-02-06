from typing import List

from api.models import log as log_model
from backend.logs_file_parser import manager as logs_file_parser_manager


def extract(file: str) -> List[log_model.Log]:
    return logs_file_parser_manager.get_logs_from_file(file)
