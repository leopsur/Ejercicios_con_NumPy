import numpy as np

np.random.seed(0)

# Ventas diarias simuladas con media 500 y desviación estándar 50
sales_data = np.random.normal(500, 50, 365)

# Ventas atípicas por promociones
sales_data[[50, 120, 180, 250, 300]] = [1500, 1400, 1600, 1700, 1800]  

# 1. Detecta y elimina los valores atípicos (aquellos que están fuera de 3 desviaciones estándar del promedio).
# Calculamos primero la media y la desviación estándar de los datos originales
promedio_original = np.mean(sales_data)
std_original = np.std(sales_data)

# Definimos los límites usando la regla de las 3 desviaciones estándar
limite_inferior = promedio_original - 3 * std_original
limite_superior = promedio_original + 3 * std_original

# Creamos una máscara booleana para quedarnos solo con los datos dentro del rango permitido
mascara_limpios = (sales_data >= limite_inferior) & (sales_data <= limite_superior)
datos_limpios = sales_data[mascara_limpios]

print("1. LIMPIEZA DE DATOS")
print(f"Límites calculados: Inferior = {limite_inferior:.2f} | Superior = {limite_superior:.2f}")
print(f"Valores eliminados por ser atípicos: {len(sales_data) - len(datos_limpios)}")
print(f"Cantidad de datos restantes: {len(datos_limpios)}")


# 2. Calcula el promedio, la mediana y la desviación estándar de las ventas después de limpiar los datos.
promedio_nuevo = np.mean(datos_limpios)
mediana_nueva = np.median(datos_limpios)
std_nuevo = np.std(datos_limpios)

print("\n 2. ESTADÍSTICAS TRAS LIMPIEZA")
print(f"Nuevo Promedio: {promedio_nuevo:.2f}")
print(f"Nueva Mediana: {mediana_nueva:.2f}")
print(f"Nueva Desviación Estándar: {std_nuevo:.2f}")


# 3. Genera una vista de las ventas de cada trimestre (3 primeros meses, 3 siguientes, etc.).
# Para mantener la relación temporal exacta del año, dividimos el array original (sales_data) en 4 bloques de 91 días y a cada bloque le aplicamos el filtro de limpieza correspondiente.
print("\n 3. VENTAS POR TRIMESTRE (DATOS LIMPIOS)")
trimestres_originales = np.array_split(sales_data, 4)

for i, trim_orig in enumerate(trimestres_originales):
    # Filtramos los atípicos dentro de este trimestre específico
    trim_limpio = trim_orig[(trim_orig >= limite_inferior) & (trim_orig <= limite_superior)]
    
    print(f"Trimestre {i+1}:")
    print(f" - Días analizados (sin atípicos): {len(trim_limpio)}")
    print(f" - Suma total de ventas: {np.sum(trim_limpio):.2f}")
    print(f" - Promedio diario: {np.mean(trim_limpio):.2f}")


# 4. Encuentra los 5 días con las ventas más bajas después de la limpieza de los datos.
# np.sort ordena los datos de menor a mayor. Tomamos las primeras 5 posiciones usando
ventas_mas_bajas = np.sort(datos_limpios)[:5]

print("\n--- 4. DÍAS CON MENOS VENTAS ---")
print("Los 5 valores de ventas más bajos registrados son:")
for idx, valor in enumerate(ventas_mas_bajas):
    print(f" Posición {idx+1}: {valor:.2f}")
