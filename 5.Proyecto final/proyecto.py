# Importación de librerías necesarias
from sklearn.datasets import fetch_openml
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

# Descarga y carga el conjunto de datos MNIST
mnist = fetch_openml(
    'mnist_784',
    version=1,
    as_frame=False,
    parser='liac-arff'
)

# X contiene las imágenes y y las etiquetas reales
X = mnist.data
y = mnist.target.astype(int)

# Diccionario para almacenar un patrón representativode cada número (0 al 9)
patrones = {}

for numero in range(10):

    # Obtiene todas las imágenes del número actual
    imagenes_numero = X[y == numero]

    # Calcula la imagen promedio del número
    patrones[numero] = np.mean(
        imagenes_numero,
        axis=0
    ).reshape(28, 28)

# Selecciona una imagen aleatoria del dataset
indice_prueba = random.randint(0, len(X) - 1)

# Obtiene la imagen y su etiqueta real
imagen_prueba = X[indice_prueba].reshape(28, 28)
etiqueta_real = y[indice_prueba]

# Reconocimiento de patrones
# Variables para almacenar el mejor resultado
mejor_numero = None
menor_error = float('inf')

# Compara la imagen de prueba con cada patrón
for numero, patron in patrones.items():

    # Calcula el error promedio entre píxeles
    error = np.mean(
        np.abs(
            imagen_prueba.astype(float)
            - patron.astype(float)
        )
    )

    # Guarda el patrón con menor error
    if error < menor_error:
        menor_error = error
        mejor_numero = numero


# Mostrar resultados
print(f"\nNúmero real: {etiqueta_real}")
print(f"Número reconocido: {mejor_numero}")
print(f"Error promedio: {menor_error:.2f}")

# Convierte la matriz en una imagen
img = Image.fromarray(
    imagen_prueba.astype(np.uint8)
)

# Amplía la imagen para mejorar la visualización
img_grande = img.resize(
    (560, 560),
    Image.Resampling.LANCZOS
)

# Crea una figura para mostrar el resultado
plt.figure(figsize=(8, 8))

plt.imshow(
    img_grande,
    cmap='gray'
)

# Muestra el número real y el reconocido
plt.title(
    f"Real: {etiqueta_real}\nReconocido: {mejor_numero}",
    fontsize=16
)

# Oculta los ejes
plt.axis('off')

# Guarda la imagen en alta calidad
plt.savefig(
    "resultado.png",
    dpi=300,
    bbox_inches='tight'
)

plt.close()

print("\nImagen guardada como resultado.png")