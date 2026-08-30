"""
Arquivos - Modo de Operação:

1 -> Modo W - write
2 -> Modo A - append
3 -> Modo R - read

"""
with open("nomes.txt", "r", encoding="utf-8") as file: #Abre o arquivo no modo leitura
    #print(file.read()) #Lê o conteúdo do arquivo e imprime na tela
    for line in file:
        print(f"Oi, {line.rstrip()}") #Lê o conteúdo do arquivo linha por linha e imprime na tela


