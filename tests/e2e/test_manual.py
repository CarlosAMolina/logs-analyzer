import unittest

# from src.backend.logs_etl import loader
from src.backend.logs_etl import transformer


class TestMain(unittest.TestCase):
    def _test_main(self):
        get_file_as_df = transformer.PandasParser("../logs-parser-results/access.log")
        logs = get_file_as_df()
        print(logs)
        # breakpoint()
        # logs.to_html("/tmp/logs.hml", justify="left")
        # printer = loader.LogsPrinter(logs)
        # logs.to_csv('access.log.csv')
        # from src import vt
        # vt.FileIpAnalyzer("../ip-addresses.txt").print_analysis_of_each_ip()
        # from src import ufw
        # ufw.FileIpAnalyzer("../ip-addresses.txt").print_rule_drop_ip_addresses()


if __name__ == "__main__":
    unittest.main()
