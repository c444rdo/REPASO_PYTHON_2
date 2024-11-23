print("Martínez Estrada Ricardo / NO. de control: 1193 / 22-11-2024")
print(" ")

# Definir una función es_palindromo() que reconozca palíndromos.
def es_palindromo(cadena):
    """
    Verifica si una cadena es un palíndromo.
    Normaliza la cadena quitando espacios y haciendo todo minúsculas.
    """
    # Normaliza la cadena quitando espacios y poniendo todo en minúsculas.
    cadena = cadena.replace(" ", "").lower()
    # Compara la cadena con su inversa calculada directamente.
    return cadena == cadena[::-1]

# Ejemplo de uso
print(es_palindromo("radar"))  # Salida: True
print(es_palindromo("hola"))   # Salida: False