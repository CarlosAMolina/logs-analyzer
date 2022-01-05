import unittest

from src.backend.logs_etl import transformer


class TestMain(unittest.TestCase):
    def _test_main(self):
        get_file_as_df = transformer.PandasParser("../logs-parser-results/access.log")
        logs = get_file_as_df()
        print(logs)
        # breakpoint()
        # logs.to_html("/tmp/logs.hml", justify="left")
        # logs.to_csv('access.log.csv')


if __name__ == "__main__":
    unittest.main()
