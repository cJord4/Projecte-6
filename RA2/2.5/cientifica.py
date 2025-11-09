# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Calculadora científica que combina calculadora.py amb el mòdul math.
# NOTA: El fitxer calculadora.py ha d'estar a la mateixa carpeta.

import calculadora
import math

print("--- CALCULADORA CIENTIFICA ---")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacio")
print("4. Divisio")
print("5. Arrel quadrada")
print("6. Potencia")
print("7. Sinus")

# Input esperat: opció del menú
opcio = int(input("Tria una opcio: "))

if opcio == 1:
    a = int(input("Primer nombre: "))
    b = int(input("Segon nombre: "))
    print("Resultat:", calculadora.suma(a, b))
elif opcio == 2:
    a = int(input("Primer nombre: "))
    b = int(input("Segon nombre: "))
    print("Resultat:", calculadora.resta(a, b))
elif opcio == 3:
    a = int(input("Primer nombre: "))
    b = int(input("Segon nombre: "))
    print("Resultat:", calculadora.multiplicacio(a, b))
elif opcio == 4:
    a = int(input("Primer nombre: "))
    b = int(input("Segon nombre: "))
    print("Resultat:", calculadora.divisio(a, b))
elif opcio == 5:
    a = int(input("Introdueix un nombre: "))
    print("Resultat:", math.sqrt(a))
elif opcio == 6:
    a = int(input("Base: "))
    b = int(input("Exponent: "))
    print("Resultat:", math.pow(a, b))
elif opcio == 7:
    a = int(input("Angle en graus: "))
    print("Resultat:", math.sin(math.radians(a)))
else:
    print("Opcio no valida")