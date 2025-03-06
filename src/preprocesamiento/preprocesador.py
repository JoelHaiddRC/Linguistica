import re

mapeo_acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
#signos_puntuacion = "¿¡!”#$%&'()*+,-./:;<=>?@[<\\]^_`{|}~"


def eliminar_stopwords(palabras: list, stopwords: list) -> list:
    """
        Dada una lista con stopwrods y un lista con palabras,
        elimina todas las palabras identificados como stop word

    """
    stop_words = set(stopwords)
    return [x for x in palabras if x not in stop_words]



def remover_puntuacion(palabras: list) -> list:
    """
        Elimina los signos de puntuacion definidos en la lista
    """
    regex = r'[^a-z0-9ñáéíóúü]+'
    tokens = [re.sub(regex, '', palabra) for palabra in palabras]
    return [token for token in tokens if token]

def pasar_a_minusculas(palabras: list) -> list:
    """
        Pasa cada palabra en la lista a su version en minusculas
    """
    return [palabra.lower() for palabra in palabras]



def remover_acentos(palabras: list) -> list:
    """
        Cambia cada acento a su version sin acento, para cada palabra en la lista
    """
    return [remover_acentos_palabra(palabra) for palabra in palabras]



def remover_acentos_palabra(palabra: str) -> str:
    """
        Funcion auxiliar para cambiar los acentos en una palabra a su version
        sin acentos
    """
    return ''.join([mapeo_acentos[letra] if letra in mapeo_acentos else letra for letra in palabra])


def pre_procesar(palabras: list, stopwords: list) -> list:
    """
    Aplixa un preprocesamiento general a una lista con palabras.
    Este consiste en pasar a minusculas, remover signos de puntuacion, normalizar acentos y remover stopwords.
    :param palabras: La lista de palabras o tokens a las cuales se aplicara el preprocesamiento
    :param stopwords: La lista de stopwords a remover
    :return: Una lista de palabras a las cuales se aplico el procesamiento
    """
    texto = pasar_a_minusculas(palabras)
    texto = remover_puntuacion(texto)
    texto = eliminar_stopwords(texto, stopwords)
    return remover_acentos(texto)