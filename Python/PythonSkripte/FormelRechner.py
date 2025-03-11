#Import von Math und Willkommensnachricht

import math
print("Willkommen zum Formelrechner, wo Flächen und Volumen verschiedener Körper berechnet werden.")
print("Möchten Sie die Fläche oder Das Volumen ausrechnen?")

#Erfassung, ob der Nutzer Volumen oder Fläche ausrechnen will.

while True:
    VOF = input("Volumen oder Fläche: ")
    if VOF in["Volumen","volumen","Fläche","fläche"]:
        break
    else:
        print("Bitte wählen Sie Volumen oder Fläche: ")

#Erfassung, welchen Körper der Nutzer berechnen will

while True:
    if VOF in["Fläche","fläche"]:
        VOF = (input("Wählen Sie zwischen Viereck, Dreieck oder Kreis: "))
    elif VOF in["Volumen","volumen"]:
        VOF = (input("Wählen Sie zwischen Prisma, Sphäre, Kegel, Würfel, Pyramide oder Quader: "))
    else:
        break

#Eigentliche Berechnung von Fläche und Volumen sowie Ausgabe

if VOF in["Viereck","viereck"]:
    FlaecheViereckA = float(input("Bitte geben Sie A an: "))
    FlaecheViereckB = float(input("Bitte geben Sie B an: "))
    print(FlaecheViereckA * FlaecheViereckB)
    print("(Hinweis: Ergebnis ist in Quadrateinheiten)")

elif VOF in["Dreieck","dreieck"]:
    GrundseiteDreieck = float(input("Bitte geben Sie die Grundseite an: "))
    HoeheDreieck = float(input("Bitte geben Sie die Höhe an: "))
    GH = (GrundseiteDreieck * HoeheDreieck)
    print(GH / 2)
    print("(Hinweis: Ergebnis ist in Quadrateinheiten)")

elif VOF in["Kreis","kreis"]:
    RadiusKreis = float(input("Bitte geben Sie den Radius an: "))
    print(math.pi * RadiusKreis * RadiusKreis)
    print("(Hinweis: Ergebnis ist in Quadrateinheiten)")

#Rein der Übersicht-dienende Trennung von Fläche und Volumen

elif VOF in["Kegel","kegel"]:
    RadiusKegel = float(input("Bitte geben Sie den Radius an: "))
    HoeheKegel = float(input("Bitte geben Sie die Höhe an: "))
    print(1 / 3 * math.pi * RadiusKegel * RadiusKegel * HoeheKegel)
    print("(Hinweis: Ergebnis ist in Kubikeinheiten)")

elif VOF in["Würfel","würfel"]:
    WuerfelA = float(input("Bitte geben Sie A an: "))
    print(WuerfelA * WuerfelA * WuerfelA)
    print("(Hinweis: Ergebnis ist in Kubikeinheiten)")

elif VOF in["Pyramide", "pyramide"]:
    PyramideA = float(input("Bitte geben Sie A an: "))
    HoehePyramide = float(input("Bitte geben Sie die Höhe an: "))
    print((1 / 3) * PyramideA * PyramideA * HoehePyramide)
    print("(Hinweis: Ergebnis ist in Kubikeinheiten)")

elif VOF in["Quader","quader"]:
    QuaderA = float(input("Bitte geben Sie A an:"))
    QuaderB = float(input("Bitte geben Sie B an:"))
    QuaderC = float(input("Bitte geben Sie C an:"))
    print(QuaderA * QuaderB * QuaderC)
    print("(Hinweis: Ergebnis ist in Kubikeinheiten)")

elif VOF in["Prisma", "prisma"]:
    PrismaGrundFlaeche = float(input("Bitte geben Sie die Grundfläche in cm² an: "))
    PrismaHoehe = float(input("Bitte geben Sie die Höhe an: "))
    print(PrismaGrundFlaeche * PrismaHoehe)
    print("(Hinweis: Ergebnis ist in Kubikeinheiten)")

elif VOF in["Sphäre","Sphäre"]:
    SphaereRadius = float(input("Bitte geben Sie den Radius an: "))
    print((3 / 4) * SphaereRadius * SphaereRadius * SphaereRadius  * math.pi)
    print("(Hinweis: Ergebnis ist in Kubikeinheiten)")