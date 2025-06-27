# Reto 3: Análisis de Datos de Viajes en Taxi 

#  Archivo: taxi_trips.csv 
from pydoc import describe
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# cargar el dataset
df = pd.read_csv('taxi_trips.csv')

# Columnas clave: distancia, duración, costo, hora_inicio, barrio 
# Pasos a seguir: 
# 1. Inspección inicial 
print(df.head(10))
print(describe(df))  # Estadísticas descriptivas
print("Dimensiones originales del archivo:", df.shape)
# Verifica si hora_inicio está en formato de fecha. 
print(df.info())

df['hora_inicio'] = pd.to_datetime(df['hora_inicio'])
print(df.info())
print(df.head(3))
# Asegúrate de que distancia, duración y costo sean numéricos.
print("\n Tipos de datos:")
print(df.dtypes)

# Observa estadísticas básicas para cada variable. 
print("\n Estadísticas básicas:")
print(df.describe())

# 2. Limpieza de datos 
# Elimina registros donde la distancia sea cero o negativa. 
registros_invalidos = df[df['distancia'] <= 0]
print("Registros con distancia cero o negativa:")
print(registros_invalidos)
print(f"Total: {len(registros_invalidos)} registros")

df = df[df['distancia'] > 0]
print((df['distancia'] <= 0).sum())

# Rellena valores faltantes en costo con el promedio del barrio. 
# Verificar valores faltantes y tipos de datos
print("Valores nulos o faltantes : \n", df.isnull().sum())
df['costo'] = df.groupby('barrio')['costo'].transform(lambda x: x.fillna(x.mean()))
print("Valores nulos o faltantes aplicado groupby : \n", df.isnull().sum())
# 3. Análisis univariado 
# Usa sns.histplot() para la distribución de distancia. 

sns.histplot(df['distancia'], kde=True)
plt.title("Distribución de la distancia")
plt.xlabel("Distancia (km)")
plt.ylabel("Frecuencia")
plt.show()

# Usa sns.boxplot() para encontrar viajes extremadamente largos. 
sns.boxplot(x=df['distancia'])
plt.title("Boxplot de la distancia")
plt.xlabel("Distancia (km)")
plt.show()

# 4. Detección de outliers 
#  Aplica IQR a distancia y costo. 
# OUTLIERS EN DISTANCIA


q1_dist = df["distancia"].quantile(0.25)
q2_dist = df["distancia"].quantile(0.50)
q3_dist = df["distancia"].quantile(0.75)

IQR_dist = q3_dist - q1_dist
limite_inferior_dist = q1_dist - 1.5 * IQR_dist
limite_superior_dist = q3_dist + 1.5 * IQR_dist

outliers_distancia = df[(df["distancia"] < limite_inferior_dist) | (df["distancia"] > limite_superior_dist)]
valores_normales_distancia = df[(df["distancia"] >= limite_inferior_dist) & (df["distancia"] <= limite_superior_dist)]

print(" DISTANCIA")
print("Q1:", q1_dist)
print("Q2 (mediana):", q2_dist)
print("Q3:", q3_dist)
print("IQR:", IQR_dist)
print("Límite inferior:", limite_inferior_dist)
print("Límite superior:", limite_superior_dist)
print("\nOutliers en distancia:")
print(outliers_distancia[["distancia"]])


# OUTLIERS EN COSTO

q1_costo = df["costo"].quantile(0.25)
q2_costo = df["costo"].quantile(0.50)
q3_costo = df["costo"].quantile(0.75)

IQR_costo = q3_costo - q1_costo
limite_inferior_costo = q1_costo - 1.5 * IQR_costo
limite_superior_costo = q3_costo + 1.5 * IQR_costo

outliers_costo = df[(df["costo"] < limite_inferior_costo) | (df["costo"] > limite_superior_costo)]
valores_normales_costo = df[(df["costo"] >= limite_inferior_costo) & (df["costo"] <= limite_superior_costo)]

print(" COSTO")
print("Q1:", q1_costo)
print("Q2 (mediana):", q2_costo)
print("Q3:", q3_costo)
print("IQR:", IQR_costo)
print("Límite inferior:", limite_inferior_costo)
print("Límite superior:", limite_superior_costo)
print("\nOutliers en costo:")
print(outliers_costo[["costo"]])
# Evalúa si son errores de captura o situaciones reales. 

print("\n Outliers en distancia:")
print(outliers_distancia[["distancia", "duracion", "costo", "hora_inicio", "barrio"]])



# 5. Análisis bivariado 
# Crea un sns.scatterplot(x='distancia', y='costo', hue='barrio') para observar si existe 
# Análisis bivariado: relación entre distancia y costo
sns.scatterplot(data=df, x='distancia', y='costo', hue='barrio')
plt.title("Relación entre distancia y costo por barrio")
plt.xlabel("Distancia (km)")
plt.ylabel("Costo ($)")
plt.legend(title="Barrio")
plt.show()
# proporcionalidad o outliers por zona. 
sns.lmplot(data=df, x='distancia', y='costo', hue='barrio', ci=None, aspect=1.5)
plt.title("Relación distancia vs costo por barrio (con tendencia)")
plt.xlabel("Distancia (km)")
plt.ylabel("Costo ($)")
plt.show()