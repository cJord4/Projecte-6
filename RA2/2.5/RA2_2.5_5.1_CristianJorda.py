# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció saluda_nom(nom="amic") que imprimeixi "Hola, <nom>".
# Si no passes cap nom, ha de imprimir "Hola, amic".

def saluda_nom(nom="amic"):
    print("Hola, " + nom)

saluda_nom("Joan")
saluda_nom()
saluda_nom("Laia")