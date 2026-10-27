import numpy as np

matriz = np.array([[1, 4, 6, 5],
                   [4, 1, 7, 3],
                   [2, 9, 1, 2],
                   [6, 3, 1, 1]])

# Elemento fila 2 y col 3 = valor 7
print(matriz[1, 2])

# Tercera fila
print(matriz[2, :])

# Segunda columna
print(matriz[:, 1])

# Segunda y tercera columna
print(matriz[:, 1:3])

# Segunda y tercera fila
print(matriz[1:3, :])

# Última columna dinámicamente
print(matriz[:, -1])

# Segunda y cuarta columna de la primera y tercera fila
print(matriz[[0, 2]][:, [1, 3]])

# De la segunda a la tercera columna y de la primera a la tercera fila
print(matriz[0:3, 1:3])

# Todas las columnas excepto la primera y la última
print(matriz[:, 1:-1])

# Todas las filas excepto la primera y la última
print(matriz[1:-1, :])

# Matriz interior (sin bordes externos)
print(matriz[1:-1, 1:-1])

# Imprime la matriz y haz que las cabeceras de cada columna sean A, B , C y D
print(f"{'A':>4} {'B':>4} {'C':>4} {'D':>4}")
for fila in matriz:
    print(f"{fila[0]:4d} {fila[1]:4d} {fila[2]:4d} {fila[3]:4d}")
