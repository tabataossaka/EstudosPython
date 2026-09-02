import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# 1 - Criando dados ficticios 
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'Stock_A': [100 + i for i in range(100)],
    'Stock_B': [100 - i for i in range(100)],
    'Stock_C': [100 + (i * 0.5) for i in range(100)]
}

df = pd.DataFrame(data)
print(df)

# 2 - Criando o gráfico de linhas interativo usando plotly
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Stock_A'], 
    mode='lines',
    name='Stock A'
))
fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Stock_B'], 
    mode='lines',
    name='Stock B'
))
fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Stock_C'], 
    mode='lines',
    name='Stock C'
))
# 3 - Layout do gráfico
fig.update_layout(
    title='Preços das Ações ao Longo do Tempo',
    xaxis_title='Data',
    yaxis_title='Preço',
    hovermode='x'
)
# 4 - Exibindo o gráfico
fig.show()