

#Desarrolle una función promedio_calificaciones que calcule el promedio de  una lista de calificaciones de estudiantes  y determine si el grupo aprueba (promedio ≥ 6,0). La  función debe: Validar que la lista no esté vacía usando len(). Calcular el promedio con statistics.mean(). 1 evolver una cadena que indique el promedio edondeado a 2 decimales) y si el grupo  aprueba o no. Importe statistics con el alias stats. Pruebe con la lista de calificaciones [7.5, 8.0, 5.5, 6.5].
import statistics as stats

def promedio_calificaciones(calificaciones):
    if len(calificaciones) == 0:
        return "La lista de calificaciones está vacía."

    promedio = stats.mean(calificaciones)
    estado = "aprueba" if promedio >= 6.0 else "no aprueba"
    return f"El promedio:  {promedio:.2f} y el grupo : {estado}."


calificaciones = [7.5, 8.0, 5.5, 6.5]
print(promedio_calificaciones(calificaciones))