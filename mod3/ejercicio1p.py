import pandas as pd

# Datos base
data = {
    'Nombre': ['Alicia', 'Bruno', 'Carlos', 'David'],
    'Departamento': ['Ventas', 'Marketing', 'TI', 'Ventas'],
    'Puntaje': [85, 90, 75, 88],
    'Calificación': ['A', 'A', 'B', 'A']
}

# Crear DataFrame con índices personalizados
df = pd.DataFrame(data, index=['E001', 'E002', 'E003', 'E004'])

print("DataFrame completo:\n", df)

# Filtrar empleados con puntajes de desempeño mayores a 80 en departamentos específicos (marketing )
altos_ventas = df[(df['Puntaje'] > 80) & (df['Departamento'] == 'Marketing')]
print(altos_ventas)
#Calcular el puntaje promedio  por departamento e identificar calificaciones únicas de desempeño.
promedio_departamento = df.groupby('Departamento')['Puntaje'].mean()
calificaciones_unicas = df['Calificación'].unique()
print("\nPuntaje promedio por departamento:\n", promedio_departamento)
print("\nCalificaciones únicas de desempeño:\n", calificaciones_unicas)

# Mostrar columnas  específicas para los empleados filtrados y sus detalles.
print(df.loc['E001'])  # Acceso a columnas específicas POR id
empleado = df[df['Nombre'] == 'Bruno'] #Acceso por nombre
print(empleado)