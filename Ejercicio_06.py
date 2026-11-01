import numpy as np

#7 filas y 8 columnas
matriz_2d = np.zeros((7, 8), dtype=int)

#Selecciona las celdas en rojo oscuro de la siguiente matriz:
#Las filas horizontales (2:5) y las columnas verticales (2:6)
matriz_2d[2:5, 2:6] = 1

print(matriz_2d)
