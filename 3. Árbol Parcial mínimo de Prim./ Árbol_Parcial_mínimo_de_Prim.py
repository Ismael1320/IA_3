def prim(grafo, inicio):

    # Lista de nodos visitados
    visitados = [inicio]

    # Aristas del árbol mínimo
    arbol = []

    # Costo total
    costo = 0

    paso = 1

    # Se ejecuta hasta visitar todos los nodos
    while len(visitados) < len(grafo):

        menor = 999
        origen = ""
        destino = ""

        # Busca la arista de menor peso
        for nodo in visitados:
            for vecino in grafo[nodo]:

                if vecino not in visitados:

                    if grafo[nodo][vecino] < menor:
                        menor = grafo[nodo][vecino]
                        origen = nodo
                        destino = vecino

        # Agrega el nuevo nodo al árbol
        visitados.append(destino)
        arbol.append((origen, destino, menor))
        costo += menor

        # Muestra el avance
        print("\n-------------------------------------------------")
        print("PASO", paso)
        print("-------------------------------------------------")
        print("Arista agregada:", origen, "--", destino)
        print("Peso:", menor)
        print("Nodos visitados:", visitados)

        paso += 1

    # Resultado final
    print("\n-------------------------------------------------")
    print("ÁRBOL PARCIAL MÍNIMO")
    print("-------------------------------------------------")

    for origen, destino, peso in arbol:
        print(origen, "--", destino, "Peso:", peso)

    print("\nCosto total del árbol:", costo)


# Grafo de ejemplo
grafo = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3}
}

print("SIMULADOR DEL ALGORITMO DE PRIM")
print("-------------------------------------------------")

# Nodo inicial predeterminado
inicio = "A"

print("Nodo inicial:", inicio)

# Ejecuta el algoritmo
prim(grafo, inicio)