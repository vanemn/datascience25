import pandas as pd

df_ventas = pd.read_csv('ventas_diarias.csv')
df_empleados = pd.read_csv('empleados_sucursal.csv')
df_productos = pd.read_csv('productos_categoria.csv')

#==========Vista previa==========
print("\n====== Vista original de  DataFrames ======\n")
print(df_ventas.head(9))   #puedo indicar el número de filas que quiero ver o dejar vacío 5
df_multi_index = df_ventas.set_index(['Sucursal', 'Fecha', 'Categoria'])
print("\n====== Vista de df set_index   ======\n")
print(df_multi_index.head(9))
# imprimir todas multi_index ventas del sur uso log
print("\n====== Vista de df ventas del Sur======\n")        
print(df_multi_index.loc['Sur'])
# imprimir todas multi_index ventas del sur y categoria electronica
print("\n====== Vista de df ventas del sur y categoria electronica ======\n")   
print(df_multi_index.loc[('Sur', slice(None), 'Electrónica')])
# imprimir todas multi_index ventas del sur y categoria electronica y fecha 2023-01-01
print("\n====== Vista de df ventas del sur y categoria electronica y fecha 2023-01-01 ======\n")   
print(df_multi_index.loc[('Sur', '2024-01-01', 'Electrónica')])
# print("\n====== Vista de df ventas del sur y fecha 2023-01-01 ======\n")
# print(df_multi_index.loc[('Sur', '2024-01-01')])

print("\n====== Vista completa de df_multi_index ======\n")
print(df_multi_index)
#==========Operaciones con DataFrames==========

#agrupar por sucursal y categoria
print
df_grouped = df_ventas.groupby(['Sucursal', 'Categoria'])['Ventas'].sum().reset_index()
print("\n====== Vista de df_grouped ======\n")
print(df_grouped)
#agrupar doblemente por sucursal, categoria  ventas y unidades y agregar promedio de ventas y unidades
df_grouped_double = df_ventas.groupby(['Sucursal', 'Categoria'])[['Ventas', 'Unidades']].agg({'Ventas': 'mean', 'Unidades': 'mean'}).reset_index()
print("\n====== Vista de df_grouped_double ======\n")   
print(df_grouped_double)

# # filtrar por ventas y electronica y hacer el resumen diario
# df_filtered = df_ventas[(df_ventas['Categoria'] == 'Electrónica') & (df_ventas['Ventas'] > 1000)]
# df_filtered_daily = df_filtered.groupby(['Fecha', 'Sucursal'])['Ventas'].sum().reset_index()
# print("\n====== Vista de df_filtered_daily ======\n")   
# print(df_filtered_daily)
#============