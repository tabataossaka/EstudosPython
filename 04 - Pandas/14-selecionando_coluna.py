import streamlit as st
import pandas as pd

caminho_arquivo = "DataSet/compras.csv"

df_compras = pd.read_csv(caminho_arquivo, sep=";", decimal=",", index_col=0)

colunas = list(df_compras.columns)  # Faz essa lista para poder usar no streamlit
colunas_selecionadas = st.sidebar.multiselect("Selecione as colunas:", colunas, colunas)

#col1 = coluna 1 
col1, col2 = st.sidebar.columns(2)
col_filtro = col1.selectbox("Selecione a coluna",
                            [c for c in colunas if c not in ["id_compra"]])  #Aqui no filtro retira o id_compra, pois nao faz sentido filtrar pelo id
valor_filtro = col2.selectbox("Selecione o valor",
                              list(df_compras[col_filtro].unique()))

st_filtrar = col1.button("Filtrar")
st_limpar = col2.button("Limpar")

if st_filtrar:      # esse loc e de localizar - funcao do pandas
    st.dataframe(df_compras.loc[df_compras[col_filtro] == valor_filtro, colunas_selecionadas])
elif st_limpar:
    st.dataframe(df_compras[colunas_selecionadas])
else:
    st.dataframe(df_compras[colunas_selecionadas])
