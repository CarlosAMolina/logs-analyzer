import datetime
import os
import unittest

from src_python.logs import transformer
from src_python.logs import extractor


class TestFileFileLineParser(unittest.TestCase):
    def test_get_file_parsed(self):
        extract_file = extractor.FileExtractor(
            os.path.join(os.path.dirname(__file__), "../files/access.log")
        )
        parse_log = transformer.FileLineParser
        logs = [parse_log(log) for log in extract_file.get_lines_in_file()]
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
