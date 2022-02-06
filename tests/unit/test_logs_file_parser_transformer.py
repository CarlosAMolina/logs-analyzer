import datetime
import unittest

from backend.logs_file_parser import transformer


class TestFileLineParser(unittest.TestCase):
    def setUp(self):
        line = (
            '8.8.8.8 - abc [28/Nov/2021:00:18:22 +0100] "GET / HTTP/1.1" 200 77 "-"'
            ' "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"'
        )
        self.parser = transformer.FileLineParser()
        self.line_parsed = self.parser.get_line_parsed(line)

    def test_remote_addr(self):
        self.assertEqual("8.8.8.8", self.parser._remote_addr)

    def test_remote_user(self):
        self.assertEqual("abc", self.parser._remote_user)

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
            self.parser._time_local,
        )

    def test_request(self):
        self.assertEqual("GET / HTTP/1.1", self.parser._request)

    def test_status(self):
        self.assertEqual(200, self.parser._status)

    def test_body_bytes_sent(self):
        self.assertEqual(77, self.parser._body_bytes_sent)

    def test_http_referer(self):
        self.assertEqual("-", self.parser._http_referer)

    def test_http_user_agent(self):
        self.assertEqual(
            (
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            ),
            self.parser._http_user_agent,
        )


if __name__ == "__main__":
    unittest.main()
