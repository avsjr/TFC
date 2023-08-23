'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Ano': [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023, 2025],
    'Indicador de Rendimento (P)': [0.70, 0.74, 0.83, 0.87, 0.91, 0.92, 0.93, 0.95, 0.97, 0.98, 1.00],
    'SAEB (N)': [4.92, 5.14, 5.44, 5.53, 5.71, 5.54, 5.69, 5.65, 5.15, 5.00, 4.74],
    'IDEB': [3.4, 3.8, 4.5, 4.8, 5.2, 5.1, 5.3, 5.3, 5.0, 4.9, 4.7]
}

df = pd.DataFrame(data)

print(df)

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df, x='Indicador de Rendimento (P)', y='SAEB (N)', hue='IDEB', s=100)

plt.xlabel('Indicador de Rendimento (P)')
plt.ylabel('SAEB (N)')
plt.title('Correlações entre as Variáveis')
plt.legend(title='IDEB', loc='upper left', bbox_to_anchor=(1, 1))

plt.show()
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Ano': [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023, 2025],
    'Indicador de Rendimento (P)': [0.70, 0.74, 0.83, 0.87, 0.91, 0.92, 0.93, 0.95, 0.97, 0.98, 1.00],
    'SAEB (N)': [4.92, 5.14, 5.44, 5.53, 5.71, 5.54, 5.69, 5.65, 5.15, 5.00, 4.74],
    'IDEB': [3.4, 3.8, 4.5, 4.8, 5.2, 5.1, 5.3, 5.3, 5.0, 4.9, 4.7]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))

scatter = sns.scatterplot(data=df, x='Indicador de Rendimento (P)', y='SAEB (N)', hue='IDEB', s=100)

plt.xlabel('Indicador de Rendimento (P)')
plt.ylabel('SAEB (N)')
plt.title('Correlações entre as Variáveis')
plt.legend(title='IDEB', loc='upper left', bbox_to_anchor=(1, 1))

# Adicionando os anos nos pontos
for index, row in df.iterrows():
    scatter.annotate(str(int(row['Ano'])), (row['Indicador de Rendimento (P)'], row['SAEB (N)']), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()
