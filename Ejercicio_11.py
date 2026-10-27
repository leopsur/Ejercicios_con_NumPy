import numpy as np

def f (vector):
    condiciones = [
        (vector <= 3),
        (vector > 3) & (vector <= 5),
        (vector > 5) & (vector <= 6),
        (vector > 6) & (vector <= 7),
        (vector > 7) & (vector <= 9),
        (vector > 9)
    ]
    valores = [0, 4, 5, 6, 8, 10]
    return np.select(condiciones, valores)

#Crea ahora el vector de numpy [1,5,4,7,3,9,8,6]
vec = np.array([1, 5, 4, 7, 3, 9, 8, 6])

#Aplicamos la funcion f
resultado_tramos = f(vec)

print("Resultado de aplicar la función por tramos:\n", resultado_tramos)
