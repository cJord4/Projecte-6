# Autor: Cristian Jorda Matei
# Data: 14/01/2026
# 1. Crea una classe Cotxe


class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any
        
    def descriure(self):
        print(f"Cotxe: {self.marca} amb Model{self.model} de l'any: {self.any}")
