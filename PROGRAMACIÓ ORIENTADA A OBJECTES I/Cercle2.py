from Cercle import Cercle

cercles = [Cercle(2), Cercle(5), Cercle(10)]

for c in cercles:
    if c.calcular_area() > 50:
        print(c.radi)