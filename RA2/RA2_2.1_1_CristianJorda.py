# Autor: Cristian Jordà
# Data: 20/09/2023
# versió: 1.0
#
# Descripció: Programa que demana un número a l'usuari i indica si és positiu, negatiu o zero.
# Especificacions de entrada:
#   - Un número enter introduït per l'usuari.

num = int(input("Introdueix un número: "))

if num == 0:
    print("El número és zero")
if num > 0:
    print("El número és positiu")
else:
    print("El número és negatiu")
