# Autor: Cristian Jorda Matei
# Data: 1/11/2025
# Crea una llista amb noms i ordena'ls alfabèticament

input = input("Introdueix noms separats per espais: ")
noms = [str(nom) for nom in input.split()]
noms.sort()

print(f"Els noms ordenats alfabeticament: {noms}")