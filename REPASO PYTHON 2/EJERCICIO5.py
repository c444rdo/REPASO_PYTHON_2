print ("Martínez Estrada Ricardo / NO. de control: 1193 / 22-11-2024")
print (" ")

# Escribir una función sum() que sume todos los números de una lista.
def sum(lista):
    # Suma todos los números de la lista utilizando un bucle.
    resultado = 0
    for num in lista:
        resultado += num
    return resultado

# Escribir una función multip() que multiplique todos los números de una lista.
def multip(lista):
    # Multiplica todos los números de la lista utilizando un bucle.
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

# Ejemplo de uso
print(sum([1, 2, 3, 4]))     # Salida: 10
print(multip([1, 2, 3, 4]))  # Salida: 24