# Autor: Cristian Jorda Matei
# Data: 1/11/2025
# Fes un programa que elimini els duplicats d'una llista.

llista_original = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4, 7]
print("Llista original:", llista_original)

llista_sense_duplicats = []
elements_vistos = set()

for element in llista_original:
    if element not in elements_vistos:
        llista_sense_duplicats.append(element)
        elements_vistos.add(element)

print(f"La llista sense duplicar es: {llista_sense_duplicats}")