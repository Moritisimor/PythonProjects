class Artikel:
    def __init__(self, bezeichnung, preis, stueckzahl):
        self.bezeichnung = bezeichnung
        self.preis = preis
        self.stueckzahl = stueckzahl

artikelListe = [
Artikel("PC", 249.99, 14),
Artikel("Laptop", 199.99, 18),
Artikel("Tastatur", 17.49, 70),
Artikel("Maus", 9.99, 93)
]

for artikel in artikelListe:
    print("-" + artikel.bezeichnung + " " + str(artikel.preis) + "€")