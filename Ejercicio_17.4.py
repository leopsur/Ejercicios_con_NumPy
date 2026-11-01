import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure(figsize=(8,8))
axes = figure.add_subplot()

# Modifica el código que genera la variable x para que sean 40 valores entre el [-3,3]
x = np.linspace(-3, 3, 40)

y = 3*(1 - x)**2 * np.exp(-x**2 ) - 10*(x/5 - x**3 )*np.exp(-x**2 ) - 1./3*np.exp(-(x + 1)**2 )
axes.plot(x, y)
axes.set_title("x con 40 valores entre [-3, 3]")
plt.show()
