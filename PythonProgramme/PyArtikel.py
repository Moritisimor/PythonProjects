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

def bestellbestaetigung(nachname, vorname, strasse, hausnummer, zahlungsmethode, lieferzeitraum, bestellter_artikel):
    print("Sie haben bestellt:")
    print(str(artikelAuswahlMenge) + "x", bestellter_artikel)
    print("Ihre Lieferadresse:")
    print(vorname, nachname)
    print(strasse, str(hausnummer))
    print("Voraussichtlicher Lieferzeitraum:")
    print(lieferzeitraum)
    print("Ihre Zahlungsmethode:")
    print(zahlungsmethode)
    input("Drücken Sie Enter zum bestätigen: ")


zahlungsmethodenListe = ["Banküberweisung", "Kreditkarte", "DebitKarte", "BuyFriend", "Rechnung"]

artikelListe = [
pc := Artikel("PC", 249.99, 14),
laptop := Artikel("Laptop", 199.99, 18),
tastatur := Artikel("Tastatur", 17.49, 70),
maus := Artikel("Maus", 9.99, 93)
]

artikelListePruefung = []
for artikel in artikelListe:
    artikelListePruefung.insert(0, artikel.bezeichnung.lower())

while True:
    for artikel in artikelListe:
        print("-", artikel.bezeichnung, str(artikel.preis) + "€")


    while True:
        artikelAuswahl = input("Wählen Sie den Artikel aus, den sie kaufen möchten: ")
        if artikelAuswahl.lower() in artikelListePruefung:
            break
        else:
            print("Bitte wählen Sie einen gültigen Artikel aus.")

    while True:
        try:
            artikelAuswahlMenge = int(input("Geben Sie an, wie viel Sie bestellen wollen: "))
            break
        except ValueError:
            print("Bitte Geben Sie nur Ganzzahlen an.")

    while True:
        bestellungNachname = input("Geben Sie Ihren Nachnamen an: ")
        bestellungVorname = input("Geben Sie Ihren Vornamen an: ")
        bestellungStrasse = input("Geben Sie Ihren Straßennamen an: ")
        while True:
            try:
                bestellungHausnummer = int(input("Geben Sie Ihre Hausnummer an: "))
                break
            except ValueError:
                print("Bitte Geben Sie nur Ganzzahlen an.")
        break

    while True:
        for zahlungsMethode in zahlungsmethodenListe:
            print("-", zahlungsMethode)

        bestellungZahlungsmethode = input("Wählen Sie Ihre Zahlungsmethode aus: ")
        if bestellungZahlungsmethode.lower() in (zahlungsMethode.lower() for zahlungsMethode in zahlungsmethodenListe):
            break
        else:
            print("Bitte wählen Sie eine der oben genannten Zahlungsmethoden aus.")

    bestellungLieferzeitraum = str(randint(2, 3)) + " Tage"

    bestellbestaetigung(bestellungNachname, bestellungVorname, bestellungStrasse, bestellungHausnummer,
    bestellungZahlungsmethode, bestellungLieferzeitraum, artikelAuswahl)

    print("Möchten Sie noch etwas bestellen?")
    nochMal = input("J/N: ")
    if nochMal.lower() in ["j", "ja"]:
        continue
    elif nochMal.lower() in ["n", "nein"]:
        break
    else:
        print("Bitte Ja oder Nein eingeben.")
