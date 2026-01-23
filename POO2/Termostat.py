# Cristian Jordà Matei
# 21/01/2026


class Termostat:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nova_temperatura):
        if 10 <= nova_temperatura <= 30:
            self.__temperatura = nova_temperatura