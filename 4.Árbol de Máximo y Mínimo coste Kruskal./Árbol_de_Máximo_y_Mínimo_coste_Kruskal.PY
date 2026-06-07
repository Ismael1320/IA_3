# Busca el representante de un conjunto
def encontrar(padre, nodo):

    while padre[nodo] != nodo:
        nodo = padre[nodo]

    return nodo


# Ejecuta el algoritmo de Kruskal
def kruskal(vertices, aristas, minimo=True):

    # Crea una copia para no modificar la lista original
    lista_aristas = aristas.copy()

    # Ordena las aristas según la opción elegida
    if minimo:
        lista_aristas.sort(key=lambda x: x[2])
    else:
        lista_aristas.sort(key=lambda x: x[2], reverse=True)

    # Inicializa cada nodo como su propio padre
    padre = {}

    for v in vertices:
        padre[v] = v

    # Guarda las aristas seleccionadas
    arbol = []

    # Acumula el costo total
    costo = 0

    paso = 1

    # Recorre todas las aristas
    for origen, destino, peso in lista_aristas:

        raiz1 = encontrar(padre, origen)
        raiz2 = encontrar(padre, destino)

        # Muestra el proceso paso a paso
        print("\n-------------------------------------------------")
        print("PASO", paso)
        print("-------------------------------------------------")
        print("Evaluando:", origen, "→", destino)
        print("Peso:", peso)

        # Agrega la arista si no forma un ciclo
        if raiz1 != raiz2:

            padre[raiz2] = raiz1
            arbol.append((origen, destino, peso))
            costo += peso

            print("Resultado: Arista agregada")

        else:
            print("Resultado: Se descarta (forma ciclo)")

        paso += 1

    # Muestra el resultado final
    print("\n-------------------------------------------------")

    if minimo:
        print("Árbol de Mínimo Coste:")
    else:
        print("Árbol de Máximo Coste:")

    for origen, destino, peso in arbol:
        print(origen, "→", destino, "  Peso:", peso)

    print()

    if minimo:
        print("Costo total mínimo:", costo)
    else:
        print("Costo total máximo:", costo)


# Nodos del grafo
vertices = ["A", "B", "C", "D", "E", "F"]

# Aristas del grafo (Origen, Destino, Peso)
aristas = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("C", "E", 10),
    ("D", "E", 2),
    ("D", "F", 6),
    ("E", "F", 3)
]

print("SIMULADOR DEL ALGORITMO DE KRUSKAL\n")

print("1. Árbol de Mínimo Coste")
print("2. Árbol de Máximo Coste")

# Solicita la opción al usuario
opcion = input("\nSeleccione una opción (1 o 2): ")

# Ejecuta el algoritmo según la opción elegida
if opcion == "2":
    kruskal(vertices, aristas, minimo=False)
else:
    kruskal(vertices, aristas)