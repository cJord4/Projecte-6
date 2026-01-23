# Cristian Jordà Matei
# 21/01/2026

class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya

    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau