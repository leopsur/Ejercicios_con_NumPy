import numpy as np
from sklearn.datasets import load_iris

datos = load_iris().data
resultado = load_iris().target

#Crea un array llamado sepal_length con las 99 primeras filas y la 1º columna de la matriz datos
sepal_length = datos[:99, 0]

#Crea un array llamado petal_length con las 99 primeras filas y la 3º columna de la matriz datos
petal_length = datos[:99, 2]

#Crea un array llamado x juntando las 2 columnas sepal_length y petal_length
x = np.column_stack((sepal_length, petal_length))

#Crea un array llamado y con las 99 primeras filas del vector resultado
y = resultado[:99]

#Crea un array llamado x con las 99 primeras filas , la 1º columna y la 3º columna de la matriz datos
x_directo = datos[:99, [0, 2]]

print(sepal_length[:5])
print(petal_length[:5])
print(x[:5])
print(y[:5])
print(x_directo[:5])
print(f"\n¿x y x_directo son idénticos?: {np.array_equal(x, x_directo)}")