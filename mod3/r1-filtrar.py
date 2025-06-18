#Reto 1: Filtrar y Exportar Datos desde un CSV 
#Descripción: Lee el archivo CSV proporcionado (ventas.csv) que contiene datos de ventas (columnas: Producto, Cantidad, PrecioUnitario, Fecha). Filtra las ventas con una cantidad # mayor a 10 y exporta los resultados a un nuevo archivo CSV llamado ventas_filtradas.csv, usando un delimitador ; y sin incluir el índice. 
# Archivo de ejemplo: ventas.csv 
import pandas as pd
# Cargar el archivo CSV
df = pd.read_csv('entradas/ventas.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())

# Añadir columnas adicionales sin tocar el original
df['Cantidad'] = [5, 12, 8, 15]
df['PrecioUnitario'] = [10.0, 20.0, 15.0, 25.0]
df['Fecha'] = ['2025-06-01', '2025-06-02', '2025-06-03', '2025-06-04']

df_filtrado = df[df['Cantidad'] > 10].copy()

# Guardar filtrado
df_filtrado.to_csv('salidas/ventas_filtradas.csv', sep=';', index=False)

# Opcional: mostrar ambos DataFrames para verificar
print(" DataFrame completo:")
print(df)

print("\n✅ DataFrame filtrado (Cantidad > 10):")
print(df_filtrado)


