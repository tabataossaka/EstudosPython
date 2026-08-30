from decorator import my_decorator, uppercase_decorator, split_string_decorator

@my_decorator
def my_function():
    print("Dentro da função")

my_function()

def texto():
    return "Olá, mundo!"
print(texto())

@split_string_decorator
@uppercase_decorator
def example():
    return "Aprendendo Python é divertido!"
print(example())