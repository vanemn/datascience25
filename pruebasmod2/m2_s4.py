import math
import statistics

# 1. Función para calcular el área de un rectángulo
def calcular_area_rectangulo(largo, ancho):
    return largo * ancho

# 2. Función para calcular la circunferencia de un círculo
def calcular_circunferencia(radio):
    return 2 * math.pi * radio

# 3. Función para calcular el promedio de una lista de números
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

# 4. Función para calcular el promedio usando statistics.mean
def calcular_promedio_avanzado(numeros):
    return statistics.mean(numeros)

# 5. Generación manual de números pseudoaleatorios (sin random)
# Usaremos una alternativa básica para simular números aleatorios
def generar_numeros_aleatorios(cantidad, limite):
    numeros = []
    semilla = 42  # Semilla arbitraria
    for _ in range(cantidad):
        semilla = (semilla * 7 + 13) % limite + 1
        numeros.append(semilla)
    return numeros

# 6. Programa que utiliza todas las funciones
if __name__ == "__main__":
    print("Área del rectángulo:", calcular_area_rectangulo(5, 10))
    print("Circunferencia del círculo:", calcular_circunferencia(7))
    lista_numeros = [10, 20, 30, 40, 50]
    print("Promedio de la lista:", calcular_promedio(lista_numeros))
    print("Promedio avanzado de la lista:", calcular_promedio_avanzado(lista_numeros))
    print("Lista de números aleatorios:", generar_numeros_aleatorios(5, 100))