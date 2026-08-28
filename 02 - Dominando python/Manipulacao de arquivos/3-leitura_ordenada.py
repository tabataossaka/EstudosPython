names = []

with open("nomes.txt", "r", encoding="utf-8") as file: #Abre o arquivo no modo leitura
    for line in file:
        names.append(line.rstrip()) #Lê o conteúdo do arquivo linha por linha e adiciona na list

for name in sorted(names, reverse = False): #Ordena a lista em ordem alfabética 
    print(f"Oi, {name}") #Imprime os nomes em ordem alfabética


