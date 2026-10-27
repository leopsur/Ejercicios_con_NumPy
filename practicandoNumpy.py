import numpy as np

""" # Un array de una dimensión (Vector)
vector = np.array([1, 2, 3, 4, 5])

# Un array de dos dimensiones (Matriz de 2 filas y 3 columnas)
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Truco: Crear arrays automáticos
ceros = np.zeros((3, 3))       # Crea una matriz de 3x3 llena de ceros (0)
rango = np.arange(0, 10, 2)    # Crea números del 0 al 9, yendo de 2 en 2 -> [0, 2, 4, 6, 8]

 """

""" ejercicio1 = np.arange(5,16
                       )

print(ejercicio1) """

""" precios = np.array([10,20,30])

precios_con_iva = precios * 1.21

print(precios_con_iva)

precios2 = np.array([2,1,3])

total = precios*precios2

print(total) """


""" temperatura = np.array ([20,25,30,22,28])

farenge = temperatura*1.8 + 32

print(farenge) """


""" mi_matriz = np.array ([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(mi_matriz[2:,:]) """


edades = np.array ([15,25,12,18,40,30])

mayores = edades >= 18

print(mayores)

