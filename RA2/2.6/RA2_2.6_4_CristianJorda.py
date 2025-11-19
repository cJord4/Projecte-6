# Autor: Cristian Jorda Matei
# Data: 17/11/2025
# Comptar línies: Llegeix un fitxer i mostra quantes línies té.

print("EXERCICI 1: Comptar línies")
print("-" * 40)

with open("sortida.txt", "r", encoding="utf-8") as fitxer:
    linies = fitxer.readlines()
    print(f"El fitxer té {len(linies)} línies.")