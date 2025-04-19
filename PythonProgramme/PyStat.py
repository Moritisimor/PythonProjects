#Willkommensnachricht und Import von Math

print("Willkommen zum Simple PyStat, Einem Statistik Tool")
Liste = (input("Geben Sie Ihre Liste an Daten an (x, y, z): "))
Liste = [float(num) for num in Liste.split()]
ArithMittel = sum(Liste) / len(Liste)
print(ArithMittel)
