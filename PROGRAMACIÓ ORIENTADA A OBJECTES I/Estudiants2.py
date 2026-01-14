from Estudiant import Estudiant


estudiants = [
    Estudiant("Anna", 8),
    Estudiant("Marc", 4),
    Estudiant("Laura", 6)
]

for e in estudiants:
    if e.ha_aprovat():
        print(e.nom)
