import streamlit as st
import pandas as pd

caminho_compras = "DataSet/compras.csv"

df_compras = pd.read_csv(caminho_compras, sep=";", decimal=",")

st.dataframe(df_compras)

"""
- Comando para rodar
    cd ".\04 - Pandas"
    python -m streamlit run . \13-visualization.py

"""
