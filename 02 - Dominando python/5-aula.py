# Utilizando Operadores

num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

# Operadores aritiméticos

sum= num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Soma:{sum}")
print(f"subtração: {sub}")
print(f"Divisão: {div}")
print(f"Multiplicação {mult}")
print(f"Resto da divisão: {mod}")
print(f"Exponencial {exp}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal =  num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2


print(f"Os números {num1} e {num2} são iguais {equal}")
print(f"O número {num1} é maior ou igual a {num2}?  são iguais? {bigger_equal}")

