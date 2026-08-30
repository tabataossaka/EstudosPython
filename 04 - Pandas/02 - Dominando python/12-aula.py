# Vamos estudar Set

filmSet = {"Inception", "Sherek", "Avatar", 
             "Cread","Interstellar"}

# 1 - Buscar tamanho do set
print(len(filmSet))

# 2 - True e 1 são considerados o mesmo valor
exemploSet = {"Inception", True, 1, 8.6}

# 3 - Adicionar item de outro set
filmSet.update(exemploSet)
print(filmSet)

# 4 - remover um iten no Set
filmSet.remove(True)
filmSet.remove(8.6)
print(filmSet)