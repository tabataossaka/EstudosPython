import csv

cursos = []

with open("cursos.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursos.append({
            "languege": row["language"],
            "category": row["category"]
        })

print(cursos)