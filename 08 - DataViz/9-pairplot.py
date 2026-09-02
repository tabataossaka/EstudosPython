import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 1 - Criando dados ficticios de um DataFrame
data = {
    'Preco': [20,25,30,18,22],
    'Quantidade': [100,150,200,80,120],
    'Receita': [2000,3750,6000,1440,2640]
}

df = pd.DataFrame(data)
print(df)

# 2 - Criando o pairplot usando seaborn
sns.set(style='ticks')
sns.pairplot(df, diag_kind='kde')
plt.suptitle('Relacoes entre preco, quantidade e receita', y=1.02)
plt.show()