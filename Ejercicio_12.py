import numpy as np

a = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
b = np.array([[2, 3], [5, 7], [11, 13], [17, 19], [23, 29], [31, 37]])
c = np.array([[[2, 3], [5, 7]], [[11, 13], [17, 19]], [[23, 29], [31, 37]]])

#Muestra con numpy el número de dimensiones de los siguientes arrays:
print("Dimensiones de a:", a.ndim)
print("Dimensiones de b:", b.ndim)
print("Dimensiones de c:", c.ndim)