from http import HTTPStatus
import unittest
import mock

from src.resources import log
from tests import LOGS_PATH


class TestLogListResource(unittest.TestCase):
    def setUp(self):
        self.class_ = log.LogListResource()

    def test_post_with_file_that_exits(self):
        class FakeRequest:
            @staticmethod
            def get_json():
                return {"logs-path": LOGS_PATH}

        with mock.patch("src.resources.log.request", FakeRequest):
            result = self.class_.post()
            self.assertEqual(2, len(result[0]["data"]))
            self.assertEqual(HTTPStatus.OK, result[1])

    def test_post_with_file_that_does_not_exit(self):
        class FakeRequest:
            @staticmethod
            def get_json():
                return {"logs-path": "/foo/bar"}

        with self.assertRaises(FileNotFoundError) as cm:
            with mock.patch("src.resources.log.request", FakeRequest):
                self.class_.post()
        the_exception = cm.exception
        self.assertIsInstance(the_exception, FileNotFoundError)


if __name__ == "__main__":
    unittest.main()
