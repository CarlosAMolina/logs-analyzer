import unittest

import pandas as pd

# from src_python.logs import loader
from src_python import analyzer


class TestLogsRepr(unittest.TestCase):
    def test_repr(self):
        logs = pd.DataFrame({"a": ["foo"], "b": [1]})
        repr_logs = analyzer.LogsRepr(logs)
        self.assertEqual("foo 1", repr(repr_logs))

    def test_repr_empty(self):
        logs = pd.DataFrame()
        repr_logs = analyzer.LogsRepr(logs)
        self.assertEqual("", repr(repr_logs))


class TestLogsPrinter(unittest.TestCase):
    def setUp(self):
        logs = pd.DataFrame(
            {
                "remote_addr": ["1.1.1.1", "1.1.1.1", "2.2.2.2"],
                "request": [None] * 3,
                "status": [None] * 3,
            }
        )
        self.printer = analyzer.LogsPrinter(logs)

    def test_methods_do_not_raise_exception(self):
        self.printer.print_remote_addr()
        self.printer.print_remote_addr_count()
        self.printer.print_logs_group_by_remote_addr()


if __name__ == "__main__":
    unittest.main()
