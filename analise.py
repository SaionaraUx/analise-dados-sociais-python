import pandas as pd


def extrair_dados(caminho_arquivo):
    """
    Função responsável por extrair os dados do arquivo CSV.
    """
    return pd.read_csv(caminho_arquivo)


def transformar_dados(df):
    """
    Função responsável pela limpeza e transformação dos dados.
    """
    df = df.dropna()

    # Exemplo de transformação
    df["Valor_Ajustado"] = df.iloc[:, 1] * 2

    return df


def carregar_dados(df, caminho_saida):
    """
    Função responsável por salvar os dados tratados.
    """
    df.to_csv(caminho_saida, index=False)


def main():
    print("Iniciando pipeline de dados...")

    # Extração
    df = extrair_dados("dados.csv")

    # Transformação
    df_transformado = transformar_dados(df)

    # Pequena análise
    media = df_transformado.iloc[:, 1].mean()
    print(f"Média calculada: {media}")

    # Carga
    carregar_dados(df_transformado, "dados_tratados.csv")

    print("Pipeline finalizado com sucesso!")


if __name__ == "__main__":
    main()
