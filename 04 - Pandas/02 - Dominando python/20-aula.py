# Vamos aprender argumentos de uma funcao

# 1 - Funcao para imprimir um nome completo 
def full_name(first_name, last_name):
    print(f"Nome e: {first_name} {last_name}")

full_name("Fulano", "Santos")

# 2 - funcao para somar dois numeros 
def sum_number(a, b):
    return a + b

print(f"Soma e: {sum_number(10,50)}")

# 3 - Funcao com parametro default 
def address(country = "Brasil"):
    print(f"Eu moro em : {country}")

address()
address("Portugual")

# 4 - Funcao para avaliar filme 
def rate_movie(num_rating, movie_name):
    total = 0
    for i in range(num_rating):
        nota = float(input("Digite a nota do filme:\n"))
        total += nota

    if num_rating > 0:
        average = total / num_rating
    else:
        average = 0

    print(f"Media de avaliacao do filme: {movie_name} e : {average:.2f}")

rate_movie(2, "Sonic")
    