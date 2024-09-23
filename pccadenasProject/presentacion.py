#1
name = "Dangie"
age = 39
favoriteFood = "Sandwich"
presentacion = f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi comida favorita es el {favoriteFood}"
print(presentacion)

#2
fullName = input("Ingrese su nombre completo: ")
nombresinEspacios = fullName.replace(" ", "")
cantidadLetras = len(nombresinEspacios)
print(f"Hola, {fullName}! Tu nombre tiene {cantidadLetras} letras, excluyendo los espacios.")