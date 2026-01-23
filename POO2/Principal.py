# ============================================
# PRINCIPAL.PY - PROVES DE LES CLASSES
# ============================================
from Termostat import Termostat
from Sensor import Sensor
from Producte import Producte
from Rellotge import Rellotge
from Alumne import Alumne
from Joc import Joc
from CompteUsuari import CompteUsuari



def mostrar_menu():
    print("\n" + "="*60)
    print("MENÚ PRINCIPAL - PROVES DE CLASSES")
    print("="*60)
    print("1. Provar Termostat")
    print("2. Provar Sensor")
    print("3. Provar Producte")
    print("4. Provar Rellotge")
    print("5. Provar Alumne")
    print("6. Provar Joc")
    print("7. Provar CompteUsuari")
    print("8. Executar totes les proves automàtiques")
    print("0. Sortir")
    print("="*60)

def provar_termostat():
    print("\n--- PROVES TERMOSTAT ---")
    t = Termostat()
    print(f"Temperatura inicial: {t.temperatura}°C")
    
    t.temperatura = 25
    print(f"Nova temperatura: {t.temperatura}°C")
    
    t.temperatura = 10
    print(f"Temperatura mínima: {t.temperatura}°C")
    
    t.temperatura = 30
    print(f"Temperatura màxima: {t.temperatura}°C")
    
    print("\nProvant valors invàlids:")
    t.temperatura = 5   # Error
    t.temperatura = 35  # Error


def provar_sensor():
    print("\n--- PROVES SENSOR ---")
    s = Sensor()
    print(f"Valor inicial: {s.get_valor()}")
    
    s.set_valor(50)
    print(f"Nou valor: {s.get_valor()}")
    
    s.set_valor(0)
    print(f"Valor mínim: {s.get_valor()}")
    
    s.set_valor(100)
    print(f"Valor màxim: {s.get_valor()}")
    
    print("\nProvant valors invàlids:")
    s.set_valor(-10)  # Error
    s.set_valor(150)  # Error


def provar_producte():
    print("\n--- PROVES PRODUCTE ---")
    p = Producte("Portàtil", 800)
    print(f"Producte: {p.nom}")
    print(f"Preu: {p.get_preu()}€")
    
    p.set_preu(750)
    print(f"Preu rebaixat: {p.get_preu()}€")
    
    p.nom = "Ordinador Gaming"
    print(f"Nom actualitzat: {p.nom}")
    
    print("\nProvant preu invàlid:")
    p.set_preu(-50)  # Error
    p.set_preu(0)    # Error


def provar_rellotge():
    print("\n--- PROVES RELLOTGE ---")
    r = Rellotge()
    print(f"Hora inicial: {r.mostrar()}")
    
    r.set_hores(9)
    print(f"Matí: {r.mostrar()}")
    
    r.set_hores(14)
    print(f"Tarda: {r.mostrar()}")
    
    r.set_hores(23)
    print(f"Nit: {r.mostrar()}")
    
    print("\nProvant hora invàlida:")
    r.set_hores(25)  # Error
    r.set_hores(-1)  # Error


def provar_alumne():
    print("\n--- PROVES ALUMNE ---")
    a = Alumne("Maria Garcia", 18)
    print(f"Alumne: {a.nom}")
    print(f"Edat: {a.get_edat()} anys")
    
    a.set_edat(19)
    print(f"Edat actualitzada: {a.get_edat()} anys")
    
    a.nom = "Maria Garcia López"
    print(f"Nom complet: {a.nom}")
    
    print("\nProvant edat invàlida:")
    a.set_edat(-5)  # Error


def provar_joc():
    print("\n--- PROVES JOC ---")
    j = Joc()
    print(f"Puntuació inicial: {j.get_puntuacio()}")
    
    j.sumar_punts(10)
    print(f"Després de guanyar 10 punts: {j.get_puntuacio()}")
    
    j.sumar_punts(25)
    print(f"Després de guanyar 25 punts més: {j.get_puntuacio()}")
    
    j.sumar_punts(15)
    print(f"Després de guanyar 15 punts més: {j.get_puntuacio()}")
    
    print("\nReiniciant partida...")
    j.reiniciar()
    print(f"Puntuació després de reiniciar: {j.get_puntuacio()}")


def provar_compte_usuari():
    print("\n--- PROVES COMPTE USUARI ---")
    c = CompteUsuari("Joan Martínez")
    print(f"Usuari: {c.nom}")
    
    c.set_email("joan@example.com")
    print(f"Email: {c.get_email()}")
    
    c.set_email("joan.martinez@empresa.cat")
    print(f"Email actualitzat: {c.get_email()}")
    
    print("\nProvant emails invàlids:")
    c.set_email("emailsensearrova")      # Error
    c.set_email("email@sensepunt")        # Error
    c.set_email("emailinvalid")           # Error
    
    print(f"Email actual (sense canvis): {c.get_email()}")


def proves_automatiques():
    print("\n" + "="*60)
    print("EXECUTANT TOTES LES PROVES AUTOMÀTIQUES")
    print("="*60)
    
    provar_termostat()
    input("\nPrem ENTER per continuar...")
    
    provar_sensor()
    input("\nPrem ENTER per continuar...")
    
    provar_producte()
    input("\nPrem ENTER per continuar...")
    
    provar_rellotge()
    input("\nPrem ENTER per continuar...")
    
    provar_alumne()
    input("\nPrem ENTER per continuar...")
    
    provar_joc()
    input("\nPrem ENTER per continuar...")
    
    provar_compte_usuari()
    
    print("\n" + "="*60)
    print("TOTES LES PROVES COMPLETADES!")
    print("="*60)


# ============================================
# EXECUCIÓ DEL PROGRAMA
# ============================================

def main():
    while True:
        mostrar_menu()
        opcio = input("\nSelecciona una opció (0-8): ")
        
        if opcio == "1":
            provar_termostat()
        elif opcio == "2":
            provar_sensor()
        elif opcio == "3":
            provar_producte()
        elif opcio == "4":
            provar_rellotge()
        elif opcio == "5":
            provar_alumne()
        elif opcio == "6":
            provar_joc()
        elif opcio == "7":
            provar_compte_usuari()
        elif opcio == "8":
            proves_automatiques()
        elif opcio == "0":
            print("\n👋 Sortint del programa...")
            break
        else:
            print("\n❌ Opció invàlida! Tria entre 0 i 8.")
        
        if opcio != "8" and opcio != "0":
            input("\nPrem ENTER per tornar al menú...")


if __name__ == "__main__":
    main()