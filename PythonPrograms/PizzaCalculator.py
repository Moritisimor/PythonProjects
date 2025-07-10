from math import pi

def getvalidfloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please only enter numbers.")

print("Welcome to the pizza calculator. \nThis tool will tell you which of two pizzas offers more value per cm².")
while True:

    radius1 = getvalidfloat("Enter the radius of the first pizza: ")
    price1 = getvalidfloat("Enter the price of the first pizza: ")
    radius2 = getvalidfloat("Enter the radius of the second pizza: ")
    price2 = getvalidfloat("Enter the price of the second pizza: ")

    # Calculation of Price/cm²

    area1 = (pi * radius1 * radius1)
    area2 = (pi * radius2 * radius2)
    pricePerSquareScm1 = (price1 / area1)
    pricePerSquareScm2 = (price2 / area2)

    # Comparison

    if pricePerSquareScm1 > pricePerSquareScm2:
        print("Pizza 2 holds more value per cm² than pizza 1.")
    elif pricePerSquareScm1 < pricePerSquareScm2:
        print("Pizza 1 holds more value per cm² than pizza 2.")
    else:
        print("Both pizzas hold the same value per cm².")

    print("Would you like to calculate another pizza?")
    again = input("Y/N: ")
    if again.lower() in ["y", "yes"]:
        continue
    else:
        exit()