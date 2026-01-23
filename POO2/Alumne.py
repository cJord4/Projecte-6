# Cristian Jordà Matei
# 21/01/2026

class Alumne:
    def __init__(self, nom, edat):
        self.nom = nom
        self.__edat = 0
        self.set_edat(edat)
    
    def get_edat(self):
        return self.__edat
    
    def set_edat(self, edat):
        if edat < 0:
            print("Error: l'edat no pot ser negativa")
        else:
            self.__edat = edat
