#Willkommensnachricht, Eingabeerfassungen und Import von Pi sowie Sleep


from math import pi
from time import sleep

print("Willkommen zum Pizza Rechner, einem Tool, das Ihnen Zeigt, welche von 2 Pizzen günstiger pro cm² ist.")
Radius1 = float(input("Geben Sie den Radius der ersten Pizza in cm an: "))
Preis1 = float(input("Geben Sie den Preis der ersten Pizza in Euro an: "))
Radius2 = float(input("Geben Sie den Radius der zweiten Pizza in cm an: "))
Preis2 = float(input("Geben Sie den Preis der zweiten Pizza in Euro an: "))

#Ab hier werden die Preise in Euro pro cm² berechnet


Flaeche1 = (pi * Radius1 * Radius1)
Flaeche2 = (pi * Radius2 * Radius2)
Preisprocm1 = (Preis1 / Flaeche1 )
Preisprocm2 = (Preis2 / Flaeche2 )

#Berechnung

if Preisprocm1 > Preisprocm2:
    print("Pizza 2 ist preiswerter als Pizza 1.")
    sleep(3)
elif Preisprocm1 < Preisprocm2:
    print("Pizza 1 ist preiswerter als Pizza 2.")
    sleep(3)
else:
    print("Beide Pizzen sind gleich preiswert.")
    sleep(3)