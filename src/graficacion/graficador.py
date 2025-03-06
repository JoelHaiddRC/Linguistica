import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def graficar_frecuencias(tabla_frecuencias: pd.DataFrame, ax, log_scale: bool) -> list:
    rango = tabla_frecuencias.index.values.tolist()
    frecuencias = tabla_frecuencias["frecuencia"]
    ax.plot(rango, frecuencias, "-o")
    ax.set_xlabel("Rango (r)")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Frecuencia por rango")
    if log_scale:
        ax.set_xscale("log")
        ax.set_yscale("log")
    return ax

