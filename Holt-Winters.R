install.packages("forecast")

library(forecast)

ano <- c(2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019)
indice_aprovacao <- c(0.70, 0.74, 0.83, 0.87, 0.91, 0.92, 0.93, 0.95)

serie_temporal <- ts(indice_aprovacao, start = min(ano), frequency = 1)

modelo_hw <- forecast::hw(serie_temporal, seasonal = "additive")

print(modelo_hw)

previsao <- forecast::forecast(modelo_hw, h = 3)
print(previsao)
