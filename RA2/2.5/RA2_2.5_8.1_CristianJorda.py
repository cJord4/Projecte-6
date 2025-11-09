# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció factorial(n) que calculi el factorial d'un nombre n de forma recursiva.
# Pista: factorial de n és n * factorial(n-1), amb factorial(0) = 1.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(0))
print(factorial(3))
print(factorial(5))