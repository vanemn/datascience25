from pydoc import describe
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# cargar el dataset
df = pd.read_csv('empleados_150.csv')
# mostrar las primeras filas del dataset
print(df.head(10))
print(describe(df))  # Estadísticas descriptivas
# mostrar información general del dataset
print(df.info())
print("Dimensiones originales del archivo:", df.shape)

# Verificar valores faltantes y tipos de datos
print("Valores nulos:\n", df.isnull().sum())
# Verificar filas duplicadas
print("Filas duplicadas:", df.duplicated().sum())
# Verificar tipos de datos
print("Tipos de datos:\n", df.dtypes)
# Eliminar duplicados
duplicados = df.duplicated().sum()
df = df.drop_duplicates()
print(f"Duplicados encontrados y eliminados: {duplicados}")
# detectar valores nulos en una columna ejemplo "Edad"
df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")
media_edad = df['Edad'].median() # Calcular la mediana de la columna Edad
df['Edad'] = df['Edad'].fillna(media_edad) # Reemplazar valores nulos con la mediana
print(f"Valores nulos en la columna 'Edad' reemplazados por la mediana: {media_edad}")

# calcular la media, mediana y desviación estándar de la columna 'Salario'
print("Media de la columna 'Salario':", df['Salario'].mean())
print("Mediana de la columna 'Salario':", df['Salario'].median())
print("Desviación estándar de la columna 'Salario':", df['Salario'].std())

#Visualización de datos
# Histograma de la columna 'Edad'
plt.figure(figsize=(10, 6))
sns.histplot(df['Edad'], bins=20, kde=True)
plt.title('Histograma de Edad')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de dispersión  'Salario'
histograma_salario = sns.histplot(df['Salario'], bins=20, kde=True)
plt.title('Histograma de Salario')
plt.xlabel('Salario')
plt.ylabel('Frecuencia')
plt.show()

# Gráfico de dispersión entre 'Edad' y 'Salario'

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Edad', y='Salario', data=df)
plt.title('Dispersión entre Edad y Salario')
plt.xlabel('Edad')
plt.ylabel('Salario')
plt.show()

# 
sns.pairplot(df [['Edad', 'Salario']])
plt.title('Pairplot de Edad y Salario')
plt.show()

# mapa de calor de la relacion entre variable   

