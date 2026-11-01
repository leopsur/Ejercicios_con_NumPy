import numpy as np

def imprimir_datos(matriz):
    # Separamos X (características: todas las columnas menos la última)
    x = matriz[:, :-1]
    
    # Separamos Y (tipos de vino: la última columna)
    y = matriz[:, -1]
    
    # 1. Imprime cuantas muestra de vino tenemos
    num_muestras = matriz.shape[0]
    print(f"Muestras de vino que tenemos: {num_muestras}")
    
    # 2. Imprime cuantos tipos distintos de vino tenemos y cuales son
    tipos_distintos = np.unique(y)
    print(f"Cantidad de tipos distintos de vino: {len(tipos_distintos)}")
    print(f"Tipos de vino que son: {tipos_distintos}")
    
    # 3. Imprime cuantas características tenemos de cada tipo de vino
    num_caracteristicas = x.shape[1]
    print(f"Cantidad de características que tenemos de cada tipo de vino: {num_caracteristicas}")
    
    # 4. Imprime los valores máximos y mínimos de cada característica
    maximos = np.max(x, axis=0)
    minimos = np.min(x, axis=0)
    print("\nValores máximos y mínimos de cada característica:")
    for i in range(num_caracteristicas):
        print(f" Característica {i+1}: Mínimo = {minimos[i]}, Máximo = {maximos[i]}")
        
    # 5. Retorna una nueva matriz llamada x solo con las características y un nuevo array llamado y solo con los tipos de vino
    return x, y

# Carga con numpy el fichero wine.csv que contiene una matriz de números separados por coma
datos_vino = np.genfromtxt('wine.csv', delimiter=',')

# Llama a la función imprimir_datos con los datos de wine.csv
x, y = imprimir_datos(datos_vino)
