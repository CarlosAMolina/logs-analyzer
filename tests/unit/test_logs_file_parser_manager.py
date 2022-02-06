import datetime
import unittest

from backend.logs_file_parser import manager
from tests import LOGS_PATH


class TestFunctions(unittest.TestCase):
    def test_get_logs_from_file(self):
        result = manager.get_logs_from_file(LOGS_PATH)
        self.assertEqual(3, len(result))
        self.assertEqual("8.8.8.8", result[0].remote_addr)
        self.assertEqual("111.222.33.4", result[1].remote_addr)
        self.assertEqual("-", result[0].remote_user)
        self.assertEqual("abc", result[1].remote_user)
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
            result[0].time_local,
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
            result[1].time_local,
        )
        self.assertEqual("GET / HTTP/1.1", result[0].request)
        self.assertEqual("GET /foo/bar HTTP/1.1", result[1].request)
        self.assertEqual(200, result[0].status)
        self.assertEqual(404, result[1].status)
        self.assertEqual(77, result[0].body_bytes_sent)
        self.assertEqual(118, result[1].body_bytes_sent)
        self.assertEqual("-", result[0].http_referer)
        self.assertEqual("-", result[1].http_referer)
        self.assertEqual("foo bar 1", result[0].http_user_agent)
        self.assertEqual("foo bar 2", result[1].http_user_agent)


if __name__ == "__main__":
    unittest.main()
