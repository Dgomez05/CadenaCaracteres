#5
def contar_palabras(text):
  palabras = text.split()
  return len(palabras)
text = "El nombre \"Python\" viene dado por la afición de Van Rossum al grupo Monty Python."
numero_palabras = contar_palabras(text)
print(f"Número de palabras en la frase: {numero_palabras}")