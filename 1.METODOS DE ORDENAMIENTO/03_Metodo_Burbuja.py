# Este algoritmo ordena una lista comparando elementos
# adyacentes (vecinos) e intercambiándolos cuando están
# en el orden incorrecto.
#
# En cada recorrido, los valores más grandes se desplazan
# gradualmente hacia el final de la lista, de forma similar
# a cómo una burbuja asciende a la superficie del agua.
#
# Después de cada pasada, una parte de la lista queda
# ordenada, por lo que el algoritmo necesita revisar cada
# vez menos elementos.
#
# El proceso se repite hasta que todos los valores se
# encuentran en la posición que les corresponde.
#-----------------------------------------------------------

# Lista de números a ordenar
numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:")
print(numeros)

# Recorremos la lista varias veces
for i in range(len(numeros)):

    # Comparamos elementos vecinos
    for j in range(len(numeros) - 1 - i):

        # Si están en el orden incorrecto
        # los intercambiamos
        if numeros[j] > numeros[j + 1]:

            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Mostramos el resultado final
print("\nLista ordenada:")
print(numeros)