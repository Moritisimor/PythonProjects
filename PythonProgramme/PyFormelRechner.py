#Import von Pi und Sleep und Willkommensnachricht.

from math import pi

print("Willkommen zum Formelrechner, wo Flächen und Volumen verschiedener Körper berechnet werden.")
print("Möchten Sie die Fläche oder Das Volumen ausrechnen?")

#Erfassung, ob der Nutzer Volumen oder Fläche ausrechnen will.

flaechenKoerper = ["Viereck", "Dreieck", "Kreis"]
volumenKoerper = ["Kegel", "Pyramide", "Quader", "Sphäre", "Würfel", "Prisma"]

#Globable While True Schleife, um zu sehen, ob der Nutzer noch mal was ausrechnen will.

while True:
    while True:
        VOF = input("Volumen oder Fläche: ")
        if VOF.lower() in["volumen","fläche"]:
            break
        else:
            print("Bitte wählen Sie Volumen oder Fläche.")

    #Erfassung, welchen Körper der Nutzer berechnen will.

    while True:
        if VOF.lower() == "fläche": #Falls Fläche ausgewählt wurde.
            print("Momentan sind folgende Körper verfügbar:") #Verfügbare Körper Zeile für Zeile aufgelistet.
            for koerper in flaechenKoerper :
                print("-" + koerper)

            koerperAuswahl = input("Wählen Sie einen der Körper aus: ") #Körperauswahl.
            if koerperAuswahl.lower() in [koerper.lower() for koerper in flaechenKoerper]:
                break
            else:
                print("Bitte wählen Sie einen gültigen Körper aus.")

        elif VOF.lower() == "volumen": #Falls Volumen ausgewählt wurde.
            print("Momentan sind folgende Körper verfügbar:") #Verfügbare Körper werden Zeile für Zeile aufgelistet.
            for koerper in volumenKoerper:
                print("-" + koerper)
            
            koerperAuswahl = input("Wählen Sie einen der Körper aus: ")
            if koerperAuswahl.lower() in [koerper.lower() for koerper in volumenKoerper]:
                break
            else:
                print("Bitte wählen Sie einen gültigen Körper aus.")

    #Eigentliche Berechnung von Fläche und Volumen.
    #Try-Except Block um Fehler abzufangen bei ungültiger Eingabe.

    try:
            if koerperAuswahl.lower() == "viereck":
                FlaecheViereckA = float(input("Bitte geben Sie A an: "))
                FlaecheViereckB = float(input("Bitte geben Sie B an: "))
                print(FlaecheViereckA * FlaecheViereckB)

                print("(Hinweis: Ergebnis ist in Quadrateinheiten)")
                
            elif koerperAuswahl.lower() == "dreieck":
                GrundseiteDreieck = float(input("Bitte geben Sie die Grundseite an: "))
                HoeheDreieck = float(input("Bitte geben Sie die Höhe an: "))
                GH = (GrundseiteDreieck * HoeheDreieck)
                print(GH / 2)
                print("(Hinweis: Ergebnis ist in Quadrateinheiten)")

            elif koerperAuswahl.lower() == "kreis":
                RadiusKreis = float(input("Bitte geben Sie den Radius an: "))
                print(pi * RadiusKreis * RadiusKreis)
                print("(Hinweis: Ergebnis ist in Quadrateinheiten)")

            #Rein der Übersicht-dienende Trennung von Fläche und Volumen.

            elif koerperAuswahl.lower() == "kegel":
                RadiusKegel = float(input("Bitte geben Sie den Radius an: "))
                HoeheKegel = float(input("Bitte geben Sie die Höhe an: "))
                print(1 / 3 * pi * RadiusKegel * RadiusKegel * HoeheKegel)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
            
            elif koerperAuswahl.lower() == "würfel":
                WuerfelA = float(input("Bitte geben Sie A an: "))
                print(WuerfelA * WuerfelA * WuerfelA)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
                
            elif koerperAuswahl.lower() == "pyramide":
                PyramideA = float(input("Bitte geben Sie A an: "))
                HoehePyramide = float(input("Bitte geben Sie die Höhe an: "))
                print((1 / 3) * PyramideA * PyramideA * HoehePyramide)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
                
            elif koerperAuswahl.lower() == "quader":
                QuaderA = float(input("Bitte geben Sie A an: "))
                QuaderB = float(input("Bitte geben Sie B an: "))
                QuaderC = float(input("Bitte geben Sie C an: "))
                print(QuaderA * QuaderB * QuaderC)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
                
            elif koerperAuswahl.lower() == "prisma":
                PrismaGrundFlaeche = float(input("Bitte geben Sie die Grundfläche an: "))
                PrismaHoehe = float(input("Bitte geben Sie die Höhe an: "))
                print(PrismaGrundFlaeche * PrismaHoehe)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
                
            elif koerperAuswahl.lower() == "sphäre":
                SphaereRadius = float(input("Bitte geben Sie den Radius an: "))
                print((4 / 3) * pi * SphaereRadius * SphaereRadius  * SphaereRadius)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
                
            nochmal = input("Möchten Sie noch etwas berechnen? ")
            if nochmal in["nein","n"]:
                break

    except ValueError:
        print("Bitte richtige Zahlen eingeben.")
        print("Erlaubt sind Gleitkommazahlen (3.5, 6.4, 15.3 etc.) und Ganzzahlen (1, 2, 5, 10 etc.).")