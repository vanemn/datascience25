# Reto 1: Gestor de Números Pares e Impares
#  Crea un programa que tenga un menú interactivo usando un ciclo while. El usuario podrá:
# - Agregar un número a una lista
# - Ver la lista completa
# - Ver solo los números pares
# - Ver solo los números impares
# - Salir del programa
numeros = []

while True:
    print("\n--- Gestor de Números Pares e Impares ---")
    print("1. Agregar un número")
    print("2. Ver la lista completa")
    print("3. Ver solo los números pares")
    print("4. Ver solo los números impares")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero = int(input("Ingrese un número: "))
        numeros.append(numero)
        print(f"Número {numero} agregado.")

    elif opcion == "2":
        print("\nLista completa de números:")
        print(numeros if numeros else "La lista está vacía.")

    elif opcion == "3":
        pares = [num for num in numeros if num % 2 == 0]
        print("\nNúmeros pares:")
        print(pares if pares else "No hay números pares en la lista.")

    elif opcion == "4":
        impares = [num for num in numeros if num % 2 != 0]
        print("\nNúmeros impares:")
        print(impares if impares else "No hay números impares en la lista.")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")