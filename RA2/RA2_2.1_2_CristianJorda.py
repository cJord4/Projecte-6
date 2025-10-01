# Autor: Cristian Jordà
# Data: 20/09/2023
# versió: 1.0
#
# Descripció: Programa que demana un número a l'usuari i indica si és parell o inparell.
# Especificacions de entrada:


num = int(input("Introdueix un número: "))

if num % 2 == 0:
    print("Es parell")
else:
    print("Es inparell")