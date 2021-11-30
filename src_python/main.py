import pandas as pd

import parser


if __name__ == "__main__":
    get_file_as_df = PandasParser()
    df = get_file_as_df("../access.log")
    with pd.option_context(
        "display.max_rows",
        None,
        "display.max_columns",
        None,
    ):
        print(df.to_string())
    print(df)
    print(dir(parser.LogParser))
