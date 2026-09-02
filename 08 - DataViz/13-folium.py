import folium as fl
import pandas as pd

# 1 - Criar um mapa centrado em uma localização específica (latitude e longitude)
mapa = fl.Map(location=[-23.5505, -46.6333], zoom_start=12)  # São Paulo, Brasil

# 2 - Adicionar marcadores ao mapa
# Exemplo de dados fictícios de locais
cafeteiras = [
    {'localizacao': [-23.5505, -46.6333], 'nome': 'Cafeteria A'},
    {'localizacao': [-23.5685, -46.6621], 'nome': 'Cafeteria B'},
    {'localizacao': [-23.5432, -46.6250], 'nome': 'Cafeteria C'},
    {'localizacao': [-23.5300, -46.6100], 'nome': 'Cafeteria D'}
]

for cafe in cafeteiras:
    fl.Marker(
        location=cafe['localizacao'],
        popup=cafe['nome'],
        icon=fl.Icon(icon='coffee', color='#8B4513')
    ).add_to(mapa)

mapa.save('data/mapa_cafeterias.html')  # Salvar o mapa em um arquivo HTML
