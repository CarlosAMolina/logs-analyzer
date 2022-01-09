import unittest

from src.backend.logs_file_analyzer import transformer


class TestLogsAnalyzer(unittest.TestCase):
    def test_get_remote_addrs_count(self):
        class FakeLog:
            def __init__(self, remote_addr: str):
                self.remote_addr = remote_addr

        logs = [
            FakeLog("1.1.1.1"),
            FakeLog("2.2.2.2"),
            FakeLog("2.2.2.2"),
        ]
        expected_result = [
            {"remoteAddr": "2.2.2.2", "count": 2},
            {"remoteAddr": "1.1.1.1", "count": 1},
        ]
        result = [
            remote_addr_count.data
            for remote_addr_count in transformer.get_remote_addrs_count(logs)
        ]
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
