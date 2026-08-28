# Parametros adicionais Argumentos e Kwargs

""" 
* args - Utilizamos ele quando nao temos 
certeza de quantos argumentos queremos ter numa funcao.
-Os argumentos sao passados como uma tupla

**Kwags - Alem dos valores podemos passar tambem as respectivas chaves para cada argumento.
- Os argumentos sao passados como um dicionario
"""

# 1 - Soma de numeros 
def sum(*num):   # O * e o arg, pois pode passar varios parametros
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma e : {sum_total}")

sum(10)
sum(10, 5, 7)

# 2 - Apresenta cao de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Lista de Cursos:")

presentation(name= "Python", category="Backend", Level="Iniciante")
presentation(name= "Visao Computacional", category="IA", Level="Avancado")
presentation(name= "Dashboard com dash", category="Data Science", Level="Intermediario")