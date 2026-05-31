# Este método pertenece a la familia de Merge Sort.

# La idea principal es combinar dos listas que ya están
# ordenadas para formar una sola lista también ordenada.
#
# Se comparan los primeros elementos de ambas listas y
# se agrega el menor al resultado.

# Después se continúa comparando los siguientes elementos
# hasta que una de las listas se quede sin datos.

# Finalmente se agregan los elementos restantes de la
# lista que aún contiene valores.

# Este procedimiento es la base del algoritmo Merge Sort.
#--------------------------------------------------------------


# Función para mezclar dos listas ordenadas
def straight_merge(lista1, lista2):

    resultado = []

    i = 0
    j = 0

    # Comparamos elementos de ambas listas
    while i < len(lista1) and j < len(lista2):

        # Agregamos el menor de los dos
        if lista1[i] < lista2[j]:

            resultado.append(lista1[i])
            i += 1

        else:

            resultado.append(lista2[j])
            j += 1

    # Agregamos los elementos restantes
    while i < len(lista1):

        resultado.append(lista1[i])
        i += 1

    while j < len(lista2):

        resultado.append(lista2[j])
        j += 1

    return resultado


# Dos listas previamente ordenadas
lista_a = [1, 4, 7, 9]
lista_b = [2, 3, 5, 8]

print("Lista A:")
print(lista_a)

print("\nLista B:")
print(lista_b)

# Realizamos la mezcla
resultado = straight_merge(lista_a, lista_b)

print("\nLista mezclada y ordenada:")
print(resultado)