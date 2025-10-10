# Autor: Cristian Jorda Matei
# Data: 08/10/2025
# Descripció: Programa que genera un número aleatori entre 1 i 100 i demana a l'usuari que l'endevini.

import random 

numero = random.randint(1, 100)

numero_adivinar = int(input("Introdueix un número per endevinar: "))

while numero_adivinar != numero:
    if numero_adivinar < numero:
        print("El número és més petit")
    else:
        print("El número és més gran")
    numero_adivinar = int(input("Introdueix un altre número per endevinar: "))

print("Has endevinat el número!")