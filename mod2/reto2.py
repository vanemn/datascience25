# Tupla base con nombres de frutas
frutas = ("Manzana", "Platano", "Naranja", "Manzana", "Uva", "Kiwi", "Naranja", "piña")

while True:
    print("\n--- Inventario de Frutas ---")
    print("1. Ver todas las frutas")
    print("2. Contar cuántas veces aparece una fruta específica")
    print("3. Convertir tupla a lista y agregar una fruta")
    print("4. Mostrar el inventario actualizado")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nFrutas en el inventario:")
        print(frutas)

    elif opcion == "2":
        fruta_buscar = input("Ingrese el nombre de la fruta: ").lower()
        print(f"La fruta '{fruta_buscar}' aparece {sum(1 for fruta in frutas if fruta.lower() == fruta_buscar)} veces.")

    elif opcion == "3":
        frutas_lista = list(frutas)  # Convertir la tupla en lista
        nueva_fruta = input("Ingrese la nueva fruta a agregar: ")
        frutas_lista.append(nueva_fruta)
        frutas = tuple(frutas_lista)  # Convertir la lista nuevamente en tupla
        print(f"La fruta '{nueva_fruta}' ha sido agregada.")

    elif opcion == "4":
        print("\nInventario actualizado:")
        print(frutas)

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")