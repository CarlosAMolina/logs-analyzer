import unittest

from src_python import parser as m_parser

class TestLineParser(unittest.TestCase):
    def setUp(self):
        self.parser = m_parser.LineParser(None)

    def test_get_ip(self):
        self.assertEqual("8.8.8.8", self.parser.ip)


class TestFileParser(unittest.TestCase):
    def test_get_file_parsed(self):
        parse_file = m_parser.FileParser()
        line_parsed = parse_file("tests/access.log")[0]
        self.assertEqual("8.8.8.8", line_parsed.ip)


if __name__ == '__main__':
    unittest.main()

