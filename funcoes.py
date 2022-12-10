import pandas as pd
from PIL import Image


def tratar_dataset(dataset_name:str, headers:list) -> pd.DataFrame:
    """Essa função usa a bilioteca pandas para ler o arquivo csv e atualizar o nome das colunas com uma lista de cabeçalhos.

    Args:
        dataset_name (str): Nome do dataset em csv.
        headers (list): Lista de titulos para atualizar.

    Returns:
        pd.DataFrame: Retorna o dataset com os titulos atualizados
    """
    return pd.read_csv(dataset_name, names=headers, header=0)


def importar_foto_perfil(nome_arquivo:str):
    """Cria variaveis do tipo image para usar no streamlit.image

    Args:
        nome_arquivo (str): nome do arquivo com a foto

    Returns:
        _type_: Retorna uma variavel image
    """
    return Image.open(nome_arquivo)


def descrever_dados(dataset:pd.DataFrame):
    """Descreve os dados do dataset informado

    Args:
        dataset (pd.DataFrame): dataset

    Returns:
        _type_: descrição do dataset
    """
    return dataset.describe()