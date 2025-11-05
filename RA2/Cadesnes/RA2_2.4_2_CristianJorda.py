# Autor: Cristian Jorda Matei
# Data: 30/10/2025
# Demana una frase i compta quantes vocals conté.

frase = str(input("Introdueix una frase: "))
vocals = "aeiouàèéíòóúüAEIOUÀÈÉÍÒÓÚÜ"
contador = 0


for caracter in frase:
    if caracter in vocals:
        contador += 1
print(f"Hi ha {contador} vocals")
