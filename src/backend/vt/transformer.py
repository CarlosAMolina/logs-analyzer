from typing import Union
import datetime
import os


API_KEY = os.environ["VT_KEY"]


class IPResults:
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
    def last_modification_date(self) -> Union[datetime.datetime, None]:
        if not self._is_error:
            try:
                epoch = self._attributes["last_modification_date"]
                return datetime.datetime.utcfromtimestamp(epoch)
            except KeyError:
                return None


class IPSummary:
    def __init__(self, response: dict):
        self._analysis = IPResults(response)

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
