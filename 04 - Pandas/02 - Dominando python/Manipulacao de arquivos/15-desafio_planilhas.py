import pandas as pd
import os
from pathlib import Path

# 1 - Importando dados de um arquivo Excel todas as abas
tb_clientes_dict = pd.read_excel("dados_clientes.xlsx", sheet_name=None)
print(tb_clientes_dict)
print(type(tb_clientes_dict))

# 2 - Criand uma pasta 'planilhas_separadas' se n'ao existir 
pasta_saida = "planilhas_separadas"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# 3 - Separando as planilhas
for nome_aba, tabela in tb_clientes_dict.items():
    caminho_arquivo = os.path.join(pasta_saida, f"{nome_aba}.xlsx")
    tabela.to_excel(caminho_arquivo, index=False)

# 4 - Criando a pasta de 'planilhas_consilidades' 
pasta_consolidadas = "planilhas_consolidadas"
if not os.path.exists(pasta_consolidadas):
    os.makedirs(pasta_consolidadas)

# 5 - Caminho para o arquivo consolidado
caminho_arquivo_consolidado = os.path.join(pasta_consolidadas, "dados_clientes_consolidados.xlsx")

# 6 - Concatenando as planilhas em um único DataFrame
with pd.ExcelWriter(caminho_arquivo_consolidado, engine="openpyxl") as consolidada:
    for arquivo in Path(pasta_saida).glob("*.xlsx"):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidada, sheet_name=arquivo.stem, index=False)
