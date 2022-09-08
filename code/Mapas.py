# %%
import pandas as pd
import json
# %%
json_EU = open('../data/gz_2010_us_050_00_500k.json')
states = json.load(json_EU)
json_EU.close()
# %%
data_hispana = pd.read_csv('../data/Poblacion Hispana 2020 Ciudad Total.csv')
data_hispana['Porcentaje'] = (data_hispana['Pob Hispana']/data_hispana['Pob Total'])*100
data_hispana
# %%
import plotly.express as px
# %%
fig = px.choropleth(data_frame = data_hispana,          # Datos
                    geojson = states,           # Recibe los datos geoson
                    locations = 'ID',       # Columna del CSV que contiene el dato enlace con el geojson
                    color = 'Porcentaje',             # La columna que se desea usar para el mapa
                    color_continuous_scale = 'purples',  # Familia de color
                    featureidkey = 'properties.GEO_ID',      # Dato que conecta el la columna del CSV
                    basemap_visible = True,             # Elimina un marco alrededor del mapa
                    scope = 'usa',
                    hover_name = 'Ciudad',
                    width = 800,
                    height = 400
                    )
# %%
fig.update_layout(title_text = 'Población Hispana (2010)',   # Titulo
                  title_font_family = 'Times New Roman',                     # Tipo de letra
                  title_font_size = 22,                                      # Tamaño de letra
                  title_font_color = 'black',                                # Color de letra
                  title_x = 0.5,                                             # Posición del titulo
                  annotations = [dict(y = -0.2,
                                      xref = 'paper',
                                      yref = 'paper',
                                      text = 'Fuente: United States Census Bureau',
                                      font_family = 'Times New Roman',
                                      font_size = 18,
                                      showarrow = False)])
fig.write_image("../media/Poblacion Hispana.png")
fig.show()
# %%
data_mexicana = pd.read_csv('../data/Poblacion Mexicana.csv')
data_mexicana['Porcentaje'] = (data_mexicana['Poblacion Mexicana']/data_mexicana['Poblacion Total'])*100
data_mexicana.head()
# %%
fig = px.choropleth(data_frame = data_mexicana,          # Datos
                    geojson = states,           # Recibe los datos geoson
                    locations = 'ID',       # Columna del CSV que contiene el dato enlace con el geojson
                    color = 'Porcentaje',             # La columna que se desea usar para el mapa
                    color_continuous_scale = 'purples',  # Familia de color
                    featureidkey = 'properties.GEO_ID',      # Dato que conecta el la columna del CSV
                    basemap_visible = True,             # Elimina un marco alrededor del mapa
                    scope = 'usa',
                    hover_name = 'Entidad',
                    width = 800,
                    height = 400
                    )
# %%
fig.update_layout(title_text = 'Población Mexicana Estimada (2010)',   # Titulo
                  title_font_family = 'Times New Roman',                     # Tipo de letra
                  title_font_size = 22,                                      # Tamaño de letra
                  title_font_color = 'black',                                # Color de letra
                  title_x = 0.5,                                             # Posición del titulo
                  annotations = [dict(y = -0.2,
                                      xref = 'paper',
                                      yref = 'paper',
                                      text = 'Fuente: United States Census Bureau',
                                      font_family = 'Times New Roman',
                                      font_size = 18,
                                      showarrow = False)])
fig.write_image("../media/Poblacion Mexicana.png")         
fig.show()