# Quick Sort (Ordenamiento Rápido)
# Este algoritmo ordena una lista dividiéndola en grupos más pequeños.
#
# La idea principal es elegir un elemento llamado "pivote".
# Después, los valores menores que el pivote se colocan a la izquierda
# y los mayores a la derecha.
#
# El mismo proceso se repite para cada grupo hasta que todos
# los elementos quedan ordenados.
#
# Quick Sort es uno de los algoritmos de ordenamiento más utilizados
# debido a su buena eficiencia para listas grandes.


# Función Quick Sort
def quick_sort(lista):

    # Si la lista tiene 0 o 1 elemento,
    # ya está ordenada
    if len(lista) <= 1:
        return lista

    # Elegimos el último elemento como pivote
    pivote = lista[-1]

    menores = []
    mayores = []

    # Comparamos cada elemento con el pivote
    for elemento in lista[:-1]:

        # Los menores van a una lista
        if elemento < pivote:
            menores.append(elemento)

        # Los mayores o iguales van a otra
        else:
            mayores.append(elemento)

    # Ordenamos recursivamente ambos grupos
    return quick_sort(menores) + [pivote] + quick_sort(mayores)


# Lista de números a ordenar
numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:")
print(numeros)

# Ordenamos la lista
ordenados = quick_sort(numeros)

print("\nLista ordenada:")
print(ordenados)