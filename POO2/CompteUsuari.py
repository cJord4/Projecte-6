# Cristian Jordà Matei
# 21/01/2026

class CompteUsuari:
    def __init__(self, nom):
        self.nom = nom
        self.__email = ""
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        if "@" not in email or "." not in email:
            print("Error: email invàlid (ha de contenir @ i .)")
        else:
            self.__email = email
