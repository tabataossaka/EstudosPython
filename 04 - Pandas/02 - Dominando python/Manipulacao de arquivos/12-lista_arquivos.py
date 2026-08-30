import glob, os, zipfile

# 1 - Diretório atual
print("Diretório atual:", os.getcwd())

# 2 - Listar todos os arquivos txt 
for file in glob.glob("*.txt"):
    print(file)

# 3 - Listar todos os arquivos csv
for file in glob.glob("*.csv"):
    print(file)

# 4 - Compactar arquivos txt em um arquivo zip
with zipfile.ZipFile("arquivos_txt.zip", "w") as zipf:
    for file in glob.glob("*.txt"):
        zipf.write(file)

# 5 - Compactar todos os arquivos em um arquivo zip
with zipfile.ZipFile("todos_arquivos.zip", "w") as zipf:
    for file in glob.glob("*.*"):
        zipf.write(file)