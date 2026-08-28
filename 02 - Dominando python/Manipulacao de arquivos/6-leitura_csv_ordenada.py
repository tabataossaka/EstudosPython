cursos = []

with open("cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        course, area = line.rstrip().split(",")
        cursos.append(f"{course} -> {area}")

for curso in sorted(cursos):
    print(curso)