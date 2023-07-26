import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Ano': [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019],
    'Indice_Aprovacao': [0.70, 0.74, 0.83, 0.87, 0.91, 0.92, 0.93, 0.95]
}

dados = pd.DataFrame(data)

plt.plot(dados['Ano'], dados['Indice_Aprovacao'], marker='o', linestyle='-')
plt.xlabel('Ano')
plt.ylabel('Índice de Aprovação (P)')
plt.title('Evolução do Índice de Aprovação ao longo dos anos')
plt.grid(True)
plt.show()
