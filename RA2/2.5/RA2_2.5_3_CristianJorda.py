# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció area_rectangle(base, altura) que retorni l'àrea (base * altura).

def area_rectangle(base, altura):
    return base * altura

# Input esperat: dos nombres (base, altura)
base = int(input("Introdueix la base: "))
altura = int(input("Introdueix l'altura: "))
print(area_rectangle(base, altura))