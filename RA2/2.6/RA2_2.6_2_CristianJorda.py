# Autor: Cristian Jorda Matei
# Data: 17/11/2025
# Escriure en un fitxer: Crea un programa que escrigui les següents 3 línies en un fitxer nou anomenat sortida.txt. El contingut anterior (si n'hi ha) ha de desaparèixer.

linies = [
    "Primera linia \n",
    "Segona linia\n",
    "Tercera línia.\n"
]

# Escriure
with open("sortida.txt", "w", encoding="utf-8") as fitxer:
    fitxer.writelines(linies)

# Llegir
with open("sortida.txt", "r", encoding="utf-8") as fitxer:
    contingut = fitxer.read()

print(contingut)