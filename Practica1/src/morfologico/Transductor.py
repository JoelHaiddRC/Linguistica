import re

def define_verb(lema: str) -> str:

    regexs = {}

    #INDICATIVO
    #Presente:
    # o -> PRES/IND-1S
    # as -> PRES/IND-2S
    # a -> PRES/IND-3S
    # amos -> PRES/IND-1P|PRET/IND-1P 
    # an -> PRES/IND-2P

    #Copretérito
    # aba -> COP/IND-1S|COP/IND-3S
    # abas -> COP/IND-2S
    # aba -> COP/IND-3S|COP/IND-1S
    # ábamos -> COP/IND-1P
    # aban -> COP/IND-2P

    #Pretérito
    # é -> PRET/IND-1S
    # aste -> PRET/IND-2S
    # ó -> PRET/IND-3S
    # amos -> PRET/IND-1P|PRES/IND-1P
    # aron -> PRET/IND-2P

    #Futuro
    # ré -> FUT/IND-1S
    # rás -> FUT/IND-2S
    # rá -> FUT/IND-3S
    # remos -> FUT/IND-1P
    # rán -> FUT/IND-2P

    #Condicional
    # ría -> COND/IND-1S|3S
    # rías -> COND/IND-2S
    # ría -> COND/IND-3S|1S
    # ríamos -> CON/IND-1P
    # rían -> CON/IND-2P

    #SUBJUNTIVO
    #Presente:
    # e -> PRES/SUB-1S|3S
    # es -> PRES/SUB-2S
    # e -> PRES/SUB-3S|1S
    # emos -> PRES/SUB-1P 
    # en -> PRES/SUB-2P

    #Pretérito
    # ara|ase -> PRET/SUB-1S|3S
    # aras|ases -> PRET/SUB-2S
    # ara|ase -> PRET/SUB-3S|1S
    # áramos|ásemos -> PRET/SUB-1P
    # aran|asen -> PRET/SUB-2P

    #Futuro
    # are -> FUT/SUB-1S|3S
    # ares -> FUT/SUB-2S
    # are -> FUT/SUB-3S|3S
    # áremos -> FUT/SUB-1P
    # aren -> FUT/SUB-2P

    #Imperativo
    # ad -> IMP

    #Infinitivo
    # ar -> INF

    #Gerundio
    #ando -> GER
    
    #Participio
    #ado -> PAR

    regexs["-COND/IND-1P"]  = r"ríamos$"
    regexs["-COP/IND-1P"]   = r"ábamos$"
    
    regexs["-FUT/IND-1P"]   = r"remos$"
    regexs["-PRET/SUB-1P"]  = r"áramos|ásemos$"
    regexs["-FUT/SUB-1P"]   = r"áremos$"

    regexs["-COP/IND-2S"]           = r"abas$"
    regexs["-COP/IND-2P"]           = r"aban$"
    regexs["-PRET/IND-2S"]          = r"aste$"
    regexs["-PRET/IND-2P"]          = r"aron$"
    regexs["-COND/IND-2S"]          = r"rías$"
    regexs["-PRES/IND|PRET/IND-1P"] = r"amos$"
    regexs["-COND/IND-2P"]          = r"rían$"

    regexs["-PRES/SUB-1P "] = r"emos$"
    regexs["-PRET/SUB-2S"]  = r"aras|ases$"
    regexs["-PRET/SUB-2P"]  = r"aran|asen$"
    regexs["-FUT/SUB-2S"]   = r"ares$"
    regexs["-FUT/SUB-2P"]   = r"aren$"
    regexs["-GER"]          = r"ando$"

    regexs["-COP/IND-1S|3S"]    = r"aba$"
    regexs["-FUT/IND-2S"]       = r"rás$"
    regexs["-FUT/IND-2P"]       = r"rán$"
    regexs["-COND/IND-1S|3S"]   = r"ría$"
    regexs["-PRET/SUB-1S|3S"]   = r"ara|ase$"
    regexs["-FUT/SUB-1S|3S"]    = r"are$"
    regexs["-PAR"]              = r"ado$"

    regexs["-FUT/IND-1S"]   = r"ré$"
    regexs["-FUT/IND-3S"]   = r"rá$"
    regexs["-PRES/IND-2S"]  = r"as$"
    regexs["-PRES/IND-2P"]  = r"an$"
    regexs["-PRES/SUB-2S"]  = r"es$"
    regexs["-PRES/SUB-2P"]  = r"en$"
    regexs["-IMP"]          = r"ad$"
    regexs["-INF"]          = r"ar$"
    regexs["-IMP"]          = r"ad$"

    regexs["-PRES/IND-3S"]      = r"a$"
    regexs["-PRET/IND-3S"]      = r"ó$"
    regexs["-PRET/IND-1S"]      = r"é$"
    regexs["-PRES/IND-1S"]      = r"o$"
    regexs["-PRES/SUB-3S|1S"]   = r"e$"
    regexs["-PRES/IND-1S"]      = r"o$"


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
