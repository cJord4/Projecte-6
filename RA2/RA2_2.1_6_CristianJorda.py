# Autor: Cristian Jordà
# Data: 20/09/2023
# versió: 1.0
#
# Descripció: Programa que demana una lletra a l'usuari i indica si és vocal o consonant.
# Especificacions de entrada: Una lletra introduïda per l'usuari.




lletra = str(input("Introdueix una lletra: "))
if lletra in "aeiou":
    print("La lletra és una vocal")
else:
    print("La lletra és una consonant")
