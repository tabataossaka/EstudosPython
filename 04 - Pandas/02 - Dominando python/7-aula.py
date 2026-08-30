# Slice

movieName = "Top Gun"

# String[inicio:fim] - índice começa na posição 0 / íncie final - 1
# 1 - Buscar toda string a partir da primeira posição
print(movieName[:5]) 

# Dentro dos [ : ] você pode ir determinando o que você quer imprimir 

"""
string [inicio:fim:passo]
índice começa na posição 0 | índice final -1 
passo - determinao o incremento. POr padrão esse número é o 1.
"""

# 2 - Busca toda string de 2 em 2 caracteres
print(movieName[::2])

# 3 - Buscar toda a string nos índices impares
print(movieName[1::2])

# 4 - Inverter uma string de trás para frente 
print(movieName[::-1])