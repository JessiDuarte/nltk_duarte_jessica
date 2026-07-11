# 1. Mostrar el texto original
import os
os.system("cls")

from pathlib import Path

texto = Path("comentarios_youtube.txt").read_text(encoding="utf-8")

print("===== TEXTO ORIGINAL =====")
print(texto)

# 2. Separar el texto en oraciones

from nltk.tokenize import sent_tokenize

oraciones = sent_tokenize(texto, language="spanish")

print("\n===== ORACIONES ENCONTRADAS =====")

for i, oracion in enumerate(oraciones):
    print(f"Oración {i+1}: {oracion}")

print("\nCantidad de oraciones:")
print(len(oraciones))

# 3. Tokenizar el texto

from nltk.tokenize import word_tokenize

# Separar el texto en tokens (palabras y signos)
tokens = word_tokenize(texto, language="spanish")

# Mostrar la lista de tokens obtenidos
print("\n===== TOKENS =====")
print(tokens)

# Mostrar cantidad total de tokens
print("\nCantidad de tokens:")
print(len(tokens))

# 4. Normalizar palabras
# Convertir todos los tokens a letras minúsculas

tokens_minuscula = [token.lower() for token in tokens]

# Mostrar tokens normalizados
print("\n===== TOKENS NORMALIZADOS =====")
print(tokens_minuscula)


# 5. Eliminar signos de puntuación
# Conservamos únicamente las palabras formadas por letras

palabras = [
   token
   for token in tokens_minuscula
   if token.isalpha()
]

print("\nTexto sin puntuación:")
print(palabras)

print("\nCantidad de palabras:")
print(len(palabras))

# 6. Eliminar palabras vacías (stopwords)

from nltk.corpus import stopwords

# Obtener las stopwords del idioma español
stopwords_es = stopwords.words("spanish")

# Eliminar palabras vacías del texto
palabras_sin_stopwords = [
   palabra
   for palabra in palabras
   if palabra not in stopwords_es
]

print("\nPalabras sin stopwords:")
print(palabras_sin_stopwords)

print("\nCantidad de palabras luego de eliminar stopwords:")
print(len(palabras_sin_stopwords))

# 7. Aplicar Stemming
# Reducir las palabras a una raíz común utilizando SnowballStemmer

from nltk.stem import SnowballStemmer

# Crear el stemmer para idioma español
stemmer = SnowballStemmer("spanish")

# Aplicar stemming a las palabras sin stopwords
stems = [
   stemmer.stem(palabra)
   for palabra in palabras_sin_stopwords
]

print("\nPalabras originales y su stem:")

# Mostrar una tabla con las primeras 20 palabras
for i in range(20):
    print(f"{palabras_sin_stopwords[i]:15} -> {stems[i]}")


    # 8. Frecuencia de palabras
# Obtener las palabras que aparecen con mayor frecuencia en el texto

from nltk.probability import FreqDist

# Crear la distribución de frecuencia
frecuencia = FreqDist(palabras_sin_stopwords)

print("\n===== PALABRAS MÁS FRECUENTES =====")

# Mostrar las 20 palabras más frecuentes
for palabra, cantidad in frecuencia.most_common(20):
    print(f"{palabra}: {cantidad}")



    # 9. Estadísticas del análisis del texto

print("\n===== ESTADÍSTICAS =====")

# Cantidad de comentarios analizados
comentarios = texto.count("\n")

print("Cantidad de comentarios analizados:")
print(comentarios)

# Cantidad de oraciones
print("\nCantidad de oraciones:")
print(len(oraciones))

# Cantidad de tokens obtenidos
print("\nCantidad de tokens:")
print(len(tokens))

# Cantidad de palabras luego de eliminar puntuación
print("\nCantidad de palabras sin puntuación:")
print(len(palabras))

# Cantidad de palabras luego de eliminar stopwords
print("\nCantidad de palabras sin stopwords:")
print(len(palabras_sin_stopwords))

# Cantidad de palabras diferentes (vocabulario)
vocabulario = set(palabras_sin_stopwords)

print("\nCantidad de palabras diferentes:")
print(len(vocabulario))

# Cantidad de stems diferentes
stems_diferentes = set(stems)

print("\nCantidad de stems diferentes:")
print(len(stems_diferentes))

# 3. Conclusiones finales

print("=========================================")
print("CONCLUSIONES")
print("=========================================")

print("\nVideo analizado:")
print("Video sobre SQL y consultas INNER JOIN")

print("\nCantidad de comentarios:")
print("100")

print("\nLas palabras más frecuentes fueron:")

print("gracias")
print("muchas")
print("explicación")
print("videos")
print("bien")

print("\nEl stemming permitió agrupar palabras con distintas terminaciones bajo una misma raíz.")

print("\nLa temática predominante de los comentarios está relacionada con el aprendizaje de Bases de Datos y SQL, especialmente con el uso de consultas INNER JOIN.")