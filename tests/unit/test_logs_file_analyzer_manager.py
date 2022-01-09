import unittest

from src.backend.logs_file_analyzer import manager
from tests import LOGS_PATH


class TestFunctions(unittest.TestCase):
    def test_get_remote_addrs_count_from_file(self):
        remote_addrs_count = manager.get_remote_addrs_count_from_file(LOGS_PATH)
        result = [remote_addr_count.data for remote_addr_count in remote_addrs_count]
        self.assertEqual(
            [
                {"count": 2, "remoteAddr": "8.8.8.8"},
                {"count": 1, "remoteAddr": "111.222.33.4"},
            ],
            result,
        )


if __name__ == "__main__":
    unittest.main()
