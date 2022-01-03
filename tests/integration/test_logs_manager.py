import unittest

from src.backend.logs_etl import manager
from tests import LOGS_PATH


class TestFunctions(unittest.TestCase):
    def test_get_logs_from_file(self):
        result = manager.get_logs_from_file(LOGS_PATH)
        self.assertEqual(2, len(result))


if __name__ == "__main__":
    unittest.main()
