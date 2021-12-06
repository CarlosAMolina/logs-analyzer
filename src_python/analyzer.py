from typing import List
import pandas as pd


class LogsRepr:
    def __init__(self, logs: pd.DataFrame):
        self._logs = logs

    def __repr__(self) -> str:
        with pd.option_context(*self._repr_option_content):
            return self._get_repr(self._logs)

    def _get_repr(self, df: pd.DataFrame) -> str:
        return "" if df.empty else df.to_string(**self._repr_args)

    @property
    def _repr_option_content(self) -> tuple:
        return (
            "display.max_rows",
            None,
            "display.max_columns",
            None,
        )

    @property
    def _repr_args(self) -> dict:
        return {"header": False, "index": False}


class LogsAnalyzer:
    def __init__(self, logs: pd.DataFrame):
        self._logs = logs

    def get_remote_addr(self) -> List[str]:
        return self._logs["remote_addr"].drop_duplicates().tolist()

    def get_remote_addr_count(self) -> pd.DataFrame:
        column = "remote_addr"
        result = self._get_column_count(column)
        return result.sort_values(["count"], ascending=False).reset_index(drop=True)

    def _get_column_count(self, column) -> pd.DataFrame:
        return self._logs.groupby([column])[column].count().reset_index(name="count")

    def get_logs_of_remote_addr(self, ip: str) -> pd.DataFrame:
        return self._logs.loc[self._logs["remote_addr"] == ip]

    def is_logs_count_suspicious(self) -> bool:
        return len(self._logs) > 10


class LogsSummarize:
    def __init__(self):
        self._logs = None

    def __call__(self, logs: pd.DataFrame) -> pd.DataFrame:
        self._logs = logs
        self._remove_not_required_columns()
        self._remove_not_suspcicious_requests()
        return self._logs.reset_index(drop=True)

    def _remove_not_required_columns(self):
        columns = [
            "remote_addr",
            "request",
            "status",
        ]
        self._logs = self._logs[columns]

    def _remove_not_suspcicious_requests(self):
        regex = r"GET /(index.css|agallas.png|robots.txt|favicon.ico)? HTTP/1.[0|1]"
        exp = self._logs["request"].str.match(regex, na=False)
        self._logs = self._logs.loc[~exp]


class LogsPrinter:
    def __init__(self, logs: pd.DataFrame):
        self._logs = logs
        self._get_logs_analizer = LogsAnalyzer
        self._get_logs_summarized = LogsSummarize()
        self._logs_analizer = self._get_logs_analizer(logs)
        self._logs_repr = LogsRepr

    def print_remote_addr(self):
        print(*self._logs_analizer.get_remote_addr(), sep="\n")

    def print_remote_addr_count(self):
        with pd.option_context("display.max_rows", None):
            print(self._logs_analizer.get_remote_addr_count())

    def print_logs_group_by_remote_addr(self):
        for index, row in self._logs_analizer.get_remote_addr_count().iterrows():
            ip_logs = self._logs_analizer.get_logs_of_remote_addr(row["remote_addr"])
            ip_logs_suspicious = self._get_logs_summarized(ip_logs)
            if (
                len(ip_logs_suspicious) == 0
                and not self._get_logs_analizer(ip_logs).is_logs_count_suspicious()
            ):
                continue
            print(
                "## {ip} ({count_suspicious}/{count_total})\n{logs}\n".format(
                    ip=row["remote_addr"],
                    count_suspicious=len(ip_logs_suspicious),
                    count_total=len(ip_logs),
                    logs=repr(self._logs_repr(ip_logs_suspicious)),
                )
            )
