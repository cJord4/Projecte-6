# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció filtra_parells(llista) que:
# - Rebi una llista de nombres.
# - Retorni una nova llista només amb els nombres parells.

def filtra_parells(llista):
    parells = []
    for num in llista:
        if num % 2 == 0:
            parells.append(num)
    return parells

# Input esperat: una llista de nombres
entrada = input("Introdueix nombres separats per espais: ")
nombres = [int(x) for x in entrada.split()]
print(filtra_parells(nombres))