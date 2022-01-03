from unittest import mock
import unittest

from src.backend.vt import extractor


def mocked_requests_get(*args, **kwargs):
    """This method will be used by the mock to replace requests.get

    ..https://stackoverflow.com/questions/15753390/how-can-i-mock-requests-and-the-response

    """

    class MockResponse:
        def __init__(self, json_data, status_code):
            self._json_data = json_data
            self._status_code = status_code

        def json(self):
            return self._json_data

    return MockResponse({"data": "foo"}, 200)


class TestRequestIp(unittest.TestCase):
    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_get_analysis(self, mock_get):
        vt_ip = extractor.RequestIp()
        response = vt_ip.get_analysis("8.8.8.8")
        self.assertEqual({"data": "foo"}, response)


if __name__ == "__main__":
    unittest.main()
