import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

# 1 - Gerando dados aleatorios
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

# 2 - Criando grafico de dispoersao
plt.figure(figsize=(8,5))
plt.scatter(x, y)
plt.title('Grafico de Dispersao com Dados Aleatorios')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)

plt.show()

# 3 - Criando grafico 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z)

ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')
ax.set_title('Grafico de dispersao 3D')

plt.show()


