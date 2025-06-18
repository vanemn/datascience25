import pandas as pd

# #forma con series

# dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
# temperaturas = [20, 22, 19, 21, 23]

# serie = pd.Series(data=temperaturas, index=dias)

# print("\nTemperaturas por día:\n", serie)

sales =pd.Series(data=[100, 200, 150, 300, 250], index=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
print("\nVentas por día:\n", sales)
print("\nVentas de lunes:\n", sales["Lunes"])  # Acceso a la venta del lunes
print("\nacceso a venta del lunes x posicion:", sales.iloc[0])  # Acceso a la venta del lunes usando la posición
print("Acceso a la venta del lunes usando el nombre del índice:", sales.loc["Lunes"])  # Acceso a la venta del lunes usando el nombre del índice
print("Acceso a las ventas del Martes y Miércoles", sales[1:3])  # Acceso a las ventas del Martes y Miércoles usando el índice numérico
print("Acceso a las ventas del Martes y Miércoles usando la posición:", sales.iloc[1:3])  # Acceso a las ventas del Martes y Miércoles usando la posición
print("Acceso a las ventas del Martes y Miércoles usando el nombre del índice:", sales.loc["Martes":"Miércoles"])  # Acceso a las ventas del Martes y Miércoles usando el nombre del índice
print("\nVentas mayores a 200:\n", sales[sales > 200])  # Acceso a las ventas mayores a 200
print("\nventas promedio:", sales.mean())  # Cálculo del promedio de ventas
print("\nventas max:", sales.max())  # Cálculo del máximo de ventas 
print("\nventas min:", sales.min())  # Cálculo del mínimo de ventas
print("ventas desviación estándar:", sales.std())  # Cálculo de la desviación estándar de las ventas
