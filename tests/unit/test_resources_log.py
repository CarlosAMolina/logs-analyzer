import unittest
import mock

from src.api.resources import log
from tests import LOGS_PATH


class TestLogListResource(unittest.TestCase):
    def setUp(self):
        self.class_ = log.LogListResource()

    def test_post_with_file_that_exits(self):
        class FakeRequest:
            @staticmethod
            def get_json():
                return {"logs-file": LOGS_PATH}

        with mock.patch("src.api.resources.log.flask.request", FakeRequest):
            result = self.class_.post()
            self.assertEqual(3, len(result.json))
            self.assertEqual("200 OK", result.status)

    def test_post_with_file_that_does_not_exit(self):
        class FakeRequest:
            @staticmethod
            def get_json():
                return {"logs-file": "/foo/bar"}

        with self.assertRaises(FileNotFoundError) as cm:
            with mock.patch("src.api.resources.log.flask.request", FakeRequest):
                self.class_.post()
        the_exception = cm.exception
        self.assertIsInstance(the_exception, FileNotFoundError)


if __name__ == "__main__":
    unittest.main()
