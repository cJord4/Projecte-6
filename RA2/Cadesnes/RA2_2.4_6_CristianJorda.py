# Autor: Cristian Jorda Matei
# Data: 30/10/2025
# Demana una cadena i mostra la primera i l'última lletra.

frase = str(input("Introdueix una frase: "))

llargada_total = int(len(frase))

print(llargada_total)
print(f"La primera lletra es {frase[0]} i la ultima es {frase[llargada_total - 1]}" )     
