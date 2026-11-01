import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure(figsize=(8,8))
axes = figure.add_subplot()

# Se modifica x para que sea un array de NumPy explícitamente float
x = np.array([-3, -2, -1, 0, 1, 2, 3], dtype=float)

y = 3*(1 - x)**2 * np.exp(-x**2 ) - 10*(x/5 - x**3 )*np.exp(-x**2 ) - 1./3*np.exp(-(x + 1)**2 )
axes.plot(x, y, marker='o')
axes.set_title("x como array de NumPy y tipo float (7 valores originales)")
plt.show()
