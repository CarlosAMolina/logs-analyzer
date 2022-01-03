from http import HTTPStatus
import unittest
import mock
import os

from src.resources import log
from tests import LOG_FILE


class TestLogListResource(unittest.TestCase):
    def setUp(self):
        self.class_ = log.LogListResource()

    def test_get(self):
        with mock.patch("src.logs.manager.extractor.LOG_FILE", LOG_FILE):
            result = self.class_.get()
            self.assertEqual(2, len(result[0]["data"]))
            self.assertEqual(HTTPStatus.OK, result[1])

    def test_post_with_file_that_exits(self):
        class FakeRequest:
            @staticmethod
            def get_json():
                return {
                    "file": os.path.join(
                        os.path.dirname(__file__), "../files/access.log"
                    )
                }

        with mock.patch("src.logs.manager.extractor.LOG_FILE", LOG_FILE):
            with mock.patch("src.resources.log.request", FakeRequest):
                result = self.class_.post()
                self.assertEqual(2, len(result[0]["data"]))
                self.assertEqual(HTTPStatus.OK, result[1])

    def test_post_with_file_that_does_not_exit(self):
        class FakeRequest:
            @staticmethod
            def get_json():
                return {"file": "/foo/bar"}

        with self.assertRaises(FileNotFoundError) as cm:
            with mock.patch("src.logs.manager.extractor.LOG_FILE", LOG_FILE):
                with mock.patch("src.resources.log.request", FakeRequest):
                    self.class_.post()
        the_exception = cm.exception
        self.assertIsInstance(the_exception, FileNotFoundError)


if __name__ == "__main__":
    unittest.main()
