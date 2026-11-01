import numpy as np

np.random.seed(3)
ages = np.random.randint(18, 70, size=200)  # Edades de 200 personas
income = np.random.normal(50000, 15000, size=200)  # Ingresos anuales
education_years = np.random.randint(0, 20, size=200)  # Años de educación formal

# 1. Calcula la correlación entre los años de educación y los ingresos.
# np.corrcoef devuelve una matriz de correlación de 2x2
matriz_correlacion = np.corrcoef(education_years, income)
# El valor de correlación cruzada se encuentra en la posición [0, 1] o [1, 0]
correlacion = matriz_correlacion[0, 1]

print("1. CORRELACIÓN")
print(f"La correlación entre educación e ingresos es: {correlacion:.4f}")


# 2. Divide a las personas en grupos de edades (18-30, 31-45, 46-60, 61+) y calcula el ingreso promedio por grupo.
print("\n2. INGRESO PROMEDIO POR GRUPO DE EDAD")
grupos_edad = [
    ("18-30", (ages >= 18) & (ages <= 30)),
    ("31-45", (ages >= 31) & (ages <= 45)),
    ("46-60", (ages >= 46) & (ages <= 60)),
    ("61+", (ages >= 61))
]

for nombre, mascara in grupos_edad:
    ingresos_grupo = income[mascara]
    # Controlamos si un grupo se quedara vacío para evitar errores de división por cero
    promedio_grupo = np.mean(ingresos_grupo) if len(ingresos_grupo) > 0 else 0
    print(f" Grupo {nombre}: ${promedio_grupo:.2f} (Total personas: {len(ingresos_grupo)})")


# 3. Encontrar el percentil 90 de ingresos y contar cuántos ganan por encima
percentil_90 = np.percentile(income, 90)
personas_por_encima = np.sum(income > percentil_90)

print("\n3. PERCENTIL 90 DE INGRESOS")
print(f"El corte del percentil 90 se sitúa en: ${percentil_90:.2f}")
print(f"Número de personas con ingresos superiores al percentil 90: {personas_por_encima}")


# 4. Agrupa los datos en función del número de años de educación y calcula el promedio de ingresos para cada grupo.
print("\n4. PROMEDIO DE INGRESOS POR AÑOS DE EDUCACIÓN")
# Obtenemos un array ordenado con los años de educación únicos presentes en los datos
anios_unicos = np.unique(education_years)

for anio in sorted(anios_unicos):
    ingresos_anio = income[education_years == anio]
    promedio_anio = np.mean(ingresos_anio)
    print(f" Con {anio} años de educación: ${promedio_anio:.2f} (Total personas: {len(ingresos_anio)})")
