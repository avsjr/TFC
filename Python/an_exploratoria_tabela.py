import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Ano': [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023, 2025],
    'Indice Aprovação (P)': [0.70, 0.74, 0.83, 0.87, 0.91, 0.92, 0.93, 0.95, 0.97, 0.98, 1.00],
    'SAEB (N)': [4.92, 5.14, 5.44, 5.53, 5.71, 5.54, 5.69, 5.65, 5.15, 5.00, 4.74],
    'IDEB': [3.4, 3.8, 4.5, 4.8, 5.2, 5.1, 5.3, 5.3, 5.0, 4.9, 4.7]
}

df = pd.DataFrame(data)

# Criando uma tabela com a biblioteca pandas
plt.figure(figsize=(8, 4))
plt.axis('off')  # Removendo eixos

table = plt.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', cellColours=[['lightgray']*len(df.columns)]*len(df.index))

# Estilizando a tabela
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)  # Ajustando o tamanho da tabela

# Salvando a tabela em uma imagem
plt.savefig('tabela_dados.png', bbox_inches='tight', pad_inches=0.5)

plt.show()