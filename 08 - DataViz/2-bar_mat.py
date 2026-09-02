import matplotlib.pyplot as plt

# 1 - Dados ficticios - Quantidade de Produtos vendidos por vendedor
vendedores = ['Joao', 'Maria', 'Pedro', 'Ana']
quantidade_vendida = [45, 60, 30, 55]

# 2 - criando o grafico de barra
plt.figure(figsize=(8,5)) 
plt.bar(
    vendedores,
    quantidade_vendida,
    color='#4682B4'
)
# 3 - Adicionando rotulos e titulos
plt.xlabel('Vendedores')
plt.ylabel('Quantidade Vendida')
plt.title('Quatidade de Produtos Vendidos por Vendedor')

# 4 - exibir o grafico
plt.show()

