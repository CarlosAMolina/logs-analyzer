import unittest

from src.logs import manager
from tests import LOG_FILE


class TestFunctions(unittest.TestCase):
    def test_get_logs_from_file(self):
        result = manager.get_logs_from_file(LOG_FILE)
        self.assertEqual(2, len(result))


if __name__ == "__main__":
    unittest.main()
