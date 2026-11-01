import numpy as np

A = np.array([[1, 2, 3],
              [4,5,6],
              [7, 8, 9]])

# 1 Multiplica cada elemento de la matriz por sí mismo
mult_elemento = A * A
print("Multiplicación elemento a elemento:\n", mult_elemento)

# 2 Multiplica la matriz por sí misma
mult_matricial = A @ A
print("\nMultiplicación matricial (A @ A):\n", mult_matricial)
