# Autor: Cristian Jordà
# Data: 20/09/2023
# versió: 1.0
#
# Descripció: Programa que demana un número a l'usuari i indica si és parell o inparell.
# Especificacions de entrada:

num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))
num3 = int(input("Introdueix el tercer número: "))

if num1 >= num2 and num1 >= num3:
    print("El número més gran és:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El número més gran és:", num2)
elif num3 >= num1 and num3 >= num2:
    print("El número més gran és:", num3)

else:
    print("Algun dels números són iguals")