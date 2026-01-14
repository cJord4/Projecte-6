from Producte import Producte

def aplicar_descompte(productes):
    for p in productes:
        p.aplicar_descompte(10)

p1 = Producte("Pa", 1.5)
p2 = Producte("Llet", 2.0)
p3 = Producte("Formatge", 4.0)

productes = [p1, p2, p3]

aplicar_descompte(productes)