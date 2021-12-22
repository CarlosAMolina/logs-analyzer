import datetime
import unittest

import pandas as pd

from src_python.logs import transformer
from tests import LOG_FILE


class TestFileLineParser(unittest.TestCase):
    def setUp(self):
        line = (
            '8.8.8.8 - abc [28/Nov/2021:00:18:22 +0100] "GET / HTTP/1.1" 200 77 "-"'
            ' "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"'
        )
        self.parser = transformer.FileLineParser(line)

    def test_remote_addr(self):
        self.assertEqual("8.8.8.8", self.parser.remote_addr)

    def test_remote_user(self):
        self.assertEqual("abc", self.parser.remote_user)

    def test_get_time_local_as_str(self):
        self.assertEqual(
            "28/Nov/2021:00:18:22 +0100", self.parser._get_time_local_as_str()
        )

    def test_time_local(self):
        self.assertEqual(
            datetime.datetime(
                2021,
                11,
                28,
                0,
                18,
                22,
                tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)),
            ),
            self.parser.time_local,
        )

    def test_request(self):
        self.assertEqual("GET / HTTP/1.1", self.parser.request)

    def test_status(self):
        self.assertEqual(200, self.parser.status)

    def test_body_bytes_sent(self):
        self.assertEqual(77, self.parser.body_bytes_sent)

    def test_http_referer(self):
        self.assertEqual("-", self.parser.http_referer)

    def test_http_user_agent(self):
        self.assertEqual(
            (
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            ),
            self.parser.http_user_agent,
        )


class TestPandasParser(unittest.TestCase):
    def test_get_file_as_df(self):
        result_expected = pd.DataFrame(
            {
                "remote_addr": ["8.8.8.8", "111.222.33.4"],
                "remote_user": ["-", "abc"],
                "time_local": [
                    datetime.datetime(
                        2021,
                        10,
                        28,
                        0,
                        18,
                        22,
                        tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)),
                    ),
                    datetime.datetime(
                        2021,
                        11,
                        28,
                        6,
                        8,
                        15,
                        tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)),
                    ),
                ],
                "request": ["GET / HTTP/1.1", "GET /foo/bar HTTP/1.1"],
                "status": [200, 404],
                "body_bytes_sent": [77, 118],
                "http_referer": ["-", "-"],
                "http_user_agent": ["foo bar 1", "foo bar 2"],
            }
        )
        parse_file = transformer.PandasParser(LOG_FILE)
        self.assertTrue(result_expected.equals(parse_file()))


class TestLogsAnalyzer(unittest.TestCase):
    def test_remote_addr(self):
        logs = pd.DataFrame({"remote_addr": ["1.1.1.1", "1.1.1.1", "2.2.2.2"]})
        analyze_logs = transformer.LogsAnalyzer(logs)
        self.assertEqual(["1.1.1.1", "2.2.2.2"], analyze_logs.get_remote_addr())

    def test_remote_addr_count(self):
        logs = pd.DataFrame({"remote_addr": ["2.2.2.2", "1.1.1.1", "1.1.1.1"]})
        analyze_logs = transformer.LogsAnalyzer(logs)
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
        get_logs_summarized = transformer.LogsSummarize()
        expected_result = pd.DataFrame(
            data={"request": ["GET foo"], "status": [200]},
            index=["1.1.1.1"],
        )
        self.assertTrue(expected_result.equals(get_logs_summarized(logs)))


if __name__ == "__main__":
    unittest.main()
