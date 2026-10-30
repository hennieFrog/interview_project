from pandas import DataFrame, concat, read_csv

def upsert_df(new_df: DataFrame) -> DataFrame:
    old_df = DataFrame()

    try:
        old_df = read_csv('out.csv')
    except FileNotFoundError:
        print('No existing files, creating new file.')

    modified_rows = new_df.index.intersection(old_df.index)
    concatenated_rows = new_df.index.difference(old_df.index)

    result = old_df.copy()
    result.loc[modified_rows] = new_df.loc[modified_rows]
    result = concat([result, new_df.loc[concatenated_rows]])

    return result

