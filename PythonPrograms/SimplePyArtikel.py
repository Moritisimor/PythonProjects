# Eine vereinfachte Version von PyArtikel, ausgestattet mit nur dem Nötigsten.

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

artikelListe = [
pc := Artikel("PC", 249.99, 14),
laptop := Artikel("Laptop", 199.99, 18),
tastatur := Artikel("Tastatur", 17.49, 70),
maus := Artikel("Maus", 9.99, 93)
]
artikelListePruefung = []

for artikel in artikelListe:
    artikelListePruefung.insert(0, artikel.bezeichnung.lower())
    print("-", artikel.bezeichnung, str(artikel.preis) + "€")