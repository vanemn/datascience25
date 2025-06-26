from operator import index
import pandas as pd

# 1. Crear el DataFrame
datos = {
    "Jugador": ["Lionel Messi", "Cristiano Ronaldo", "Kevin De Bruyne", "Kylian Mbappé", "Luka Modric"],
    "Posición": ["Delantero", "Delantero", "Mediocampista", "Delantero", "Mediocampista"],
    "Edad": [35, 38, 31, 24, 37],
    "Goles": [20, 18, 8, 25, 3],
    "Asistencias": [10, 5, 15, 12, 8]
}
df = pd.DataFrame(datos)

# 2. selecciona una columna y mostrar los nombres de todos los jugadores
print("Nombres de todos los jugadores:\n",df["Jugador"])

# 3. Filtrar jugadores con más de 10 goles
goleadores = df[df["Goles"] > 10][["Jugador", "Goles"]]
print("jugadores con más de 10 goles:\n", goleadores)

# 4. Agregar columna de Puntos
df["Puntos"] = (df["Goles"] * 4) + (df["Asistencias"] * 2)
print("DataFrame con columna de Puntos:\n", df)

# 5. Calcular promedio de goles
promedio_goles = df["Goles"].mean()
print("Promedio de goles:", promedio_goles)

# 6. Máximo y mínimo de asistencias
max_asist = df["Asistencias"].max()
min_asist = df["Asistencias"].min()
print("Máximo de asistencias:", max_asist)
print("Mínimo de asistencias:", min_asist)

# 7. Contar cuantos jugadores por posición
conteo_posiciones = df["Posición"].groupby(df["Posición"]).size()
print("Conteo de jugadores por posición:\n", conteo_posiciones)

# 8. Ordenar DataFrame por goles descendente
df_ordenado = df.sort_values(by="Goles", ascending=False)
print("DataFrame ordenado por goles:\n", df_ordenado)

# 9. Estadísticas generales
print("Estadísticas generales:\n", df.describe())

# 10. Contar jugadores por posición con value_counts()
print("Conteo de jugadores por posición:\n", df["Posición"].value_counts())