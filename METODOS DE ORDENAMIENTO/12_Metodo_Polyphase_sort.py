# Este método es una variante de los algoritmos de mezcla.

# Su principal objetivo es reducir la cantidad de operaciones
# necesarias durante el proceso de ordenamiento cuando se trabaja
# con grandes cantidades de datos.

# La idea consiste en distribuir los datos en varios grupos
# ordenados y después combinarlos de forma gradual hasta obtener
# una única secuencia ordenada.

# En aplicaciones reales suele utilizarse en archivos muy grandes
# que no caben completamente en memoria.

# En este ejemplo simularemos el proceso mezclando grupos ya
# ordenados para obtener una lista final ordenada.
#--------------------------------------------------------------------

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


# Grupos previamente ordenados
grupo1 = [2, 5, 8]
grupo2 = [1, 4, 7]
grupo3 = [3, 6, 9]

print("Grupo 1:", grupo1)
print("Grupo 2:", grupo2)
print("Grupo 3:", grupo3)

# Primera fase de mezcla
mezcla1 = mezclar(grupo1, grupo2)

# Segunda fase de mezcla
resultado_final = mezclar(mezcla1, grupo3)

print("\nLista ordenada:")
print(resultado_final)