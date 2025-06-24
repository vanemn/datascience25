import pandas as pd
import numpy as np

# Cargar los archivos CSV o datos
df = pd.read_csv('ejemplo_datos_outliers.csv')

# inspeccionar los datos
print(df.head())
print(df.info())

# Limpiar errores intencionales (correccion de texto NaN a numérico)
df["Edad"] = pd.to_numeric(df["Edad"], errors='coerce')
df["Salario"] = pd.to_numeric(df["Salario"], errors='coerce')
df["Horas_Trabajo_Semanal"] = pd.to_numeric(df["Horas_Trabajo_Semanal"], errors='coerce')

# Pasarlo a otro csv
df.to_csv('salidas/ejemplo_datos_outliers_limpio.csv', index=False)