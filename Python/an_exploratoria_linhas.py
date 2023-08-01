import pandas as pd
import matplotlib.pyplot as plt

IR = 'Indicador de Rendimento (P)'
SAEB = 'SAEB (N)'
data = {
    'Ano': [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023, 2025],
    IR: [0.70, 0.74, 0.83, 0.87, 0.91, 0.92, 0.93, 0.95, 0.97, 0.98, 1.00],
    SAEB: [4.92, 5.14, 5.44, 5.53, 5.71, 5.54, 5.69, 5.65, 5.15, 5.00, 4.74],
    'IDEB': [3.4, 3.8, 4.5, 4.8, 5.2, 5.1, 5.3, 5.3, 5.0, 4.9, 4.7]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

plt.plot(df['Ano'], df[IR], marker='o', label=IR)
plt.plot(df['Ano'], df[SAEB], marker='o', label=SAEB)
plt.plot(df['Ano'], df['IDEB'], marker='o', label='IDEB')

# Adicionando os valores dos pontos das linhas acima ou abaixo das respectivas linhas
offset = 0.1
for col in [IR, SAEB, 'IDEB']:
    for x, y in zip(df['Ano'], df[col]):
        if col == 'IDEB':
            plt.text(x, y - offset, f'{y:.1f}', ha='right', va='top', color='red')
        else:
            plt.text(x, y + offset, f'{y:.2f}', ha='right', va='bottom', color='orange')

plt.xlabel('Ano')
plt.ylabel('Valores')
plt.title('Evolução do Indicador de Rendimento, SAEB e IDEB ao Longo dos Anos')
plt.legend()
plt.grid(True)

plt.show()
