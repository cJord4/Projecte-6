# Autor: Cristian Jorda Matei
# Data: 17/11/2025
# Crear el fitxer si no existeix: Intenta obrir un fitxer en mode lectura. Si no existeix, crea’l automàticament i escriu-hi una línia per defecte: "Fitxer creat automàticament".
# Pista: utilitza try-except amb open(...) en mode "r", i si falla, obre'l en mode "w".

try:
    with open("nou_fitxer.txt", "r", encoding="utf-8") as fitxer:
        print("El fitxer ja existeix:")
        print(fitxer.read())
except FileNotFoundError:
    with open("nou_fitxer.txt", "w", encoding="utf-8") as fitxer:
        fitxer.write("Fitxer creat automàticament.\n")
    print("Fitxer creat!")
