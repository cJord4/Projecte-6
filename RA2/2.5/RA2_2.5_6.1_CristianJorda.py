# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció multiplica_tot(*nombres) que rebi qualsevol quantitat de nombres
# i retorni la seva multiplicació.

def multiplica_tot(*nombres):
    resultat = 1
    for num in nombres:
        resultat = resultat * num
    return resultat


print(multiplica_tot(2, 3, 4))
print(multiplica_tot(5, 10))