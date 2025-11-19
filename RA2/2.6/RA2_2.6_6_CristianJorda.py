# Autor: Cristian Jorda Matei
# Data: 17/11/2025
# Comprovar si el fitxer existeix abans de llegir-lo: Fes un programa que intenti llegir un fitxer anomenat dades.txt, però abans comprovi si existeix. Si no existeix, mostra un missatge d’error amigable.

import os

if os.path.exists("dades.txt"):
    with open("dades.txt", "r", encoding="utf-8") as fitxer:
        print(fitxer.read())
else:
    print("El fitxer dades.txt no existeix.")