import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Dados fornecidos
ano = [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021]
indice_aprovacao = [0.70, 0.74, 0.83, 0.87, 0.91, 0.92, 0.93, 0.95, 0.97]
saeb = [4.92, 5.14, 5.44, 5.53, 5.71, 5.54, 5.69, 5.65, 5.15]
ideb = [3.4, 3.8, 4.5, 4.8, 5.2, 5.1, 5.3, 5.3, 5.0, 4.9, 4.7]

# Definição de constantes
IN_AP = 'Indice Aprovação'

# Criação de um DataFrame com os dados
data = pd.DataFrame({'Ano': ano, IN_AP: indice_aprovacao, 'SAEB': saeb})

# Ajuste do modelo de Holt-Winters aditivo para "Indice Aprovação (P)"
model_aprovacao = ExponentialSmoothing(data[IN_AP], seasonal_periods=2, trend='add', seasonal='add')
fit_model_aprovacao = model_aprovacao.fit()

# Ajuste do modelo de Holt-Winters aditivo para "SAEB (N)"
model_saeb = ExponentialSmoothing(data['SAEB'], seasonal_periods=2, trend='add', seasonal='add')
fit_model_saeb = model_saeb.fit()

# Previsões para 2023 e 2025 para "Indice Aprovação (P)"
future_years_aprovacao = [2023, 2025]
forecast_aprovacao = fit_model_aprovacao.forecast(steps=len(future_years_aprovacao))

# Previsões para 2023 e 2025 para "SAEB (N)"
future_years_saeb = [2023, 2025]
forecast_saeb = fit_model_saeb.forecast(steps=len(future_years_saeb))

# Criação do DataFrame com as previsões
future_data = pd.DataFrame({'Ano': future_years_aprovacao, IN_AP: forecast_aprovacao,
                            'SAEB': forecast_saeb})

# Concatenando os dados históricos com as previsões
forecast_data = pd.concat([data, future_data])

# Plot dos resultados
plt.figure(figsize=(10, 6))
plt.plot(forecast_data['Ano'], forecast_data[IN_AP], marker='o', label='Indice Aprovação (P)')
plt.plot(forecast_data['Ano'], forecast_data['SAEB'], marker='o', label='SAEB (N)')
plt.plot(ano + [2023, 2025], ideb, marker='o', label='IDEB', linestyle='--', color='red')
plt.xlabel('Ano')
plt.ylabel('Valores')
plt.title('Previsões para Indice Aprovação (P), SAEB (N) e IDEB em 2023 e 2025')
plt.legend()
plt.grid(True)

# Adicionando os valores no gráfico com deslocamento vertical
offset = 0.1
for x, y in zip(forecast_data['Ano'], forecast_data[IN_AP]):
    plt.text(x, y + offset, f'{y:.2f}', ha='right', va='bottom')
for x, y in zip(forecast_data['Ano'], forecast_data['SAEB']):
    plt.text(x, y + offset, f'{y:.2f}', ha='right', va='bottom')
for x, y in zip(ano + [2023, 2025], ideb):
    plt.text(x, y - offset, f'{y:.1f}', ha='right', va='top')  # Alterado va para 'top' para colocar abaixo dos pontos
    
plt.show()
