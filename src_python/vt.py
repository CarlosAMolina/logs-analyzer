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


class ResponseParserIp:
    def __init__(self, response: dict):
        self._response = response

    def get_summary(self) -> str:
        return (
            "{analysis} {date} UTC".format(
                analysis=self._get_last_analysis_stats(),
                date=self._get_last_modification_date(),
            )
            if self._is_ip_analyzed()
            else "-"
        )

    def _is_ip_analyzed(self) -> bool:
        return "error" not in self._response.keys()

    def _get_last_analysis_stats(self) -> str:
        analysis = self._response["data"]["attributes"]["last_analysis_stats"]
        return (
            "{malicious}/{suspicious}/{harmless} (malicious/suspicious/harmless)"
        ).format(
            malicious=analysis["malicious"],
            suspicious=analysis["suspicious"],
            harmless=analysis["harmless"],
        )

    def _get_last_modification_date(self) -> datetime.datetime:
        epoch = self._response["data"]["attributes"]["last_modification_date"]
        return datetime.datetime.utcfromtimestamp(epoch)


class IpAnalyzer:
    def __init__(self):
        self._ip_analyzer = RequestIp()
        self._parse_response = ResponseParserIp

    def __call__(self, ip: str):
        return self._parse_response(self._ip_analyzer.get_analysis(ip)).get_summary()


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
