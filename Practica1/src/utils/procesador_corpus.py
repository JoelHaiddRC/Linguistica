import nltk
import re
import string
from nltk.corpus import stopwords #Listas de stopwords
from nltk.corpus import cess_esp

nltk.download('stopwords')
nltk.download("cess_esp")
words = cess_esp.words()
print(len(words))
#Stopwords para español
stopwords_list = stopwords.words('spanish')

def preprocess_words(words: list) -> list:
    clean_words = []
    words_stopwords = []
    acentos = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'ü':'u'}
    palab =  re.compile(r'^[a-zA-Z0-9]')
    carac = re.compile(r'[^a-zA-Z0-9ñ]')
    for word in words:
      #Elimino puntuacion
      nopuntc = ""
      for ch in word:
        if ch not in string.punctuation:
          nopuntc += ch
      #Elimino acentos
      noaccents = ""
      for ch in word:
        if ch in acentos.keys():
          #Elimino caracteres que no sean letras o números
          noaccents += re.sub(carac, " ", acentos[ch])
        else:
          #Elimino caracteres que no sean letras o números
          noaccents += re.sub(carac, " ", ch)
          

      #Elimino palabras que no comiencen con alguna letra o número
      if(re.findall(palab, word)):
        words_stopwords.append(noaccents)

     #Elimino stopwords
    for stopw in words_stopwords:
      if stopw not in stopwords_list:
        clean_words.append(stopw)
    return set(clean_words)

clean_words = preprocess_words(set(words))
print(len(clean_words))