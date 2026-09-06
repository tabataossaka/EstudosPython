from conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ('The last of us', 2020, 9.8),
    ('Spider Man', 2020, 9.6)
]

for game in games:
    cursor_obj.execute(
        """
            INSERT INTO games(name, year, score)
            VALUES (%s, %s, %s)
        """,
        game
    )

conn.commit()

print("Dados inseridos com sucesso!")

conn.close()