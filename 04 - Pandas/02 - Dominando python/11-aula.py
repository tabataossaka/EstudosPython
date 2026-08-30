# Vamos estudar tuplas

filmsList = ("Inception", "Sherek", "Avatar", 
             "Cread","Interstellar")

print(type(filmsList))

# 1 - Buscar os dois primeiros itens da tupla
print(filmsList[0:2])

# 2 - Buscar o último item da tupla 
print(filmsList[-1])

# 3 - Buscar filmos até uma determinada posição 
print(filmsList[0:3])

# 4- Buscar filmes de uma posição em diante 
print(filmsList[2:])

# 5 - Recuperar um item da tupla pelo nome
print(filmsList.index("Avatar"))

