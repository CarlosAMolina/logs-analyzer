from typing import List
import pandas as pd


class LogsAnalyzer:
    def __init__(self, logs: pd.DataFrame):
        self._logs = logs

    def __len__(self) -> int:
        return len(self._logs)

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

    def get_repr_summary(self) -> str:
        with pd.option_context(*self._repr_option_content):
            return self._get_repr(
                self._logs[
                    [
                        "request",
                        "status",
                    ]
                ]
            )

    def get_remote_addr(self) -> List[str]:
        return self._logs["remote_addr"].drop_duplicates().tolist()

    def get_remote_addr_count(self) -> pd.DataFrame:
        column = "remote_addr"
        result = self._get_column_count(column)
        return result.sort_values(["count"], ascending=False).reset_index(drop=True)

    def _get_column_count(self, column) -> pd.DataFrame:
        return self._logs.groupby([column])[column].count().reset_index(name="count")

    def get_logs_columns(self, columns: List[str]) -> pd.DataFrame:
        return self._logs[columns]

    def get_logs_of_remote_addr(self, ip: str) -> pd.DataFrame:
        return self._logs.loc[self._logs["remote_addr"] == ip]

    def get_logs_remove_not_suspicious_requests(self) -> pd.DataFrame:
        regex = r"GET /(index.css|agallas.png)? HTTP/1.[0|1]"
        exp = self._logs["request"].str.match(regex, na=False)
        return self._logs.loc[~exp]

    def is_logs_count_suspicious(self) -> bool:
        return len(self._logs) > 10


class LogsPrinter:
    def __init__(self, logs: pd.DataFrame):
        self._logs = logs
        self._analyze_logs = LogsAnalyzer(logs)

    def print_remote_addr(self):
        print(*self._analyze_logs.get_remote_addr(), sep="\n")

    def print_remote_addr_count(self):
        with pd.option_context("display.max_rows", None):
            print(self._analyze_logs.get_remote_addr_count())

    def print_logs_group_by_remote_addr(self):
        for index, row in self._analyze_logs.get_remote_addr_count().iterrows():
            ip_logs_analyzer = LogsAnalyzer(
                self._analyze_logs.get_logs_of_remote_addr(row["remote_addr"])
            )
            ip_suspicious_logs_analyzer = LogsAnalyzer(
                ip_logs_analyzer.get_logs_remove_not_suspicious_requests()
            )
            if (
                len(ip_suspicious_logs_analyzer) == 0
                and not ip_logs_analyzer.is_logs_count_suspicious()
            ):
                continue
            print(
                "## {ip} ({count_suspicious}/{count_total})\n{logs}\n".format(
                    ip=row["remote_addr"],
                    count_suspicious=len(ip_suspicious_logs_analyzer),
                    count_total=len(ip_logs_analyzer),
                    logs=ip_suspicious_logs_analyzer.get_repr_summary(),
                )
            )
