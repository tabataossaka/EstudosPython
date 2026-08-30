name = input("Digite seu nome: ")

"""
Arquivos - Modo de Operação:

1 -> Modo W - write
2 -> Modo A - append
3 -> Modo R - read

"""

#Implementação 1
#file = open("nomes.txt", "a", encoding="utf-8") #Abre o arquivo no modo escrita
#file.write(f"{name}\n") #Escreve o nome no arquivo
#file.close() #Fecha o arquivo

# Implementacao 2
with open("nomes.txt", "a", encoding="utf-8") as file: #Abre o arquivo no modo escrita
    file.write(f"{name}\n") #Escreve o nome no arquivo

