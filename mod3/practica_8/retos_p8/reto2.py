# Reto 2: Rendimiento Académico Nacional 

# 1. Carga los datos y explora los primeros registros. 
import pandas as pd
# Cargar los datos
df_calificaciones = pd.read_csv('calificaciones_escuelas.csv')
df_materias = pd.read_csv('materias.csv')
# Explorar los primeros registros
print("\n====== Vista de calificaciones_escuelas ======\n")
print(df_calificaciones.head())
print("\n====== Vista de materias ======\n")        
print(df_materias.head())

# 2. Elimina duplicados. 
df_calificaciones = df_calificaciones.drop_duplicates()
df_materias = df_materias.drop_duplicates()
# Explorar los datos después de eliminar duplicados
print("\n====== Vista de calificaciones_escuelas sin duplicados ======\n")
print(df_calificaciones.head())
print("\n====== Vista de materias sin duplicados ======\n")
print(df_materias.head())

# 3. Convierte Calificacion a numérico con coerción de errores. 

df_calificaciones['Calificacion'] = pd.to_numeric(df_calificaciones['Calificacion'], errors='coerce')
# Explorar los datos después de la conversión
print("\n====== Vista de calificaciones_escuelas con Calificacion numérico ======\n")
print(df_calificaciones.head())
#ver tipos de datos
print("\n====== Tipos de datos de calificaciones_escuelas ======\n")
print(df_calificaciones.dtypes)

# 4. Rellena valores nulos con la mediana general. 
mediana_calificacion = df_calificaciones['Calificacion'].median()
df_calificaciones['Calificacion'] = df_calificaciones['Calificacion'].fillna(mediana_calificacion)
# Explorar los datos después de rellenar valores nulos
print("\n====== Vista de calificaciones_escuelas con Calificacion sin nulos ======\n")
print(df_calificaciones.head(10))
# Verificar si hay valores nulos
print("\n====== Verificar valores nulos en calificaciones_escuelas ======\n")
print(df_calificaciones.isnull().sum())

# 5. Aplica pd.qcut() para categorizar calificaciones en Q1, Q2, Q3, Q4. 
df_calificaciones['Cuartil'] = pd.qcut(df_calificaciones['Calificacion'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
# Explorar los datos después de categorizar calificaciones

print("\n====== Vista de calificaciones_escuelas con Cuartil ======\n")
print(df_calificaciones.head(10))
# Verificar la distribución de cuartiles
print("\n====== Distribución de cuartiles ======\n")
print(df_calificaciones['Cuartil'].value_counts())

# 6. Une con materias.csv para clasificar las materias por tipo. 
df_calificaciones = pd.merge(df_calificaciones, df_materias, on='Materia', how='left')
# Explorar los datos después de unir con materias
print("\n====== Vista de calificaciones_escuelas con Materia y Tipo ======\n")
print(df_calificaciones.head(10))
# Verificar si hay valores nulos en Tipo
print("\n====== Verificar valores nulos en Tipo ======\n")
print(df_calificaciones['Tipo'].isnull().sum())
# Verificar tipos de datos después de la unión
print("\n====== Tipos de datos de calificaciones_escuelas después de la unión ======\n")
print(df_calificaciones.dtypes)
# guardar el DataFrame con la unión
df_calificaciones.to_csv('salidas/calificaciones_escuelas_con_materias.csv', index=False)

# 7. Agrupa por Escuela y Tipo de materia, y calcula el promedio por grupo. 
df_promedio = df_calificaciones.groupby(['Escuela', 'Tipo'])['Calificacion'].mean().reset_index()
print("\n====== Vista de promedio por Escuela y Tipo ======\n")
print(df_promedio.head(10))
# Guardar el DataFrame con el promedio
df_promedio.to_csv('salidas/promedio_escuela_tipo.csv', index=False)

# 8. Usa .pivot() para crear una tabla dinámica por Escuela vs Tipo. 
df_pivot = df_calificaciones.pivot_table(index='Escuela', columns='Tipo', values='Calificacion', aggfunc='mean').fillna(0)
print("\n====== Vista de tabla dinámica por Escuela vs Tipo ======\n")
print(df_pivot.head(10))
# Guardar el DataFrame pivotado
df_pivot.to_csv('salidas/tabla_dinamica_escuela_tipo.csv')

# 9. Convierte la tabla de nuevo con .melt() para análisis posterior. 
df_despivot = df_pivot.reset_index().melt(id_vars='Escuela', var_name='Tipo', value_name='Calificacion')
print("\n====== Vista de tabla despivotada ======\n")
print(df_despivot.head(10))
# Guardar el DataFrame despivotado
df_despivot.to_csv('salidas/tabla_despivotada.csv', index=False)