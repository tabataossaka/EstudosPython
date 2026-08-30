movieName = "Top Gun"
movieDescription = """ 
    Top Gun é um filme de aviação e aventura muito legal    
    """

print(movieName.upper())
print(movieName.lower())
print(movieName.capitalize())
print(movieName.title())
print(movieName.center(10, '-')) # retorna string centralizada com caractere de preenchimento
print(movieName.find("u")) # retorna posição de um determinado caracter 
print(movieName.find("o")) # Conta o caracter
print(movieName.replace("Top", "Matrix")) # Altera elemento pelo outro
print(movieName.split(','))