# Autor: Cristian Jordà
# Data: 20/09/2023
# versió: 1.0
#
# Descripció: 
# Especificacions de entrada:

any_naixement = int(input("Introdueix l'any de naixement: "))
edat = 2025 - any_naixement
if edat >= 18:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")