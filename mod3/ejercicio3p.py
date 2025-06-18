import pandas as pd

data = {
    'Tienda': ['T1', 'T1', 'T2', 'T2'],
    'Producto': ['Portátil', 'Ratón', 'Teléfono', 'Tableta'],
    'Precio': [999.99, 19.99, 499.99, 299.99],
    'Cantidad': [5, 50, 8, 3]
}
df = pd.DataFrame(data)

# Filtrar artículos con bajo inventario (<10 unidades) en tiendas específicas.
bajo_inventario = df[df['Cantidad'] < 10]
print("\nArtículos con bajo inventario en la tienda T2:\n", bajo_inventario[bajo_inventario['Tienda'] == 'T2'])

#print("\nDataFrame original:\n", df)

# Calcular   valor total del inventario por tienda (precio * cantidad)Ygenerar un df.
df['Valor_Parcial'] = df['Precio'] * df['Cantidad']

valor_inventario_df = df.groupby('Tienda')['Valor_Parcial'].sum().reset_index(name='Valor_Inventario')

print(valor_inventario_df)

# Identificar tipos de productos  únicos y sus conteos. 

print("\nNúmero total de tipos únicos:", df['Producto'].nunique())
print(df['Producto'].unique()) #si quiero ver cuales
print(df['Producto'].count())