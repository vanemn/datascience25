
# valores desde el cuerpo

class Pelota():
 def __init__(self):
 self.color = "blanco"
 self.tamanio = 20
 self.material = "plástico"
p = Pelota()
# Salida: blanco 20 plástico
print(p.color, p.tamanio, p.material)



# parámetros

class Pelota():
 def __init__(self, color: str, tamanio: int, material: str):
 self.color = color
 self.tamanio = tamanio
 self.material = material
p = Pelota("Amarillo", 16, "plástico")
# Salida: Amarillo 16 plástico
print(p.color, p.tamanio, p.material)
# Salida:
# TypeError: __init__() missing 3 required positional arguments:
# 'color', 'tamanio', and 'material'
p2 = Pelota()




class Pelota():
 def __init__(self, color: str, tamanio = 20, material =
"plástico"):
 self.color = color
 self.tamanio = tamanio
 self.material = material
p = Pelota("Amarillo", 16)
# Salida: Amarillo 16 plástico
print(p.color, p.tamanio, p.material)