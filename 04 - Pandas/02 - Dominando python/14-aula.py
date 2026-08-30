# Dicionário dentro de dicionário 
import pprint

filmsDict = {
    "Inception":{
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "Interstellar":{
        "yearRelease": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"]
    },
    "Avatar":{
        "yearRelease": 2009,
        "imdbRating": 9.1,
        "genre": ["Sci-fi", "Action"]
    }

}
pp = pprint.PrettyPrinter(depth=4)  # melhora forma de mostar o dado, facilitando a leitura
pp.pprint(filmsDict)

# 1 - Busca informação dentro de um dicionário aninhado
print(filmsDict["Interstellar"]["genre"])

# 2 - Adicionar novo item 
filmsDict["Inception"]["director"] = "Christopher"
print(filmsDict["Inception"])

# 3 - excluir um dicionário
del filmsDict["Avatar"]
pp.pprint(filmsDict)


# Exercício do CURSO 
"""
Escreva um programa que:
Leia o nome de três produtos e seus respectivos preços.
Armazene os dados em um dicionário, onde a chave é o nome do produto e o valor é o preço (float).

Imprima:
O dicionário completo.
O produto mais caro.
A média dos preços.
"""

prod1 = input()
prec1 = float(input())
prod2 = input()
prec2 = float(input())
prod3 = input()
prec3 = float(input())

listaDict = {
    prod1: prec1, 
    prod2: prec2,
    prod3: prec3
    
}

produto_mais_caro  = max(listaDict, key=listaDict.get)
media = sum(listaDict.values())/ len(listaDict)

print(listaDict)
print(produto_mais_caro )
print(round(media, 2))