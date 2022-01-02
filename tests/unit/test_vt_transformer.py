from unittest import mock
import json
import unittest
import os

import pandas as pd

from src.vt import transformer


class TestIpSummary(unittest.TestCase):
    def test_get_summary(self):
        with open(
            os.path.join(os.path.dirname(__file__), "files/ip-response.json"), "r"
        ) as f:
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


class TestFileAnalyzer(unittest.TestCase):
    @mock.patch("src.vt.transformer.IpSummary")
    @mock.patch("src.vt.extractor.RequestIp")
    def test_print_analysis_of_each_ip(self, mock_request_ip, mock_response_parser):
        mock_request_ip().get_analysis.return_value = "foo"
        mock_response_parser().get_summary.return_value = "bar"
        transformer.FileIpAnalyzer(
            os.path.join(os.path.dirname(__file__), "files/ip-addresses.txt")
        ).print_analysis_of_each_ip()


class TestIPsAnalyzerAsDf(unittest.TestCase):
    @mock.patch("src.vt.extractor.RequestIp")
    @mock.patch("src.vt.transformer.IpResults")
    def test_get_analysis_of_ips_as_df(self, mock_ip_results, mock_request_ip):
        class MockIPResults:
            malicious = 4.0
            suspicious = 3.0
            harmless = 10.0

            def __init__(self, *args):
                pass

        class MockIPResultsA(MockIPResults):
            last_modification_date = "2021-01"

        class MockIPResultsB(MockIPResults):
            last_modification_date = "2021-02"

        mock_ip_results.side_effect = [MockIPResultsA, MockIPResultsB]
        expected_result = pd.DataFrame(
            data={
                "malicious": [4, 4],
                "suspicious": [3, 3],
                "harmless": [10, 10],
                "last_modification_date": ["2021-01", "2021-02"],
            },
            index=["1.1.1.1", "2.2.2.2"],
        )
        get_vt_analysis_as_df_of_ips = transformer.IPsAnalyzerAsDf()
        result = get_vt_analysis_as_df_of_ips(["1.1.1.1", "2.2.2.2"])
        self.assertTrue(expected_result.equals(result))


if __name__ == "__main__":
    unittest.main()
