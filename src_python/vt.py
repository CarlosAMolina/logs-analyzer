"""Module to work with Virus Total
"""

import datetime
import os

import requests


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
        return "{analysis} {date} UTC".format(
            analysis=self._get_last_analysis_stats(),
            date=self._get_last_modification_date(),
        )

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
