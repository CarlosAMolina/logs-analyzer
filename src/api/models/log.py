import datetime as datetime


class LogFile:
    def __init__(
        self,
        is_file: bool,
        path: str,
    ):
        self.is_file = is_file
        self.path = path

    @property
    def data(self):
        return {
            "isFile": self.is_file,
            "path": self.path,
        }


class Log:
    def __init__(
        self,
        remote_addr: str,
        remote_user: str,
        time_local: datetime.datetime,
        request: str,
        status: int,
        body_bytes_sent: int,
        http_referer: str,
        http_user_agent: str,
    ):
        self.remote_addr = remote_addr
        self.remote_user = remote_user
        self.time_local = time_local
        self.request = request
        self.status = status
        self.body_bytes_sent = body_bytes_sent
        self.http_referer = http_referer
        self.http_user_agent = http_user_agent

    @property
    def data(self):
        return {
            "remoteAddr": self.remote_addr,
            "remoteUser": self.remote_user,
            "timeLocal": self._time_local_str,
            "request": self.request,
            "status": self.status,
            "bodyBytesSent": self.body_bytes_sent,
            "httpReferer": self.http_referer,
            "httpUserAgent": self.http_user_agent,
        }

    @property
    def _time_local_str(self) -> str:
        return str(self.time_local)


class RemoteAddrCount:
    def __init__(
        self,
        remote_addr: str,
        count: int,
    ):
        self.remote_addr = remote_addr
        self.count = count

    @property
    def data(self):
        return {
            "remoteAddr": self.remote_addr,
            "count": self.count,
        }


