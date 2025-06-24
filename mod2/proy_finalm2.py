

class Libro:
    def __init__(self, id_libro, titulo, autor, precio, stock):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        return f"{self.id_libro} - {self.titulo} por {self.autor} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

class Inventario:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        print("\nLibros disponibles:\n")
        for libro in self.libros:
            print(libro)

    def filtrar_por_precio(self, precio_min, precio_max):
        filtrados = [libro for libro in self.libros if precio_min <= libro.precio <= precio_max]
        return filtrados

    def buscar_libro(self, id_libro):
        for libro in self.libros:
            if libro.id_libro == id_libro:
                return libro
        return None

class Carrito:
    def __init__(self):
        self.contenido = []

    def agregar(self, libro, cantidad):
        if libro.stock >= cantidad:
            self.contenido.append({'libro': libro, 'cantidad': cantidad})
            print(f"\nSe han agregado {cantidad} ejemplares de '{libro.titulo}' al carrito.")
        else:
            print(f"\nNo hay suficiente stock para '{libro.titulo}'.")

    def mostrar_carrito(self):
        print("\nResumen del carrito:\n")
        total = 0
        for item in self.contenido:
            libro = item['libro']
            cantidad = item['cantidad']
            subtotal = libro.precio * cantidad
            total += subtotal
            print(f"{libro.titulo} | Cantidad: {cantidad} | Subtotal: ${subtotal:.2f}")
        print(f"\nTotal sin descuentos: ${total:.2f}")
        return total

def aplicar_descuento(total, codigo_descuento):
    descuentos = {
        'DESCUENTO10': 0.10,
        'DESCUENTO20': 0.20
    }
    if codigo_descuento in descuentos:
        porcentaje = descuentos[codigo_descuento]
        descuento = total * porcentaje
        total_final = total - descuento
        print(f"\nDescuento aplicado: {porcentaje*100}% (${descuento:.2f})")
        return total_final
    else:
        print("\nCódigo de descuento inválido.")
        return total

def crear_inventario():
    inventario = Inventario()
    inventario.agregar_libro(Libro('L1', 'Cien años de soledad', 'Gabriel García Márquez', 150.00, 5))
    inventario.agregar_libro(Libro('L2', 'El amor en los tiempos del cólera', 'Gabriel García Márquez', 120.00, 3))
    inventario.agregar_libro(Libro('L3', 'Don Quijote de la Mancha', 'Miguel de Cervantes', 200.00, 2))
    inventario.agregar_libro(Libro('L4', 'War and Peace', 'Leo Tolstoy', 250.00, 4))
    inventario.agregar_libro(Libro('L5', 'Pride and Prejudice', 'Jane Austen', 100.00, 6))
    return inventario

def main():
    inventario = crear_inventario()
    carrito = Carrito()

    while True:
        print("\n--- Sistema de Libros & Bytes ---")
        print("1. Mostrar todos los libros")
        print("2. Filtrar libros por rango de precio")
        print("3. Agregar libro al carrito")
        print("4. Ver carrito")
        print("5. Aplicar descuento y finalizar compra")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            inventario.mostrar_libros()

        elif opcion == '2':
            try:
                precio_min = float(input("Precio mínimo: "))
                precio_max = float(input("Precio máximo: "))
                filtrados = inventario.filtrar_por_precio(precio_min, precio_max)
                print("\nLibros en rango de precio:")
                for libro in filtrados:
                    print(libro)
            except ValueError:
                print("Entrada inválida.")

        elif opcion == '3':
            id_libro = input("Ingrese el ID del libro: ")
            libro = inventario.buscar_libro(id_libro)
            if libro:
                try:
                    cantidad = int(input("Cantidad: "))
                    carrito.agregar(libro, cantidad)
                except ValueError:
                    print("Cantidad inválida.")
            else:
                print("Libro no encontrado.")

        elif opcion == '4':
            total = carrito.mostrar_carrito()

        elif opcion == '5':
            total = carrito.mostrar_carrito()
            codigo_descuento = input("Ingrese código de descuento (si no tiene, presione Enter): ").strip()
            if codigo_descuento:
                total_final = aplicar_descuento(total, codigo_descuento)
            else:
                total_final = total
            print(f"\nTotal a pagar después de descuentos: ${total_final:.2f}")
            print("\n¡Gracias por su compra!")
            break

        elif opcion == '6':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    main()