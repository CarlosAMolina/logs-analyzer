import datetime
from typing import List


class Log:
    def __init__(self, ip: str, datetime_: datetime.datetime):
        self.ip = ip
        self.datetime_ = datetime_


class LineParser:
    def __init__(self, line: str):
        self._line = line

    @property
    def ip(self):
        return "8.8.8.8"


class FileParser:
    def __init__(self):
        self._parse_line = LineParser

    def __call__(self, file: str):
        return self._get_file_parsed(file)

    def _get_file_parsed(self, file: str) -> List[LineParser]:
        with open(file, "r") as f:
            return [
                Log(
                    ip=self._parse_line(line).ip,
                    datetime_=None,
                )
                for line in f.readlines()[0]
            ]

