# Autor: Cristian Jorda Matei
# Data: 22/10/2025
# Demana a l'usuari un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest nombre.​

def es_primer(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    n = int(input("Introdueix un nombre enter: "))

    print(f"Nombres primers entre 2 i {n}:")
    for i in range(2, n + 1):
        if es_primer(i):
            print(i)

except ValueError:
    print("Error: has d'introduir un nombre sencer.")
