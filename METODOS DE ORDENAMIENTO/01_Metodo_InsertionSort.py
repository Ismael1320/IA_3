# Este algoritmo organiza los elementos de una lista de forma
# gradual, construyendo una sección ordenada desde el inicio.

# En cada iteración toma un elemento de la parte no ordenada
# y lo compara con los elementos anteriores para encontrar
# la posición que le corresponde.

# Si encuentra valores mayores, estos se desplazan una posición
# hacia la derecha para hacer espacio al elemento actual.

# De esta manera, después de cada recorrido, la parte izquierda
# de la lista permanece ordenada y va creciendo hasta incluir
# todos los elementos.

# El proceso termina cuando cada elemento ha sido insertado
# en su posición correcta dentro de la lista.
#---------------------------------------------------------------------------


# Lista de números a ordenar
numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:")
print(numeros)

# Recorremos la lista desde el segundo elemento
for i in range(1, len(numeros)):

    # Guardamos el valor actual
    actual = numeros[i]

    # Posición del elemento anterior
    j = i - 1

    # Mientras haya elementos mayores que el actual,
    # los movemos una posición a la derecha
    while j >= 0 and numeros[j] > actual:

        numeros[j + 1] = numeros[j]
        j -= 1

    # Colocamos el valor en su posición correcta
    numeros[j + 1] = actual

# Mostramos el resultado final
print("\nLista ordenada:")
print(numeros)