print ("Martínez Estrada Ricardo / NO. de control: 1193 / 22-11-2024")
print (" ")

# Definir una función superposicion() que compare dos listas.
def superposicion(lista1, lista2):
    # Verifica si hay al menos un elemento en común utilizando bucles anidados.
    for elem1 in lista1:
        for elem2 in lista2:
            if elem1 == elem2:
                return True
    return False

# Ejemplo de uso
print(superposicion([1, 2, 3], [3, 4, 5]))  # Salida: True
print(superposicion([1, 2], [3, 4]))        # Salida: False