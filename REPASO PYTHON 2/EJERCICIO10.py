print ("Martínez Estrada Ricardo / NO. de control: 1193 / 22-11-2024")
print (" ")

# Definir un procedimiento histograma() que imprima un histograma.
def histograma(lista):
    # Recorre la lista e imprime un número de asteriscos igual al valor de cada elemento.
    for valor in lista:
        print('*' * valor)

# Ejemplo de uso
histograma([4, 9, 7])
# Salida:
# ****
# *********
# *******