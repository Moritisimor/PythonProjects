#Import von Pi und Sleep und Willkommensnachricht

from math import pi
from time import sleep

print("Willkommen zum Formelrechner, wo Flächen und Volumen verschiedener Körper berechnet werden.")
print("Möchten Sie die Fläche oder Das Volumen ausrechnen?")

#Erfassung, ob der Nutzer Volumen oder Fläche ausrechnen will.
while True:
    while True:
        VOF = input("Volumen oder Fläche: ")
        if VOF.lower() in["volumen","fläche"]:
            break
        else:
            print("Bitte wählen Sie Volumen oder Fläche: ")

    #Erfassung, welchen Körper der Nutzer berechnen will

    while True:
        if VOF.lower() in["fläche"]:
            VOF = (input("Wählen Sie zwischen Viereck, Dreieck oder Kreis: "))
        elif VOF.lower() in["volumen"]:
            VOF = (input("Wählen Sie zwischen Prisma, Sphäre, Kegel, Würfel, Pyramide oder Quader: "))
        else:
            break

    #Eigentliche Berechnung von Fläche und Volumen sowie Ausgabe
    try:
            if VOF.lower() in["viereck"]:
                FlaecheViereckA = float(input("Bitte geben Sie A an: "))
                FlaecheViereckB = float(input("Bitte geben Sie B an: "))
                print(FlaecheViereckA * FlaecheViereckB)
                sleep(1)
                print("(Hinweis: Ergebnis ist in Quadrateinheiten)")
                
            elif VOF.lower() in["dreieck"]:
                GrundseiteDreieck = float(input("Bitte geben Sie die Grundseite an: "))
                HoeheDreieck = float(input("Bitte geben Sie die Höhe an: "))
                GH = (GrundseiteDreieck * HoeheDreieck)
                print(GH / 2)
                sleep(1)
                print("(Hinweis: Ergebnis ist in Quadrateinheiten)")

            elif VOF.lower() in["kreis"]:
                RadiusKreis = float(input("Bitte geben Sie den Radius an: "))
                print(pi * RadiusKreis * RadiusKreis)
                sleep(1)
                print("(Hinweis: Ergebnis ist in Quadrateinheiten)")

            #Rein der Übersicht-dienende Trennung von Fläche und Volumen

            elif VOF.lower() in["kegel"]:
                RadiusKegel = float(input("Bitte geben Sie den Radius an: "))
                HoeheKegel = float(input("Bitte geben Sie die Höhe an: "))
                print(1 / 3 * pi * RadiusKegel * RadiusKegel * HoeheKegel)
                sleep(1)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
            
            elif VOF.lower() in["würfel"]:
                WuerfelA = float(input("Bitte geben Sie A an: "))
                print(WuerfelA * WuerfelA * WuerfelA)
                sleep(1)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
                
            elif VOF.lower() in["pyramide"]:
                PyramideA = float(input("Bitte geben Sie A an: "))
                HoehePyramide = float(input("Bitte geben Sie die Höhe an: "))
                print((1 / 3) * PyramideA * PyramideA * HoehePyramide)
                sleep(1)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
                
            elif VOF.lower() in["quader"]:
                QuaderA = float(input("Bitte geben Sie A an:"))
                QuaderB = float(input("Bitte geben Sie B an:"))
                QuaderC = float(input("Bitte geben Sie C an:"))
                print(QuaderA * QuaderB * QuaderC)
                sleep(1)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
                
            elif VOF.lower() in["prisma"]:
                PrismaGrundFlaeche = float(input("Bitte geben Sie die Grundfläche in cm² an: "))
                PrismaHoehe = float(input("Bitte geben Sie die Höhe an: "))
                print(PrismaGrundFlaeche * PrismaHoehe)
                sleep(1)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
                
            elif VOF.lower() in["sphäre"]:
                SphaereRadius = float(input("Bitte geben Sie den Radius an: "))
                print((3 / 4) * SphaereRadius * SphaereRadius * SphaereRadius  * pi)
                sleep(1)
                print("(Hinweis: Ergebnis ist in Kubikeinheiten)")
                
            nochmal = input("Möchten Sie noch etwas berechnen? ")
            if nochmal in["nein","n"]:
                break
            else:
                continue

    except(ValueError):
        print("Bitte richtige Zahlen eingeben.")
        print("Erlaubt sind Gleitkommazahlen (3.5, 6.4, 15.3 etc.) und Ganzzahlen (1, 2, 5, 10 etc.)")