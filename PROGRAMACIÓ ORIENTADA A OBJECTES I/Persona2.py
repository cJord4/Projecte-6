from Persona import Persona

def persones_mes_30(persones):
    """Mostra les persones amb més de 30 anys"""
    for p in persones:
        if p.edat > 30:
            p.presentar_se()

# Exemple d'ús
if __name__ == "__main__":
    # Crear una llista de persones
    persones = [
        Persona("Anna", 25),
        Persona("Joan", 35),
        Persona("Maria", 42),
        Persona("Pere", 28),
        Persona("Laura", 31)
    ]
    
    print("Persones amb més de 30 anys:")
    persones_mes_30(persones)