def square(x):
    y = x * x
    return y

def cube(x):
    y = x * x * x
    return y

try:
    x = float(input("Enter a number you would like to cube or square: "))
    cubeOrSquare = input("Select cube or square: ")
    if cubeOrSquare.lower() == "square":
        print(square(x))
    elif cubeOrSquare.lower() == "cube":
        print(cube(x))
    else:
        print("Select a valid option next time.")
except ValueError:
    print("Only enter numbers.")