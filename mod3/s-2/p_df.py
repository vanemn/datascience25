import pandas as pd
# dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
# temperaturas = [20, 22, 19, 21, 23]

# df = pd.DataFrame({
#     "Día": dias,
#     "Temperatura": temperaturas
# })
# print("\nDataFrame de días y temperaturas:\n", df)

# # Añadir una columna booleana que indique si la temperatura es mayor a 20
# df["Mayor_a_20"] = df["Temperatura"] > 20
# print("\nDataFrame con columna adicional 'Mayor_a_20':\n", df)

# data ={
#     "Nombre": ["Juan", "Ana", "Pedro", "María", "Luis"],
#     "Calificaciones": [4,3,5,7,6],
#     "Asignatura": ["Matemáticas", "Ciencias", "Historia", "Lengua", "Inglés"]
# }
# df = pd.DataFrame(data)
# print("\nDataFrame de estudiantes:\n", df)

# # Accediendo desde listas
# products = ["Camiseta", "Pantalón", "Zapatos"]
# prices = [20.5, 35.0, 50.0]
# df_products = pd.DataFrame({
#     "Producto": products,
#     "Precio": prices
# })
# print("\nDataFrame de productos:\n", df_products)
# # Accediendo desde multiples columnas
data2 = {
    "Nombre": ["Juan", "Ana", "Pedro", "María", "Luis"],
    "Salario": [3000, 3200, 2800, 3500, 4000],
    "Departamento": ["Ventas", "Marketing", "IT", "Recursos Humanos", "Finanzas"]
}
df_employees = pd.DataFrame(data2)
print("\nDataFrame de empleados:\n", df_employees)
# Acceso a columnas
print("\nAcceso a la columna 'Nombre':\n", df_employees["Nombre"])
# # Acceso a múltiples columnas
print("\nAcceso a las columnas 'Nombre' y 'Salario':\n", df_employees[["Nombre", "Salario"]])
# # Acceso a filas por índice
print("\nAcceso a la fila con índice 2:\n", df_employees.iloc[2])  # Acceso a la fila con índice 2
##Acceso Salario por beetween entre 300 y 4000
print("\nAcceso a las filas con salario entre 3000 y 4000:\n", df_employees[(df_employees["Salario"] >= 3000) & (df_employees["Salario"] <= 4000)])
print(df_employees[df_employees["Salario"].between(3000, 4000)])  # Acceso a las filas con salario entre 3000 y 4000
print(df_employees.head(3))  # Muestra las primeras 3 filas del DataFrame
print(df_employees.tail(2))  # Muestra las últimas 2 filas del DataFrame
print(df_employees.shape)  # Muestra la forma del DataFrame (número de filas y columnas)
print(df_employees.describe())  # Muestra estadísticas descriptivas del DataFrame
print(df_employees.info())  # Muestra información general del DataFrame
print(df_employees)
print("\nAcceso a las filas entre los índices 1 y 3:\n", df_employees.iloc[1:4])  # Acceso a las filas entre los índices 1 y 3
