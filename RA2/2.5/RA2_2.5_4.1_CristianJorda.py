# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció es_parell(numero) que retorni True si numero és parell i False si no.

def es_parell(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

llista = [1, 2, 3, 4, 5, 6]

for numero in llista:
    if es_parell(numero) == True:
        print(f"El numero {numero} es parell")
    elif es_parell(numero) == False:
        print(f"El numero {numero} es inparell")