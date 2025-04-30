print("Welcome to the unit converter written in python.")
print("What would you like to convert?")
print("-" "Temperature")
print("-" "Length")
print("-" "Mass")

def Fahrenheit():
    StartValue = int(input("Enter your Fahrenheit value: "))
    ConvertToUnit = input("Enter the Value you want to convert to: ")
    if ConvertToUnit.lower() in ["celsius"]:
        print("In Celsius: ", (StartValue - 32) * 5/9)
    elif ConvertToUnit.lower() in ["kelvin"]:
        print("In Kelvin: ", ((StartValue - 32) / 1.8) + 273.15)

Fahrenheit()