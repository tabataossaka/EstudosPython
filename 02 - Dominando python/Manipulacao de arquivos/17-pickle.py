""""
pickle é um módulo do Python usado para salvar objetos Python em arquivos e depois recuperá-los exatamente como estavam.

Uma forma simples de pensar:

JSON → bom para compartilhar dados entre sistemas.
Pickle → bom para salvar objetos Python para usar novamente no Python.
"""

import pickle

class Cliente:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def __str__(self):
        return f"{self.nome} {self.idade} anos - {self.cidade}"

clientes = [
    Cliente("Ana", 25, "Sao Paulo"),
    Cliente("Carlos", 30, "Rio de Janeiro"),
    Cliente("Fernanda", 22, "Curitiba")    
]

# Salvar lista de clientes em arquivo pickle
with open("clientes.pkl", "wb") as file:
    pickle.dump(clientes, file)


# Adicionar cliente 
novo_cliente = Cliente("Marcos", 28, "Porto Alegre")
clientes.append(novo_cliente)

with open("clientes.pkl", "wb") as file:
    pickle.dump(clientes, file)

# Carregando os dados do arquivo pickle
with open("clientes.pkl", "rb") as file:
    clientes_carregados = pickle.load(file)

for cliente in clientes_carregados:
    print(cliente)
