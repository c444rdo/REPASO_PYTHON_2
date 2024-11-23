print ("Martínez Estrada Ricardo / NO. de control: 1193 / 22-11-2024")
print (" ")

# Escribir una función que tome un carácter y devuelva True si es una vocal.
def es_vocal(caracter):
    # Verifica si el carácter está en la lista de vocales.
    return caracter.lower() in 'aeiou'

# Ejemplo de uso
print(es_vocal('a'))  # Salida: True
print(es_vocal('b'))  # Salida: False