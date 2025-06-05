import numpy as np
import math
import random
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import torch    
import torch.nn as nn

#EJEMPLO
BOS = "<BOS>"
EOS = "<EOS>"
corpus = [[BOS, "el", "niño", "juega"],
          [BOS, "el", "niño", "salta"],
          [BOS, "el", "perro", "juega"],
          [BOS, "el", "perro", "salta"]]

salidas = [["el", "niño", "juega",EOS],
          ["el", "niño", "salta", EOS],
          ["el", "perro", "juega", EOS],
          ["el", "perro", "salta", EOS]]
#VIEJO
def lista_indices(corpus:list, palabras_a_indices:dict) -> list:
    """Genera una lista de indices que representan las palabras de un corpus 
    Parameters
    ----------
    corpus : list
        corpus a procesar
    indices_a_palabras : dict
        Diccionario de palabras a indices
    Returns
    -------
    list
        Lista de indices que representan las palabras del corpus
    """
    indices = []
    for sent in corpus:
        renglon = []
        for token in sent:
            renglon.append(get_id(palabras_a_indices, token))
        indices.append(renglon)
    return indices

def get_id(palabra_a_id: dict, palabra: str) -> int:
    ETIQUETA_UNK = "UNKNOW"
    id_unknow = palabra_a_id[ETIQUETA_UNK]
    return palabra_a_id.get(palabra, id_unknow)

#EJEMPLO
palabras_a_indices = {"el" : 0, "niño" : 1, "perro" : 2, "juega" : 3, "salta" : 4, BOS : 5, EOS : 6, "UNKNOW" : 7}
indices_a_palabras = {0 : "el", 1 : "niño", 2 : "perro", 3 : "juega", 4 : "salta", 5 : BOS, 6 : EOS, 7: "UNKNOW"}
x = lista_indices(corpus, palabras_a_indices)
y = lista_indices(salidas, palabras_a_indices)
print(x)
print(y)
#Inicializacion de variables

class RecurrentNetwork(nn.Module):
    def __init__(self, dim_in, dim_out, dim=100, dim_h=200):
        super().__init__()
        #Capa de embedding
        self.emb = nn.Embedding(dim_in,dim)
        #Capa de RNN (bidireccional)
        self.recurrence = nn.RNN(dim, dim_h, bidirectional=True)
        #Capa lineal
        lineal = nn.Linear(2*dim_h,dim_out)
        #Activacion
        pre = nn.Softmax(dim=2)
        #Salida
        self.ffw = nn.Sequential(lineal, pre)
        
    def forward(self, x):
        #Se convierte en tensor
        x = torch.tensor(x)
        #Embedding
        x = self.emb(x)
        x = x.unsqueeze(1)
        #Capas recurrentes
        h, c = self.recurrence(x)
        #Activación
        h = h.tanh()
        #Salida
        y_pred = self.ffw(h)
        y_pred = y_pred.transpose(1, 2)
        return y_pred
    
#Se crea la red recurrente
#Numero de iteraciones
EPOCHS = 100
#Taza de aprendizaje
LEARNING_RATE = 0.02
#Dimension
dim = 2

rnn = RecurrentNetwork(len(indices_a_palabras.keys()), len(indices_a_palabras.keys()))

#Se define la función de riesgo y el optimizador
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adagrad(rnn.parameters(), LEARNING_RATE)

#Se entrena el modelo
for epoch in range(EPOCHS):
    for x_i, y_i in zip(x, y):
        #Forward
        y_pred = rnn(x_i)

        #Backward
        y_i = (torch.tensor(y_i)).unsqueeze(1)

        #Se calcula el eror
        loss = criterion(y_pred, y_i)

        #zero grad
        optimizer.zero_grad()
        #Backprop
        loss.backward()
        #Actualizar parametros
        optimizer.step()

    print(f"Epoch={epoch}. Training loss={loss}")


def get_valor(tupla):
    return tupla[1]

def get_proba(corpus_eval : list, palabras_a_ind : dict, sort_func) -> list:
    probas = []
    ind_corpus = [palabras_a_ind[w] for w in corpus_eval]
    output = rnn(ind_corpus)
    for i in range(len(corpus_eval)):
        renglon = []
        for j in range(len(palabras_a_ind.keys())):
            palabras = list(palabras_a_ind.keys())
            valor = output[i][j].item()
            renglon.append((palabras[j], valor, j))
        renglon.sort(key=sort_func, reverse=True)
        probas.append(renglon)
    return probas


prueba = [BOS, "el", "niño", "salta", EOS]
probas = get_proba(prueba, palabras_a_indices, get_valor)
"""
for p in range(len(probas)):
    print(f"Probas para {prueba[p]}")
    for proba in probas[p]:
        print(proba)
    print("")
 """       


#Perplejidad
def get_perplexity(corpus_eval : list, palabras_a_ind : dict) -> float:
    perplexity = 0
    indices_corpus = []
    for token in corpus_eval:
        if token in palabras_a_ind.keys():
            indices_corpus.append(palabras_a_ind[token])
        else:
            indices_corpus.append(palabras_a_ind["UNKNOW"])
    output = rnn(indices_corpus)
    probas = []
    for i in range(len(output)-1):
        probas.append(output[i][indices_corpus[i+1]].item())

    for p in probas:
        if(perplexity != 0):
            perplexity != 1/p
        else:
            perplexity = 1/p
    return perplexity ** (1/(len(corpus_eval)-2))

evaluacion = [BOS, "perro", "niño", "jaja", EOS]
perplejidad = get_perplexity(evaluacion, palabras_a_indices)
print(f"Perplejidad de la oración 'El niño salta': {perplejidad}")

def generate_words(palabras_a_ind: dict, longitud: int) -> str:
    oracion = ""
    ultima = "<BOS>"
    for i in range(longitud):
        result = get_proba([ultima], palabras_a_ind, get_valor)
        siguiente = "<UNK>"
        ind = random.randint(0, 10)
        while siguiente == "<UNK>": #Se vuelve a elegir si toca un UNK
            siguiente = result[0][ind][0]
            ind = random.randint(0, 10)
        if(siguiente == "<EOS>"):
            oracion += ". "
        elif(siguiente != "<BOS>"):
            oracion += f"{siguiente} "
        ultima = siguiente
    return oracion

last_ind = len(list(indices_a_palabras.keys()))
last_emb = torch.tensor(list(range(last_ind)))
print(rnn.emb(last_emb).detach().numpy())

#Obteniendo los embeddings
def plot_words(Z, ids): 
    r=0
    plt.scatter(Z[:,0],Z[:,1], marker='o', c='teal')
    for label,x,y in zip(ids, Z[:,0], Z[:,1]):
        plt.annotate(label, xy=(x,y), xytext=(-1,1), textcoords='offset points', ha='center', va='bottom')
        r+=1

plot_words(rnn.emb(last_emb).detach().numpy(), list(palabras_a_indices.keys()))
plt.title('Embeddings')
plt.show()