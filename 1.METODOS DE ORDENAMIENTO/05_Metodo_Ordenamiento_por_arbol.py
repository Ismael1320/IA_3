# Este método utiliza una estructura de árbol binario
# para organizar los elementos antes de mostrarlos ordenados.
#
# Cada número se inserta en el árbol siguiendo una regla:
# - Los valores menores van a la izquierda.
# - Los valores mayores van a la derecha.
#
# Una vez construido el árbol, se recorre en orden
# (izquierda, raíz, derecha) para obtener los elementos
# de menor a mayor.
#
# Este algoritmo es útil porque aprovecha la estructura
# del árbol para mantener organizados los datos.
#-----------------------------------------------------------

# Clase para representar un nodo del árbol
class Nodo:

    def __init__(self, valor):

        self.valor = valor
        self.izquierda = None
        self.derecha = None


# Función para insertar un valor en el árbol
def insertar(raiz, valor):

    # Si el árbol está vacío, creamos el primer nodo
    if raiz is None:
        return Nodo(valor)

    # Los valores menores van a la izquierda
    if valor < raiz.valor:
        raiz.izquierda = insertar(raiz.izquierda, valor)

    # Los valores mayores o iguales van a la derecha
    else:
        raiz.derecha = insertar(raiz.derecha, valor)

    return raiz


# Recorremos el árbol en orden para obtener los números ordenados
def recorrido_en_orden(raiz, resultado):

    if raiz:

        recorrido_en_orden(raiz.izquierda, resultado)

        resultado.append(raiz.valor)

        recorrido_en_orden(raiz.derecha, resultado)


# Lista de números a ordenar
numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:")
print(numeros)

# Construimos el árbol
raiz = None

for numero in numeros:
    raiz = insertar(raiz, numero)

# Obtenemos los elementos ordenados
ordenados = []

recorrido_en_orden(raiz, ordenados)

print("\nLista ordenada:")
print(ordenados)