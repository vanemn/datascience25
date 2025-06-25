import pandas as pd

df_ventas = pd.read_csv('ventas_diarias.csv')
df_empleados = pd.read_csv('empleados_sucursal.csv')
df_productos = pd.read_csv('productos_categoria.csv')

#==========Vista previa==========
print("\n====== Vista original de  DataFrames ======\n")
print(df_ventas.head(9))   #puedo indicar el número de filas que quiero ver o dejar vacío 5
df_multi_index = df_ventas.set_index(['Sucursal', 'Fecha', 'Categoria'])
print("\n====== Vista de df set_index agrupado  ======\n")
print(df_multi_index.head(9))
# Vista de df completo ventas
print("\n====== Vista completa de df ventas ======\n")
print(df_ventas)
# Vista completa de df_multi_index
print("\n====== Vista completa de df_multi_index ======\n")
print(df_multi_index)