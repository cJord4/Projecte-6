# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció estat_persona(edat) que:
# - Retorni "Menor d'edat", "Adult" o "Jubilat" segons l'edat.
# - Torni tant l'estat com una descripció (return estat, descripcio).

def estat_persona(edat):
    if edat < 18:
        estat = "Menor d'edat"
        descripcio = "No té 18 anys"
    elif edat < 65:
        estat = "Adult"
        descripcio = "Entre 18 i 64 anys"
    else:
        estat = "Jubilat"
        descripcio = "Té 65 anys o més"
    
    return estat, descripcio

# Input esperat: un nombre enter (edat)
edats = [12, 25, 70]

for edat in edats:
    print(f"{edat} es {estat_persona(edat)}")