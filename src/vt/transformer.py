from typing import List
import datetime
import os

import pandas as pd

from ..logs import extractor as logs_extractor
from . import extractor as vt_extractor


API_KEY = os.environ["VT_KEY"]


class IpResults:
    def __init__(self, response: dict):
        self._response = response
        self._is_error = "error" in self._response.keys()

    @property
    def _attributes(self) -> dict:
        if not self._is_error:
            return self._response["data"]["attributes"]

    @property
    def _stats(self) -> dict:
        if not self._is_error:
            return self._attributes["last_analysis_stats"]

    @property
    def malicious(self):
        if not self._is_error:
            return self._stats["malicious"]

    @property
    def suspicious(self):
        if not self._is_error:
            return self._stats["suspicious"]

    @property
    def harmless(self):
        if not self._is_error:
            return self._stats["harmless"]

    @property
    def last_modification_date(self) -> datetime.datetime:
        if not self._is_error:
            epoch = self._attributes["last_modification_date"]
            return datetime.datetime.utcfromtimestamp(epoch)


class IpSummary:
    def __init__(self, response: dict):
        self._analysis = IpResults(response)

    def get_summary(self) -> str:
        result = (
            "{malicious}/{suspicious}/{harmless}"
            " (malicious/suspicious/harmless) {date} UTC"
        )
        result = result.format(
            malicious=self._analysis.malicious,
            suspicious=self._analysis.suspicious,
            harmless=self._analysis.harmless,
            date=self._analysis.last_modification_date,
        )
        return result.replace("None", "-")


class IpAnalyzer:
    def __init__(self):
        self._ip_analyzer = vt_extractor.RequestIp()
        self._get_ip_summary = IpSummary

    def __call__(self, ip: str):
        return self._get_ip_summary(self._ip_analyzer.get_analysis(ip)).get_summary()


class FileIpAnalyzer:
    def __init__(self, file: str):
        self._file_reader = logs_extractor.FileExtractor(file)
        self._get_ip_analysis = IpAnalyzer()

    def print_analysis_of_each_ip(self):
        for ip in self._file_reader.get_lines_in_file():
            print(
                "## {ip}: {analysis}".format(
                    ip=ip,
                    analysis=self._get_ip_analysis(ip),
                )
            )


class IPsAnalyzerAsDf:
    def __init__(self):
        self._get_vt_info_of_ip = vt_extractor.RequestIp().get_analysis
        self._get_ip_info_parsed = IpResults

    def __call__(self, ips: List[str]):
        return self._get_analysis_of_ips_as_df(ips)

    def __get_analysis_of_ips_as_df(self, ips: List[str]) -> pd.DataFrame:
        data = {
            "remote_addr": [],
            "malicious": [],
            "suspicious": [],
            "harmless": [],
            "last_modification_date": [],
        }
        for ip in ips:
            ip_info = self._get_ip_info_parsed(self._get_vt_info_of_ip(ip))
            data["remote_addr"].append(ip)
            data["malicious"].append(ip_info.malicious)
            data["suspicious"].append(ip_info.suspicious)
            data["harmless"].append(ip_info.harmless)
            data["last_modification_date"].append(ip_info.last_modification_date)
        return pd.DataFrame(data)

    def _get_analysis_of_ips_as_df(self, ips: List[str]) -> pd.DataFrame:
        data = {
            "remote_addr": [],
            "malicious": [],
            "suspicious": [],
            "harmless": [],
            "last_modification_date": [],
        }
        for ip in ips:
            ip_info = self._get_ip_info_parsed(self._get_vt_info_of_ip(ip))
            data["remote_addr"].append(ip)
            data["malicious"].append(ip_info.malicious)
            data["suspicious"].append(ip_info.suspicious)
            data["harmless"].append(ip_info.harmless)
            data["last_modification_date"].append(ip_info.last_modification_date)
        result = pd.DataFrame(data)
        return self._format_dataframe(result)

    def _format_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.astype(
            {"malicious": "int64", "suspicious": "int64", "harmless": "int64"}
        )
        df.set_index("remote_addr", inplace=True)
        df.sort_index(inplace=True)
        df.index.name = None
        return df
