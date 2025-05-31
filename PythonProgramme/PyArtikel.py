class Artikel:
    def __init__(self, bezeichnung, preis, stueckzahl):
        self.bezeichnung = bezeichnung
        self.preis = preis
        self.stueckzahl = stueckzahl

    def kaufen(self):
        if self.stueckzahl == 0:
            print("Entschuldigung, aber das Produkt ist ausverkauft.")
        else:
            self.stueckzahl -= 1

    def rueckgabe(self):
        self.stueckzahl += 1

artikelListe = [
pc := Artikel("PC", 249.99, 14),
laptop := Artikel("Laptop", 199.99, 18),
tastatur := Artikel("Tastatur", 17.49, 70),
maus := Artikel("Maus", 9.99, 93)
]

artikelListePruefung = []

for artikel in artikelListe:
    print("-", artikel.bezeichnung, str(artikel.preis) + "€")
    artikelListePruefung.insert(0, artikel.bezeichnung.lower())

print(artikelListePruefung)

while True:
    artikelAuswahl = input("Wählen Sie Ihren gewünschten Artikel aus: ")
    if artikelAuswahl.lower() in artikelListePruefung:
        print("Auswahl erfolgreich getätigt!")
        break
    else:
        print("Bitte wählen Sie einen gültigen Artikel aus.")