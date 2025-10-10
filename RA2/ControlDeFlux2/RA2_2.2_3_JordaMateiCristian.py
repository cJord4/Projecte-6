# Autor: Cristian Jorda Matei
# Data: 08/10/2025
# Descripció: Demana a l'usuari un número enter i mostra la seva taula de multiplicar del 1 al 10.

num = int(input("Intrdueix un nombre per el cual vols veure la taula del 10: "))

comptador = 1

while comptador <= 10:
    print(f"{num} x {comptador} = {num * comptador}")
    comptador = comptador + 1

print("Aquin tens la teva taula del 10!")