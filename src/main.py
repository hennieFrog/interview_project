from pandas import DataFrame
import transform, utils

if __name__ == "__main__":

    transformer = transform.GithubTransformer(owner= 'home-assistant', repo= 'operating-system')
    data = DataFrame()
    data = transformer.transform()

    merged_df = utils.upsert_df(data)

    print(merged_df.head())
    merged_df.to_csv('out.csv', index=False)


