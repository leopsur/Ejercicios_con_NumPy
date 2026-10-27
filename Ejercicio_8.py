import numpy as np

matriz_o = np.array([[1, 4, 6, 5], [4, 1, 7, 3], [2, 9, 1, 2], [6, 3, 1, 1]])

#A todos los elementos de la matriz sumale un 10. Usando las funciones de numpy
res_numpy_1 = np.add(matriz_o, 10)

#A todos los elementos de la matriz sumale un 10 y divídelos entre 2. Usando las funciones de numpy
res_numpy_2 = np.divide(np.add(matriz_o, 10), 2)

#A todos los elementos de la matriz sumale un 10. Usando operadores
res_op_1 = matriz_o + 10

#A todos los elementos de la matriz sumale un 10 y divídelos entre 2. Usando operadores
res_op_2 = (matriz_o + 10) / 2

print("Se les suma 10 \n", res_numpy_1)
print("Se les suma 10 y divide entre 2 \n", res_numpy_2)
print("Se les suma 10 usando operadores \n", res_op_1)
print("Se les suma 10 y divide entre 2 usando operadores \n",res_op_2)

