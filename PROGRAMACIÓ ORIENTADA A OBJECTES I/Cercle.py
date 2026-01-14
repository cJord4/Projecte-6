# Autor: Cristian Jorda Matei
# Data: 14/01/2026
# 7. Crea una classe Cercle

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def calcular_area(self):
        return math.pi * self.radi ** 2

    def calcular_perimetre(self):
        return 2 * math.pi * self.radi