import matplotlib.pyplot as plt
import numpy as np

# 1 - Dados ficticios
pontuacoes = np.random.randint(50, 100, 100)

# 2 - Criando o histograma
plt.figure(figsize= (8,5))
plt.hist(
    pontuacoes,
    bins=10,
    color='#F08080',
    edgecolor='Black'
)

plt.xlabel('Pontuacao')
plt.ylabel('Frequencia')
plt.title('Distibuicao das pontuacoes do teste')

plt.show()