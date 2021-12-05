import unittest
import os

from src_python import ufw


class TestRuleGenerator(unittest.TestCase):
    def test_get_drop_ip(self):
        self.assertEqual(
            "-A ufw-before-input -s 1.1.1.1 -j DROP",
            ufw.RuleGenerator().get_drop_ip("1.1.1.1"),
        )


class TestFileIpAnalyzer(unittest.TestCase):
    def test_print_rule_drop_ip_addresses_does_not_raise_error(self):
        ufw.FileIpAnalyzer(
            os.path.join(os.path.dirname(__file__), "files/ip-addresses.txt")
        ).print_rule_drop_ip_addresses()


if __name__ == "__main__":
    unittest.main()
