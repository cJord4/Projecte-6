# Autor: Cristian Jorda Matei
# Data: 8/11/2025
# Escriu una funció filtra_parells(llista) que:
# - Rebi una llista de nombres.
# - Retorni una nova llista només amb els nombres parells.

def filtra_parells(llista):
    parells = []
    for num in llista:
        if num % 2 == 0:
            parells.append(num)
    return parells

llista1 = [1, 2, 3, 4, 5, 6]
llista2 = [10, 15, 20, 25, 30]

print(f"Els parells son {filtra_parells(llista1)}")
print(f"Els parells son {filtra_parells(llista2)}")