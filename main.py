import pandas as pd


def le_csv():
    # Lê o arquivo CSV original com os dados das medalhas
    df = pd.read_csv('quadromedalhas.csv')
    return df


def peso_medalhas(df):
    peso_ouro = 3
    peso_prata = 2
    peso_bronze = 1
    df['Peso_Total'] = (df['Ouro'] * peso_ouro) + (df['Prata'] * peso_prata) + (df['Bronze'] * peso_bronze)

    # Ordenar por Peso_Total, depois por Ouro, Prata e Bronze (do maior para o menor),
    # isso garante que países com maior número de ouros fiquem na frente caso empatem no peso,
    # com número maior numero de pratas caso empatem no ouro tb e assim por diante
    df_ordenado = df.sort_values(by=['Peso_Total', 'Ouro', 'Prata', 'Bronze'], ascending=[False, False, False, False])

    # Calcular o número total de grupos (para inverter a ordem)
    total_grupos = df_ordenado.groupby(['Peso_Total', 'Ouro', 'Prata', 'Bronze']).ngroup().max() + 1

    # Adicionar uma coluna de posição considerando empates, ajustando para a ordem correta
    df_ordenado['Posição'] = total_grupos - df_ordenado.groupby(['Peso_Total', 'Ouro', 'Prata', 'Bronze']).ngroup()

    return df_ordenado


def salva_csv(df_ordenado):
    colunas = ['Posição'] + [coluna for coluna in df_ordenado.columns if coluna != 'Posição']  # conserta a ordem da
    # coluna de posicoes
    df_ordenado = df_ordenado[colunas]
    df_ordenado.to_csv('ranking_medalhas.csv', index=False)
    print("Arquivo 'ranking_medalhas.csv' criado com sucesso.")


if __name__ == '__main__':
    df = le_csv()
    df_ordenado = peso_medalhas(df)
    salva_csv(df_ordenado)
