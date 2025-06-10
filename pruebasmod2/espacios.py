#Contador de Espacios: Desarrolle un programa que pida una frase y cuente cuántos espacios contiene sumando los caracteres " " en la cadena. Muestre el total.  

frase = input("Introduce una frase: ")
cantidad_espacios = frase.count(" ")
cantidad_caracteres = len(frase)
print(f"La frase contiene {cantidad_espacios} espacios.")
print(f"La frase contiene {cantidad_caracteres} caracteres en total.")
