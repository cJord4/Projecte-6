# Cristian Jordà Matei
# 21/01/2026

class Joc:
    def __init__(self):
        self.__puntuacio = 0
    
    def get_puntuacio(self):
        return self.__puntuacio
    
    def sumar_punts(self, punts):
        self.__puntuacio += punts
    
    def reiniciar(self):
        self.__puntuacio = 0
