import math as m

def calcular_descuento(precio, porcentaje):
    if precio > 0 and 0 <= porcentaje <= 100: 
        precio_final = precio * (1 - porcentaje / 100)
        return m.floor(precio_final)
    else:
        return "Valores inválidos."

precio = 1500
porcentaje = 20
print(calcular_descuento(precio, porcentaje)) 
