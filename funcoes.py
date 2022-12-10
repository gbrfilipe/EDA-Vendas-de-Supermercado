import pandas as pd
from PIL import Image

def tratar_dataset(dataset_name:str, headers:list) -> pd.DataFrame:

    return pd.read_csv(dataset_name, names=headers, header=0)


def importar_foto_perfil(nome_arquivo:str):
    
    return Image.open(nome_arquivo)


def descrever_dados(dataset:pd.DataFrame):
    
    return dataset.describe()