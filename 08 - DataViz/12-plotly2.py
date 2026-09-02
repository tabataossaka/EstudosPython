import seaborn as sns
import plotly.express as px

#print(sns.get_dataset_names())

# 1- Carregando o dataset de diamonds do seaborn
data = sns.load_dataset('diamonds')
print(data)

# 2 - Criando o gráfico de dispersão interativo usando plotly
fig = px.scatter(
    data, 
    x='carat', 
    y='price', 
    color='cut', 
    size='depth', 
    hover_data=['x', 'y'],
    title='Dispersão do Preço dos Diamantes por Quilate e Corte'
)

# 3 - Exibindo o gráfico
fig.show()