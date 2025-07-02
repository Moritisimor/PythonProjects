from math import pi

def square(x):
    return x * x

def cube(x):
    return x * x * x

def triangle(base, height):
    return (base * height) / 2

def circle(radius):
    return pi * square(radius)

def cone(radius, height):
    return (1 / 3) * pi * square(radius) * height
                
def pyramid(a, height):
    return (1 / 3) * square(a) * height
                
def cuboid(a, b, c):
    return a * b * c

def prism(baseArea, height):
    return baseArea * height

def sphere(radius):
    return (4 / 3) * pi * cube(radius)

funcsDict = {
    "square"    : square,
    "cube"      : cube,
    "triangle"  : triangle,
    "circle"    : circle,
    "cone"      : cone,
    "pyramid"   : pyramid,
    "cuboid"    : cuboid,
    "prism"     : prism,
    "sphere"    : sphere
}

for func in funcsDict:
    print(f"- {func}")
while True:
    bodyToCalc = input("Enter the body you would like to calculate: ").lower().strip()
    if bodyToCalc in (func.lower() for func in funcsDict):
        break
    elif bodyToCalc == "exit":
        exit()
    else:
        print("Error, try again or enter exit to quit.")

funcsDict[bodyToCalc]()