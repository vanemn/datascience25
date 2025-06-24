import pandas as pd
df = pd.read_csv('ejemplo_datos_outliers.csv')
#pasar datos a tipo numérico coerce errores de conversión pone el NA,raice no deja pasar texto a numérico
df["Salario"] = pd.to_numeric(df["Salario"], errors='coerce')
# Calcular el primer cuartil (q) de la columna "Salario"
q1 = df["Salario"].quantile(0.25)
q2 = df["Salario"].quantile(0.50)
q3 = df["Salario"].quantile(0.75)   

# Calcular el rango intercuartílico (IQR) y los límites para detectar outliers
IQR = q3 - q1
limite_inferior = q1 - 1.5 * IQR
limite_superior = q3 + 1.5 * IQR
# Detectar outliers
# Los outliers son los valores que están por debajo del límite inferior o por encima del límite
outliers = df[(df["Salario"] < limite_inferior) | (df["Salario"] > limite_superior)]
valores_normales = df[(df["Salario"] >= limite_inferior) & (df["Salario"] <= limite_superior)]

print("Primer cuartil (Q1):", q1)
print("Segundo cuartil (Q2):", q2)
print("Tercer cuartil (Q3):", q3)
print("Rango intercuartílico (IQR):", IQR)
print("\nOutliers detectados:")
print(outliers[["ID", "Salario"]])