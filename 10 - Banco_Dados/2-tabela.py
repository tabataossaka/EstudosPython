import sqlite3

#1 - conectando no banco de dados
conexao = sqlite3.connect('titulo.db')

#2 - Criando o cursor
cursor = conexao.cursor()

#3 - Criando a tabela de filme
cursor.execute(
    """
        CREATE TABLE filmes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXTO NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
)

# 4 - Fecha a conexao 
conexao.close()
print("Tabela foi criada")