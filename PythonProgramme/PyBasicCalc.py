print("Welcome to the Basic Calculator written in python.")
try:
    x = float(input("Enter your first number: "))
    y = float(input("Enter your second number: "))
    op = input("Enter your operator: ")
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x - y)
    elif op == "*":
        print(x * y)
    elif op == "/":
        print(x / y)
except ValueError:
    print("Please only enter numbers.")