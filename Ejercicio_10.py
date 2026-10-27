import numpy as np

#Crea una función llamada f que acepte como parámetro el número y que retorne el valor multiplicado por 2 y además que se le sume 1
def f(numero):
    return (numero * 2) + 1

#Crea ahora el vector de numpy [1,5,4,7,3,9,8,6]
vec = np.array([1, 5, 4, 7, 3, 9, 8, 6])

#Aplicamos la función al vector
resultado_f = f(vec)
print("Resultado de aplicar f al vector:\n", resultado_f)
