import csv

linguagem = input("Digite a linguagem: \n")
categoria = input("Digite a categoria: \n")

with open("cursos.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([linguagem, categoria])