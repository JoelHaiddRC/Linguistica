from collections import Counter


def iniciar_bpe(tokens:list)->list:
    """
    Funcion para inicializar el proceso de Byte Pair Encoding
    Contamos las frecuencias de cada token y separamos los tokens en subpalabras
    de una letra
    :param tokens: Los tokens de nuestro corpues a aplicar BPE
    :return: Un diccionario  cuyas llaves son los tokens dividos en letras y con valor la frecuencia del token
    """
    frecuencias = Counter()
    for token in tokens:
        letras = ' '.join(token)
        frecuencias[letras] += 1
    return frecuencias


def obtener_frec_subwords(frecuencias_tokens:Counter)-> Counter:
    """
    Obtiene las frecuencias de cada pareja consecutiva de subwords
    :param frecuencias_tokens: La frecuencia de los tokens de nuestro corpus
    :return: Un counter con las frecuencias de cada pareja consecutiva de subwords
    """
    subwords_frec = Counter()
    for token, frec in frecuencias_tokens.items():
        subwords = token.split()
        for i in range(len(subwords) - 1):
            subwords_frec[(subwords[i], subwords[i+1])] += frec
    return subwords_frec

def agregar_nueva_subword(frecuencias_tokens:Counter, nueva_subword: tuple)-> Counter:
    """
    Agregamos un nuevo subword a nuestro vocabulario, modifcamos los tokens para que se vea reflejado el uso
    del nuevo subword
    :param frecuencias_tokens: Un counter con los tokens de nuestro corpus y sus frecuencias
    :param nueva_subword: La nuevo subword a agregar
    :return:
    """
    tokens = Counter()
    for token, freq in frecuencias_tokens.items():
        subword = ''.join(nueva_subword)
        token_en_subword = token.replace(" ".join(nueva_subword), subword)
        tokens[token_en_subword] = freq
    return tokens


def aplicar_byte_pair_encoding(tokens:list, iteraciones: int) -> list:
    """
    Modifca los tokens de un corpus para generar nuevos tokens usando BPE.
    :param tokens: Los tokens de nuestro corpus
    :param iteraciones: El numero de iteraciones de BPE
    :return: Un nuevo counter con las frecuencias de cada subword generado por BPE para nuestro corpus
    """
    tokens_bpe = iniciar_bpe(tokens)
    i = iteraciones
    while i > 0:
        candidatos_subword = obtener_frec_subwords(tokens_bpe)
        max_subword =  max(candidatos_subword, key=candidatos_subword.get)
        tokens_bpe = agregar_nueva_subword(tokens_bpe, max_subword)
        i -= 1
    frecs_nuevos_tokens = Counter()
    for token, freq in tokens_bpe.items():
        nuevos_tokens = token.split()
        for sub_token in nuevos_tokens:
            frecs_nuevos_tokens[sub_token] += freq
    return frecs_nuevos_tokens
