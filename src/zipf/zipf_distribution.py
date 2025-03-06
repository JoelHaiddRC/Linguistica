import numpy as np
import pandas as pd
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


