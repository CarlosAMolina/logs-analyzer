import unittest

import pandas as pd

from src_python import analyzer


class TestLogsAnalyzer(unittest.TestCase):
    def test_repr(self):
        logs = pd.DataFrame({"a": ["foo"], "b": [1]})
        analyze_logs = analyzer.LogsAnalyzer(logs)
        self.assertEqual("foo 1", repr(analyze_logs))

    def test_remote_addr(self):
        logs = pd.DataFrame({"remote_addr": ["1.1.1.1", "1.1.1.1", "2.2.2.2"]})
        analyze_logs = analyzer.LogsAnalyzer(logs)
        self.assertEqual(["1.1.1.1", "2.2.2.2"], analyze_logs.get_remote_addr())

    def test_remote_addr_count(self):
        logs = pd.DataFrame({"remote_addr": ["2.2.2.2", "1.1.1.1", "1.1.1.1"]})
        analyze_logs = analyzer.LogsAnalyzer(logs)
        self.assertTrue(
            pd.DataFrame(
                {
                    "remote_addr": ["1.1.1.1", "2.2.2.2"],
                    "count": [2, 1],
                }
            ).equals(analyze_logs.get_remote_addr_count())
        )

    def test_get_logs_columns(self):
        logs = pd.DataFrame({"a": ["foo"], "b": [1]})
        analyze_logs = analyzer.LogsAnalyzer(logs)
        self.assertTrue(
            pd.DataFrame({"a": ["foo"]}).equals(analyze_logs.get_logs_columns(["a"]))
        )


class TestLogsPrinter(unittest.TestCase):
    def setUp(self):
        logs = pd.DataFrame({"remote_addr": ["1.1.1.1", "1.1.1.1", "2.2.2.2"]})
        self.printer = analyzer.LogsPrinter(logs)

    def test_methods_do_not_raise_exception(self):
        self.printer.print_remote_addr()
        self.printer.print_remote_addr_count()
        self.printer.print_logs_group_by_remote_addr()


if __name__ == "__main__":
    unittest.main()
