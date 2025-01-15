# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import zipfile
import os

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
        o "neutral". Este corresponde al nombre del directorio donde se
        encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```
"""
    # Ruta del archivo zip
    zip_file = "files/input.zip"
    # Ruta de destino donde se extraerán los archivos
    output_dir = "input"

    # Verificar si el archivo zip existe
    if not os.path.exists(zip_file):
        print(f"El archivo {zip_file} no existe.")
        return

    # Descomprimir el archivo
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
        print(f"El archivo {zip_file} ha sido descomprimido correctamente en {output_dir}")

# Llamar a la función para ejecutar la descompresión
pregunta_01()

import os
import pandas as pd

# Crear carpeta de salida dentro de 'files' si no existe
output_dir = os.path.join('files', 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Inicializar listas para frases y sentimientos para cada conjunto
phrases_test = []
targets_test = []
phrases_train = []
targets_train = []

# Ajustar las rutas base para `test` y `train`
test_dir = os.path.join('input', 'input', 'test')
train_dir = os.path.join('input', 'input', 'train')

# Definir los subdirectorios que contienen los archivos de texto
sentiment_dirs = ['positive', 'negative', 'neutral']

# Recorrer las carpetas de `test` y agregar los datos
for sentiment in sentiment_dirs:
    sentiment_path = os.path.join(test_dir, sentiment)
    
    if not os.path.exists(sentiment_path):
        print(f"El directorio {sentiment_path} no existe.")
        continue

    # Leer los archivos dentro de cada directorio
    for filename in os.listdir(sentiment_path):
        file_path = os.path.join(sentiment_path, filename)
        
        if os.path.isfile(file_path):
            # Leer el contenido del archivo de texto
            with open(file_path, 'r', encoding='utf-8') as file:
                phrase = file.read().strip()
                
            # Añadir la frase y su sentimiento a las listas
            phrases_test.append(phrase)
            targets_test.append(sentiment)

# Recorrer las carpetas de `train` y agregar los datos
for sentiment in sentiment_dirs:
    sentiment_path = os.path.join(train_dir, sentiment)
    
    if not os.path.exists(sentiment_path):
        print(f"El directorio {sentiment_path} no existe.")
        continue

    # Leer los archivos dentro de cada directorio
    for filename in os.listdir(sentiment_path):
        file_path = os.path.join(sentiment_path, filename)
        
        if os.path.isfile(file_path):
            # Leer el contenido del archivo de texto
            with open(file_path, 'r', encoding='utf-8') as file:
                phrase = file.read().strip()
                
            # Añadir la frase y su sentimiento a las listas
            phrases_train.append(phrase)
            targets_train.append(sentiment)

# Crear DataFrames para `test` y `train`
test_data = pd.DataFrame({'phrase': phrases_test, 'target': targets_test})
train_data = pd.DataFrame({'phrase': phrases_train, 'target': targets_train})

# Mezclar aleatoriamente los datos
test_data = test_data.sample(frac=1, random_state=42).reset_index(drop=True)
train_data = train_data.sample(frac=1, random_state=42).reset_index(drop=True)

# Guardar los DataFrames como archivos CSV en la carpeta 'files/output'
test_data.to_csv(os.path.join(output_dir, "test_dataset.csv"), index=False)
train_data.to_csv(os.path.join(output_dir, "train_dataset.csv"), index=False)

print("Archivos 'train_dataset.csv' y 'test_dataset.csv' generados correctamente en la carpeta 'files/output'.")
