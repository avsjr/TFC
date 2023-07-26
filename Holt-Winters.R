# Instalando a biblioteca forecast
install.packages("forecast")

# Carregando a biblioteca forecast
library(forecast)

# Dados fornecidos
ano <- c(2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021)
indice_aprovacao <- c(0.70, 0.74, 0.83, 0.87, 0.91, 0.92, 0.93, 0.95, 0.97)
saebe <- c(4.92, 5.14, 5.44, 5.53, 5.71, 5.54, 5.69, 5.65, 5.15)

# Criando um data frame com os dados
data <- data.frame(Ano = ano, Indice_Aprovacao = indice_aprovacao, SAEBE = saebe)

# Ajuste do modelo de suavização exponencial simples para "Indice Aprovação (P)"
model_aprovacao <- ets(data$Indice_Aprovacao, model = "ANN")

# Ajuste do modelo de suavização exponencial simples para "SAEBE (N)"
model_saebe <- ets(data$SAEBE, model = "ANN")

# Previsões para 2023 e 2025 para "Indice Aprovação (P)"
future_years_aprovacao <- c(2023, 2025)
forecast_aprovacao <- forecast(model_aprovacao, h = length(future_years_aprovacao))

# Previsões para 2023 e 2025 para "SAEBE (N)"
future_years_saebe <- c(2023, 2025)
forecast_saebe <- forecast(model_saebe, h = length(future_years_saebe))

# Criação do data frame com as previsões
future_data <- data.frame(Ano = future_years_aprovacao, Indice_Aprovacao = forecast_aprovacao$mean,
                          SAEBE = forecast_saebe$mean)

# Concatenando os dados históricos com as previsões
forecast_data <- rbind(data, future_data)

# Plot dos resultados
plot(forecast_data$Ano, forecast_data$Indice_Aprovacao, type = "o", pch = 16, col = "blue",
     xlab = "Ano", ylab = "Indice Aprovação (P)", main = "Previsões para Índice Aprovação (P) e SAEBE (N) em 2023 e 2025",
     ylim = c(0, max(forecast_data$Indice_Aprovacao, forecast_data$SAEBE) + 0.1))
lines(forecast_data$Ano, forecast_data$SAEBE, type = "o", pch = 16, col = "orange")
legend("bottomright", legend = c("Indice Aprovação (P)", "SAEBE (N)"), col = c("blue", "orange"), pch = 16)
grid()
