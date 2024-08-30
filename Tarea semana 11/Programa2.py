#crear una matriz bidimensional 3x3
matriz = [
    [30, 6, 15],
    [12, 9, 3],
    [18, 24, 21]
]

# Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort_fila(fila):
    s = len(fila)
    for i in range(s - 1):
        for j in range(s - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for Fila in matriz:
        print(Fila)

# Mostrar la matriz original
print("Matriz Original:")
mostrar_matriz(matriz)

# Ordenar cada fila de la matriz utilizando Bubble Sort
for fila in matriz:
    bubble_sort_fila(fila)

# Mostrar la matriz ordenada
print("\nMatriz Ordenada por Filas:")
mostrar_matriz(matriz)