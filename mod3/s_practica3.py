import pandas as pd

# Cargar desde web
url = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_poblaci%C3%B3n'
tablas = pd.read_html(url)
print(f"Se han encontrado {len(tablas)} tablas en la página web.")

# Mostrar y guardar la primera tabla
df = tablas[0]
print(df.head())
df.to_excel('entradas/paises_dependientes.xlsx', index=False, sheet_name='PaisesDependientes')

#revisar contenido de segunda tabla
print(f"Contenido de la segunda tabla:")
df2 = tablas[1]
print(df2.head())    
print(f"Total de filas en la segunda tabla: {len(df2)}")
print(df2.columns)