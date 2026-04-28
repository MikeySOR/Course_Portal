#---------------------------------------------------------Introductie

print("=" * 23)
print("|| Dit is project 13 ||")
print("=" * 23)

#---------------------------------------------------------Aanmelding
import random

gebruikers = []
vakken = {
    "1": ("Wiskunde", "876545678876","Bjorn Deboodt", 450,
          "Het ontrafelen van wiskundige structuren, intellectuele puzzels en problemen analyseren met behulp van logische gedachtestappen"),
    "2": ("Python", "367845635476","Kenny Vanbellinghen", 250,
          "Opleiding Softwareprogrammeur leer je creatief en probleemoplossend denken."),
    "3": ("Java", "890132875634", "Jan Willems", 250,
          "Een hoogwaardige, algemene, geheugenveilige, objectgeoriënteerde programmeertaal"),
    "4": ("Linux", "794534376015", "Bryan DeLeeuw", 300,
          "Kerncomponent in een besturingssysteem dat de centrale verwerkingseenheid (CPU), het geheugen en de randapparatuur op een computer beheert."),
    "5": ("PhotoShop", "836578934215", "Piet Timmermans", 200,
          "Een grafisch programma ontwikkeld door Adobe voor het met de computer bewerken van foto's en ander digitaal beeldmateriaal."),
    "6": ("Engels", "784563547825", "Bob Lammertyne", 150,
          "Een Indo-Europese taal"),
    "7": ("Hardwarebeheer", "968745356785", "Lynn Peeters", 350,
          "De processen, tools en strategieën voor het beheer van de fysieke onderdelen van computers en gerelateerde systemen."),
    "8": ("Cyber Security", "692735143907", "Patrick Vanbever", 400,
          "Processen, aanbevolen procedures, en technologische oplossingen die je helpen kritieke systemen, gegevens en netwerken te beschermen tegen digitale aanvallen."),
    "9": ("Netwerkbeheer", "392018374655", "Max Vertongen", 300,
          "Het proces van het ontwerpen, beheren, monitoren en beveiligen van IT-netwerken.")
}

#--------------------------Test accounts
gebruikers.append({
    "Voornaam": "Jan",
    "Naam": "Van",
    "Adres": "Brussel",
    "Geboorte": "20/10/2000",
    "Code": 1111,
    "Functie": "1",
    "gegeven_vak": "Wiskunde",  
    "gekozen_vakken": [],
    "mijn_cursussen": []
})

gebruikers.append({
    "Voornaam": "Lisa",
    "Naam": "Van",
    "Adres": "Molenbeek",
    "Geboorte": "21/2/2001",
    "Code": 2222,
    "Functie": "2",
    "gegeven_vak" : None,
    "gekozen_vakken": [],
    "mijn_cursussen": []
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
                print("|Foutieve ingave.")
                print("\n")
                continue
        
        except ValueError:
            print("|Foutieve keuze.")
            print("\n")
            continue
        

#-----------------------------------------------Nieuwe gebruiker optie

def Nieuw_gebruiker():
    while True:
        print("Voer u naam en voornaam in.")
        voornaam = input("Voornaam: ").strip()
        naam = input("Naam: ").strip()
        adres = input("Adres: ")
        geboorte = input("Geboorte: ")
        functie = input("""
1: Docent
2: Student
Keuze: """).strip()
        
        if functie == "1":
            print("""
Welk vak geef je?
1: Wiskunde
2: Python
3: Java
4: Linux
5: PhotoShop
6: Engels
7: Hardwarebeheer
8: Cyber Security
9: Netwerkbeheer """)

        if functie == "1":
            vak_keuze = input("| ")
        
            if vak_keuze in vakken:
                vak = vakken[vak_keuze][0]
            
            else:
                print("|Ongeldige keuze\n")
                continue

            code = random.randint(1000, 99999999999)
            
        elif functie == "2":
            code = random.randint(1000, 9999999)
            
        else:
            print("|Ongeldige keuze.\n")
            continue
    
        gebruikers.append({
            "Voornaam": voornaam,
            "Naam": naam,
            "Adres": adres,
            "Geboorte": geboorte,
            "Code" : code,
            "Functie" : functie,
            "gegeven_vak": vak if functie == "1" else None,
            "gekozen_vakken": [],
            "mijn_cursussen": []
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
                    
                    if "gekozen_vakken" not in gebruiker:
                        gebruiker["gekozen_vakken"] = []
                        
                    if "mijn_cursussen" not in gebruiker:
                        gebruiker["mijn_cursussen"] = [] 
               
                    Main(gebruiker)
                    return
            
            print("|Gegevens niet correct. Probeer opnieuw.\n")  
            

        except ValueError:
            print("|Foutieve keuze.")
            print("\n")
            continue

            
        

#-----------------------------------------------Home Screen
    
def Main(gebruiker):
    while True:
        print("\n")
        print("_" *27)
        print(f"WELKOM: {gebruiker['Voornaam']}!")
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
                Cursussen(gebruiker)
                
            elif antwoord == 2:
                Mijn_cursussen(gebruiker)
                
            elif antwoord == 3:
                Betalingen(gebruiker)
                
            elif antwoord == 4:
                Persoonlijke_gegevens(gebruiker)
                
            elif antwoord == 5:
                print("|U word afgemeld.\n")
                break
                
            else:
                print("|Ongeldige keuze.\n")
                continue
                
            
        except ValueError:
            print("|Foutieve keuze.")
            print("\n")
            continue

#-----------------------------------Cursussen

def Cursussen(gebruiker):
    while True:
        print("\n")
        print("_" *33)
        print("Cursussen")
        print("_" *33)
        
        
        for key, (vak, serienummer, leerkracht, prijs, beschrijving) in vakken.items():
            print(f"[{key}] {vak} ")
            print(f"       -Serienummer: {serienummer}")
            print(f"       -Leerkracht: {leerkracht}")
            print(f"       -Prijs: €{prijs}")
            print(f"       -{beschrijving}")
            print("-" * 100)
        
        
        print("0: Terug")
        
        
        try:
            antwoord = input("| ")
            
            
            if antwoord in vakken:
                vak, serienummer, leerkracht, prijs, beschrijving = vakken[antwoord]
                gekozen_vakken = gebruiker["gekozen_vakken"]
                
    
                if gebruiker["Functie"] == "1" and vak == gebruiker.get("gegeven_vak"):
                    print("Je kan je eigen vak niet aankopen.")
                    continue
                
                if vak in [v[0] for v in gekozen_vakken]:
                    print("Je hebt dit vak al gekozen.")
                
                else:
                    gekozen_vakken.append((vak, serienummer, leerkracht, prijs))
                    print(f"{vak} is toegevoegd aan uw betalingen.")
                
            elif antwoord == "0":
                return 
            
            else:
                print("|Ongeldige keuze.\n")
                
        
        except ValueError:
            print("|Foutieve keuze.")
            print("\n")
            
 
 #----------------------------------Betalingen
 
def Betalingen(gebruiker):
    while True:
        print("\n")
        print("_" *27)
        print("Betalingen")
        print("_" *27)
        
        if "gekozen_vakken" not in gebruiker:
            gebruiker["gekozen_vakken"] = []
            
        if "mijn_cursussen" not in gebruiker:
            gebruiker["mijn_cursussen"] = []
        
        gekozen_vakken = gebruiker["gekozen_vakken"]
        mijn_cursussen = gebruiker["mijn_cursussen"]
        
        aantal_vakken = len(gekozen_vakken)
        totaal = 0
        korting = 0
        
        if not gekozen_vakken:
            print("Geen vakken om te betalen.")
        else:
            for i, (vak, serienummer, leerkracht, prijs) in enumerate(gekozen_vakken, start=1):
                print(f"{i}. {vak} ({serienummer}) ({leerkracht}) - €{prijs}")
                totaal += prijs
        

            if gebruiker["Functie"] == "1": 
                korting = totaal * 0.05
                totaal -= korting
                print("-" * 27)
                print(f"Docent korting (5%): -€{korting:.2f}")

            elif gebruiker["Functie"] == "2" and aantal_vakken >= 3:  # Student
                korting = totaal * 0.05
                totaal -= korting
                print("-" * 27)
                print(f"Student korting (5%): -€{korting:.2f}")
        
            print("-" *27)
            print(f"Totaal: €{totaal}\n")
            
         
        print("1: Betalen") 
        print("0: Terug")
        print("_" *27)
        
        
        
        try:
            antwoord = input("| ")
            
            if antwoord == "1":
                mijn_cursussen.extend(gekozen_vakken) 
                gekozen_vakken.clear()                
                print("Betaling geslaagd!")
            
            elif antwoord == "0":
                return
            
            else:
                print("|Ongeldige keuze.\n")
                
        
        except ValueError:
            print("|Foutieve keuze.")
            print("\n")


 #----------------------------------Mijn cursussen


def Mijn_cursussen(gebruiker):
    while True:
        print("\n")
        print("_" *27)
        print("Mijn cursussen")
        print("_" *27)
        
        mijn_cursussen = gebruiker["mijn_cursussen"]
        
        if not mijn_cursussen:
            print("Je hebt nog geen cursussen gekocht.")
        else:
            for i, (vak, serienummer, leerkracht, prijs) in enumerate(mijn_cursussen, start=1):
                print(f"{i}. {vak} ({serienummer}) ({leerkracht}) - €{prijs}")
        
        print("0: Terug")
        print("_" *27)
        
        try:
            antwoord = input("| ")
            
            if antwoord == "0":
                return
            
            else:
                print("|Ongeldige keuze.\n")
                
        except ValueError:
            print("|Foutieve keuze.")
            print("\n")
                
            
#-------------------------------Persoonlijke gegevens
            
def Persoonlijke_gegevens(gebruiker):
    while True:
        print("\n")
        print("_" *27)
        print("Persoonlijke gegevens     ")
        print("_" *27)
        print(f"Voornaam: {gebruiker['Voornaam']}")
        print(f"Naam:     {gebruiker['Naam']}")
        print(f"Adres:    {gebruiker['Adres']}")
        print(f"Geboorte: {gebruiker['Geboorte']}")
        functie_naam = "Docent" if gebruiker["Functie"] == "1" else "Student"
        print(f"Functie:  {functie_naam}")
        if gebruiker["Functie"] == "1":
            print(f"Vak:      {gebruiker['gegeven_vak']}")
        print("0: Terug")
        print("_" *27)
        
        try:
            antwoord = input("| ")
            
            if antwoord == "0":
                return
            
            else:
                print("|Ongeldige keuze.\n")
                
        except ValueError:
            print("|Foutieve keuze.")
            print("\n")
            
                
Aanmelding()