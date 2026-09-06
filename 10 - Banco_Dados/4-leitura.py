import sqlite3

# 1 - conectando no banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Leitura de dados
dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())