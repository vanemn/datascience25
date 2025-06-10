# Formateador de Fecha: Haga un programa que solicite el día, mes y año como números, los convierta a cadenas, y genere una fecha en formato "DD/MM/AAAA" (por ejemplo, 5, 6, 2025"05/06/2025"). Muestre la fecha.  → 

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))
fecha = f"{dia:02}/{mes:02}/{año}"
print(f"Fecha formateada: {fecha}")
