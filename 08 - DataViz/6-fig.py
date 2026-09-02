import matplotlib.pyplot as plt
import numpy as np

# 1 - Dados ficticios para os graficos
x = np.arange(1, 6)
y1 = np.array([3, 5, 9, 7, 3])
y2 = np.array([1, 6, 2, 8, 4])

# 2 - Criando subplots
fig, ax = plt.subplots(2, figsize=(8,8))

# 3 - Grafico de barras no subplot superior
ax[0].bar(x, y1, color='#FFB6C1')
ax[0].set_title('Grafico de Barras')

#4 - Grafico de linhas no subplot inferior
ax[1].plot(x, y2, marker='o', linestyle='-', color='#CD5C5C')
ax[1].set_title('Grafico de Linhas')

# 5 - Ajusta espacamento entre subplots
#plt.tight_layout()

plt.show()