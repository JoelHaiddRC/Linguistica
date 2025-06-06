# Lingüistica Computacional
## Práctica 2: Modelos del lenguaje.
### Alumnos: Joel Haidd Reyes Cedillo \\ Semenov Flores Dimitri

En esta práctica se implementan un par de redes neuronales, una con el modelo de bigramas usando únicamente numpy, y otra con el modelo recurrente usando pytorch.
Se selecciona un corpus de al menos 1000 oraciones, se preprocesa, normaliza y se ejecuta el BPE para obtener los tókens de los cuáles se hará el entrenamiento.

IMPORTANTE:
Es necesario tener instalado python3 y un entorno con terminal donde poder ejecutar archivos ```ipynb```.

Además se deben instalar a traves de pip los siguientes paquetes:

```pip install pandas```
```pip install numpy```
```pip install torch```
```pip install matplotlib```
```pip install -U scikit-learn```
```pip install --user -U nltk```


Instrucciones:

- Dentro de la carpeta ```preprocesamiento``` se encuentra un notebook llamado ```Ejercicio1.ipynb``` donde viene el modelo de bigramas y otro notebook llamado  ```Ejercicio2.ipynb``` donde se implementa el modelo recurrente.

- Solamente se deben ejecutar los archivos ```Ejercicio1.ipynb``` y ```Ejercicio2.ipynb```, el resto de archivos son los diferentes módulos que usan los dos notebooks anteriores para poder funcionar.

- Además de lo anterior se incluye un par de archivos extra llamados ```redNeuronal.py``` y ```redRecurrente``` para probar el funcionamiento de los modelos con un corpus pequeño sin usar BPE ni preprocesamiento.
