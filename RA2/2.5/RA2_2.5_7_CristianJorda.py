# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció maxim(a, b, c) que retorni el nombre més gran entre els tres.

def maxim(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

# Input esperat: tres nombres (a, b, c)
a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))
c = int(input("Introdueix el tercer nombre: "))
print(maxim(a, b, c))