# Lista para EVALUAR CALIFICACIONES de los estudiantes
estudiantes = []

while True:
# 1 Ingresar nombre y calificación
    nombre = input("Ingrese el nombre del estudiante: ")

    while (calificación := float(input("Ingrese la calificación (0-100): "))) not in range(101):
        print("Valor fuera de rango. Intente de nuevo.")
# 1 Usando if y else para evaluar la calificación
    print(f"{nombre} ha {'aprobado' if calificación >= 60 else 'no aprobado'}.")
# 3 Ingresar calificaciones de 3 materias y calcular el promedio
    materias = ["Matemáticas", "Ciencias", "Inglés"]
    promedio = sum(float(input(f"Ingrese calificación de {materia}: ")) for materia in materias) / len(materias)
#4 Evaluar el promedio y asignar comentarios if elif else
    if promedio >= 90:
        comentario = "Excelente"
    elif 75 <= promedio <= 89:
        comentario = "Bueno"
    else:
        comentario = "Necesita mejorar"
    comentario += " ¡Felicitaciones, puntuación perfecta!" if promedio == 100 else ""

    estudiantes.append({"nombre": nombre, "comentario": comentario, "promedio": promedio})
#2 bucle while para ingresar más estudiantes 
    if input("¿Ingresar otro estudiante? (s/n): ").lower() != "s":
        break
# 5 Imprimir resultados de los estudiantes bucle for 
print("\nResultados de los estudiantes:")
for estudiante in estudiantes:
#6 expresion termaria
    print(f"Nombre: {estudiante['nombre']}, Comentario: {estudiante['comentario']}, Promedio: {estudiante['promedio']:.2f}")
    

