# Autor: Cristian Jorda Matei
# Data: 1/11/2025
# Demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal.

paraules = input("Escriu paraules separades per espais: ").split()

vocals = "aeiouAEIOU"

paraules_vocals = [p for p in paraules if p[0] in vocals]

print("Paraules que comencen per vocal:", paraules_vocals)
