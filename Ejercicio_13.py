import numpy as np

def mostrar_tamanyo(arr):
    for i, dim in enumerate(arr.shape):
        print(f"El nº de elementos de la dimension {i} es {dim}")

a = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
b = np.array([[2, 3], [5, 7], [11, 13], [17, 19], [23, 29], [31, 37]])
c = np.array([[[2, 3], [5, 7]], [[11, 13], [17, 19]], [[23, 29], [31, 37]]])

print("Tamaños de a")
mostrar_tamanyo(a)
print("\n Tamaños de b")
mostrar_tamanyo(b)
print("\n Tamaños de c")
mostrar_tamanyo(c)
