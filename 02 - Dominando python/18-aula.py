# Utilizando Lista Comprehension

# 1 - Listar valores de 0 a 10 que sejam menores do que 4
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# 2 - Filmes que possuem a letra 'e' no titulo 
moviesList = ["Titanic", "The GodFather", "Inception","Jurassic Park"]
moviesWithE = [movie for movie in moviesList if 'e' in movie.lower() ]
print(moviesWithE)

# 3 - Filmes que eu assisti 
moviesWatched = [movie for movie in moviesList if movie != "The GodFather"]
print(moviesWatched)

# 4 - Encontrando um filme pelo nome

while True:
    searchName = input("Digite o nome do filme para busca:\n")
    if searchName.lower() == "sair":
        print("Programa encerrado")
        break

    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme encontrado com o nome: {searchName}:")
        for foundMovies in foundMovies:
            print(foundMovies)

    else:
        print(f"Nenhum filme foi encontrado com o nome {searchName}. Tente novamente!")
