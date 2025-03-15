import numpy as np
import pandas as pd
from nest_asyncio import apply
from scipy.optimize import minimize



def estimar_param_zipf(tabla_frecuencias: pd.DataFrame) -> float:
    """
    Estima el parametro alpha de una distribucion zipf utilizando las frecuencias de un corpus dado
    :param tabla_frecuencias: Las frecuencias de los tokens de un corpus
    :return: El parametro alpha de la distribucion zipf para el corpus dado
    """
    rangos = np.array(tabla_frecuencias.index) + 1
    frecuencias = np.array(tabla_frecuencias["frecuencia"])

    # Valor inicial propuesto para alpha
    alpha0 = 1

    # Error cuadratico, visto en funcion de alpha
    error_cuadratico = lambda a: sum((np.log(frecuencias)-(np.log(frecuencias[0])-a*np.log(rangos)))**2)

    # Minimizamos el error cuadratico usando por minimos cuadrados
    alpha = minimize(error_cuadratico, alpha0).x[0]

    return alpha


def crea_tabla_zipf(alpha, tabla_frecuencias) -> pd.DataFrame:
    """
    Dado el parametro alpha de distribucion de zipf para el corpus dado, calcula la distribucion zipf para cada rango del
    corpus. Generamos un dataframe con los rangos y sus valores de la distribucion zipf
    :param alpha: El parametro alpha de la distribucion zipf
    :param tabla_frecuencias: Las frecuencias de cada token del corpus
    :return: Un dataframe con los valores de la distribucion zipf para cada rango del corpus
    """
    max_freq = tabla_frecuencias["frecuencia"].max()
    rangos = [x+1 for x in range(len(tabla_frecuencias.index))]
    calcular_zipf = lambda rango: np.log(max_freq)- alpha * np.log(rango)
    ley_zipf = [calcular_zipf(x) for x in rangos]
    return pd.DataFrame({'Rango': rangos, 'Zipf': ley_zipf})


