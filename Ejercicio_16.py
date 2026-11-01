import numpy as np

# Datos de ejemplo simulados
X = np.array([[5.1, 3.5], 
              [4.9, 3.0], 
              [4.7, 3.2]])
y = np.array([0, 1, 0])

# Opción recomendada: np.column_stack añade el vector y como la última columna de X
nueva_matriz = np.column_stack((X, y))

print("Nueva Matriz unida:\n", nueva_matriz)
