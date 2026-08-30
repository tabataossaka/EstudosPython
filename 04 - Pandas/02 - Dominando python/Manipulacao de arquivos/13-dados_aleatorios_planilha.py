import pandas as pd
import numpy as np

dados_aba1 = {
    "Id": [1, 2, 3, 4, 5],
    "Nome": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Idade": [25, 30, 35, 40, 45],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"]
    
}
dados_aba2 = {
    "Id": [6, 7, 8, 9, 10], 
    "Nome": ["Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Idade": [50, 55, 60, 65, 70],
    "Cidade": ["Fortaleza", "Salvador", "Recife", "Manaus", "Belém"]

}

dados_aba3 = {
    "Id": [11, 12, 13, 14, 15],
    "Nome": ["Karen", "Leo", "Mia", "Nina", "Oscar"],
    "Idade": [75, 80, 85, 90, 95],
    "Cidade": ["Goiânia", "Vitória", "João Pessoa", "Teresina", "Aracaju"]
}

daods_aba4 = {
    "Id": [16, 17, 18, 19, 20],
    "Nome": ["Paul", "Quinn", "Rita", "Steve", "Tina"],
    "Idade": [100, 105, 110, 115, 120   ],
    "Cidade": ["Cuiabá", "Campo Grande", "Macapá",  "Palmas", "Boa Vista"]
}

df_aba1 = pd.DataFrame(dados_aba1)
df_aba2 = pd.DataFrame(dados_aba2)
df_aba3 = pd.DataFrame(dados_aba3)
df_aba4 = pd.DataFrame(daods_aba4)

caminho_arquivo = "dados_clientes.xlsx"

with pd.ExcelWriter(caminho_arquivo, engine='openpyxl') as writer:
    df_aba1.to_excel(writer, sheet_name='Clientes_1', index=False)
    df_aba2.to_excel(writer, sheet_name='Clientes_2', index=False)
    df_aba3.to_excel(writer, sheet_name='Clientes_3', index=False)
    df_aba4.to_excel(writer, sheet_name='Clientes_4', index=False)

print()