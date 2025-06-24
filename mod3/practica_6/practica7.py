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

# Pasarlo a otro csv,INDEX=False no carga indices, y colocar el nan es con 
df.to_csv('salidas/ejemplo_datos_outliers_limpio.csv', index=False, na_rep='NaN')
print(df.info())
#Sacar cuartiles y detectar outliers

# revisar filas eliminadas
antes = len(df)
#df_sin_duplicados = df.drop_duplicates()
df_sin_duplicados = df.drop_duplicates().copy()

despues = len(df_sin_duplicados)
eliminados = antes - despues
df_sin_duplicados.to_csv('salidas/ejemplo_datos_outliers_limpio_sin_duplicados.csv', index=False, na_rep='NaN')
print(df_sin_duplicados.info())
# Revisar el número de filas eliminadas
print(f"Filas eliminadas: {eliminados}")
print(" Filas antes de eliminar duplicados:", antes)
print(" Filas después de eliminar duplicados:", despues)


# Rellenar valores nulos  de cada columna

df_sin_duplicados["Edad"] = df_sin_duplicados["Edad"].fillna(df_sin_duplicados["Edad"].median())
df_sin_duplicados["Salario"] = df_sin_duplicados["Salario"].fillna(df_sin_duplicados["Salario"].mean())
df_sin_duplicados["Horas_Trabajo_Semanal"] = df_sin_duplicados["Horas_Trabajo_Semanal"].fillna(df_sin_duplicados["Horas_Trabajo_Semanal"].mean())



# df rellenado
df_sin_duplicados.to_csv('salidas/ejemplo_datos_rellenado.csv', index=False)


# Discrettizar la columna " Horas_Trabajo_Semanal" en categorías

df_sin_duplicados["Horas_Categoria"] = pd.cut(
    df_sin_duplicados["Horas_Trabajo_Semanal"],bins= [0, 30, 40, 50,np.inf],labels=["Baja", "Media", "Alta", "Extremo"])

# Guardar el DataFrame con la nueva columna
df_sin_duplicados.to_csv('salidas/ejemplo_datos_categorias.csv', index=False)

# Agregar discrecion del nivel edicativo (join externo)
niveles = pd.read_csv("nivel_educativo_referencia.csv")
df = df_sin_duplicados.merge(niveles, left_on="Nivel_Educativo", right_on="Codigo", how="left")

df.to_csv("salidas/datos_con_nivel_educativo.csv")
#Paso 8 : Agrupacion por departamento y horas de trabajo"
df["Horas_Categoria"] = pd.cut(
    df["Horas_Trabajo_Semanal"],
    bins=[0, 30, 40, 50, np.inf],
    labels=["Baja", "Media", "Alta", "Extremo"]
)
print("Resumen")
print(df)

