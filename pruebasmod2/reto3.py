#Reto 3: Panel de Control de Estudiantes
#  Crea un programa con un diccionario de estudiantes y sus calificaciones. El menú debe permitir:
# - Ver todos los estudiantes
# - Agregar un nuevo estudiante
# - Mostrar estudiantes aprobados y reprobados
# - Calcular el promedio general
# - Salir
# Lista para EVALUAR CALIFICACIONES de los estudiantes
# Diccionario para almacenar estudiantes y sus calificaciones
estudiantes = []

while True:
    # Ingresar nombre
    nombre = input("Ingrese el nombre del estudiante: ")

    # Ingresar calificaciones de 3 materias y calcular el promedio
    materias = ["Matemáticas", "Ciencias", "Inglés"]
    calificaciones = [float(input(f"Ingrese calificación de {materia} (1 - 7): ")) for materia in materias]
    
    promedio = sum(calificaciones) / len(materias)

    # Evaluar si el estudiante aprueba o reprueba
    estado = "Aprobado" if promedio >= 4 else "Reprobado"

    # Guardar datos del estudiante
    estudiantes.append({"nombre": nombre, "promedio": promedio, "estado": estado})

    # Preguntar si desea ingresar otro estudiante
    if input("¿Ingresar otro estudiante? (s/n): ").lower() != "s":
        break

# Imprimir resultados de todos los estudiantes
print("\nResultados de los estudiantes:")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Promedio: {estudiante['promedio']:.1f}, Estado: {estudiante['estado']}")

# Calcular el promedio general de todos los estudiantes
if estudiantes:
    promedio_general = sum(est["promedio"] for est in estudiantes) / len(estudiantes)
    print(f"\nPromedio general de la clase: {promedio_general:.1f}")
else:
    print("\nNo hay suficientes datos para calcular el promedio general.")
