# Vamos estudar o for 

moviesList = ["Titanic", "The GodFather", "Inception","Jurassic Park"]

# 1 - Interar valores de uma lista

for movie in moviesList:
    print(movie)

# 2 - Quando o loop for atendido, o loop sera encerrado
for movie in moviesList:
    if movie == "Inception":
        break
    print(movie)

# 3 - Quando a condicao foe atendida, o loop vai para a proxima interacao
for movie in moviesList:
    if movie == "Inception":
        continue
    print(movie)

# 4 - Avaliacao do filme 
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliacoes deseja fazer:\n "))

total = 0
for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Media de avaliacao do filme {movieName} e : {average:.2f}")