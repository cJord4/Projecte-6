# Autor: Cristian Jorda Matei
# Data: 14/01/2026
# 9. Crea una classe Llibre


class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"Títol: {self.titol}")
        print(f"Autor: {self.autor}")
        print(f"Any: {self.any}")