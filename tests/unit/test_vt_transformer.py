import datetime
import json
import unittest

from backend.vt import transformer
import tests


class TestIPResults(unittest.TestCase):
    def test_get_last_modification_date(self):
        response = {"data": {"attributes": {"last_modification_date": 1638704981}}}
        vt_parser = transformer.IPResults(response)
        self.assertEqual(
            datetime.datetime(2021, 12, 5, 11, 49, 41), vt_parser.last_modification_date
        )

    def test_get_last_modification_date_if_value_not_in_response(self):
        response = {"data": {"attributes": {}}}
        vt_parser = transformer.IPResults(response)
        self.assertIsNone(vt_parser.last_modification_date)


class TestIPSummary(unittest.TestCase):
    def test_get_summary(self):
        with open(tests.IP_RESPONSE_PATH, "r") as f:
            response = json.load(f)
        vt_parser = transformer.IPSummary(response)
        self.assertEqual(
            "1/0/79 (malicious/suspicious/harmless) 2021-12-05 11:49:41 UTC",
            vt_parser.get_summary(),
        )

    def test_get_summary_error(self):
        response = {"error": "bar"}
        vt_parser = transformer.IPSummary(response)
        self.assertEqual(
            "-/-/- (malicious/suspicious/harmless) - UTC", vt_parser.get_summary()
        )


if __name__ == "__main__":
    unittest.main()
