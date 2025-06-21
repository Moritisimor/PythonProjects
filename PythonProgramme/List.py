while True:
    print("Welcome to List.py! This program will allow you to sort numerical lists and calculate the average number.")
    print("Enter each number individually and end the list by typing 'end' at your last input.")

    listToBeSorted = []

    while True:
        try:
            entry = (input("Enter your number: "))
            if entry.lower() == "end":
                break
            else:
                listToBeSorted.append(int(entry))
        except ValueError:
            print("Only enter numbers")

    print("\nYour original list:")
    print(listToBeSorted)

    print("\nYour sorted list:")
    print(sorted(listToBeSorted))

    print("\nThe average number in your list:")
    print(sum(listToBeSorted) / len(listToBeSorted))

    again = input("Would you like to sort another list? \nY/N: ")
    if again.lower() in ["y", "yes"]:
        continue
    else:
        break