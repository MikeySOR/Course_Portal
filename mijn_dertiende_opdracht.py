#---------------------------------------------------------Introductie

print("=" * 23)
print("|| Dit is project 13 ||")
print("=" * 23)

#---------------------------------------------------------Aanmelding
import random

gebruikers = []

#--------------------------Test accounts
gebruikers.append({
    "Voornaam": "Jan",
    "Naam": "Van",
    "Code": 1111,
    "Functie": "1"
})

gebruikers.append({
    "Voornaam": "Lisa",
    "Naam": "Van",
    "Code": 2222,
    "Functie": "2"
})

#--------------------------Begin


def Aanmelding():
    while True:
        print("-" * 20)
        print("-MY-PORTAL---------")
        print("-" * 20)
        print("1: Aanmelden")
        print("2: Nieuwe gebruiker")
        
        try:
            keuze = int(input("| "))
            
            if keuze == 1:
                print("\n")
                Aanmelden()
                
                
            elif keuze == 2:
                print("\n")
                Nieuw_gebruiker()
                
            elif keuze == 9999:
                print("Einde Programma.")
                break
                
            else:
                print("Foutieve ingave.")
                print("-" *20)
                print("\n")
        
        except ValueError:
            print("Foutieve keuze.")
            print("-" *20)
            print("\n")
        

#-----------------------------------------------Nieuwe gebruiker optie

def Nieuw_gebruiker():
    while True:
        print("Voer u naam en voornaam in.")
        voornaam = input("Voornaam: ").strip()
        naam = input("Naam: ").strip()
        functie = input("""
1: Docent
2: Student
Keuze: """).strip()
        
        if functie == "1":
            code = random.randint(1000, 99999999999)
            
        elif functie == "2":
            code = random.randint(1000, 9999999)
            
        else:
            print("Ongeldige keuze.\n")
            return
    
        gebruikers.append({
            "Voornaam": voornaam,
            "Naam": naam,
            "Code" : code,
            "Functie" : functie
            })
        
        print("Gebruiker succesvol aangemaakt!")
        print(f"Uw speciale code is -{code}-\n")
        
        break
#-----------------------------------------------Bestaande gebruiker optie
    
def Aanmelden():
    while True:
        print("Log in")
        print("-" * 45)
        
        try:
            voornaam = input("Voornaam: ").strip()
            naam = input("Naam: ").strip()
            code = int(input("Voer u speciale code in: "))
            
            for gebruiker in gebruikers:
                if (
                    gebruiker["Voornaam"].lower() == voornaam.lower() and
                    gebruiker["Naam"].lower() == naam.lower() and
                    gebruiker["Code"] == code
            ):
                    Main(voornaam)
                    return
            
            print("Gegevens niet correct.\n")
            

        except ValueError:
            print("Foutieve keuze.")
            print("-" *20)
            print("\n")

            
        

#-----------------------------------------------Home Screen
    
def Main(voornaam):
    while True:
        print("\n")
        print("_" *27)
        print(f"WELKOM: {voornaam}!         ")
        print("_" *27)
        print("1: Cursussen              ")
        print("2: Mijn cursussen         ")
        print("3: Betalingen             ")
        print("4: Persoonlijke gegevens  ")
        print("5: Afmelden               ")
        print("_" *27)
        
        try:
            antwoord = int(input("| "))
            
            
            if antwoord == 1:
                print("Test")
                
            elif antwoord == 2:
                print("Test")
                
            elif antwoord == 3:
                print("Test")
                
            elif antwoord == 4:
                print("Test")
                
            elif antwoord == 5:
                print("U word afgemeld.\n")
                break
                
            else:
                print("Foutieve ingave.")
                print("-" *20)
                print("\n")
                
            
        except ValueError:
            print("Foutieve keuze.")
            print("-" *20)
            print("\n")



Aanmelding()
