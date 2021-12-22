import os
import unittest

from src_python.logs import manager


class TestFunctions(unittest.TestCase):
    def test_get_logs_from_file(self):
        file = os.path.join(os.path.dirname(__file__), "../files/access.log")
        result = manager.get_logs_from_file(file)
        self.assertEqual(2, len(result))


if __name__ == "__main__":
    unittest.main()
