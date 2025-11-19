# Autor: Cristian Jorda Matei
# Data: 17/11/2025
# Crea un fitxer de text anomenat missatge.txt amb contingut a mà (o des del codi). Escriu un programa que llegeixi i mostri el contingut per pantalla.
# Obrim el fitxer en mode lectura

with open("missatge.txt", "r", encoding="utf-8") as fitxer:
    contingut = fitxer.read()

print(contingut)
