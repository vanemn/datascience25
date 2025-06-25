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

# suma, media, maximo y minimo de ventas por sucursal
df_summary = df_ventas.groupby('Sucursal')['Ventas'].agg(['sum', 'mean', 'max', 'min']).reset_index()
print("\n====== Vista de df_summary ======\n")  
print(df_summary)
# pivotear dataframe 
df_pivot = df_ventas.pivot_table(index='Fecha', columns='Sucursal', values='Ventas', aggfunc='sum').fillna(0)
print("\n====== Vista de df_pivot ======\n")    
print(df_pivot)

# despivotear el dataframe
df_despivot = df_pivot.reset_index().melt(id_vars='Fecha', var_name='Sucursal', value_name='Ventas')
print("\n====== Vista de df_despivot ======\n") 
print(df_despivot)
#pivotear categoria 
#aggfunc='sum' para sumar las ventas por categoria y fecha
#fillna(0) para rellenar los valores nulos con 0
df_pivot_categoria = df_ventas.pivot_table(index='Fecha', columns='Categoria', values='Ventas', aggfunc='sum').fillna(0)
print("\n====== Vista de df_pivot_categoria ======\n")
print(df_pivot_categoria)

# despivotear el dataframe
df_despivot = df_pivot_categoria.reset_index().melt(id_vars='Fecha', var_name='Categoria', value_name='Ventas')
print("\n====== Vista de df_despivot ======\n")
print(df_despivot.head(9))

#copiar DataFrame
df_copy_extra = df_ventas.copy()
df_copy_extra['Fecha'] = pd.to_datetime(df_copy_extra['Fecha'])+ pd.Timedelta(days=10)
# Convertir la columna Fecha a tipo datetime
df_copy_extra['Fecha'] = df_copy_extra['Fecha'].dt.strftime("%Y-%m-%d")  # Convertir la columna Fecha a tipo datetime
print("\n====== Vista de df_copy_extra ======\n")
print(df_copy_extra.head(9))
# Concatenar DataFrames e imprimir y guardar archivo
df_concat = pd.concat([df_ventas, df_copy_extra], ignore_index=True) # o axis=0 para concatenar por filas
print("\n====== Vista de df_concat ======\n")
print(df_concat.head(9))
# Guardar el DataFrame concatenado en un nuevo archivo CSV
df_concat.to_csv('ventas_diarias_concatenadas.csv', index=False)
# Convertir la columna Fecha a tipo datetime
# df_copy_extra['Fecha'] = pd.to_datetime(df_copy_extra['Fecha'])  #

# df_copy_extra['Fecha'] =df_copy_extra['Fecha'].dt.strftime("%Y-%m-%d")  # Convertir la columna Fecha a tipo datetime


# combinaciones de DataFrames usando merge (join) left, right, inner y outer
# inner join entre df_ventas y df_productos por Categoria
df_inner_join = pd.merge(df_ventas, df_productos, on='Categoria', how='inner')
print("\n====== Vista de df_inner_join ======\n")
print(df_inner_join.head(9))
# crea archivo csv de df_inner_join
df_inner_join.to_csv('ventas_productos_inner_join.csv', index=False)

# left join entre df_ventas y df_productos por Categoria
df_left_join = pd.merge(df_ventas, df_productos, on='Categoria', how='left')
print("\n====== Vista de df_left_join ======\n")
print(df_left_join.head(9))
# crea archivo csv de df_left_join
df_left_join.to_csv('ventas_productos_left_join.csv', index=False)

# right join entre df_ventas y df_productos por Categoria
df_right_join = pd.merge(df_ventas, df_productos, on='Categoria', how='right')
print("\n====== Vista de df_right_join ======\n")
print(df_right_join.head(9))
# crea archivo csv de df_right_join
df_right_join.to_csv('ventas_productos_right_join.csv', index=False)

# right join entre df_ventas y df_productos por Categoria
df_outer_join = pd.merge(df_ventas, df_productos, on='Categoria', how='outer')
print("\n====== Vista de df_outer_join ======\n")
print(df_outer_join.head(9))
# crea archivo csv de df_outer_join
df_outer_join.to_csv('ventas_productos_outer_join.csv', index=False)




