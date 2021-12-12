import unittest

# from src_python.logs import loader
from src_python.logs import transformer


class TestMain(unittest.TestCase):
    def _test_main(self):
        get_file_as_df = transformer.PandasParser("../logs-parser-results/access.log")
        logs = get_file_as_df()
        get_logs_summarized = transformer.LogsSummarize()
        logs_summarized = get_logs_summarized(logs)
        # breakpoint()
        # logs.to_html("../logs-parser-results/logs.hml", justify="left")
        logs_summarized.to_html(
            "../logs-parser-results/logs_summarized.html", justify="left"
        )
        # printer = loader.LogsPrinter(logs)
        # printer.print_logs_group_by_remote_addr()
        # logs.to_csv('access.log.csv')
        # from src_python import vt
        # vt.FileIpAnalyzer("../ip-addresses.txt").print_analysis_of_each_ip()
        # from src_python import ufw
        # ufw.FileIpAnalyzer("../ip-addresses.txt").print_rule_drop_ip_addresses()


if __name__ == "__main__":
    unittest.main()
