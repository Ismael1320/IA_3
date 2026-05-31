# Este algoritmo utiliza una estructura llamada montículo (heap)
# para organizar los elementos antes de ordenarlos.
#
# La idea principal es colocar el valor más grande en la raíz
# del montículo y moverlo al final de la lista.
#
# Después se reconstruye el montículo con los elementos
# restantes y el proceso se repite.
#
# De esta manera, los elementos más grandes van ocupando
# sus posiciones finales hasta completar el ordenamiento.
#-----------------------------------------------------------------

# Función para mantener la propiedad del montículo
def heapify(lista, n, i):

    mayor = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    # Revisamos el hijo izquierdo
    if izquierda < n and lista[izquierda] > lista[mayor]:
        mayor = izquierda

    # Revisamos el hijo derecho
    if derecha < n and lista[derecha] > lista[mayor]:
        mayor = derecha

    # Si encontramos un valor mayor, intercambiamos
    if mayor != i:

        lista[i], lista[mayor] = lista[mayor], lista[i]

        heapify(lista, n, mayor)


# Función principal de Heap Sort
def heap_sort(lista):

    n = len(lista)

    # Construimos el montículo
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Extraemos elementos uno por uno
    for i in range(n - 1, 0, -1):

        lista[0], lista[i] = lista[i], lista[0]

        heapify(lista, i, 0)


# Lista de números a ordenar
numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:")
print(numeros)

heap_sort(numeros)

print("\nLista ordenada:")
print(numeros)