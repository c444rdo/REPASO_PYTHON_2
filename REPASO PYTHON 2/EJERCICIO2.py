print ("Martínez Estrada Ricardo / NO. de control: 1193 / 22-11-2024")
print (" ")

# Definir una función max_de_tres() que tome tres números y devuelva el mayor de ellos.
def max_de_tres(num1, num2, num3):
    # Utiliza la función max() definida anteriormente para encontrar el mayor de los tres.
    return max(max(num1, num2), num3)

# Ejemplo de uso
print(max_de_tres(3, 7, 5))  # Salida: 7