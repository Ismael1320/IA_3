# Este algoritmo ordena números procesando sus dígitos
# de derecha a izquierda.

# En lugar de comparar números completos, Radix Sort
# agrupa los elementos según el valor de cada dígito.

# Primero ordena por las unidades, luego por las decenas,
# después por las centenas y así sucesivamente.

# Al finalizar el recorrido de todos los dígitos,
# los números quedan completamente ordenados.

# Este método es especialmente útil cuando se trabaja
# con grandes cantidades de números enteros.
#----------------------------------------------------------

# Función que ordena según un dígito específico
def counting_sort(lista, posicion):

    tamaño = len(lista)

    salida = [0] * tamaño

    conteo = [0] * 10

    # Contamos cuántas veces aparece cada dígito
    for numero in lista:

        indice = (numero // posicion) % 10

        conteo[indice] += 1

    # Convertimos los conteos en posiciones
    for i in range(1, 10):

        conteo[i] += conteo[i - 1]

    # Construimos la lista ordenada
    for i in range(tamaño - 1, -1, -1):

        indice = (lista[i] // posicion) % 10

        salida[conteo[indice] - 1] = lista[i]

        conteo[indice] -= 1

    # Copiamos los resultados
    for i in range(tamaño):

        lista[i] = salida[i]


# Función principal de Radix Sort
def radix_sort(lista):

    # Buscamos el número más grande
    mayor = max(lista)

    posicion = 1

    # Procesamos unidades, decenas, centenas, etc.
    while mayor // posicion > 0:

        counting_sort(lista, posicion)

        posicion *= 10


# Lista de números a ordenar
numeros = [170, 45, 75, 90, 802, 24, 2, 66]

print("Lista original:")
print(numeros)

# Ordenamos la lista
radix_sort(numeros)

print("\nLista ordenada:")
print(numeros)