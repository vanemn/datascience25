# 1. Importar la librería NumPy (1 punto).
import numpy as np
# 2. Crear un vector de 10 elementos con valores del 1 al 10 utilizando arange() (1 punto).
vector =np.arange(1,11)
# • Muestra el vector generado.
print("Vector de 10 elementos:", vector)
# 3. Generar una matriz de 3x3 con valores aleatorios entre 0 y 1 usando random.rand() (1
# punto).
matriz_aleatoria = np.random.rand(3,3)
# • Muestra la matriz en pantalla.
print("Matriz de 3x3 con valores aleatorios:\n", matriz_aleatoria)
# 4. Crear una matriz identidad de tamaño 4x4 utilizando eye() (1 punto).
matriz_identidad = np.eye(4)
# • Muestra la matriz identidad.
print("Matriz identidad de 4x4:\n", matriz_identidad)
# 5. Redimensionar el vector creado en el punto 2 en una matriz de 2x5 usando .reshape() (1
# punto).
matriz_redimensionada = vector.reshape(2, 5)
# • Muestra la nueva matriz.
print("Matriz redimensionada de 2x5:\n", matriz_redimensionada)
# 6. Seleccionar los elementos mayores a 5 del vector original y mostrarlos (1 punto).
elementos_mayores_a_5 = vector[vector > 5]
# • Utiliza indexación condicional.
print("Elementos mayores a 5 del vector original:", elementos_mayores_a_5)
# 7. Realizar una operación matemática entre arreglos (2 puntos)
# • Crea dos arreglos de tamaño 5 con arange() y súmalos.
arreglo1 = np.arange(5)
arreglo2 = np.arange(5)
# sumando los dos arreglos
arreglo_suma = arreglo1 + arreglo2
# • Muestra el resultado.
print("Resultado de la suma de dos arreglos:\n", arreglo_suma)
# 8. Aplicar una función matemática a un arreglo (2 puntos).
# • Calcula la raíz cuadrada de los elementos del vector original.
raiz_cuadrada_vector = np.sqrt(vector)
# • Muestra el resultado.
print("Raíz cuadrada de los elementos del vector original:\n", raiz_cuadrada_vector)
