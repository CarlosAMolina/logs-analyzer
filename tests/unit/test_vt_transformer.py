import json
import unittest

from src.backend.vt import transformer
import tests


class TestIpSummary(unittest.TestCase):
    def test_get_summary(self):
        with open(tests.IP_RESPONSE_PATH, "r") as f:
            response = json.load(f)
        vt_parser = transformer.IpSummary(response)
        self.assertEqual(
            "1/0/79 (malicious/suspicious/harmless) 2021-12-05 11:49:41 UTC",
            vt_parser.get_summary(),
        )

    def test_get_summary_error(self):
        response = {"error": "bar"}
        vt_parser = transformer.IpSummary(response)
        self.assertEqual(
            "-/-/- (malicious/suspicious/harmless) - UTC", vt_parser.get_summary()
        )


if __name__ == "__main__":
    unittest.main()
