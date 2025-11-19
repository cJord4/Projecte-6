# Autor: Cristian Jorda Matei
# Data: 17/11/2025
# Llegir i escriure: Obre un fitxer en mode lectura i escriptura (r+). Mostra el contingut per pantalla i afegeix una línia al final sense esborrar el contingut anterior.

with open("sortida.txt", "r+", encoding="utf-8") as fitxer:
    contingut = fitxer.read()
    print("Contingut:")
    print(contingut)
    fitxer.write("Línia nova afegida.\n")
