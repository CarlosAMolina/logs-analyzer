import unittest

import pandas as pd

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


class TestLogsAnalyzer(unittest.TestCase):
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


class TestLogsSummarize(unittest.TestCase):
    def test_get_logs_remove_not_suspicious_requests(self):
        requests = [
            "GET / HTTP/1.0",
            "GET foo",
            "GET /index.css HTTP/1.1",
            "GET /agallas.png HTTP/1.1",
            "GET /favicon.ico HTTP/1.1",
            "GET /robots.txt HTTP/1.1",
        ]
        logs = pd.DataFrame(
            {
                "remote_addr": ["1.1.1.1"] * len(requests),
                "request": requests,
                "status": [200] * len(requests),
            }
        )
        get_logs_summarized = analyzer.LogsSummarize()
        expected_result = pd.DataFrame(
            data={"request": ["GET foo"], "status": [200]},
            index=["1.1.1.1"],
        )
        self.assertTrue(expected_result.equals(get_logs_summarized(logs)))


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
