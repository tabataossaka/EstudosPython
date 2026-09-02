import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 1 - Dados ficticios de precos de acoes para diferentes empresas ao longo do trimeste
empresas = ['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D']
trimestres = ['T1', 'T2', 'T3', 'T4']

dados = np.random.rand(4,4) * 100   # valores aleatorios entre 0 e 100 para simular os precos das acoes

# 2 - Criando o DataFrame com os dados
df = pd.DataFrame(
        dados, 
        index=empresas, 
        columns=trimestres)

print(df)

# 3 - Criando o heatmap usando seaborn
plt.figure(figsize=(8,6))
sns.heatmap(df, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap de Precos de Acoes por Empresa e Trimestre')
plt.xlabel('Trimestres')
plt.ylabel('Empresas')
plt.show()