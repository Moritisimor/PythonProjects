class Artikel:
    def __init__(self, bezeichnung, preis, stueckzahl):
        self.bezeichnung = bezeichnung
        self.preis = preis
        self.stueckzahl = stueckzahl

    # Kundenmethoden Anfang

    def kunde_kaufen(self):
        if self.stueckzahl == 0:
            print("Entschuldigung, aber das Produkt ist ausverkauft.")
        else:
            self.stueckzahl = -1

    def kunde_rueckgabe(self):
        self.stueckzahl = +1

    def auflistung_kundenmethoden(self):
        return [m for m in dir(self) if m.startswith("kunde")]

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

while True:
    artikelAuswahl = input("Wählen Sie Ihren gewünschten Artikel aus: ")
    if artikelAuswahl.lower() in artikelListePruefung:
        print("Auswahl erfolgreich getätigt!")
        break
    else:
        print("Bitte wählen Sie einen gültigen Artikel aus.")

artikelAuswahlOption = input("Wählen Sie eine Option für den Artikel aus: ")