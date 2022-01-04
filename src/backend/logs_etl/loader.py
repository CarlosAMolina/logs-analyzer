import pandas as pd

from . import transformer


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


class LogsPrinter:
    def __init__(self, logs: pd.DataFrame):
        self._logs = logs
        self._get_logs_analizer = transformer.LogsAnalyzer
        self._logs_analizer = self._get_logs_analizer(logs)
        self._logs_repr = LogsRepr

    def print_remote_addr(self):
        print(*self._logs_analizer.get_remote_addr(), sep="\n")

    def print_remote_addrs_count(self):
        with pd.option_context("display.max_rows", None):
            print(self._logs_analizer.get_remote_addrs_count())
