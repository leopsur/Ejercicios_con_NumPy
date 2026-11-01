import numpy as np

a = [2, 3, 5]
b = [2.4, 3.2, 5.6]
c = [2, 3, 5.6]

arr_a = np.array(a)
arr_b = np.array(b)
arr_c = np.array(c)

print("Tipo de a:", arr_a.dtype)  # int
print("Tipo de b:", arr_b.dtype)  # float
print("Tipo de c:", arr_c.dtype)  # float64 NumPy convierte todo a float para mantener homogeneidad
