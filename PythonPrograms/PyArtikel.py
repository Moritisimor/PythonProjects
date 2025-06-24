from random import randint

class Artikel:
    def __init__(self, bezeichnung, preis, stueckzahl):
        self.bezeichnung = bezeichnung
        self.preis = preis
        self.stueckzahl = stueckzahl

    def kunde_kaufen(self, menge):
        if self.stueckzahl < menge:
            print("Entschuldigung, aber so viel haben wir nicht mehr auf Lager.")
        else:
            self.stueckzahl -= menge

    def kunde_rueckgabe(self, menge):
        self.stueckzahl += menge

    def besitzer_lieferung(self, menge):
        self.stueckzahl += menge

zahlungsmethodenListe = ["Banküberweisung", "Kreditkarte", "Debitkarte", "BuyFriend", "Rechnung"]

artikelListe = [
pc := Artikel("PC", 249.99, 14),
laptop := Artikel("Laptop", 199.99, 18),
tastatur := Artikel("Tastatur", 17.49, 70),
maus := Artikel("Maus", 9.99, 93)
]
artikelListePruefung = []

for artikel in artikelListe:
    artikelListePruefung.insert(0, artikel.bezeichnung.lower())

while True: # Hier geht es zurück wenn der Nutzer noch was bestellen will.
    for artikel in artikelListe:
        print("-", artikel.bezeichnung, str(artikel.preis) + "€")

    while True: # Hier geht es zurück wenn der Nutzer einen Artikel auswählt, der nicht existiert.
        artikelAuswahl = input("Wählen Sie den Artikel aus, den sie kaufen möchten: ")
        if artikelAuswahl.lower() in artikelListePruefung:
            break
        else:
            print("Bitte wählen Sie einen gültigen Artikel aus.")

    while True: # Hier geht es zurück, wenn der Nutzer alles eingibt, was keine positive Ganzzahl ist.
        try:
            artikelAuswahlMenge = int(input("Geben Sie an, wie viel Sie bestellen wollen: "))
            if artikelAuswahlMenge >= 1:
                break
            else:
                print("Kann nicht 0 oder weniger bestellen.")
        except ValueError:
            print("Bitte Geben Sie nur positive Ganzzahlen an.")

    bestellungNachname = input("Geben Sie Ihren Nachnamen an: ")
    bestellungVorname = input("Geben Sie Ihren Vornamen an: ")
    bestellungStrasse = input("Geben Sie Ihren Straßennamen an: ")
    bestellungHausnummer = input("Geben Sie Ihre Hausnummer an: ")

    while True: # Hier geht es zurück, wenn der Nutzer eine Zahlungsmethode angibt, die nicht existiert.
        for zahlungsMethode in zahlungsmethodenListe:
            print("-", zahlungsMethode)

        bestellungZahlungsmethode = input("Wählen Sie Ihre Zahlungsmethode aus: ")
        if bestellungZahlungsmethode.lower() in (zahlungsMethode.lower() for zahlungsMethode in zahlungsmethodenListe):
            break
        else:
            print("Bitte wählen Sie eine der oben genannten Zahlungsmethoden aus.")

    bestellungLieferzeitraum = str(randint(2, 3)) + " Tage"

    print("Sie haben bestellt:")
    print(str(artikelAuswahlMenge) + "x", artikelAuswahl + "\n")
    print("Ihre Lieferadresse:")
    print(bestellungVorname, bestellungNachname)
    print(bestellungStrasse, bestellungHausnummer + "\n")
    print("Voraussichtlicher Lieferzeitraum:")
    print(bestellungLieferzeitraum + "\n")
    print("Ihre Zahlungsmethode:")
    print(bestellungZahlungsmethode + "\n")
    input("Drücken Sie Enter zum bestätigen: ")

    print("Möchten Sie noch etwas bestellen?")
    nochMal = input("J/N: ")
    if nochMal.lower() in ["j", "ja"]:
        continue
    elif nochMal.lower() in ["n", "nein"]:
        break
    else:
        print("Bitte Ja oder Nein eingeben.")
