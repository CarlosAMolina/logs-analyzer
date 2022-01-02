import datetime as datetime


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
        self._time_local = time_local
        self.request = request
        self.status = status
        self.body_bytes_sent = body_bytes_sent
        self.http_referer = http_referer
        self.http_user_agent = http_user_agent

    @property
    def data(self):
        return {
            "remote_addr": self.remote_addr,
            "remote_user": self.remote_user,
            "time_local": self.time_local,
            "request": self.request,
            "status": self.status,
            "body_bytes_sent": self.body_bytes_sent,
            "http_referer": self.http_referer,
            "http_user_agent": self.http_user_agent,
        }

    @property
    def time_local(self) -> str:
        return str(self._time_local)
