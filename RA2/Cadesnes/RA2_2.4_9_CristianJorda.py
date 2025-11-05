# Autor: Cristian Jorda Matei
# Data: 30/10/2025
# Crea un programa que divideixi una frase en paraules i les mostri una per una.

frase = input("Introdueix una frase: ")

paraules = frase.split()

for i in paraules:
    print(i)
