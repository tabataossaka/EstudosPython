# Vamos aprender sobre a função Lambda
power =lambda num: num ** 2
print(power(5))

# Funcao que verifica se o numero e par
is_even = lambda x: x % 2 == 0

# Funcao que divide um  numero pelo outro
div_num = lambda x, y: x / y

# Funcao que inverte uma string
reverse = lambda s: s[::-1]

print(power(5))
print(is_even(27))
print(is_even(32))
print(div_num(10,2))
print(reverse("Javascript"))

# Funcionalidades relacionadas aos filmes

moviesList = ["Titanic", "The GodFather", "Inception", "Jurassic Park"]
ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "The GodFather": [9.5, 8.9, 8.0],
    "Inception": [8.0, 8.9, 9.2],
    "Jurassic Park": [8.8, 9.2, 8.5]

}
# funcao para calcular a media de avaliacoes de um filme 
average_rating = lambda moviesList: sum(ratings[moviesList]) / len(ratings[moviesList])


#Funcao que verifica se um filme esta na lista 
check_movie = lambda moviesList: moviesList in moviesList

#Funcao para recomendar um filme com base na avaliacao media
recomenda = lambda moviesList: f"Recomendo assistir {moviesList} com media de {average_rating(moviesList)}"

print(f"Media de avaliacoes do filme Titanic: {average_rating("Titanic"):.2f} ")
print(f"Inception esta na lista? {check_movie("Inception")}")
print(f"{recomenda("Titanic")}")