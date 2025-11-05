# Autor: Cristian Jorda Matei
# Data: 1/11/2025
# Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.

entrada = input("Introdueix 10 numeros separats per espais: ")
numeros = [int(x) for x in entrada.split()]
parells = []
inparells = []

for i in numeros:
    if i % 2 == 0:
        parells.append(i)  
    elif i % 2 == 1:
        inparells.append(i)

print(f"Els parells son: {parells}")
print(f"Els inparells son: {inparells}")
