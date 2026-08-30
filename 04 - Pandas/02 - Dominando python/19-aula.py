# Vamos aprender Funcoes 

# 1 - Funcao para imprimir uma mensagem
def welcome():
    print("Bem vindo ao sistema de filmes!")

# for i in range (10):
#       welcome()

# 2 - Funcao para calcular a media de notas
def calculate_average():
    num_rating = int(input("Digite quantas avaliacoes deseja fazer pro filme:\n"))
    total = 0
    for i in range (num_rating):
        note = float(input("Digite a nota para o filme:\n"))
        total += note

    if num_rating > 0:
        average = total / num_rating
    else:
        average = 0

    return average

print(f"A media de avaliacoes e: {calculate_average():.2f}")

# 3 - Funcao para cadastrar um filme

def create_movie():
    name = input ("Digite o nome do filme:\n")
    yearLunch = int(input("Digite o ano de lançamento do filme:\n"))
    moviePrice = float(input("Digite o preco do filme:\n"))
    noteMovie = float(input("Digite a nota do filme: \n"))
    print(f"{name} ({yearLunch}) - R$ {moviePrice:.2f}")

create_movie()