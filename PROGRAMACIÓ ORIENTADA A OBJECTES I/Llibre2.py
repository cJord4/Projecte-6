from Llibre import Llibre

class Biblioteca:
    def __init__(self):
        self.llibres = []
    
    def afegir_llibre(self, llibre):
        """Afegeix un llibre a la biblioteca"""
        if isinstance(llibre, Llibre):
            self.llibres.append(llibre)
        else:
            print("Error: L'objecte no és una instància de Llibre")
    
    def mostrar_llibres(self):
        """Mostra tots els llibres de la biblioteca"""
        if len(self.llibres) == 0:
            print("La biblioteca està buida")
        else:
            print("Llibres de la biblioteca:")
            for i, llibre in enumerate(self.llibres, 1):
                print(f"{i}. {llibre.titol} - {llibre.autor} ({llibre.any})")

# Exemple d'ús
if __name__ == "__main__":
    biblio = Biblioteca()
    
    # Afegir llibres (depenent de com estigui definida la classe Llibre)
    llibre1 = Llibre("Don Quixot", "Miguel de Cervantes", 1605)
    llibre2 = Llibre("La Regenta", "Leopoldo Alas", 1884)
    
    biblio.afegir_llibre(llibre1)
    biblio.afegir_llibre(llibre2)
    
    biblio.mostrar_llibres()