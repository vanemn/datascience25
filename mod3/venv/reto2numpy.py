import numpy as np

# Crear matriz de inventario con valores aleatorios entre 0 y 100
inventario = np.random.randint(0, 101, (5, 4))

# Asegurar que al menos una tienda tenga existencias bajas (<10) por producto
for i in range(5):
    inventario[i, np.random.randint(0, 4)] = np.random.randint(0, 10)

print("Matriz de Inventario:")
print(inventario)

# Ventas semanales promedio por producto (valores entre 5 y 30)
#Primer número (5) → Valor mínimo- Segundo número (31) → Valor máximo exclusivo -  Tercer número (5) → Cantidad de valores
ventas_promedio = np.random.randint(5, 31, 5)

# Identificar productos con existencias menores a 20 unidades
productos_bajos = inventario < 20

# Priorizar reabastecimiento de productos con alta demanda (>20)
prioridad_reabastecimiento = productos_bajos & (ventas_promedio[:, None] > 20)

# Mostrar resultados
print("\nProductos con baja existencia:")
print(productos_bajos)

print("\nVentas promedio:")
print(ventas_promedio)

print("\nPrioridad de reabastecimiento (ventas > 20 y existencias bajas):")
print(prioridad_reabastecimiento)