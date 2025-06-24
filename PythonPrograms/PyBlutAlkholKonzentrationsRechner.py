print("Willkommen zum Blutalkoholkonzentrationsrechner.") # Willkommensnachricht
while True:
    try:
        anzahlBier = float(input("Wie viele Flaschen oder Gläser Bier haben Sie getrunken? (0,5L): ")) # Eingabe Bier
        anzahlKorn = float(input("Wie viele Flaschen Korn haben Sie getrunken? (0,02L): ")) # Eingabe Korn
        gewicht = float(input("Geben Sie Ihr Gewicht in KG an: ")) # Eingabe Gewicht
        break
    except ValueError:
        print("Bitte geben Sie nur Zahlen an.", "\n", "Fange neu an...")

while True: # Wenn der folgende Input nicht männlich oder weiblich entspricht geht es hier wieder zurück
    geschlecht = input("Sind Sie männlich oder weiblich?: ") # Eingabe Geschlecht
    if geschlecht.lower() in["männlich","m","weiblich","w"]: # Prüfung ob die Eingabe einer der gültigen Einträge entspricht
        break # Wenn das so ist, brich die Schleife ab.
    else: # Sonst
        print("Bitte wählen Sie ein gültiges geschlecht aus.") # Sag dem Nutzer, dass seine Eingabe ungültig war und geh zurück zum Anfang der While True Schleife

# Berechnungen

if geschlecht in ["m", "männlich"]:
    geschlechtGewichtBilanz = 0.68 * gewicht
else:
    geschlechtGewichtBilanz = 0.55 * gewicht
proMille = ((18 * anzahlBier ) + (5 * anzahlKorn) / geschlechtGewichtBilanz)

print("Ihre geschätzte Blutalkoholkonzentration liegt bei:", proMille) #Ergebnis
if proMille > 1.09:
    print("Ihre proMille ist deutlich zu hoch, Autofahren sehr illegal! Straftat mit bis zu 5 Jahre Führerscheinentzug und möglicher Freiheitsstrafe.")
elif proMille > 0.49:
    print("Ihre proMille ist zu hoch, Autofahren illegal! Ordnungswidrigkeit mit bis zu 1000€ Strafe.")
else:
    print("Autofahren wäre kein Problem, sofern Sie sich dazu bereit fühlen.")