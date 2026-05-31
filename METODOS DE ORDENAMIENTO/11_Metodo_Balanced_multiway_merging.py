# Este método combina varias listas ordenadas al mismo tiempo
# para obtener una sola lista ordenada.

# A diferencia de la mezcla simple, donde se unen dos listas,
# aquí pueden participar varias listas ordenadas.

# En cada paso se compara el primer elemento disponible
# de cada lista y se selecciona el menor.

# El proceso continúa hasta que todos los elementos
# han sido agregados a la lista final.

# Este método es muy utilizado en ordenamientos externos,
# especialmente cuando se trabaja con grandes volúmenes de datos.
#---------------------------------------------------------------------------

# Listas previamente ordenadas
lista1 = [1, 4, 7]
lista2 = [2, 5, 8]
lista3 = [3, 6, 9]

# Lista donde guardaremos el resultado
resultado = []

# Índices para recorrer cada lista
i = 0
j = 0
k = 0

# Continuamos mientras exista algún elemento por procesar
while i < len(lista1) or j < len(lista2) or k < len(lista3):

    candidatos = []

    # Agregamos el siguiente valor disponible de cada lista
    if i < len(lista1):
        candidatos.append((lista1[i], "A"))

    if j < len(lista2):
        candidatos.append((lista2[j], "B"))

    if k < len(lista3):
        candidatos.append((lista3[k], "C"))

    # Seleccionamos el menor elemento disponible
    menor, origen = min(candidatos)

    resultado.append(menor)

    # Avanzamos en la lista correspondiente
    if origen == "A":
        i += 1

    elif origen == "B":
        j += 1

    else:
        k += 1


print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)

print("\nResultado de la mezcla:")
print(resultado)