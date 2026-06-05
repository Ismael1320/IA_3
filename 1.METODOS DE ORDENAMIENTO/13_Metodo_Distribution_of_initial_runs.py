# Este método se utiliza en los algoritmos de ordenamiento
# externo para preparar los datos antes de realizar las mezclas.

# La idea consiste en dividir una lista grande en varios grupos
# más pequeños llamados "corridas" (runs).

# Cada corrida se ordena individualmente y posteriormente
# se utiliza en los procesos de mezcla para obtener una
# lista completamente ordenada.

# En este ejemplo simularemos la creación de corridas
# iniciales a partir de una lista de números.
#-------------------------------------------------------------------

# Lista original
datos = [8, 3, 5, 1, 9, 2, 7, 4, 6]

print("Lista original:")
print(datos)

# Tamaño de cada corrida
tamano_corrida = 3

corridas = []

# Dividimos la lista en grupos pequeños
for i in range(0, len(datos), tamano_corrida):

    corrida = datos[i:i + tamano_corrida]

    # Ordenamos cada corrida
    corrida.sort()

    corridas.append(corrida)

# Mostramos las corridas generadas
print("\nCorridas iniciales:")

for indice, corrida in enumerate(corridas, start=1):

    print(f"Corrida {indice}: {corrida}")