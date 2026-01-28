class CarretCompra:
    def __init__(self, total, descompte):
        self.total = total
        dself.descomte = descompte

    def calcular_total_amb_descompte(self):
        return self.descomte.aplicar(self.total)

class Descompte20:
    def aplicar(self, total):
        return total * 0.8
    