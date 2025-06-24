# #importar librerias
import pandas as pd
import numpy as np

#Reto 3: Segmentación por Años de ExperienciaArchivo:reto3_experiencia_ampliado.csvColumnas:•ID•Edad•Experiencia•Area Objetivos:
#Paso1: Carga los datos
df = pd.read_csv("reto3_experiencia_ampliado.csv")
#Paso 2: inspeccionar rapidamente
print(df.head())
print(df.info())
#Paso3 : Limpiar errores  intencionales(Correccion de texto a NaN)
# Detectar valores faltantes
print(df.isnull().sum())
#1.Detectar nulos en Experiencia y rellenar con la mediana por Area.
df["Experiencia"] = pd.to_numeric(df["Experiencia"], errors="coerce")
mediana_experiencia = df['Experiencia'].median()
df['Experiencia'] = df['Experiencia'].fillna(mediana_experiencia)
print("Mediana de Experiencia:", mediana_experiencia)
# Detectar valores faltantes
print(df.isnull().sum())

# 2.Detectar y tratar outliers.
# Calcular cuartil (q) de la columna "Experiencia"
q1 = df["Experiencia"].quantile(0.25)
q2 = df["Experiencia"].quantile(0.50)
q3 = df["Experiencia"].quantile(0.75)   

# Calcular el rango intercuartílico (IQR) y los límites para detectar outliers
IQR = q3 - q1
limite_inferior = q1 - 1.5 * IQR
limite_superior = q3 + 1.5 * IQR
# Detectar outliers
# Los outliers son los valores que están por debajo del límite inferior o por encima del límite
outliers = df[(df["Experiencia"] < limite_inferior) | (df["Experiencia"] > limite_superior)]
valores_normales = df[(df["Experiencia"] >= limite_inferior) & (df["Experiencia"] <= limite_superior)]  
print("Primer cuartil (Q1):", q1)
print("Segundo cuartil (Q2):", q2)          
print("Tercer cuartil (Q3):", q3)
print("Rango intercuartílico (IQR):", IQR)
print("\nOutliers detectados:")
print(outliers[["ID", "Experiencia"]])

#Paso4 : Eliminar duplicados
antes = len(df)
df= df.drop_duplicates()
despues = len(df)
eliminado = antes - despues
df.to_csv("salidas/exp_sin_duplicados.csv", index=False, na_rep="NaN")
print("Filas Antes:",antes)
print("Filas despues:", despues)
print("Filas eliminadas", eliminado)
#Paso5 : Rellenar valores nulos

#Paso6  Discretizar  en categoria
#3.Clasificar con pd.cut()en:oPrincipiante (0–2)oIntermedio (3–5)oAvanzado (6–10)oExperto (>10)Resultado: Grupo_Experiencia4.Analizar relación entre Edady Experiencia
df["Grupo_Experiencia"] = pd.cut(df["Experiencia"], 
                                  bins=[-np.inf, 2, 5, 10, np.inf], 
                                    labels=["Principiante", "Intermedio", "Avanzado", "Experto"])
print(df[["ID", "Edad", "Experiencia", "Grupo_Experiencia"]].head())
df.to_csv("salidas/exp_categorizadas.csv", index=False) 
 
#paso 7: Agregar descripcion (join externo)


#Paso 8 : Agrupaciones


