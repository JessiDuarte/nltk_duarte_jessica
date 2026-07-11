# nltk_duarte_jessica
# Análisis de comentarios de YouTube utilizando NLTK

## Datos del estudiante

**Nombre y apellido:** Jessica Giselle Duarte
**Carrera:** Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial

## Objetivo del trabajo

El objetivo de este trabajo práctico es aplicar técnicas básicas de Procesamiento del Lenguaje Natural (PLN) utilizando la biblioteca NLTK de Python.

A partir de comentarios reales obtenidos desde un video de YouTube, se realizaron procesos de lectura de archivos, tokenización, normalización de texto, eliminación de signos de puntuación, eliminación de stopwords, stemming y análisis de frecuencia de palabras.

## Video analizado

URL del video:

https://www.youtube.com/watch?v=0BstRqp6Svg&t=6s

## Cantidad de comentarios descargados

Se descargaron y analizaron los primeros 100 comentarios del video seleccionado.

## Bibliotecas utilizadas

* **NLTK:** biblioteca utilizada para el procesamiento del lenguaje natural.
* **youtube-comment-downloader:** biblioteca utilizada para obtener los comentarios del video de YouTube.
* **Pathlib:** utilizada para la lectura del archivo de texto.

## Instrucciones para ejecutar el programa

1. Clonar o descargar el repositorio.

2. Crear un entorno virtual:

```bash
python -m venv venv
```

3. Activar el entorno virtual:

En Windows PowerShell:

```bash
.\venv\Scripts\activate
```

4. Instalar las dependencias necesarias:

```bash
pip install nltk
pip install youtube-comment-downloader
```

5. Descargar los recursos de NLTK:

```python
import nltk

nltk.download("punkt")
nltk.download("stopwords")
```

6. Ejecutar el programa de descarga de comentarios:

```bash
python descargar_comentarios.py
```

7. Ejecutar el análisis del texto:

```bash
python analizar_comentarios.py
```

El programa generará el análisis de los comentarios aplicando las técnicas de Procesamiento del Lenguaje Natural.
