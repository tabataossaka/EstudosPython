# Vamos aprender While

moviesList = ["Titanic", "The GodFather", "Inception","Jurassic Park"]

# 1 - Interando valores de uma lista de filme usando while

index = 0
while index < len(moviesList):
    print(moviesList[index])
    index += 1

# 2 - Quando a condicao for arendida, o loop sera encerrado
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        break
    print(moviesList[index])
    index += 1

# 3 - Quando a condicao for atendida, o loop vai para a proxima interacao

index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        index += 1 
        continue
    print(moviesList[index])
    index += 1

# 4 - Avaliacao do filme com while

movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliacoes deseja fazer:\n "))

total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme:\n"))
    total += note
    count += 1

if movieRating > 0:
    average = total / movieRating
else:
    average = 0

print(f"Media de avaliacao do filme {movieName} e : {average:.2f}")