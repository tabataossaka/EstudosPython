cursos = []

with open("cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        course, area = line.rstrip().split(",")
        curso = {}
        curso["languege"] = course
        curso["category"] = area
        cursos.append(curso)

for curso in cursos:
    print(f"{curso['languege']} -> {curso['category']}") #Note que usa aspas simples para acessar os valores do dicionário, pois as chaves são strings.
    