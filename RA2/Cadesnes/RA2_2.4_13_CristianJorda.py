# Autor: Cristian Jorda Matei
# Data: 1/11/2025
# Escriu una funció que sumi tots els nombres d'una llista.

import random

numeros = [random.randint(1, 100) for i in range(5)]

print(f"La llista es: {numeros}")

print(f"La suma es: {sum(numeros)}")