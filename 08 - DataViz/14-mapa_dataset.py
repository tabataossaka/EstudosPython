import folium as fl
import pandas as pd

# 1 - importando o dataset 
url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
dados_terremoto = pd.read_csv(url)

print(dados_terremoto)

# 2 - Filtrar os dados para obter terremotos mais significativos (magnitude >= 6.0)
dados_significativos = dados_terremoto[dados_terremoto['mag'] >= 6.0]

print(dados_significativos)

# 3 - Criar um mapa centrado em uma localização específica (latitude e longitude)
mapa_terremotos = fl.Map(location=[0, 0], zoom_start=2)  

# 4 - Adicionar marcadores ao mapa para cada terremoto significativo
for index, terremoto in dados_significativos.iterrows():
    fl.Marker(
        location=[terremoto['latitude'], terremoto['longitude']],
        popup=f"Magnitude: {terremoto['mag']}, Profundidade: {terremoto['depth']}",
        icon=fl.Icon(color='red', icon='info-sign')
    ).add_to(mapa_terremotos)

mapa_terremotos.save('data/mapa_terremotos.html')  # Salvar o mapa em um arquivo HTML