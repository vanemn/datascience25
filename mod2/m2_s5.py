#1. Crea una lista productos que contenga al menos cinco nombres de productos (1 punto). 

productos = ["celular", "laptop", "tablet", "auriculares", "smartwatch"]

#2. Agrega dos productos más a la lista productos y luego rescata los primeros tres elementos en una nueva lista llamada productos_destacados (1 puntos).

productos.append("monitor")
productos.append("teclado")
productos_destacados = productos[:3]

#3. Crea un diccionario inventario donde cada clave sea el nombre de un producto y el valor sea la cantidad en stock. Incluye al menos cinco productos con sus cantidades (2 puntos).

inventario = {
    "celular": 50,
    "Laptop": 30,
    "tablet": 20,
    "auriculares": 100,
    "smartwatch": 75,
    "monitor": 40,
    "teclado": 60
}

#4. Agrega un nuevo producto al diccionario inventario y muestra la cantidad en stock de un producto específico (elige cualquiera de los cinco productos iniciales) (1 punto).

inventario["auriculares"] += 20  
inventario["Teclado"] = 12
producto_consultado = "Laptop"
cantidad_en_stock = inventario.get(producto_consultado, "Producto no encontrado")

# 5. Crea una tupla categorías que contenga las categorías de los productos (por ejemplo, “Electrónica”, “Ropa”, “Alimentos”). Rescata y muestra la segunda categoría (1 punto).
categorias = ("Electronica", "Ropa", "Alimentos")
segunda_categoria = categorias[1]

# 6. Empaqueta las categorías en una tupla y luego desempaquétalas en variables individuales para que cada categoría quede asignada a una variable (2 puntos). 
categoria1, categoria2, categoria3 = categorias

# 7.  Crea un set productos_unicos a partir de la lista productos y verifica que no existan elementos duplicados (1 punto)
productos_unicos = set(productos)

# 8. Usa comprensión de listas para crear una lista productos_mayusculas que contenga los nombres de productos en mayúsculas (1 punto) 
productos_mayusculas = [producto.upper() for producto in productos]

# Mostrar resultados
print("Lista de productos:", productos)
print("Productos destacados:", productos_destacados)
print("Inventario:", inventario)
print(f"Cantidad en stock de {producto_consultado}: {cantidad_en_stock}")
print("Lista de categorias:", categorias)
print("Segunda categoria:", segunda_categoria)
print("Categorias desempaquetadas:", categoria1, categoria2, categoria3)
print("Productos unicos:", productos_unicos)
print("Productos en mayusculas:", productos_mayusculas)