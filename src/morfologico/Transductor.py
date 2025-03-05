import re

def define_verb(lema: str) -> str:

    regexs = {}

    #Presente:
    # o -> PRES-1S
    # as -> PRES-2S
    # a -> PRES-3S
    # amos -> PRES-1P/PRET-1P 
    # an -> PRES-2P

    #Copretérito
    # aba -> COP-1S/COP-3S
    # abas -> COP-2S
    # aba -> COP-3S/COP-1S
    # ábamos -> COP-1P
    # aban -> COP-2P

    #Pretérito
    # é -> PRET-1S
    # aste -> PRET-2S
    # ó -> PRET-3S
    # amos -> PRET-1P/PRES-1P
    # aron -> PRET-2P

    #Futuro
    # ré -> FUT-1S
    # rás -> FUT-2S
    # rá -> FUT-3S
    # remos -> FUT-1P
    # rán -> FUT-2P

    #Condicional
    # ría -> COND-1S/3S
    # rías -> COND-2S
    # ría -> COND-3S/1S
    # ríamos -> CON-1P
    # rían -> CON-2P

    #Infinitivo
    # ar -> INF

    #Gerundio
    #ando -> GER
    
    #Participio
    #ado -> PAR

    regexs["-COND-1P"]      = r"ríamos$"
    regexs["-COP-1P"]       = r"ábamos$"

    regexs["-COP-2S"]       = r"abas$"
    regexs["-COP-2P"]       = r"aban$"
    regexs["-PRET-2S"]      = r"aste$"
    regexs["-PRET-2P"]      = r"aron$"
    regexs["-COND-2S"]      = r"rías$"
    regexs["-PRES/PRET-1P"] = r"amos$"
    regexs["-COND-2P"]      = r"rían$"
    regexs["-GER"]          = r"ando$"
    regexs["-FUT-1P"]       = r"remos$"

    regexs["-COP-1S/3S"]    = r"aba$"
    regexs["-FUT-2S"]       = r"rás$"
    regexs["-FUT-2P"]       = r"rán$"
    regexs["-COND-1S/3S"]   = r"ría$"
    regexs["-PAR"]          = r"ado$"

    regexs["-FUT-1S"]      = r"ré$"
    regexs["-FUT-3S"]       = r"rá$"
    regexs["-PRES-2S"]      = r"as$"
    regexs["-PRES-2P"]      = r"an$"
    regexs["-INF"]          = r"ar$"

    regexs["-PRES-3S"]      = r"a$"
    regexs["-PRET-3S"]      = r"ó$"
    regexs["-PRET-1S"]      = r"é$"
    regexs["-PRES-1S"]      = r"o$"

    for regex in regexs.keys():
        word = re.sub(regexs[regex], regex, lema)
        if word != lema:
            return word
    return word

archivo = open("../../data/palabras.txt")
lineas = archivo.readlines()
print("Clasificando verbos: ")
for linea in lineas:
    for palabra in linea.split():
        print(palabra + " " + define_verb(palabra))
print("Fin del archivo")
archivo.close()
