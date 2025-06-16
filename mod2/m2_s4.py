import math
import statistics
import random

# 1. Crea una función calcular_area_rectangulo que reciba dos parámetros (largo y ancho) y retorne el área del rectángulo (1 punto)
def calcular_area_rectangulo(largo, ancho):
    return largo * ancho

# 2. Crea una función calcular_circunferencia que reciba el radio de un círculo y retorne su circunferencia. Usa la constante pi del módulo math (2 puntos).
def calcular_circunferencia(radio):
    return 2 * math.pi * radio

# 3. Crea una función calcular_promedio que reciba una lista de números y retorne el promedio (1 punto). 
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

# 4. Importa la función mean del módulo statistics y úsala en una nueva función calcular_promedio_avanzado para calcular el promedio de la misma lista de números del punto anterior (2 puntos). 
def calcular_promedio_avanzado(numeros):
    return statistics.mean(numeros)

# 5. Crea una función generar_numeros_aleatorios que reciba dos parámetros (cantidad y limite), y retorne una lista de números aleatorios entre 1 y el límite especificado. Usa el módulo random (2 puntos). 
def generar_numeros_aleatorios(cantidad, limite):
    return [random.randint(1, limite) for _ in range(cantidad)]

# 6. Escribe un programa que utilice cada una de las funciones anteriores e imprime los resultados de cada cálculo (2 puntos). 
if __name__ == "__main__":
    # Solicitar entrada del usuario
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    print(f"El área del rectángulo es: {calcular_area_rectangulo(largo, ancho)}")

    radio = float(input("Ingrese el radio del círculo: "))
    print(f"La circunferencia del círculo es: {calcular_circunferencia(radio)}")

    numeros_str = input("Ingrese una lista de números separados por comas: ")
    numeros = [float(num) for num in numeros_str.split(",")]
    print(f"El promedio de los números es: {calcular_promedio(numeros)}")
    print(f"El promedio avanzado de los números es: {calcular_promedio_avanzado(numeros)}")

    cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    limite = int(input("Ingrese el límite máximo para los números aleatorios: "))
    print(f"Números aleatorios generados: {generar_numeros_aleatorios(cantidad, limite)}")