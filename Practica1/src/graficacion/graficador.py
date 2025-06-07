import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def graficar_frecuencias(tabla_frecuencias: pd.DataFrame, ax, log_scale: bool):
    """
    Grafica una tabla de frecuencias de los rangos de tokens en un corpus.
    :param tabla_frecuencias: La tabla con las frecuencias de cada rango
    :param ax: Los ejes donde dibujaremos la grafica
    :param log_scale: Indica si la grafica debe modificarse para usar escala logaritmica
    """
    rango = tabla_frecuencias.index.values.tolist()
    frecuencias = tabla_frecuencias["frecuencia"]
    ax.plot(rango, frecuencias, "-o")
    if log_scale:
        ax.set_xlabel("Log Rango (r)")
        ax.set_ylabel("Log frecuencia")
        ax.set_xscale("log")
        ax.set_yscale("log")
    else:
        ax.set_xlabel("Rango (r)")
        ax.set_ylabel("Frecuencia")
    ax.set_title("Frecuencia por rango")


def graficar_ley_zipf(tabla_ley_zipf: pd.DataFrame, ax):
    """
    Grafica una tabla de rangos con sus valores de la ley de zipf
    :param tabla_ley_zipf: Un data frame con los rangos y sus valores de la ley de zipf en logaritmo
    :param ax: Los ejes donde dibujaremos la grafica
    :return:
    """
    rango = tabla_ley_zipf["Rango"]
    valor_zipf = tabla_ley_zipf["Zipf"]
    ax.plot(rango, valor_zipf, color="r")
    ax.set_xlabel("Log Rango (r)")
    ax.set_ylabel("Log Ley Zipf")
    ax.set_xscale("log")
    ax.set_title("Frecuencias Ley Zipf")



def graficar_zipf_frec(tabla_zipf: pd.DataFrame, tabla_frecuencias, ax):
    """
    Graficamos una comparacion en entre las frecuencias de cada rango y sus valores con la ley de zipf
    :param tabla_zipf: Un data frame con los rangos y sus valores de la ley de zipf en logaritmo
    :param tabla_frecuencias:  Un dataframe con las frecuencias de cada rango
    :param ax: Los ejes donde dibujaremos la grafica
    :return:
    """
    rango = tabla_zipf["Rango"]
    frecuencias = tabla_frecuencias["frecuencia"].apply(lambda x: np.log(x))
    valor_zipf = tabla_zipf["Zipf"]
    ax.plot(rango, frecuencias, color="blue", label="Aprox_Frecuentista")
    ax.plot(rango, valor_zipf, color="red", label="Aprox_Zipf")
    ax.set_xlabel("Rango (r) en log")
    ax.set_ylabel("Frecuencia en log")
    ax.set_xscale("log")
    ax.set_title("Comparacion de Distribuciones")