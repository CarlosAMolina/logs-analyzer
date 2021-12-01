"""This file is used for manual tests.
"""

import pandas as pd

import analyzer
import parser


if __name__ == "__main__":
    get_file_as_df = parser.PandasParser()
    logs = get_file_as_df("../access.log")
    printer = analyzer.LogsPrinter(logs)
    printer.print_full_logs()
    printer.print_remote_addr()
    printer.print_remote_addr_count()
    # print(df.request.str.len().max())
    # df.to_csv('access.log.csv')
