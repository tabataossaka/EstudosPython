import json

dados = {
    "Clientes": [
        {"Id": 1, "Nome": "Alice", "Idade": 25, "Cidade": "São Paulo"},
        {"Id": 2, "Nome": "Bob", "Idade": 30, "Cidade": "Rio de Janeiro"},
        {"Id": 3, "Nome": "Charlie", "Idade": 35, "Cidade": "Brasília"},
        {"Id": 4, "Nome": "David", "Idade": 40, "Cidade": "Belo Horizonte"},
    ]
}

caminho_arquivo = "dados_clientes.json"

# 1 - Escrevendo dados no arquivo JSON
with open(caminho_arquivo, "w", encoding="utf-8") as file:
    json.dump(dados, file, indent=4)

# 2 - Lendo dados do arquivo JSON
with open(caminho_arquivo, "r", encoding="utf-8") as file:
    dados_lidos = json.load(file)

# 3 - Alterando a idade do David
for cliente in dados_lidos["Clientes"]:
    if cliente["Nome"] == "David":
        cliente["Idade"] = 38

# 4 - Adicionando novo cliente
novo_cliente = {
    "Id": 5,
    "Nome": "Samilly",
    "Idade": 28,
    "Cidade": "Campinas"
}

dados_lidos["Clientes"].append(novo_cliente)

# 5 - Salvando as alterações
with open(caminho_arquivo, "w", encoding="utf-8") as file:
    json.dump(dados_lidos, file, indent=4, ensure_ascii=False)