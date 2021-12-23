import unittest

from src_python.logs import exception


class TestLogInFileNotParsedError(unittest.TestCase):
    def test_LogInFileNotParsedError(self):
        with self.assertRaises(exception.LogInFileNotParsedError) as cm:
            raise exception.LogInFileNotParsedError("foo")
        the_exception = cm.exception
        self.assertIsInstance(the_exception, exception.LogInFileNotParsedError)
        self.assertEqual("foo", str(the_exception))


if __name__ == "__main__":
    unittest.main()
