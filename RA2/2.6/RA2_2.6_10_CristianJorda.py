# Autor: Cristian Jorda Matei
# Data: 17/11/2025
# Assegurar el tancament del fitxer (amb error): Simula una operació amb fitxers on pot haver-hi un error durant la lectura. Assegura’t que el fitxer es tanqui sempre, fins i tot si es produeix un error en llegir-lo.
# Pista: utilitza try-finally o millor encara: comprova què passa si no utilitzes with i ho fas tot manualment amb .open() i .close().

fitxer = None
try:
    fitxer = open("sortida.txt", "r", encoding="utf-8")
    contingut = fitxer.read()
    print("Fitxer llegit.")
except Exception as e:
    print(f"Error: {e}")
finally:
    if fitxer:
        fitxer.close()
        print("Fitxer tancat.")