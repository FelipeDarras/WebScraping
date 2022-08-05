from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.tycsports.com/estadisticas/liga-profesional-de-futbol/tabla-de-posiciones.html'
page = requests.get(url)
bsoup = BeautifulSoup(page.content, 'html.parser')

# EQUIPOS
teams = bsoup.find_all('td', class_= 'equipo')

# PUNTOS
points = bsoup.find_all('td', class_='puntos')

# EXTRAER CONTENIDO Y GUARDAR EN LISTAS
equipos = list()
for team in teams:
    equipos.append(team.text)
    
equipos = [equipo.strip() for equipo in equipos]

puntos = list()
for p in points:
    puntos.append(p.text)

# CONVERSIÓN A DATAFRAME
df_zona_a = pd.DataFrame({'Equipo':equipos[:14], 'Puntos':puntos[:14]})

df_zona_b = pd.DataFrame({'Equipo':equipos[14:], 'Puntos':puntos[14:]})

print(df_zona_a)
print(df_zona_b)
