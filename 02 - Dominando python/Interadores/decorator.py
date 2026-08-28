from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Antes da função")
        resultado = func(*args, **kwargs)
        print("Depois da função")
        return resultado
    return wrapper

def uppercase_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado.upper()
    return wrapper

def split_string_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado.split()
    return wrapper