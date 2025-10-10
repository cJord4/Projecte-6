# Autor: Cristian Jorda Matei
# Data: 08/10/2025
# Descripció: Escriu un programa que mostri per pantalla una compte enrere des de 10 fins a 1, i després imprimeixi "Feliç Any Nou!".

from time import sleep

comtador = 0

while comtador <= 10:
    print(comtador)
    sleep(comtador / 3)
    comtador = comtador + 1

print("Feliç Any Nou :)")