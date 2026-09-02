import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/Pedidos.csv")

# 1- Criando uma unica figura com 4 subplots
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

# Grafico 1 - Quantidade de unidades vendidas por regiao
df.groupby("Regiao")["Unidades"].sum().plot.bar(color="#33658F", ax=ax[0,0])
ax[0,0].set_title("Quantidade de unidades vendidas por regiao")
ax[0,0].set_xlabel("Regiao")
ax[0,0].set_ylabel("Unidades")
ax[0,0].tick_params(axis='x', rotation=45)

# Grafico 2 - Distribuicao de vendas por itens (Pizza)

df['Item'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax[0,1])
ax[0,1].set_title("Distribuicao de vendas por itens")
ax[0,1].axis("equal")

# 3 - Grafico 3 - Relacao entre preco e unidades vendidas (Dispersao)
ax[1,0].scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='#F6AE2D',
)   
ax[1,0].set_title("Relacao entre preco e unidades vendidas")
ax[1,0].set_xlabel("Preco por unidade")
ax[1,0].set_ylabel("Unidades vendidas")
ax[1,0].grid(True)

# 4 - Grafico 4 - Quantidades de unidades vendidas ao longo do tempo (Linha)
#Convertendo a coluna "Data" para o tipo datetime
df['DataPedido'] = pd.to_datetime(df['DataPedido'])

df.groupby('DataPedido')['Unidades'].sum().plot(kind='line', marker='o', color='#4ECDC4', ax=ax[1,1])
ax[1,1].set_title('Quantidade de unidades vendidas ao longo do tempo')
ax[1,1].set_xlabel('Data do Pedido')
ax[1,1].set_ylabel('Unidades Vendidas')
ax[1,1].grid(True)

plt.show() 
