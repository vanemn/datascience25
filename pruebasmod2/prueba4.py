
# Definición de variables
# Solicita al usuario ingresar los valores
precio_producto = int(input("Introduce el precio del producto en pesos: "))
cantidad = int(input("Introduce la cantidad comprada: "))
descuento = int(input("Introduce el porcentaje de descuento: "))

# Cálculo del precio total sin descuento
total_sin_descuento = precio_producto * cantidad

# Cálculo del monto de descuento en porcentaje y //para entero
monto_descuento = (total_sin_descuento * descuento) // 100

# Cálculo del precio total con descuento
total_con_descuento = total_sin_descuento - monto_descuento

# Impresión de resultados con mensajes claros
print(f"Total sin descuento: {total_sin_descuento}")
print(f"Monto de descuento: {monto_descuento}")
print(f"Total con descuento: {total_con_descuento}")