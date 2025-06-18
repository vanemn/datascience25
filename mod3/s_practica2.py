import pandas as pd 

# # cargar el archivo excel
# df = pd.read_excel('entradas/reporte.xlsx', sheet_name='Ventas2023')
# print(df)

# # # cargar el archivo excel y eliminar filas con valores nulos
# df = pd.read_excel('entradas/ventas.xlsx', sheet_name='Sheet1', na_values=["N/A", "n/a", "NA", "na"])
# df = df.dropna()
# print(df)

# # Guardar el DataFrame en un archivo Excel
# df.to_excel('entradas/ventasmod.xlsx', index=False, sheet_name='ventasmod')

#crear una nueva hoja en un archivo excel existente
df = pd.read_excel('entradas/ventasmod.xlsx', sheet_name='sheet3')
print(df)

