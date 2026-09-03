import plotly.express as px

from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores


grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False},
    title='Receita por Estado'
)


grafico_rec_mensal = px.line(
    df_rec_mensal,
    x='Mês',
    y='Preço',
    markers=True,
    template='seaborn',
    range_y=(0, df_rec_mensal['Preço'].max()),
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal'
)

grafico_rec_mensal.update_layout(
    yaxis_title='Receita'
)


grafico_rec_estado = px.bar(
    df_rec_estado.head(5),
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='Top 5 - Receita por Estado'
)


grafico_rec_categoria = px.bar(
    df_rec_categoria.head(5),
    x='Categoria do Produto',
    y='Preço',
    text_auto=True,
    title='Top 5 - Receita por Categoria'
)

df_top_vendedores = (
    df_vendedores
    .sort_values('sum', ascending=False)
    .head(5)
    .reset_index()
)

grafico_rec_vendedores = px.bar(
    df_top_vendedores,
    x='sum',
    y='Vendedor',
    text_auto=True,
    title='Top 5 - Vendedores por receita'
)

df_top_vendedores = (
    df_vendedores
    .sort_values('count', ascending=False)
    .head(5)
    .reset_index()
)

grafico_vendas_vendedores = px.bar(
    df_top_vendedores,
    x='count',
    y='Vendedor',
    text_auto=True,
    title='Top 5 - Vendedores por vendas'
)