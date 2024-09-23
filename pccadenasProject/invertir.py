#7
def invertirPalabras(frase):
  palabras = frase.split()
  palabras.reverse()
  return " ".join(palabras)
sentence = "La historia del lenguaje de programación Python"
sentenceInvertida = invertirPalabras(sentence)
print(sentenceInvertida)