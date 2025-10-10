# Autor: Cristian Jorda Matei
# Data: 08/10/2025
# Descripció: Demana a l'usuari una frase i compta quantes vocals conté.

frase = input("Introdueix una frase: ")

vocals = "aeiouAEIOU"
comptador = 0

for lletra in frase:
    if lletra in vocals:
        comptador += 1

print("La frase conté", comptador, "vocals.")
