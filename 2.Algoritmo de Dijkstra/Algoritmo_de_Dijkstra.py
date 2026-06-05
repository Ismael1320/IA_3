import math

# Implementación del algoritmo de Dijkstra
def dijkstra(grafo, inicio, destino):

    # Diccionarios para guardar las distancias y el nodo anterior de cada vértice
    distancias = {}
    anteriores = {}
    visitados = []

    # Inicializa todas las distancias en infinito
    for nodo in grafo:
        distancias[nodo] = math.inf
        anteriores[nodo] = None

    # El nodo inicial tiene distancia 0
    distancias[inicio] = 0

    paso = 1

    # Repite hasta recorrer todos los nodos
    while len(visitados) < len(grafo):

        actual = None
        menor = math.inf

        # Busca el nodo no visitado con la distancia más pequeña
        for nodo in grafo:
            if nodo not in visitados:
                if distancias[nodo] < menor:
                    menor = distancias[nodo]
                    actual = nodo

        # Si no existe un nodo válido, termina
        if actual is None:
            break

        print("\n------------------------")
        print("PASO", paso)
        print("Nodo actual:", actual)
        print("--------------------------")

        # Agrega el nodo a la lista de visitados
        visitados.append(actual)

        # Recorre todos sus vecinos
        for vecino in grafo[actual]:

            peso = grafo[actual][vecino]
            nueva = distancias[actual] + peso

            print(actual, "->", vecino, "Peso:", peso)

            # Actualiza la distancia si encuentra un camino más corto
            if nueva < distancias[vecino]:
                print(
                    "Actualiza:",
                    distancias[vecino],
                    "->",
                    nueva
                )

                distancias[vecino] = nueva
                anteriores[vecino] = actual
            else:
                print("No mejora.")

        # Muestra el estado actual de las distancias
        print("\nTabla de distancias")
        for n in distancias:
            print(n, "=", distancias[n])

        paso += 1

    # Reconstruye el camino mínimo
    camino = []
    nodo = destino

    while nodo is not None:
        camino.insert(0, nodo)
        nodo = anteriores[nodo]

    # Imprime el resultado final
    print("\nRESULTADO")
    print("Camino mínimo:")
    print(" -> ".join(camino))
    print("Costo total:", distancias[destino])


# Grafo de ejemplo
grafo = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3}
}

# Solicita el nodo de inicio y destino
inicio = input("Nodo inicial: ").upper()
destino = input("Nodo destino: ").upper()

# Ejecuta el algoritmo
dijkstra(grafo, inicio, destino)