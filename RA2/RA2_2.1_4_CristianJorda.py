# Autor: Cristian Jordà
# Data: 20/09/2023
# versió: 1.0
#
# Descripció: Programa que demana una nota a l'usuari i indica si està aprovat o suspès.
# Especificacions de entrada: La nota de l'usuari (0-10).

nota = int(input("Introdueix la nota: "))
if nota >= 5:
    print("Aprovat")
else:
    print("Suspès")
