import numpy as np

# Creación del array
numeros = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

# 1. Último elemento sin conocer la longitud
print(numeros[-1])

# 2. Tercer elemento
print(numeros[2]) 

# 3. Último y tercer elemento
print(numeros[[-1, 2]])

# 4. Del 2º al 5º elemento 
print(numeros[1:5])

# 5. El 2º y el 5º elemento
print(numeros[[1, 4]])

# 6. Último y penúltimo elemento sin conocer su longitud
print(numeros[[-1, -2]]) 
