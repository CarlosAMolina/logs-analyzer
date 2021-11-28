import datetime as datetime
import re
from typing import List


class Log:
    def __init__(self, remote_addr: str, time_local: datetime.datetime):
        self.remote_addr = remote_addr
        self.time_local = time_local


class LineParser:
    """
    https://docs.nginx.com/nginx/admin-guide/monitoring/logging/
    """

    def __init__(self, line: str):
        regex = r'^(([0-9]{1,3}[\.]){3}[0-9]{1,3})\s-\s(.+)\s\[(.*)\]\s"(.*)"\s(\d{1,3})\s(\d+)\s"(.*)"\s"(.*)"'
        self._match = re.search(regex, line)

    @property
    def remote_addr(self) -> str:
        return self._match.group(1)

    @property
    def remote_user(self) -> str:
        return self._match.group(3)

    @property
    def time_local(self) -> datetime.datetime:
        result = self._get_time_local_as_str()
        return self._get_time_local_as_datetime(result)

    def _get_time_local_as_str(self) -> str:
        return self._match.group(4)

    def _get_time_local_as_datetime(self, datetime_str: str) -> datetime.datetime:
        """
        https://www.programiz.com/python-programming/datetime/strptime
        """
        format = "%d/%b/%Y:%H:%M:%S %z"
        return datetime.datetime.strptime(datetime_str, format)

    @property
    def request(self) -> str:
        return self._match.group(5)

    @property
    def status(self) -> int:
        result = self._match.group(6)
        return int(result)

    @property
    def body_bytes_sent(self) -> int:
        result = self._match.group(7)
        return int(result)

    @property
    def http_referer(self) -> str:
        return self._match.group(8)

    @property
    def http_user_agent(self) -> str:
        return self._match.group(9)


class FileParser:
    def __init__(self):
        self._parse_line = LineParser

    def __call__(self, file: str):
        return self._get_file_parsed(file)

    def _get_file_parsed(self, file: str) -> List[LineParser]:
        with open(file, "r") as f:
            return [
                Log(
                    remote_addr=self._parse_line(line).remote_addr,
                    time_local=None,
                )
                for line in f.read().splitlines()
            ]
