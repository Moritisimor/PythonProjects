class Artikel:
    def __init__(self, bezeichnung, preis, stueckzahl):
        self.bezeichnung = bezeichnung
        self.preis = preis
        self.stueckzahl = stueckzahl

    def kunde_kaufen(self):
        if self.stueckzahl == 0:
            print("Entschuldigung, aber das Produkt ist ausverkauft.")
        else:
            self.stueckzahl -= 1

    def kunde_rueckgabe(self):
        self.stueckzahl += 1

    def besitzer_lieferung(self, anzahl):
        self.stueckzahl = self.stueckzahl + anzahl

artikelListe = [
pc := Artikel("PC", 249.99, 14),
laptop := Artikel("Laptop", 199.99, 18),
tastatur := Artikel("Tastatur", 17.49, 70),
maus := Artikel("Maus", 9.99, 93)
]

artikelListePruefung = []

def zeig_artikel():
    for artikel in artikelListe:
        print("-", artikel.bezeichnung, str(artikel.preis) + "€")
        artikelListePruefung.insert(0, artikel.bezeichnung.lower())

zeig_artikel()

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