import transform

if __name__ == "__main__":
    transformer = transform.GithubTransformer(owner= 'home-assistant', repo= 'operating-system')
    data = transformer.transform()

    for entry in data:
        print(str(entry))
