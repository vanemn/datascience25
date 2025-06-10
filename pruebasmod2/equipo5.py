def formateador_fecha():
    dia = input("Introduce el día: ")
    mes = input("Introduce el mes: ")
    año = input("Introduce el año: ")
    print(f"Fecha formateada: {dia.zfill(2)}/{mes.zfill(2)}/{año}")

def contador_espacios():
    frase = input("Introduce una frase: ")
    print(f"La frase contiene {frase.count(' ')} espacios.")

def mensaje_motivacional():
    nombre = input("Introduce tu nombre: ")
    objetivo = input("Introduce tu objetivo personal: ")
    print(f"{nombre}, ¡tú puedes lograr {objetivo}!")

def ejecutar():
    formateador_fecha()
    contador_espacios()
    mensaje_motivacional()

ejecutar()