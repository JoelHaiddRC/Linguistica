import numpy as np
import math   

#EJEMPLO
BOS = "<BOS>"
EOS = "<EOS>"
corpus = [BOS, "el", "niño", "juega",EOS,
          BOS, "el", "niño", "salta", EOS,
          BOS, "el", "perro", "juega", EOS,
          BOS, "el", "perro", "salta", EOS]

#NUEVO:
def crear_one_hot(ind : int, size : int) -> list:
    onehot = np.zeros(size)
    onehot[ind] = 1
    return onehot

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
taza_aprend = 0.1
EPOCHS = 1000

C = np.random.randn(d, N) / np.sqrt(N)
W =  np.random.randn(m, d) / np.sqrt(d)
b = np.random.randn(m) / np.sqrt(m)
U = np.random.randn(N,m) / np.sqrt(m)
c = np.random.randn(N) / np.sqrt(N)

#NUEVO

#Backward
def backward(EPOCHS : int, W : np.array):
    losses = []
    for epoch in range(EPOCHS):
        # Acumula el riesgo de la epoch
        loss = 0
        for bigrama in bigramas:
            # Forward de entrenamiento
            u_w = C.T[bigrama[0]]
            # Salida
            a = np.dot(W, u_w)
            output = np.exp(a)

            # Softmax
            f = output / output.sum(0)
            # Calcula loss por ejemplo
            loss += -np.log(f)[bigrama[1]]

            # Backpropagation
            # Variable de salida
            d_out = f
            d_out[bigrama[1]] -= 1

            # Variable de embedding
            d_emb = np.dot(d_out, W)

            # Actualizamos a la salida
            W -= taza_aprend * np.outer(d_out, u_w)

            # Actualizamos embedding
            C.T[bigrama[0]] -= taza_aprend * d_emb
        # Guardamos el loss
        losses.append(loss)
        print(f"Epoch {epoch}, loss: {loss}")


#Forward
def forward(ind_palabra : int, N : int):
    #Obtener one-hot
    one_hot = crear_one_hot(ind_palabra, N)


    #Embedding
    Ci = np.dot(C,one_hot)
    
    #Capa oculta
    WCi = np.dot(W, Ci)
    tanh = np.vectorize(lambda x: math.tanh(x))
    hi = tanh(WCi + b)
    #Pre-activacion
    ai = np.dot(U, hi) + c

    #activacion
    probas = []
    npexp = np.vectorize(lambda x: math.exp(x))
    expai = npexp(ai) 
    for aj in ai:
        probas.append(math.exp(aj) / expai.sum())
    return probas
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



backward(EPOCHS, W)
#EJEMPLO
for bigrama in bigramas:
    print("calculando probas para: " + str(bigrama[0]) + " = " + indices_a_palabras[bigrama[0]])
    result = forward(bigrama[0], N)
    pal = list(palabras_a_indices.keys())
    for i in range(len(result)):
        r = pal[i] + " = " + str(result[i])
        print(r)