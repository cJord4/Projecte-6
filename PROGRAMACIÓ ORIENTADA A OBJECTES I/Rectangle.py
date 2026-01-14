# Autor: Cristian Jorda Matei
# Data: 14/01/2026
# 3. calcula l'àrea i el perímetre d'un rectangle

class Rectangle:
    def __init__(self, amplada, alcada):
        self.amplada = amplada
        self.alcada = alcada

    def area(self):
        return self.amplada * self.alcada

    def perimetre(self):
        return 2 * (self.amplada + self.alcada)
