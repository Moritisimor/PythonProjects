class Auto:
    def __init__(self, Marke, PS):
        self.Marke = Marke
        self.PS = PS

    def fahren(self):
        print("Das Auto der Marke " + self.Marke + " fährt.")

BMW = Auto("BMW", 100)

print(BMW.Marke)
BMW.fahren()