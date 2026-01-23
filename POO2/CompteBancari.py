# Cristian Jordà Matei
# 21/01/2026


class Compte:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultar(self):
        return self.__saldo
    
    def ingressar(self, quantitat):
        if quantitat > 0:
            self.__saldo += quantitat

    def traure(self, quantitat):
        if quantitat > 0 and quantitat <= self.__saldo:
            self.__saldo -= quantitat