#6
def reemplazarLetra(cadena, letraOriginal, letraNueva):
  return cadena.replace(letraOriginal, letraNueva)
word = "Camila"
newWord = reemplazarLetra(word, "a", "e")
print(newWord)