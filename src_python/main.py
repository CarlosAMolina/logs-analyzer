import pandas as pd

import parser


if __name__ == "__main__":
    get_file_as_df = parser.PandasParser()
    df = get_file_as_df("access.log")
    with pd.option_context(
        "display.max_rows",
        None,
        "display.max_columns",
        None,
    ):
        print(df.to_string())
    print(df.request.str.len().max())
    #df.to_csv('access.log.csv')
