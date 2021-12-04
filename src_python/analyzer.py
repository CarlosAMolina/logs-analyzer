from typing import List
import pandas as pd


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

    def get_log_repr(self, log: pd.DataFrame) -> str:
        return log.to_string(header=False, index=False)


class LogsPrinter:
    def __init__(self, logs: pd.DataFrame):
        self._logs = logs
        self._analyze_log = LogsAnalyzer(logs)

    def print_remote_addr(self):
        print(*self._analyze_log.get_remote_addr(), sep="\n")

    def print_remote_addr_count(self):
        with pd.option_context("display.max_rows", None):
            print(self._analyze_log.get_remote_addr_count())

    def print_full_logs(self):
        with pd.option_context(
            "display.max_rows",
            None,
            "display.max_columns",
            None,
        ):
            print(self._logs.to_string())

    def print_logs_group_by_ip(self):
        for indes, row in self._analyze_log.get_remote_addr_count().iterrows():
            print(f"## {row['remote_addr']} ({row['count']})")
            print(
                self._analyze_log.get_log_repr(
                    self._logs.loc[self._logs["remote_addr"] == row["remote_addr"]]
                )
            )
            print("\n")
