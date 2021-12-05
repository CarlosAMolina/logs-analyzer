import unittest

from src_python import analyzer as m_analyzer
from src_python import parser
from src_python import ufw as m_ufw

# from src_python import vt as m_vt


class TestMain(unittest.TestCase):
    def test_main(self):
        get_file_as_df = parser.PandasParser("../access.log")
        logs = get_file_as_df()
        printer = m_analyzer.LogsPrinter(logs)
        printer.print_logs_group_by_remote_addr()
        # logs.to_csv('access.log.csv')
        # m_vt.FileIpAnalyzer("../ip-addresses.txt").print_analysis_of_each_ip()
        m_ufw.FileIpAnalyzer("../ip-addresses.txt").print_rule_drop_ip_addresses()

    if __name__ == "__main__":
        unittest.main()
