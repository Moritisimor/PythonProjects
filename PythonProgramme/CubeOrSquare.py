def square(x):
    y = x * x
    print(y)

def cube(x):
    y = x * x * x
    print(y)

try:
    x = float(input("Enter a number you would like to cube or square: "))
    cubeOrSquare = input("Select cube or square: ")
    if cubeOrSquare.lower() == "square":
        square(x)
    elif cubeOrSquare.lower() == "cube":
        cube(x)
    else:
        print("Select a valid option next time.")
except ValueError:
    print("Only enter numbers.")