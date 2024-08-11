import pandas as pd


def imprimir_20_primeiras_linhas():
    df = pd.read_csv('ranking_medalhas.csv', header=None, skiprows=1)
    print(df.head(20))


if __name__ == '__main__':
    imprimir_20_primeiras_linhas()
