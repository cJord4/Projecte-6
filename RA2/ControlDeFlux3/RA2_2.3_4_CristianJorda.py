# Autor: Cristian Jorda Matei
# Data: 22/10/2025
# Demana a l'usuari un nombre enter i imprimeix tots els nombres parells des de 0 fins a aquest nombre.

try: 
    n = int(input("Introdueix un nombre senser: "))
    if n % 2 == 0:
        for i in range(0, n+1, 2) if n >= 0 else range(0, n-1, -2):
            print(i)
    elif n % 2 == 1:
        print("Sisplau introdueix un nombre parell")

except ValueError:
    print(f"{ValueError}: Nombre no senser")