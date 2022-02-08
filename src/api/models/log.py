from sqlalchemy.dialects import postgresql

from api.extensions import db


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


class Log(db.Model):
    """
    Serial column:
    https://stackoverflow.com/questions/20848300/unable-to-create-autoincrementing-primary-key-with-flask-sqlalchemy
    """

    __tablename__ = "log"

    id = db.Column(db.Integer, primary_key=True)
    remote_addr = db.Column(postgresql.INET)
    remote_user = db.Column(db.Text)
    time_local = db.Column(db.TIMESTAMP(timezone=True))
    request = db.Column(db.Text)
    status = db.Column(db.SmallInteger)
    body_bytes_sent = db.Column(db.Integer)
    http_referer = db.Column(db.Text)
    http_user_agent = db.Column(db.Text)

    # TODO fix. flask migrate does not work with this column
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

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
