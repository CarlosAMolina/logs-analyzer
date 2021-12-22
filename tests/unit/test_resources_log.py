from http import HTTPStatus
import unittest
import mock

from src_python.resources import log
from tests import LOG_FILE


class TestLogListResource(unittest.TestCase):
    def test_get(self):
        with mock.patch("src_python.logs.manager.extractor.LOG_FILE", LOG_FILE):
            class_ = log.LogListResource()
            result = class_.get()
            self.assertEqual(2, len(result[0]["data"]))
            self.assertEqual(HTTPStatus.OK, result[1])


if __name__ == "__main__":
    unittest.main()
