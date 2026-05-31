# Este algoritmo ordena una lista comparando cada elemento
# con todos los elementos que se encuentran después de él.

# Cuando encuentra un valor menor que el actual, ambos
# elementos intercambian sus posiciones.

# A medida que avanzan las comparaciones, los valores más
# pequeños se van colocando al inicio de la lista y los
# más grandes quedan al final.

# El proceso continúa hasta que todos los elementos han
# sido comparados y ordenados correctamente.
#-------------------------------------------------------------

# Lista de números a ordenar
numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:")
print(numeros)

# Recorremos la lista
for i in range(len(numeros) - 1):

    # Comparamos el elemento actual con los que están a su derecha
    for j in range(i + 1, len(numeros)):

        # Si encontramos un número menor,
        # intercambiamos posiciones
        if numeros[i] > numeros[j]:

            numeros[i], numeros[j] = numeros[j], numeros[i]

# Mostramos la lista ordenada
print("\nLista ordenada:")
print(numeros)