import pandas as pd


data = {
 'Cliente': ['C1', 'C2', 'C1', 'C3'],
 'Producto': ['Portátil', 'Teléfono', 'Tableta', 'Ratón'],
 'Categoría': ['Electrónica', 'Electrónica', 'Electrónica', 'Accesorios'],
 'Monto': [999.99, 499.99, 299.99, 19.99],
 'Fecha': ['2025-10-01', '2025-09-15', '2025-11-01', '2025-08-01']
}
df = pd.DataFrame(data)

#Filtrar compras realizadas en el último trimestre (suponiendo que se proporcionan fechas)
df['Fecha'] = pd.to_datetime(df['Fecha'])
ultimo_trimestre = df[df['Fecha'] >= '2025-10-01']
print("\nCompras realizadas en el último trimestre:\n", ultimo_trimestre)
print(df)

# Calcular el monto  total de compras por cliente usando una operación de Serie.
monto_por_cliente = df.groupby('Cliente')['Monto'].sum()
print("\nMonto total por cliente:\n", monto_por_cliente)

#Resumir estadísticas de compras y contar categorías únicas de productos.
estadisticas_compras = df.describe()
categorias_unicas = df['Categoría'].unique()
print("\nEstadísticas de compras:\n", estadisticas_compras)
print("\nCategorías únicas de productos:\n", categorias_unicas)

# Mostrar los tres principales clientes por  monto total de compra.
top_clientes = df.groupby('Cliente')['Monto'].sum().nlargest(3)
print("\nTop 3 clientes por monto total de compra:\n", top_clientes)