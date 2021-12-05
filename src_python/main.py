"""This file is used for manual tests.
"""

import analyzer as m_analyzer
import parser

# import vt as m_vt


if __name__ == "__main__":
    get_file_as_df = parser.PandasParser()
    logs = get_file_as_df("../access.log")
    printer = m_analyzer.LogsPrinter(logs)
    printer.print_logs_group_by_remote_addr()
    # logs.to_csv('access.log.csv')
    # m_vt.FileIpAnalyzer("../ip-addresses.txt").print_analysis_of_each_ip()
