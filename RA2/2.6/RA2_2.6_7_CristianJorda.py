# Autor: Cristian Jorda Matei
# Data: 17/11/2025
# Gestionar errors d'escriptura: Escriu un programa que intenti escriure en un fitxer anomenat resultats.txt, però gestiona l'error que es pot produir si el fitxer és només de lectura o si el sistema impedeix escriure-hi (permisos denegats).
# Pista: captura PermissionError.

try:
    with open("resultats.txt", "w", encoding="utf-8") as fitxer:
        fitxer.write("Dades escrites correctament.\n")
    print("Fitxer escrit amb èxit!")
except PermissionError:
    print("Error: No tens permisos per escriure.")