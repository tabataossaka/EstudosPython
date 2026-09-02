import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/Pedidos.csv")

# Grafico 1 - Quantidade de unidades vendidas por regiao
plt.figure(figsize=(8,5))
df.groupby("Regiao")["Unidades"].sum().plot.bar(color="#33658F")
plt.title("Quantidade de unidades vendidas por regiao")
plt.xlabel("Regiao")
plt.ylabel("Unidades")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grafico 2 - Distribuicao de vendas por itens (Pizza)
plt.figure(figsize=(8,5))
df['Item'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("Distribuicao de vendas por itens")
plt.axis("equal")
plt.show()

# 3 - Grafico 3 - Relacao entre preco e unidades vendidas (Dispersao)
plt.figure(figsize=(8,5))
plt.scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='#F6AE2D',
)   
plt.title("Relacao entre preco e unidades vendidas")
plt.xlabel("Preco por unidade")
plt.ylabel("Unidades vendidas")
plt.grid(True)
plt.show()

# 4 - Grafico 4 - Quantidades de unidades vendidas ao longo do tempo (Linha)
#Convertendo a coluna "Data" para o tipo datetime
df['DataPedido'] = pd.to_datetime(df['DataPedido'])

plt.figure(figsize=(10, 6))
df.groupby('DataPedido')['Unidades'].sum().plot(kind='line', marker='o', color='#4ECDC4')
plt.title('Quantidade de unidades vendidas ao longo do tempo')
plt.xlabel('Data do Pedido')
plt.ylabel('Unidades Vendidas')
plt.grid(True)
plt.show()

# 5 - Grafico 5 - Quantidade de unidades vendidas por Estado em cada regiao (Barras empilhadas)
pivot = df.pivot_table(
    index='Estado',
    columns='Regiao',
    values='Unidades',
    aggfunc='sum',
    fill_value=0
)
plt.figure(figsize=(8, 5))
pivot.plot(kind='bar', stacked=True)
plt.title('Quantidade de unidades vendidas por Estado em cada regiao')
plt.xlabel('Estado')
plt.ylabel('Total de Unidades Vendidas')
plt.xticks(rotation=45)
plt.legend(title='Regiao', loc='upper left', bbox_to_anchor=(1.05, 1))

plt.show()

