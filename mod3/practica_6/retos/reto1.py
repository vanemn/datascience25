#importar librerias
import pandas as pd
import numpy as np

#Reto 1: Clasificación de Temperaturas DiariasArchivo:reto1_temperatura_ampliado.csvColumnas:•ID•Ciudad•Temperatura_Maxima•Humedad_RelativaObjetivos:
#Paso1: Carga los datos
df = pd.read_csv("reto1_temperatura_ampliado.csv")
#Paso 2: inspeccionar rapidamente
print(df.head())
print(df.info())
#Paso3 : Limpiar errores  intencionales(Correccion de texto a NaN)
# Detectar valores faltantes
print(df.isnull().sum())
#1.Detectar y rellenar valores nulos en Temperatura_Maximacon la media.
df["Temperatura_Maxima"] = pd.to_numeric(df["Temperatura_Maxima"], errors="coerce")
media_temp = df['Temperatura_Maxima'].mean()
df['Temperatura_Maxima'] = df['Temperatura_Maxima'].fillna(media_temp)
print("Media de Temperatura_Maxima:", media_temp)
# Detectar valores faltantes
print(df.isnull().sum())

#Paso4 : Eliminar duplicados
antes = len(df)
df= df.drop_duplicates()
despues = len(df)
eliminado = antes - despues
df.to_csv("salidas/temp_sin_duplicado.csv", index=False, na_rep="NaN")
print("Filas Antes:",antes)
print("Filas despues:", despues)
print("Filas eliminadas", eliminado)
#Paso5 : Rellenar valores nulos

#Paso6  Discretizar  en categoria
#2.Discretizar con pd.cut()en categorías:oFrío (≤15)oTemplado (15–25)oCaluroso (>25)Resultado: Categoria_Temp3.Analizar diferencias de temperatura por ciudad.
df["Categoria_Temp"] = pd.cut(df["Temperatura_Maxima"], 
                              bins=[-np.inf, 15, 25, np.inf],
                                labels=["Frío", "Templado", "Caluroso"])
print(df[["Ciudad", "Temperatura_Maxima", "Categoria_Temp"]].head())
df.to_csv("salidas/temp_categorizadas.csv",index=False)
#paso 7: Agregar descripcion (join externo)


#Paso 8 : Agrupaciones
#4.Investigar relación entre Temperatura_Maximay Humedad_Relativa

relacion = df.groupby("Ciudad")[["Temperatura_Maxima", "Humedad_Relativa"]].mean().reset_index()
print("Relación entre Temperatura_Maxima y Humedad_Relativa por Ciudad:")
print(relacion)