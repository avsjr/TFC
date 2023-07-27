import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Dados fornecidos
ano = [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021]
indice_aprovacao = [0.70, 0.74, 0.83, 0.87, 0.91, 0.92, 0.93, 0.95, 0.97]
saeb = [4.92, 5.14, 5.44, 5.53, 5.71, 5.54, 5.69, 5.65, 5.15]

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

print(forecast_data)
