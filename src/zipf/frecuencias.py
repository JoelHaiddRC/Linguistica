from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def obtener_top_frecuencias(tokens: Counter, top_n: int) -> list:
    return [_[1] for _ in tokens.most_common(top_n)]

def obtener_frequencias(tokens: Counter) -> list:
    num_tipos = len(tokens)
    return [_[1] for _ in tokens.most_common(num_tipos)]

def crear_tabla_frecuencias(tokens: Counter) -> pd.DataFrame:
    tabla_datos = pd.DataFrame.from_dict(tokens, orient='index', columns=['frecuencia'])
    tabla_datos.sort_values('frecuencia', ascending=False, inplace=True)
    tabla_datos.reset_index(inplace=True)
    tabla_datos.rename(columns={'index': 'palabra'}, inplace=True)
    return tabla_datos

