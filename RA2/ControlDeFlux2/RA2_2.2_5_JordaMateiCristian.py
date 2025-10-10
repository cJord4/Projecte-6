# Autor: Cristian Jorda Matei
# Data: 08/10/2025
# Descripció: Demana a l'usuari un número enter positiu i determina si és un nombre primer o no

num = int(input("Introdueix un número: "))

if num <= 1:
    print("Introdueix un numero senser positiu.")
else:
    divisor = 2
    es_primer = True

    while divisor * divisor <= num:  # fins a l'arrel quadrada de num
        if num % divisor == 0:
            es_primer = False
            break
        divisor += 1

    if es_primer:
        print("És un número primer.")
    else:
        print("No és un número primer.")
