"""Module to work with Virus Total
"""

import datetime
import os

import requests

from . import file_extractor


API_KEY = os.environ["VT_KEY"]


class RequestIp:
    URL = "https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    def get_analysis(self, ip: str) -> dict:
        response = requests.get(
            self.URL.format(ip=ip),
            headers={"x-apikey": API_KEY},
        )
        return response.json()


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
        self._ip_analyzer = RequestIp()
        self._get_ip_summary = IpSummary

    def __call__(self, ip: str):
        return self._get_ip_summary(self._ip_analyzer.get_analysis(ip)).get_summary()


class FileIpAnalyzer:
    def __init__(self, file: str):
        self._file_reader = file_extractor.FileExtractor(file)
        self._get_ip_analysis = IpAnalyzer()

    def print_analysis_of_each_ip(self):
        for ip in self._file_reader.get_lines_in_file():
            print(
                "## {ip}: {analysis}".format(
                    ip=ip,
                    analysis=self._get_ip_analysis(ip),
                )
            )
