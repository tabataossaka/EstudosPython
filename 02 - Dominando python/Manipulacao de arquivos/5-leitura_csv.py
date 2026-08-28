with open("cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        # course, area = line.rstrip().split(",")
        # print(f"Curso: {course}, Área: {area}")
        linguagem, area = line.rstrip().split(",")
        print(f"{linguagem} -> {area}")

        