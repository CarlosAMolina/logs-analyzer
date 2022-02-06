from unittest import mock
import json
import unittest

from backend.vt import manager
import tests


class TestFunctions(unittest.TestCase):
    @mock.patch("backend.vt.extractor.RequestIP")
    def test_get_analysis_of_ip(self, mock_request_ip):
        with open(tests.IP_RESPONSE_PATH, "r") as f:
            vt_response = json.load(f)
        mock_request_ip().get_analysis.return_value = vt_response
        ip = "8.8.8.8"
        result = manager.get_analysis_of_ip(ip)
        self.assertEqual(
            {
                "ip": ip,
                "malicious": 1,
                "suspicious": 0,
                "harmless": 79,
                "lastModificationDate": "2021-12-05 11:49:41",
            },
            result.data,
        )


if __name__ == "__main__":
    unittest.main()
