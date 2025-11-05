# Autor: Cristian Jorda Matei
# Data: 30/10/2025
# Escriu una funció que reverteixi una cadena.

frase = str(input("Introdueix una frase: "))

def revertir(frase):
        return frase[::-1]

frase_revertida = revertir(frase)

print(frase_revertida)