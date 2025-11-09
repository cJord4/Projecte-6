# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció saluda_nom(nom="amic") que imprimeixi "Hola, <nom>".
# Si no passes cap nom, ha de imprimir "Hola, amic".

def saluda_nom(nom="amic"):
    print("Hola, " + nom)

# Input esperat: un nom (string) o cap paràmetre
nom = input("Introdueix un nom (o prem Enter per defecte): ")
if nom == "":
    saluda_nom()
else:
    saluda_nom(nom)