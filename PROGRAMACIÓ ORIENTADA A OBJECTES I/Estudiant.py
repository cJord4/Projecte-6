# Autor: Cristian Jorda Matei
# Data: 14/01/2026
# 5. Crea una classe Estudiant

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota
    
    def ha_aprovat(self):
        if self.nota >= 5:
            print(f"{self.nom} ha aprovat amb una nota de {self.nota}")
        else:
            print(f"{self.nom} ha suspès amb una nota de {self.nota}")
