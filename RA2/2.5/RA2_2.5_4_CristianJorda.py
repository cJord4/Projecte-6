# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció es_parell(numero) que retorni True si numero és parell i False si no.

def es_parell(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Input esperat: un nombre enter (numero)
numero = int(input("Introdueix un nombre: "))
print(es_parell(numero))