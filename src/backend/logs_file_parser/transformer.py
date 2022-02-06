import datetime as datetime
import re

from api.models import log as log_model
from backend.logs_file_parser import exception


def transform(log: str) -> log_model.Log:
    return FileLineParser().get_line_parsed(log)


class FileLineParser:
    """
    Log parts: https://docs.nginx.com/nginx/admin-guide/monitoring/logging/
    """

    _REGEX = (
        r'^(([0-9]{1,3}[\.]){3}[0-9]{1,3})\s-\s(.+)\s\[(.*)\]\s"(.*)"\s(\d{1,3})'
        r'\s(\d+)\s"(.*)"\s"(.*)"'
    )

    def get_line_parsed(self, line: str) -> log_model.Log:
        self._match = re.search(self._REGEX, line)
        if self._match is None:
            raise exception.LogInFileNotParsedError(line)
        return log_model.Log(
            remote_addr=self._remote_addr,
            remote_user=self._remote_user,
            time_local=self._time_local,
            request=self._request,
            status=self._status,
            body_bytes_sent=self._body_bytes_sent,
            http_referer=self._http_referer,
            http_user_agent=self._http_user_agent,
        )

    @property
    def _remote_addr(self) -> str:
        return self._match.group(1)

    @property
    def _remote_user(self) -> str:
        return self._match.group(3)

    @property
    def _time_local(self) -> datetime.datetime:
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
    def _request(self) -> str:
        return self._match.group(5)

    @property
    def _status(self) -> int:
        result = self._match.group(6)
        return int(result)

    @property
    def _body_bytes_sent(self) -> int:
        result = self._match.group(7)
        return int(result)

    @property
    def _http_referer(self) -> str:
        return self._match.group(8)

    @property
    def _http_user_agent(self) -> str:
        return self._match.group(9)
