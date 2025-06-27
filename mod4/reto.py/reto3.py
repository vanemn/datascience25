# Reto 3: Análisis de Datos de Viajes en Taxi 

#  Archivo: taxi_trips.csv 
# Columnas clave: distancia, duración, costo, hora_inicio, barrio 
# Pasos a seguir: 
# 1. Inspección inicial 
df
# o Verifica si hora_inicio está en formato de fecha. 
# o Asegúrate de que distancia, duración y costo sean numéricos. 
# o Observa estadísticas básicas para cada variable. 
# 2. Limpieza de datos 
# o Elimina registros donde la distancia sea cero o negativa. 
# o Rellena valores faltantes en costo con el promedio del barrio. 
# 3. Análisis univariado 
# o Usa sns.histplot() para la distribución de distancia. 
# o Usa sns.boxplot() para encontrar viajes extremadamente largos. 
# 4. Detección de outliers 
# o Aplica IQR a distancia y costo. 
# o Evalúa si son errores de captura o situaciones reales. 
# 5. Análisis bivariado 
# o Crea un sns.scatterplot(x='distancia', y='costo', hue='barrio') para observar si existe 
# proporcionalidad o outliers por zona. 