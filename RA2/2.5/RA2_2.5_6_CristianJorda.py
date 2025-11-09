# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció multiplica_tot(*nombres) que rebi qualsevol quantitat de nombres
# i retorni la seva multiplicació.

def multiplica_tot(*nombres):
    resultat = 1
    for num in nombres:
        resultat = resultat * num
    return resultat

# Input esperat: qualsevol quantitat de nombres
num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))
num3 = int(input("Introdueix el tercer nombre: "))
print(multiplica_tot(num1, num2, num3))