# Lingüistica Computacional
## Práctica 1: Modelos formales y pre-procesamiento.
### Alumnos: Joel Haidd Reyes Cedillo \\ Semenov Flores Dimitri

En esta práctica se implementa un transductor finito para realizar análisis morfológico de los verbos de primera clase, así como un el pre-procesamiento de un corpus y su graficación para obtener la curva de Zipf tanto con las palabras normalizadas como con las subwords usando BPE.

IMPORTANTE:
Es necesario tener instalado python3 y un entorno con terminal donde poder ejecutar archivos ```ipynb```.

Además se deben instalar a traves de pip los siguientes paquetes:

```pip install <nombre_paquete>```

Instrucciones:

- Dentro de la carpeta ```notebooks``` se encuentra un notebook llamado ```Ejercicio1.ipynb``` donde viene el transductor finito y en la carpeta src otro notebook llamado  ```Ejercicio2.ipynb``` donde se implementa el pre-procesamiento y graficación del corpus.

- Dentro de la carpeta ```data``` se encuentra un archivo de texto con palabras de ejemplo para el transductor del Ejercicio1, si se quiere probar otras palabras de ejemplo se puede modificar dicho archivo (es necesario que cada palabra se divida por espacios en blanco y no tener signos de puntuación para poder etiquetarla adecuadamente) 

- Solamente se deben ejecutar los archivos ```Ejercicio1.ipynb``` y ```Ejercicio2.ipynb```, el resto de archivos son los diferentes módulos que usan los dos notebooks anteriores para poder funcionar.
