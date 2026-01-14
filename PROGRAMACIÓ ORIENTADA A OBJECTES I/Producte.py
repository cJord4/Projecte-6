# Autor: Cristian Jorda Matei
# Data: 14/01/2026
# 4. Crea una classe Producte

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def aplicar_descompte(self, percentatge):
        descompte = self.preu * (percentatge / 100)
        self.preu = self.preu - descompte
        print(f"Descompte del {percentatge}% aplicat. Nou preu: {self.preu}€")
