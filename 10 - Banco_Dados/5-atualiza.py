import sqlite3

# 1 conectando BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - atualizando dados 
id = 2
cursor.execute(
    """
        UPDATE filmes SET nota = ?
        WHERE id = ?

    """,
    ("9.3", id)

)

conexao.commit()
print("Dados Atualizados")