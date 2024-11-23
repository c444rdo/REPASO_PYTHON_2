print ("Martínez Estrada Ricardo / NO. de control: 1193 / 22-11-2024")
print (" ")

# Definir una función que calcule la longitud de una lista o cadena sin usar len().
def longitud(objeto):
    # Recorre el objeto y cuenta los elementos.
    contador = 0
    for _ in objeto:
        contador += 1
    return contador

# Ejemplo de uso
print(longitud([1, 2, 3, 4]))  # Salida: 4
print(longitud("cadena"))      # Salida: 6