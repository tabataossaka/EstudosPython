import matplotlib.pyplot as plt

# 1 - Criar dados ficticios - Vendas ao longo dos meses
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
vendas = [150, 200, 180, 300, 250, 400]

# 2 - Criandoo o grafico de linha 
plt.figure(figsize=(8,5))
plt.plot(
    meses,
    vendas,
    marker='o',
    linestyle='-',
    color='Blue',
    label='Vendas',

)
# 3 - Adicionando rotulos e titulo ao grafico
plt.xlabel('Mes')
plt.ylabel('Vendas')
plt.title('Vendas ao londo dos meses')
plt.legend()
plt.grid(True)

# 4 - Excibindo o grafico 
plt.show()

