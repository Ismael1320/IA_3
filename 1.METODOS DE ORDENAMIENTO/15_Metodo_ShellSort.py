# Este algoritmo es una mejora del método de inserción.
#
# En lugar de comparar únicamente elementos cercanos,
# comienza comparando elementos que están separados
# por cierta distancia llamada "gap".
#
# A medida que el algoritmo avanza, la distancia se
# reduce hasta llegar a 1.
#
# Cuando el gap vale 1, el proceso se comporta como
# un Insertion Sort, pero con gran parte del trabajo
# ya realizado.
#
# Esto permite ordenar listas de manera más eficiente
# que el método de inserción tradicional.
#---------------------------------------------------------

# Función Shell Sort
def shell_sort(lista):

    n = len(lista)

    # Calculamos la distancia inicial
    gap = n // 2

    # Reducimos la distancia gradualmente
    while gap > 0:

        # Recorremos los elementos
        for i in range(gap, n):

            temporal = lista[i]

            j = i

            # Reordenamos los elementos separados por el gap
            while j >= gap and lista[j - gap] > temporal:

                lista[j] = lista[j - gap]

                j -= gap

            lista[j] = temporal

        # Reducimos la distancia
        gap //= 2


# Lista de números a ordenar
numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:")
print(numeros)

shell_sort(numeros)

print("\nLista ordenada:")
print(numeros)