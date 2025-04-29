from collections import Counter
import pandas as pd
import numpy as np



def obtener_top_frecuencias(tokens: Counter, top_n: int) -> list:
    """
    Dada las frecuencuas de cada token, obtiene los n tokes con mayor frecuencia
    :param tokens: Los tokens con sus frecuencias
    :return: Una lista ordenada (de forma ascendente) con los n tokes de mayor de frecuencia
    """
    return [_[1] for _ in tokens.most_common(top_n)]

def obtener_frequencias(tokens: Counter) -> list:
    """
    Convierte el conteo de tokes en una lista
    """
    num_tipos = len(tokens)
    return [_[1] for _ in tokens.most_common(num_tipos)]

def crear_tabla_frecuencias(tokens: Counter) -> pd.DataFrame:
    """
    Dadas las frecuencias de los tokens, generamos una tabla (dataframe) con
    dos columnas, [palabra, frecuencia], que indican el token y su frecuencia
    :param tokens: Los tokens con sus frecuencias
    :return: Una tabla con los tokens con frecuencias
    """
    tabla_datos = pd.DataFrame.from_dict(tokens, orient='index', columns=['frecuencia'])
    tabla_datos.sort_values('frecuencia', ascending=False, inplace=True)
    tabla_datos.reset_index(inplace=True)
    tabla_datos.rename(columns={'index': 'palabra'}, inplace=True)
    return tabla_datos

