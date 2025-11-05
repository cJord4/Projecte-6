# Autor: Cristian Jorda Matei
# Data: 30/10/2025
# Demana una paraula i verifica si és un palíndrom (ex: "anna", "civic", etc.).

frase = str(input("Introdueix una frase: "))

def revertir(frase):
        return frase[::-1]

frase_revertida = revertir(frase)

if frase == frase_revertida:
    print("As trobat un palindrom!")
else:
    print("No es palidrom =(")