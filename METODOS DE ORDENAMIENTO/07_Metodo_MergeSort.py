# Este algoritmo ordena una lista dividiéndola en partes más pequeñas.

# Primero divide la lista en dos mitades hasta que cada
# sublista tenga un solo elemento.

# Después comienza a unir las sublistas comparando sus valores
# para colocarlos en el orden correcto.

# El proceso de dividir y mezclar se repite hasta obtener
# una única lista completamente ordenada.

# Merge Sort es muy eficiente para trabajar con grandes
# cantidades de datos y garantiza un buen rendimiento.
#------------------------------------------------------------------

# Función principal de Merge Sort
def merge_sort(lista):

    # Si la lista tiene un solo elemento,
    # ya está ordenada
    if len(lista) <= 1:
        return lista

    # Calculamos el punto medio
    medio = len(lista) // 2

    # Dividimos la lista en dos partes
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # Ordenamos ambas mitades
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    # Mezclamos las dos mitades ordenadas
    return mezclar(izquierda, derecha)


# Función para unir dos listas ordenadas
def mezclar(izquierda, derecha):

    resultado = []

    i = 0
    j = 0

    # Comparamos elementos de ambas listas
    while i < len(izquierda) and j < len(derecha):

        if izquierda[i] < derecha[j]:

            resultado.append(izquierda[i])
            i += 1

        else:

            resultado.append(derecha[j])
            j += 1

    # Agregamos los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


# Lista de números a ordenar
numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:")
print(numeros)

# Ordenamos la lista
ordenados = merge_sort(numeros)

print("\nLista ordenada:")
print(ordenados)