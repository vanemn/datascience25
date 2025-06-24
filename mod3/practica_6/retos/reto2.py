# #importar librerias
import pandas as pd
import numpy as np

#Reto 2: Cuartiles de Calificaciones AcadémicasArchivo:reto2_calificaciones_ampliado.csvColumnas:•ID•Genero•Materia•CalificacionObjetivos:
df = pd.read_csv("reto2_calificaciones_ampliado.csv")
#Paso 2: inspeccionar rapidamente
print(df.head())
print(df.info())
#Paso3 : Limpiar errores  intencionales(Correccion de texto a NaN)
# Detectar valores faltantes
print(df.isnull().sum())
#1.Eliminar duplicados y detectar valores nulos en Calificacion.2.Imputar nulos con la media por materia.
#Paso1: Carga los datos
df["Calificacion"] = pd.to_numeric(df["Calificacion"], errors="coerce")
media_calificacion = df['Calificacion'].mean()  
df['Calificacion'] = df['Calificacion'].fillna(media_calificacion)
print("Media de Calificacion:", media_calificacion)
# Detectar valores faltantes
print(df.isnull().sum())

#Paso4 : Eliminar duplicados
antes = len(df)
df= df.drop_duplicates()
despues = len(df)
eliminado = antes - despues
df.to_csv("salidas/calif_sin_duplicado.csv", index=False, na_rep="NaN")
print("Filas Antes:",antes)
print("Filas despues:", despues)
print("Filas eliminadas", eliminado)
#Paso5 : Rellenar valores nulos

#Paso6  Discretizar  en categoria
#3.Aplicar pd.qcut()para categorizar en: Q1, Q2, Q3, Q4.Resultado: Nivel_Calificacion4.Analizar diferencias por género y materia.
df["Nivel_Calificacion"] = pd.qcut(df["Calificacion"], 
                                    q=4,
                                    labels=["Q1", "Q2", "Q3", "Q4"])
print(df[["Genero", "Materia", "Calificacion", "Nivel_Calificacion"]].head())
df.to_csv("salidas/calif_categorizadas.csv", index=False)
  
#paso 7: Agregar descripcion (join externo)


#Paso 8 : Agrupaciones


