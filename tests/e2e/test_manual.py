import unittest

from src_python import analyzer
from src_python import parser


class TestMain(unittest.TestCase):
    def _test_main(self):
        get_file_as_df = parser.PandasParser("../access.log")
        logs = get_file_as_df()
        printer = analyzer.LogsPrinter(logs)
        printer.print_logs_group_by_remote_addr()
        # logs.to_csv('access.log.csv')
        # from src_python import vt
        # vt.FileIpAnalyzer("../ip-addresses.txt").print_analysis_of_each_ip()
        # from src_python import ufw
        # ufw.FileIpAnalyzer("../ip-addresses.txt").print_rule_drop_ip_addresses()


if __name__ == "__main__":
    unittest.main()
