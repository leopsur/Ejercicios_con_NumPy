import numpy as np

#Cubo de 7 filas, 8 columnas y 3 de profundidad
cubo_3d = np.zeros((7, 8, 3), dtype=int)

#Selecciona las celdas en rojo oscuro de la siguiente matriz
celdas_rojo_frente = cubo_3d[2:5, 2:6, 0]

#Ahora selecciona las celdas en rojo oscuro pero también las verdes y azules que hay por detrás de las rojo oscuro
bloque_profundo = cubo_3d[2:5, 2:6, :]

print("Forma del bloque extraído en profundidad:", bloque_profundo.shape)

