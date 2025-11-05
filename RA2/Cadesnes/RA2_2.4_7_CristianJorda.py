# Autor: Cristian Jorda Matei
# Data: 30/10/2025
# Demana una cadena i compta quantes vegades apareix una lletra concreta.

frase = str(input("Introdueix una frase: "))
lletra = str(input("Quina lletra vols veure cuantes vegades apareixi: "))
print (f"La lletra {lletra} apareix {frase.count(lletra) or frase.count(lletra).upper} vegades")



