import unittest

from src_python.logs import manager
from tests import log_file


class TestFunctions(unittest.TestCase):
    def test_get_logs_from_file(self):
        result = manager.get_logs_from_file(log_file)
        self.assertEqual(2, len(result))


if __name__ == "__main__":
    unittest.main()
