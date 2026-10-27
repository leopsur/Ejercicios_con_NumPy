import numpy as np

temps = np.array([10.2, 10.7, 13.3, 15.8, 19.3, 23.6, 26, 25.9, 22.8, 19.1, 13.9, 10.8])

# Temperaturas mayores que 20
print(temps[temps > 20])

# Temperaturas menores que 11
print(temps[temps < 11])

# Temperaturas mayores que 20 o menor que 11
print(temps[(temps > 20) | (temps < 11)])
