import numpy as np

# Creación de la matriz de inventario (Equipo 1)
inventario = np.array([
    [45, 8, 67, 92],  # Medicamentos
    [73, 55, 4, 88],  # Alimentos
    [19, 82, 63, 3],  # Accesorios
    [91, 47, 9, 76],  # Vacunas
    [34, 95, 81, 2]   # Antiparasitarios
])

#Primer número (5) → Valor mínimo- Segundo número (31) → Valor máximo exclusivo -  Tercer número (5) → Cantidad de valores
#ventas_promedio = np.random.randint(5, 31, 5)

# Ventas semanales promedio por producto (valores entre 5 y 30)
ventas_promedio = np.array([15, 25, 10, 22, 8])

# Identificar productos con existencias menores a 20 unidades
productos_bajos = inventario < 20

# Priorizar reabastecimiento de productos con alta demanda (>20)
prioridad_reabastecimiento = productos_bajos & (ventas_promedio[:, None] > 20)

# Mostrar resultados
print("\nMatriz de Inventario:")
print(inventario)

print("\nProductos con baja existencia (<20 unidades):")
print(productos_bajos)

print("\nVentas promedio por producto:")
print(ventas_promedio)

print("\nPrioridad de reabastecimiento (ventas > 20 y existencias bajas):")
print(prioridad_reabastecimiento)