# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Programa que simula llençar un dau usant el mòdul random.

import random

def llenca_dau():
    return random.randint(1, 6)

def llenca_dau_n_vegades(n):
    suma = 0
    for i in range(n):
        resultat = llenca_dau()
        print("Tirada", i + 1, ":", resultat)
        suma = suma + resultat
    mitjana = suma / n
    return mitjana

# Input esperat: nombre de tirades
n = int(input("Quantes vegades vols llençar el dau? "))
mitjana = llenca_dau_n_vegades(n)
print("Mitjana de les tirades:", mitjana)