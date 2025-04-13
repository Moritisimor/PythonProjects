from time import sleep

print("Willkommen zum Blutalkoholkonzentrationsrechner.") #Willkommensnachricht
AnzahlBier = float(input("Wie viele Flaschen oder Gläser Bier haben Sie getrunken? (0,5L): ")) #Eingabe Anzahl Bier
AnzahlKorn = float(input("Wie viele Flaschen Korn haben Sie getrunken? (0,02L): ")) #Eingabe Anzahl Korn
Gewicht = float(input("Geben Sie Ihr Gewicht in KG an: ")) #Eingabe Gewicht
while True: #Da Geschlecht ein String ist, kann es potenziell undefiniert sein oder die Eingabe nicht im Array liegen
    Geschlecht = input("Sind Sie männlich oder weiblich?: ") #Eingabe Geschlecht
    if Geschlecht.lower() in["männlich","m","weiblich","w"]:
        break
    else: #Deswegen werden Fehler hier abgefangen bei ungültiger Eingabe
        print("Bitte wählen Sie ein gültiges Geschlecht aus.")

if Geschlecht.lower() in["männlich","m"]:
    GeschlechtFaktor = 0.68 #Definierung des Geschlechtfaktors bei Männlichkeit
else:
    GeschlechtFaktor = 0.55 #Definierung des Geschlechtfaktors bei Weiblichkeit

#Berechnungen

GramAlkoholBier = 18 * AnzahlBier
GramAlkoholKorn = 5 * AnzahlKorn
GeschlechtGewichtBilanz = GeschlechtFaktor * Gewicht
if AnzahlBier == 0:
    BAK = (GramAlkoholKorn / GeschlechtGewichtBilanz)
elif AnzahlKorn == 0:
    BAK = (GramAlkoholBier / GeschlechtGewichtBilanz)
else:
    BAK = ((GramAlkoholBier + GramAlkoholKorn) / GeschlechtGewichtBilanz)

print("Ihre geschätzte Blutalkoholkonzentration liegt bei:",BAK) #Ergebnis
sleep(2)
if BAK > 1.09:
    print("Ihre BAK ist deutlich zu hoch, Autofahren sehr illegal! Straftat mit bis zu 5 Jahre Führerscheinentzug und möglicher Freiheitsstrafe.")
    sleep(10)
elif BAK > 0.49:
    print("Ihre BAK ist zu hoch, Autofahren illegal! Ordnungswidrigkeit mit bis zu 1000€ Strafe.")
    sleep(10)