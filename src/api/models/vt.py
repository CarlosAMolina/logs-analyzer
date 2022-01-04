from typing import Union
import datetime as datetime


class IPVTAnalysis:
    def __init__(
        self,
        ip: str,
        malicious: Union[int, str],
        suspicious: Union[int, str],
        harmless: Union[int, str],
        last_modification_date: Union[datetime.datetime, str],
    ):
        self.ip = ip
        self.malicious = malicious
        self.suspicious = suspicious
        self.harmless = harmless
        self.last_modification_date = last_modification_date

    @property
    def data(self):
        return {
            "ip": self.ip,
            "malicious": self.malicious,
            "suspicious": self.suspicious,
            "harmless": self.harmless,
            "last_modification_date": self.last_modification_date,
        }
