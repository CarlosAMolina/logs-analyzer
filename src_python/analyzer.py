from typing import List
import pandas as pd


class LogsAnalyzer:
    def __init__(self, logs: pd.DataFrame):
        self._logs = logs

    def __repr__(self) -> str:
        with pd.option_context(
            "display.max_rows",
            None,
            "display.max_columns",
            None,
        ):
            return self._logs.to_string(header=False, index=False)

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
            print(
                "## {ip} ({count})\n{logs}\n".format(
                    ip=row["remote_addr"],
                    count=row["count"],
                    logs=repr(
                        LogsAnalyzer(
                            self._analyze_logs.get_logs_of_remote_addr(
                                row["remote_addr"]
                            )[
                                [
                                    "request",
                                    "status",
                                ]
                            ]
                        )
                    ),
                )
            )
