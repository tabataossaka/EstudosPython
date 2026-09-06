import sqlite3

# 1 conectando BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Exclui dados 
id = (1, 2)
cursor.execute(
    """
        DELETE FROM filmes
        WHERE ID in (?, ?)
    """,
    id
)

conexao.commit()
print("Dados excluidos com sucesso!")