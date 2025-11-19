# Autor: Cristian Jorda Matei
# Data: 17/11/2025
# Afegir continguts: Afegeix una línia nova a un fitxer existent (sortida.txt) sense esborrar el que ja hi ha.

with open("sortida.txt", "a", encoding="utf-8") as fitxer:
    fitxer.write("Línia afegida.\n")

print("Línia afegida correctament!")