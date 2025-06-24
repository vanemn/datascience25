
# 1. Lista de libros - Definir variables básicas y tipos de datos
#Crea una lista que contenga al menos cinco libros, donde cada libro sea un diccionario con los atributos título (cadena de caracteres), autor (cadena de caracteres), precio (decimal) y cantidad en stock (entero)
libros = [
    {"título": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "precio": 15000.0, "stock": 5},
    {"título": "Rayuela", "autor": "Julio Cortázar", "precio": 12000.0, "stock": 3},
    {"título": "1984", "autor": "George Orwell", "precio": 9500.0, "stock": 1},
    {"título": "Fahrenheit 451", "autor": "Ray Bradbury", "precio": 10000.0, "stock": 6},
    {"título": "El Aleph", "autor": "Jorge Luis Borges", "precio": 13000.0, "stock": 4}
]

# 6. Descuentos por autor - Estructura de datos, gestión de descuentos
# Usa un diccionario para almacenar descuentos especiales por autor. Por ejemplo, aplica un 10% de descuento en libro de un autor especifico. 
# En la función comprar_libro, certifica si el autor tiene descuento y aplícalo al monto total si corresponde. 
descuentos = {
    "Gabriel García Márquez": 0.10,
    "Ray Bradbury": 0.10
}

# 7 Variables para resumen final factura
total_libros = 0
total_pagado = 0
total_ahorro = 0


# 2. Mostrar libros disponibles con más de una unidad - Control de flujo
# Implementa una función llamada mostrar_libros_disponibles() que recorra la lista de libros y muestre en pantalla los libros que tienen más de una unidad en stock usando una sentencia for y una condición if.
def mostrar_libros_disponibles():
    print("\nLibros disponibles con más de una unidad:")
    for libro in libros:
        if libro["stock"] > 1:
            print(f"- {libro['título']} de {libro['autor']} - ${libro['precio']} (Stock: {libro['stock']})")

# 3. Filtrar libros por rango de precio - Condiciones y operadores
# Solicita al usuario que ingrese un rango de precios (mínimo y máximo) y utiliza una sentencia if elif else para filtrar los libros en el rango ingresado y mostrarlos en pantalla.
def filtrar_por_precio(min_precio, max_precio):
    print(f"\nLibros en el rango de precio ${min_precio} a ${max_precio}:")
    encontrados = False
    for libro in libros:
        if min_precio <= libro["precio"] <= max_precio:
            print(f"- {libro['título']} de {libro['autor']} - ${libro['precio']}")
            encontrados = True
    if not encontrados:
        print("No se encontraron libros en ese rango de precio.")

# 4. Comprar libros - Función personalizada para simular una compra
#Crea una función comprar_libros(título, cantidad) que reciba como parámetros el título del libro y la cantidad a comprar.
def comprar_libros(título, cantidad):
    global total_libros, total_pagado, total_ahorro
    # La función debe:▪ Verificar si el libro está en el inventario y si la cantidad deseada está disponible. 
    for libro in libros:
        if libro["título"].lower() == título.lower():
            #▪ Si la compra es válida, restar la cantidad comprada al stock y mostrar el monto total de la compra. 
            if libro["stock"] >= cantidad:
                # 6. Aplicar descuento si corresponde - En la función comprar_libro, certifica si el autor tiene descuento y aplícalo al monto total si corresponde. 
                descuento = descuentos.get(libro["autor"], 0)
                subtotal = libro["precio"] * cantidad
                ahorro = subtotal * descuento
                total = subtotal - ahorro
                libro["stock"] -= cantidad
                total_libros += cantidad
                total_pagado += total
                total_ahorro += ahorro
                print(f"\nCompra exitosa: {cantidad} x {libro['título']} - Total a pagar: ${total:.2f} (Ahorro: ${ahorro:.2f})")
                return
            #▪ Si la cantidad solicitada es mayor al stock disponible, mostrar un mensaje de error
            else:
                print("No hay suficiente stock disponible.")
                return
    print("El libro no se encuentra en el inventario.")

# 5. Menú interactivo - Uso de bucle while para iterar hasta que el usuario decida salir
#Implementa un bucle while que permita al usuario realizar múltiples compras hasta que ingrese una opción de salida
while True:
    print("\n--- Menú ---")
    print("1. Mostrar libros disponibles")
    print("2. Filtrar libros por precio")
    print("3. Comprar libro")
    print("4. Salir y ver factura")
    opción = input("Selecciona una opción: ")

    if opción == "1":
        mostrar_libros_disponibles()
    elif opción == "2":
        try:
            min_precio = float(input("Ingrese precio mínimo: "))
            max_precio = float(input("Ingrese precio máximo: "))
            filtrar_por_precio(min_precio, max_precio)
        except ValueError:
            print("Por favor, ingresa valores numéricos válidos.")
    elif opción == "3":
        título = input("Título del libro a comprar: ")
        try:
            cantidad = int(input("Cantidad a comprar: "))
            comprar_libros(título, cantidad)
        except ValueError:
            print("La cantidad debe ser un número entero.")
            # 7 Simulación de una factura
            #Al finalizar la compra, muestra un resumen con el total de libros comprados, el monto total pagado y el ahorro por descuentos. 
    elif opción == "4":
        print("\n--- Factura ---")
        print(f"Total de libros comprados: {total_libros}")
        print(f"Total pagado: ${total_pagado:.2f}")
        print(f"Ahorro total por descuentos: ${total_ahorro:.2f}")
        print("¡Gracias por tu compra en Libros & Bytes!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
