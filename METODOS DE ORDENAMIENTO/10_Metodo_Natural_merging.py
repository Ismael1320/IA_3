# Este método aprovecha las secuencias que ya están ordenadas
# dentro de una lista para realizar el proceso de ordenamiento.

# En lugar de dividir la lista en partes del mismo tamaño,
# busca grupos consecutivos que ya se encuentran ordenados.

# Después combina esas secuencias para formar grupos cada vez
# más grandes hasta obtener una lista completamente ordenada.

# Este enfoque puede ser más eficiente cuando la lista ya
# contiene partes parcialmente ordenadas.
#------------------------------------------------------------------

# Función para mezclar dos listas ordenadas
def mezclar(lista1, lista2):

    resultado = []

    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):

        if lista1[i] <= lista2[j]:

            resultado.append(lista1[i])
            i += 1

        else:

            resultado.append(lista2[j])
            j += 1

    # Agregamos los elementos restantes
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])

    return resultado


# Lista con secuencias parcialmente ordenadas
datos = [1, 3, 5, 2, 4, 6]

print("Lista original:")
print(datos)

# Detectamos dos secuencias naturales
secuencia1 = [1, 3, 5]
secuencia2 = [2, 4, 6]

print("\nSecuencia 1:")
print(secuencia1)

print("\nSecuencia 2:")
print(secuencia2)

# Mezclamos ambas secuencias
resultado = mezclar(secuencia1, secuencia2)

print("\nLista ordenada:")
print(resultado)