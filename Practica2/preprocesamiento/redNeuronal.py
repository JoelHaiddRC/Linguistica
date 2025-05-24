import numpy as np
import math   
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#EJEMPLO
BOS = "<BOS>"
EOS = "<EOS>"
corpus = [BOS, "el", "niño", "juega",EOS,
          BOS, "el", "niño", "salta", EOS,
          BOS, "el", "perro", "juega", EOS,
          BOS, "el", "perro", "salta", EOS]

#VIEJO
def lista_bigramas(corpus:list, palabras_a_indices:dict) -> list:
    bigramas = []
    for i in range(len(corpus)-1):
        x = get_id(palabras_a_indices, corpus[i])
        y = get_id(palabras_a_indices, corpus[i+1])
        bigrama = (x, y)
        bigramas.append(bigrama)
    return bigramas

def get_id(palabra_a_id: dict, palabra: str) -> int:
    ETIQUETA_UNK = "UNKNOW"
    id_unknow = palabra_a_id[ETIQUETA_UNK]
    return palabra_a_id.get(palabra, id_unknow)

#EJEMPLO
palabras_a_indices = {"el" : 0, "niño" : 1, "perro" : 2, "juega" : 3, "salta" : 4, BOS : 5, EOS : 6, "UNKNOW" : 7}
indices_a_palabras = {0 : "el", 1 : "niño", 2 : "perro", 3 : "juega", 4 : "salta", 5 : BOS, 6 : EOS, 7: "UNKNOW"}
bigramas = lista_bigramas(corpus, palabras_a_indices)

#Inicializacion de variables
np.random.seed(42)

N = len(palabras_a_indices.keys())
d = 2
m = N
taza_aprend = 0.05
EPOCHS = 100

C = np.random.randn(d, N) / np.sqrt(N)
W =  np.random.randn(m, d) / np.sqrt(d)
b = np.random.randn(m) / np.sqrt(m)
U = np.random.randn(N,m) / np.sqrt(m)
c = np.random.randn(N) / np.sqrt(N)

#NUEVO

C_old = np.copy(C)
W_old = np.copy(W)
b_old = np.copy(b)
U_old = np.copy(U)
c_old = np.copy(c)

losses = []
for epoch in range(EPOCHS):
    # Acumula el riesgo de la epoch
    loss = 0
    for bigrama in bigramas:
        # Forward de entrenamiento
        #u_w = C.T[bigrama[0]]
        ## Salida
        #a = np.dot(W, u_w)
        #output = np.exp(a)

        ## Softmax
        #f = output / output.sum(0)
        
        #Obtener one-ho
        
        #Embedding
        Ci = C.T[bigrama[0]]

        #Capa oculta
        WCi = np.dot(W, Ci)
        hi = np.tanh(WCi + b)

        #Pre-activacion
        ai = np.dot(U, hi) + c

        #activacion
        expai = np.exp(ai)
        f =  expai / expai.sum(0)
                
        # Calcula loss por ejemplo
        loss += -np.log(f)[bigrama[1]]

        # Backpropagation
        # Variable de salida
        d_out = f
        d_out[bigrama[1]] -= 1

        U -= (taza_aprend * np.outer(d_out, hi))

        b -= taza_aprend * d_out
            
        dh = np.dot(d_out, U) * (1-(hi**2))
        W -= (taza_aprend * np.outer(dh, Ci))

        c -= taza_aprend * d_out

        dc = np.dot(dh, W)
        C.T[bigrama[0]] -= (taza_aprend * dc)

        # Guardamos el loss
    losses.append(loss)
    print(f"Epoch {epoch}, loss: {loss}")

#Forward
def forward(ind_palabra : int, N : int):
    #Embedding
    Ci = C.T[ind_palabra]
    
    #Capa oculta
    WCi = np.dot(W, Ci)
    tanh = np.vectorize(lambda x: math.tanh(x))
    hi = tanh(WCi + b)
    #Pre-activacion
    ai = np.dot(U, hi) + c

    #activacion
    expai = np.exp(ai)
    salidas =  expai / expai.sum(0)
    return salidas
    """
    #backwards
    #Capa de salida
    dout = np.zeros((len(probas)))
    j = ind_objetivo
    yi = 0
    for k in range(len(probas)):
        if(k == j):
            yi = 1
        else:
            yi = 0
        dout[k] = (probas[k] - yi)
    
    #Capa oculta
    dh = (1-(hi**2)) * (np.dot(dout, U[k,:])).sum()

    du = np.dot(dh, W)
    #Capa de emmbeding
    dc = np.dot(du, U)
        
    for k in range(len(dout)):
        U[ind_palabra, k] -= taza_aprend * np.dot(dout[k], hi)
        W[ind_palabra, k] -= taza_aprend * np.dot(dh[k], Ci)
        C[ind_palabra, k] -= taza_aprend * np.dot(dc[k], one_hot)
    """

def proba_bigrama(ind_palabra: int, ind_objetivo : int, N : int):
    probas = forward(ind_palabra, N)
    return probas[ind_objetivo]

#EJEMPLO

for palabra in palabras_a_indices.keys():
    print("calculando probas para: " + palabra + " = " + str(palabras_a_indices[palabra]))
    result = forward(palabras_a_indices[palabra], N)
    suma = 0
    lista_palabras = list(palabras_a_indices.keys())
    s = ""
    for i in range(len(result)):
        suma += result[i]
        r = lista_palabras[i] + " = " + str(result[i]) + "; "
        s += r
    print(f"{s}\n suma: {suma}\n")

#Perplejidad
def get_perplexity(corpus_eval : list, palabras_a_ind : dict) -> float:
    bigramas = lista_bigramas(corpus_eval, palabras_a_ind)
    probas = 0
    for bigrama in bigramas:
        if(probas != 0):
            probas *= 1/proba_bigrama(bigrama[0], bigrama[1], N)
        else:
            probas = 1/proba_bigrama(bigrama[0], bigrama[1], N)
    return probas ** (1/(len(corpus_eval)-2))

evaluacion = [BOS, "el", "niño", "salta", EOS]
perplejidad = get_perplexity(evaluacion, palabras_a_indices)
print(f"Perplejidad de la oración 'El niño salta': {perplejidad}")


def generate_words(palabras_a_ind: dict, ind_a_palabras: dict, longitud: int) -> str:
    oracion = ""
    ultima = BOS
    for i in range(longitud):
        result = forward(palabras_a_ind[ultima], N)
        indice = list(result).index(max(result))
        siguiente = ind_a_palabras[indice]
        if(siguiente == EOS):
            oracion += ". "
        elif(siguiente != BOS):
            oracion += f"{siguiente} "
        ultima = siguiente
    return oracion
print("Generando oracion: ")
print(generate_words(palabras_a_indices, indices_a_palabras, 10))


def plot_words(Z, ids):
    Z = PCA(2).fit_transform(Z)
    r=0
    plt.scatter(Z[:,0],Z[:,1], marker='o', c='teal')
    for label,x,y in zip(ids, Z[:,0], Z[:,1]):
        plt.annotate(label, xy=(x,y), xytext=(-1,1), textcoords='offset points', ha='center', va='bottom')
        r+=1

plot_words(C.T, list(palabras_a_indices.keys()))
plt.title('Embeddings')
plt.show()