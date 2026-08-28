# Vamos aprender condições 
# Informações sobre o filme
"""
nome = input("Digite o nome do filme:\n")
yearRealese = int(input("Digite o ano de lançamento:\n"))
rating = float(input("Digite a nota de avaliação do filme:\n"))

# Verifica se o filme é recomendado 
if rating > 8 and yearRealese > 2015:
    print(f"O filtme {nome} é muito bom. Recomanedo assisti-lo.")
else:
    print(f"O filme {nome} ainda não atingiu uma boa nota ou é muito antigo.")
"""

num1 = float(input("Digite o primeiro numero:\n"))
num2 = float(input("Digite o segundo numero:\n"))

operation = input("Digite a operação a ser realizada: (+ - * /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisão por Zero")
        result = 0
else:
    print("Operação inválida")
    result = 0

print(f"Resultado da operação é: {result:.2f}")
