from pandas import DataFrame
import transform


if __name__ == "__main__":
    transformer = transform.GithubTransformer(owner= 'home-assistant', repo= 'operating-system')
    data = DataFrame()
    data = transformer.transform()

    print(data.head())
    data.to_csv('out.csv')

