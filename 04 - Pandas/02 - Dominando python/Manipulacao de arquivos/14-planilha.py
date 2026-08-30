import pandas as pd

# 1 - Importando dados de um arquivo Excel
tb_clientes = pd.read_excel("dados_clientes.xlsx")
print(tb_clientes)
print(type(tb_clientes))

# 2 - Adicionar coluna de index
tb_clientes = pd.read_excel("dados_clientes.xlsx", index_col=0)
print(tb_clientes)

# 3 - Importando colunas específicas de um arquivo Excel
tb_clientes = pd.read_excel("dados_clientes.xlsx", usecols=[1,2])
print(tb_clientes)

# 4 - exportando dados para um arquivo Excel
tb_clientes_aba1 = pd.read_excel("dados_clientes.xlsx", sheet_name="Clientes_1")
tb_clientes_aba2 = pd.read_excel("dados_clientes.xlsx", sheet_name="Clientes_2")

with pd.ExcelWriter("dados_clientes_exportados.xlsx", engine="openpyxl") as nova_planilha:
    tb_clientes_aba1.to_excel(nova_planilha, sheet_name="Clientes_1", index=False)
    tb_clientes_aba2.to_excel(nova_planilha, sheet_name="Clientes_2", index=False)