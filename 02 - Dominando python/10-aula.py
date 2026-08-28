# + Listas 

filmsList = ["Inception", "Sherek", "Avatar", 
             "Cread","Interstellar"]

# 1 - Tamanho da lista 
print(len(filmsList))

# 2 - recuperar um item da lista pelo índice
print(filmsList.index("Interstellar"))

# 3 - Adicionar item ao final da lista 
filmsList.append("Senhor dos aneis")
print(filmsList)

# 4 - Ordenar a lista 
filmsList.sort()
print(filmsList)

#  5 - Copiar os itens das listas para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Cread")
print(filmsCopy)

# 6 - Remove todos os itens da list 
filmsList.clear()
print(filmsList)
