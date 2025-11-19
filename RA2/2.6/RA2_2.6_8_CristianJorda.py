# Autor: Cristian Jorda Matei
# Data: 17/11/2025
# Evitar que el programa es bloquegi si el fitxer està mal format: Suposa que tens un fitxer nombres.txt que hauria de contenir un nombre enter per línia. Fes un programa que llegeixi cada línia i la transformi en enter. Si alguna línia no és un enter vàlid, captura l’error i mostra un missatge, però continua amb la resta.

with open("nombres.txt", "w", encoding="utf-8") as f:
    f.write("10\n20\nno és nombre\n30\n")

with open("nombres.txt", "r", encoding="utf-8") as fitxer:
    for linia in fitxer:
        try:
            nombre = int(linia.strip())
            print(f"Nombre: {nombre}")
        except ValueError:
            print(f"Error: '{linia.strip()}' no és un nombre.")
