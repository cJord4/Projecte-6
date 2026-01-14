# Autor: Cristian Jorda Matei
# Data: 14/01/2026
# 6. Crea una classe CompteBancari


class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo
    
    def ingressar(self, quantitat):
        if quantitat > 0:
            self.saldo += quantitat
            print(f"S'han ingressat {quantitat}€. Saldo actual: {self.saldo}€")
        else:
            print("La quantitat a ingressar ha de ser positiva")
    
    def retirar(self, quantitat):
        if quantitat > 0:
            if quantitat <= self.saldo:
                self.saldo -= quantitat
                print(f"S'han retirat {quantitat}€. Saldo actual: {self.saldo}€")
            else:
                print(f"Saldo insuficient. Saldo actual: {self.saldo}€")
        else:
            print("La quantitat a retirar ha de ser positiva")
    
    def veure_saldo(self):
        print(f"El teu saldo actual és: {self.saldo}€")
        return self.saldo