# Cristian Jordà Matei
# 21/01/2026

class Rellotge:
    def __init__(self):
        self.__hores = 0
    
    def get_hores(self):
        return self.__hores
    
    def set_hores(self, hores):
        if hores < 0 or hores > 23:
            print("Error: hores entre 0 i 23")
        else:
            self.__hores = hores
    
    def mostrar(self):
        return f"{self.__hores:02d}:00"
