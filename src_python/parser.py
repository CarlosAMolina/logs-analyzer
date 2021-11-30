import datetime as datetime
import re
from typing import Iterator

import pandas as pd


class LogParser:
    """
    https://docs.nginx.com/nginx/admin-guide/monitoring/logging/
    """

    def __init__(self, line: str):
        regex = (
            r'^(([0-9]{1,3}[\.]){3}[0-9]{1,3})\s-\s(.+)\s\[(.*)\]\s"(.*)"\s(\d{1,3})'
            r'\s(\d+)\s"(.*)"\s"(.*)"'
        )
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
        self._parse_log = LogParser

    def __call__(self, file: str):
        return self._get_file_parsed(file)

    def _get_file_parsed(self, file: str) -> Iterator[LogParser]:
        with open(file, "r") as f:
            for line in f.read().splitlines():
                yield LogParser(line)


class PandasParser:
    def __init__(self):
        self._get_logs_from_file = FileParser()

    def __call__(self, file: str):
        result = self._get_file_as_df(file)
        return self._get_df_cast_values(result)

    def _get_file_as_df(self, file: str) -> pd.DataFrame:
        result = pd.DataFrame()
        for log in self._get_logs_from_file(file):
            result = result.append(
                {
                    "remote_addr": log.remote_addr,
                    "remote_user": log.remote_user,
                    "time_local": log.time_local,
                    "request": log.request,
                    "status": log.status,
                    "body_bytes_sent": log.body_bytes_sent,
                    "http_referer": log.http_referer,
                    "http_user_agent": log.http_user_agent,
                },
                ignore_index=True,
            )
        return result

    def _get_df_cast_values(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df
        result["status"] = result["status"].astype(int)
        result["body_bytes_sent"] = result["body_bytes_sent"].astype(int)
        return result

