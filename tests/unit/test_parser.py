import datetime
import unittest

from src_python import parser as m_parser


class TestLogParser(unittest.TestCase):
    def setUp(self):
        line = (
            '8.8.8.8 - abc [28/Nov/2021:00:18:22 +0100] "GET / HTTP/1.1" 200 77 "-"'
            ' "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"'
        )
        self.parser = m_parser.LogParser(line)

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


class TestFileParser(unittest.TestCase):
    def test_get_file_parsed(self):
        parse_file = m_parser.FileParser()
        logs = [log for log in parse_file("tests/access.log")]
        self.assertEqual("8.8.8.8", logs[0].remote_addr)
        self.assertEqual("111.222.33.4", logs[1].remote_addr)
        self.assertEqual("-", logs[0].remote_user)
        self.assertEqual("abc", logs[1].remote_user)
        self.assertEqual(
            datetime.datetime(
                2021,
                10,
                28,
                0,
                18,
                22,
                tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)),
            ),
            logs[0].time_local,
        )
        self.assertEqual(
            datetime.datetime(
                2021,
                11,
                28,
                6,
                8,
                15,
                tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)),
            ),
            logs[1].time_local,
        )
        self.assertEqual("GET / HTTP/1.1", logs[0].request)
        self.assertEqual("GET /foo/bar HTTP/1.1", logs[1].request)
        self.assertEqual(200, logs[0].status)
        self.assertEqual(404, logs[1].status)
        self.assertEqual(77, logs[0].body_bytes_sent)
        self.assertEqual(118, logs[1].body_bytes_sent)
        self.assertEqual("-", logs[0].http_referer)
        self.assertEqual("-", logs[1].http_referer)
        self.assertEqual("foo bar 1", logs[0].http_user_agent)
        self.assertEqual("foo bar 2", logs[1].http_user_agent)


if __name__ == "__main__":
    unittest.main()
