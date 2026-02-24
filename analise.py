import pandas as pd


def extrair_dados(caminho_arquivo):
    """Função responsável por ler o arquivo CSV"""
    return pd.read_csv(caminho_arquivo)


def transformar_dados(df):
    """Função responsável pela limpeza e transformação"""
    df = df.dropna()
    df["Valor_Ajustado"] = df.iloc[:, 1] * 2
    return df


def carregar_dados(df, caminho_saida):
    """Função responsável por salvar os dados tratados"""
    df.to_csv(caminho_saida, index=False)


def main():
    print("Iniciando pipeline...")

    df = extrair_dados("dados.csv")
    df_transformado = transformar_dados(df)

    media = df_transformado.iloc[:, 1].mean()
    print(f"Média calculada: {media}")

    carregar_dados(df_transformado, "dados_tratados.csv")

    print("Pipeline finalizado com sucesso!")


if __name__ == "__main__":
    main()
