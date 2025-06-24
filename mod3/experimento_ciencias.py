import pandas as pd
import csv


# Datos en una lista de diccionarios
datos = [
    {"Estudiante": "Ana", "Grado": 6, "Experimento": "Densidad del Agua", "Resultado": 1.02, "Unidad": "g/cm³", "Fecha": "2025-04-15", "Observaciones": "Sin anomalías"},
    {"Estudiante": "Luis", "Grado": 6, "Experimento": "Crecimiento de Moho", "Resultado": 3.4, "Unidad": "cm", "Fecha": "2025-04-16", "Observaciones": "Poca luz"},
    {"Estudiante": "Marta", "Grado": 5, "Experimento": "Cambios de Estado", "Resultado": 80, "Unidad": "°C", "Fecha": "2025-04-17", "Observaciones": "Hervido"},
    {"Estudiante": "Pedro", "Grado": 5, "Experimento": "Conductividad Térmica", "Resultado": 50, "Unidad": "°C", "Fecha": "2025-04-17", "Observaciones": "Metal calentar"},
    {"Estudiante": "Lucía", "Grado": 6, "Experimento": "Fotosíntesis", "Resultado": 2.1, "Unidad": "% O₂", "Fecha": "2025-04-18", "Observaciones": "Baja tasa observada"},
]

# Crear el archivo CSV
nombre_archivo = 'salidas/experimentosc_ciencias.csv'

# Escribir datos en CSV
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
    campos = ["Estudiante", "Grado", "Experimento", "Resultado", "Unidad", "Fecha", "Observaciones"]
    writer = csv.DictWriter(archivo_csv, fieldnames=campos)

    writer.writeheader()
    for fila in datos:
        writer.writerow(fila)

print(f"Archivo {nombre_archivo} creado con éxito.")
# Ruta del archivo CSV
archivo = 'salidas/experimentosc_ciencias.csv'

# Cargar los datos
# Dado el formato no muy estructurado, quizás necesitemos hacer una limpieza previa
# Aquí asumimos que ya tienes un CSV bien estructurado
# Si no, necesitaríamos parsear el texto manualmente

# Solo como ejemplo, si tienes un CSV estructurado, carga con pd.read_csv
df = pd.read_csv(archivo)

# Mostrar los primeros datos para verificar
print(df.head())

# Funciones para las aplicaciones

# 1. Filtrar resultados por experimento o estudiante
def filtrar_por_experimento_o_estudiante(df, criterio):
    # criterio puede ser el nombre del experimento o estudiante
    return df[df.apply(lambda row: row.astype(str).str.contains(criterio, case=False).any(), axis=1)]

# 2. Convertir unidades (ejemplo: cm a m, °C a K)
def convertir_unidades(df, columna, from_unit, to_unit):
    if from_unit == 'cm' and to_unit == 'm':
        df[columna] = df[columna] / 100
    elif from_unit == '°C' and to_unit == 'K':
        df[columna] = df[columna] + 273.15
    return df

# 3. Calcular promedios por experimento, grado o fecha
def calcular_promedios(df, columna_resultado, grupo_por):
    return df.groupby(grupo_por)[columna_resultado].mean()

# 4. Limpiar datos con valores nulos o inválidos
def limpiar_datos(df):
    return df.dropna()

# 5. Agrupar y contar experimentos por grado
def contar_experimentos_por_grado(df):
    return df.groupby('Grado')['Experimento'].count()

# 6. Detectar anomalías (valores extremos)
def detectar_anomalias(df, columna):
    # Ejemplo simple: valores fuera de 1.5*IQR
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    anomalias = df[(df[columna] < lower_bound) | (df[columna] > upper_bound)]
    return anomalias

# 7. Exportar resultados a un nuevo CSV
def exportar_resultados(df, nombre_archivo):
    df.to_csv(nombre_archivo, index=False)

# Ejemplo de uso:
# Filtrar por estudiante 'Luis'
resultado_filtrado = filtrar_por_experimento_o_estudiante(df, 'Luis')
print(resultado_filtrado)

# Convertir distancia de cm a m en columna 'Resultado'
df = convertir_unidades(df, 'Resultado', 'cm', 'm')

# Calcular promedios por fecha
promedios_fecha = calcular_promedios(df, 'Resultado', 'Fecha')
print(promedios_fecha)

# Detectar anomalías en resultado
anomalias = detectar_anomalias(df, 'Resultado')
print(anomalias)

# Exportar resultados filtrados y análisis
exportar_resultados(resultado_filtrado, 'salidas/resultado_filtrado.csv')
exportar_resultados(anomalias, 'salidas/anomalias.csv')