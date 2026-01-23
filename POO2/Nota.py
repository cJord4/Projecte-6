# Cristian Jordà Matei
# 21/01/2026



class Estudiant:    
    
    def __init__(self, nota):
        self._nota = nota

    def llegir_nota(self):
        return self._nota

    def modificar_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
