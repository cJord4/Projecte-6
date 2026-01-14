# Autor: Cristian Jorda Matei
# Data: 14/01/2026
# 10. Crea una classe Punt

import math

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, altre_punt):
        return math.sqrt((self.x - altre_punt.x) ** 2 + (self.y - altre_punt.y) ** 2)