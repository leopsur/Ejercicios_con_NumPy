import numpy as np

# Transforma el siguiente array en 8 bits sin signo y muestra cuánto ocupa en memoria
a = np.array([1, -2, 3]).astype(np.uint8)
print(f"a cambiado a uint8: {a}, Memoria ocupada: {a.nbytes} bytes") 

# Transforma el siguiente array en 8 bits sin signo y muestra cuánto ocupa en memoria
b1 = np.array([1, 254, 255]).astype(np.uint8)
print(f"b1 cambiado a uint8: {b1}, Memoria ocupada: {b1.nbytes} bytes")

# Transforma el siguiente array en 8 bits con signo y muestra cuánto ocupa en memoria
b2 = np.array([1, 127, 128]).astype(np.int8)
print(f"b2 cambiado a int8: {b2}, Memoria ocupada: {b2.nbytes} bytes") 

#Transforma el siguiente array en 8 bits con signo y muestra cuánto ocupa en memoria
b3 = np.array([1, -128, -129]).astype(np.int8)
print(f"b3 cambiado a int8: {b3}, Memoria ocupada: {b3.nbytes} bytes") 

# Transforma el siguiente array en float32 y muestra cuánto ocupa en memoria
b4 = np.array([1, 2, 3]).astype(np.float32)
print(f"b4 cambiado a float32: {b4}, Memoria ocupada: {b4.nbytes} bytes")

# Transforma el siguiente array en int32 y muestra cuánto ocupa en memoria
b5 = np.array([1.9, 2.01, 3.51]).astype(np.int32)
print(f"b5 cambiado a int32 (trunca decimales): {b5}, Memoria ocupada: {b5.nbytes} bytes")
