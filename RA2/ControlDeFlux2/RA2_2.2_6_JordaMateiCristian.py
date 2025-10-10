# Autor: Cristian Jorda Matei
# Data: 08/10/2025
# Descripció: Utilitzar un bucle per imprimir el següent patró d’estrelles

num_files = int(input("Introdueix el nombre de files a crear: "))

for i in range(num_files):
    print((' ' * (num_files - i - 1)) + ('*' * (2 * i + 1)))
