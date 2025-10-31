# Autor: Cristian Jorda Matei
# Data: 22/10/2025
# Demana a l'usuari un nombre enter i calcula la suma de tots els nombres des de 1 fins a aquest nombre.

try:
    num_user = int(input("Introdueix el nombre fins al que vols contar: "))

    for i in range(0, num_user):
        print(i + 1)

except ValueError:
    print("Error: Has de introduir un nombre sencer.")

