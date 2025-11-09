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


print(maxim(3, 7, 5))
print(maxim(10, 2, 8))
print(maxim(1, 1, 1))