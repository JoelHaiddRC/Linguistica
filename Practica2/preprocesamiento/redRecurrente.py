import numpy as np
import math   
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
        #Capa de RNN (se toma bidireccional)
        self.recurrence = nn.RNN(dim, dim_h, bidirectional=True)
        #Salida
        self.ffw = nn.Sequential(nn.Linear(2*dim_h,dim_out), nn.Softmax(dim=2))
        
    def forward(self, x):
        #Se pasa a formato torch
        x = torch.tensor(x)
        #Embedding
        x = self.emb(x)
        #Ajustes de tamaño
        x = x.unsqueeze(1)
        #Estados de recurrencia
        h, c = self.recurrence(x)
        #Activación
        h = h.tanh()
        #Salida
        y_pred = self.ffw(h)
        #Se acomoda la salida para que la tome el loss
        y_pred = y_pred.transpose(1, 2)
        
        return y_pred
    
rnn = RecurrentNetwork(len(indices_a_palabras.keys()), len(indices_a_palabras.keys()))

#EJEMPLO
#Numero de iteraciones
epochs = 100
#La función de riesgo es la entropía cruzada
criterion = torch.nn.CrossEntropyLoss()
#Los parametros que se van a actualizar
optimizer = torch.optim.Adagrad(rnn.parameters(), lr=0.02)

#Se entrena el modelo
for epoch in range(epochs):
    for x_i, y_i in zip(x, y):
        #FORWARD
        y_pred = rnn(x_i)

        #BACKWARD
        #Resize de las variables esperadas (se agrega dimension de length_seq)
        y_i = (torch.tensor(y_i)).unsqueeze(1)
        #Se calcula el eror
        loss = criterion(y_pred, y_i)

        #zero grad
        optimizer.zero_grad()
        #Backprop
        loss.backward()
        #Se actualizan los parametros
        optimizer.step()

    print(f"Epoch={epoch}. Training loss={loss}")

output = rnn([5, 0, 1, 3])

print(output)

probas = []
"""
for i in range(len(indices_a_palabras.keys())):
    indices = list(indices_a_palabras.keys())
    palabra = indices_a_palabras[indices[i]]
    valor = output[i].item()
    #print(f"{palabra} = {valor}")
    probas.append((palabra, valor))

def get_proba(tupla):
    return tupla[1]

probas.sort(key=get_proba, reverse=True)
print(probas)
"""