# contador = 1
# while contador <= 5:
#     print("Hola", contador)
#     contador += 1


# contador = 100
# while contador >= 50:  # Se ejecuta mientras contador sea 50 o más
#     print("Hola", contador)
#     contador -= 1  # Disminuye el contador en cada iteración
# print("Fin del programa.")

# contador = 1
# while contador <= 5:
#     if contador % 2 == 0:  # Si el número es divisible por 2, es par
#         tipo = "par"
#     else:
#         tipo = "impar"
#     print(f"Hola {contador}, es un número {tipo}.")
#     contador += 1  # Incremento del contador
# print("Fin del programa.")



# palabra = input("Introduce un texto: ")
# contador = 0
# while contador < len(palabra):
#     print(palabra[contador])
#     contador += 1 

# texto = input("Introduce un texto: ")
# indice = 0  
# while indice < len(texto):  
#     print(f"Posición {indice}: {texto[indice]}")
#     indice += 1 
# print(f"Total de letras: {len(texto)}")  


# opcion = ""
# while opcion != "4":
#     print("1. suma")
#     print("2. resta 2")
#     print("3. multiplicacion")
#     print("4. Salir")
#     opcion = input("Seleccione una opción: ")
    
#     if opcion == "1":
#         numero1 = float(input("Ingrese el primer número: "))
#         numero2 = float(input("Ingrese el segundo número: "))
#         resultado = numero1 + numero2
#         print(f"La suma de {numero1} y {numero2} es: {resultado}")
#     elif opcion == "2":
#         numero1 = float(input("Ingrese el primer número: "))
#         numero2 = float(input("Ingrese el segundo número: "))
#         resultado = numero1 - numero2
#         print(f"La resta de {numero1} y {numero2} es: {resultado}")
#     elif opcion == "3":
#         numero1 = float(input("Ingrese el primer número: "))
#         numero2 = float(input("Ingrese el segundo número: "))
#         resultado = numero1 * numero2
#         print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
#     elif opcion == "4":
#         print("Saliendo del programa...")
#     else:
#         print("Opción no válida, por favor intente de nuevo.")



# Ingresar los cuatro números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
num4 = float(input("Ingrese el cuarto número: "))

opcion = ""

while opcion != "4":
    print("\nMenú de operaciones:")
    print("1. Calcular suma total")
    print("2. Calcular promedio")
    print("3. Mostrar número mayor y menor")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        suma_total = num1 + num2 + num3 + num4
        print(f"La suma total es: {suma_total}")
    
    elif opcion == "2":
        promedio = (num1 + num2 + num3 + num4) / 4
        print(f"El promedio es: {promedio}")
    
    elif opcion == "3":
        mayor = num1
        menor = num1

        if num2 > mayor:
            mayor = num2
        elif num2 < menor:
            menor = num2

        if num3 > mayor:
            mayor = num3
        elif num3 < menor:
            menor = num3

        if num4 > mayor:
            mayor = num4
        elif num4 < menor:
            menor = num4

        print(f"El número mayor es: {mayor}")
        print(f"El número menor es: {menor}")

    elif opcion == "4":
        print("Saliendo del programa...")

    else:
        print("Opción no válida, por favor intente de nuevo.")

