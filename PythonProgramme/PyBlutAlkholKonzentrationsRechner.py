print("Willkommen zum Blutalkoholkonzentrationsrechner.") # Willkommensnachricht
while True:
    try:
        AnzahlBier = float(input("Wie viele Flaschen oder Gläser Bier haben Sie getrunken? (0,5L): ")) # Eingabe Bier
        AnzahlKorn = float(input("Wie viele Flaschen Korn haben Sie getrunken? (0,02L): ")) # Eingabe Korn
        Gewicht = float(input("Geben Sie Ihr Gewicht in KG an: ")) # Eingabe Gewicht#
        break
    except ValueError:
        print("Bitte geben Sie nur Zahlen an.", "\n", "Fange neu an...")

while True: # Wenn der folgende Input nicht männlich oder weiblich entspricht geht es hier wieder zurück
    Geschlecht = input("Sind Sie männlich oder weiblich?: ") # Eingabe Geschlecht
    if Geschlecht.lower() in["männlich","m","weiblich","w"]: # Prüfung ob die Eingabe einer der gültigen Einträge entspricht
        break # Wenn das so ist, brich die Schleife ab.
    else: # Sonst
        print("Bitte wählen Sie ein gültiges Geschlecht aus.") # Sag dem Nutzer, dass seine Eingabe ungültig war und geh zurück zum Anfang der While True Schleife

if Geschlecht.lower() in["männlich","m"]: # Wenn die Eingabe männlich ist:
    GeschlechtFaktor = 0.68 #Definierung des Geschlechtfaktors bei Männlichkeit
else: # Sonst:
    GeschlechtFaktor = 0.55 #Definierung des Geschlechtfaktors bei Weiblichkeit

#Berechnungen

GramAlkoholBier = 18 * AnzahlBier
GramAlkoholKorn = 5 * AnzahlKorn
GeschlechtGewichtBilanz = GeschlechtFaktor * Gewicht
if AnzahlBier == 0: # Wenn der Nutzer kein Bier getrunken hat, fällt das nicht in die Berechnung, denn durch Null teilen wird nichts bringen
    BAK = (GramAlkoholKorn / GeschlechtGewichtBilanz)
elif AnzahlKorn == 0: # Gleiches Prinzip, nur mit Korn
    BAK = (GramAlkoholBier / GeschlechtGewichtBilanz)
else: # Wenn beide größer als Null 
    BAK = ((GramAlkoholBier + GramAlkoholKorn) / GeschlechtGewichtBilanz)

print("Ihre geschätzte Blutalkoholkonzentration liegt bei:", BAK) #Ergebnis
if BAK > 1.09:
    print("Ihre BAK ist deutlich zu hoch, Autofahren sehr illegal! Straftat mit bis zu 5 Jahre Führerscheinentzug und möglicher Freiheitsstrafe.")
elif BAK > 0.49:
    print("Ihre BAK ist zu hoch, Autofahren illegal! Ordnungswidrigkeit mit bis zu 1000€ Strafe.")