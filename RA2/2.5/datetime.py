# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Programa que usa el mòdul datetime per mostrar dates i calcular dies.

from datetime import datetime

# Mostrar data i hora actual
ara = datetime.now()
data_formatada = ara.strftime("%d/%m/%Y %H:%M")
print("Data i hora actual:", data_formatada)

# Calcular dies fins Nadal
nadal = datetime(2025, 12, 25)
diferencia = nadal - ara
dies = diferencia.days
print("Dies fins a Nadal:", dies)