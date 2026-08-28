# Concatemnação

name = input ("Digite o nome do filme:\n")
yearLunch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme: \n"))

#Alternativa 1
# print("Dados do Filme")
# print("===========")
# print("Nome do Filme:", name)
# print("Ano de Lançamento", yearLunch)
# print("Nota do Filme:", noteMovie)

#Alternativa 2

print("Nome do Filme:", name, "\nAno de Lançamento", yearLunch, "\nNota do Filme:", noteMovie)

# Alternativa 3

print(f"Nome do jogo? {name}\n"
        f"Ano de Lançamento: {yearLunch}\n"
        f"Nota do filme? {noteMovie}\n"
      )