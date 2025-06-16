# # Programa que valida si un número es par o impar
# numero = int(input("Introduce un número: "))

# if numero % 2 == 0:
#     print(f"El número {numero} es par.")
# else:
#     print(f"El número {numero} es impar.")


# # Programa si el número es positivo, negativo o cero
# numero = int(input("Introduce un número: "))

# if numero > 0:
#     print(f"El número {numero} es positivo.")
# elif numero < 0:
#     print(f"El número {numero} es negativo.")
# else:
#     print(f"El número {numero} es cero.")


# # Verificar un usuario y contraseña en cadena
# usuario = input("Introduce tu usuario: ")
# contraseña = input("Introduce tu contraseña: ")

# if usuario == "admin" and contraseña == "1234":
#     print("Acceso concedido.")
# else:
#     print("Acceso denegado.")   

# #programa que valide la capital de un pais
# pais = input("Introduce el nombre de un país: ")
# if pais == "Francia":
#     print("La capital de Francia es París.")
# elif pais == "España":
#     print("La capital de España es Madrid.")
# elif pais == "Italia":
#     print("La capital de Italia es Roma.")
# else:
#     print("No tengo información sobre la capital de ese país.")


# #programa que valide la capital de un pais
# pais = input("Introduce el nombre de un país: ")
# if pais.upper() == "CHILE":
#     print("La capital de Chile es Santiago.")
# elif pais == "España":
#     print("La capital de España es Madrid.")
# elif pais == "Italia":
#     print("La capital de Italia es Roma.")
# else:
#     print("No tengo información sobre la capital de ese país.")

# Programa que asigne una letra a una calificación numérica de notas
# nota = float(input("Introduce la calificación numérica: "))

# if 9 <= nota <= 10:
#     print("La calificación es A.")
# elif 7 <= nota < 9:
#     print("La calificación es B.")
# elif 5 <= nota < 7:
#     print("La calificación es C.")
# elif 0 <= nota < 5:
#     print("La calificación es D.")
# else:
#     print("Calificación no válida.")


# Programa que clasifica la edad de una persona
edad = int(input("Introduce tu edad: "))
# debo recordar que esté dentro de un rango válido sino que no procese
if edad < 0 or edad > 120:
    print("Edad no válida.")
else:
    # Si la edad es válida,me separo tab para hacer la otra condición 
    if edad <= 12:
        print("Eres un niño.")
    elif edad <= 17:
        print("Eres un adolescente.")
    elif edad <= 59:
        print("Eres un adulto.")
    else:
        print("Eres un adulto mayor.")