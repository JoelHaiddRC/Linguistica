import re

mapeo_acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}

def eliminar_stopwords(palabras: list, stopwords: list) -> list:
    """
    Dada una lista de tokens, elimina los tokens que son identificados como stopwords
    :param palabras: La lista de palabras (tokens) que va a ser revisada
    :param stopwords: La lista de stopwords a eliminar de la lista de tokens
    :return: Una sublista de palabras (tokens) que contiene los tokens sin stopwords
    """
    stop_words = set(stopwords)
    return [x for x in palabras if x not in stop_words]



def remover_puntuacion(palabras: list) -> list:
    """
    Elimina caulquier simbolo que no sea alfanumerico, ñ o vocal acentuada (minusculas)
    :param palabras: La lista de palabras (tokens) a la que se va a eliminar simbolos
    :return: Una lista con los tokens sin simbolos que no sean  alfanumerico, ñ o vocal acentuada (minusculas)
    """
    regex = r'[^a-z0-9ñáéíóúü]+'
    tokens = [re.sub(regex, '', palabra) for palabra in palabras]
    return [token for token in tokens if token]


def pasar_a_minusculas(palabras: list) -> list:
    """
    Convierte una lista de palabras (tokens) a su version en minusculas
    :param palabras: Las lista de palabras (tokens) a pasar a minusculas
    :return: La lista de palabras (tokens) en minusculas
    """
    return [palabra.lower() for palabra in palabras]



def remover_acentos(palabras: list) -> list:
    """
    Convierte las vocales acentuadas a su version sin acentos
    :param palabras: La lista de palabras (tokens) a las que se les quitara acentos
    :return: La lista de palabras (tokens) sin acentos
    """
    return [remover_acentos_palabra(palabra) for palabra in palabras]



def remover_acentos_palabra(palabra: str) -> str:
    """
    Funcion axuliar que elimina acentos de una palabra
    :param palabra: La palabra a la que se eliminaran los acentos
    :return: La palabra sin acentos
    """
    return ''.join([mapeo_acentos[letra] if letra in mapeo_acentos else letra for letra in palabra])


def remover_secuencia_asterisco(palabras: list) -> list:
    """
    En nuestro corpus a analizar, se identifica la cadena *0*. Eliminamos esta cadena de nuestro analisis
    :param palabras: La lista de palabras (tokens) a la que se va a *0*
    :return: Una lista con los tokens sin el token *0*
    """
    tokens = [palabra.replace("*0*", "")  for palabra in palabras]
    return [token for token in tokens if token]

def pre_procesar(palabras: list, stopwords: list) -> list:
    """
    Aplica un preprocesamiento general a una lista con palabras (tokens).
    Este consiste en pasar a minusculas, remover signos de puntuacion, normalizar acentos y remover stopwords.
    :param palabras: La lista de palabras (tokens) a las cuales se aplicara el preprocesamiento
    :param stopwords: La lista de stopwords a remover
    :return: La lista de palabras (tokens) con el procesamiento aplicado
    """
    texto = pasar_a_minusculas(palabras)
    texto = remover_secuencia_asterisco(texto)
    texto = remover_puntuacion(texto)
    texto = eliminar_stopwords(texto, stopwords)
    return remover_acentos(texto)