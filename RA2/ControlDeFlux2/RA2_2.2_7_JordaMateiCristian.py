# Autor: Cristian Jorda Matei
# Data: 08/10/2025
# Descripció: Mostra els primers 10 termes de la seqüència de Fibonacci.

text = input("Introdueix una cadena de text: ")

invertit = ""
for car in text:
    invertit = car + invertit
print("La cadena invertida és:", invertit)
