# Autor: Cristian Jorda Matei
# Data: 08/10/2025
# Descripció: Calcula la suma dels primers 100 nombres enters positius (de 1 a 100) i mostra el resultat.

comptador = 1
suma = 0

while comptador <= 100:
    suma += comptador
    comptador += 1

print("La suma dels primers 100 nombres enters positius és:", suma)
