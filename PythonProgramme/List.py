print("Welcome to List.py! This program will allow you to sort numerical lists and calculate the average number.")

while True:
    print("Enter each number individually and end the list by typing 'end' at your last input or by just leaving it blank.")

    listToBeSorted = []

    while True:
        try:
            entry = (input("Enter your number: "))
            if entry.lower().strip() in ["end", ""]:
                break
            else:
                listToBeSorted.append(float(entry))
        except ValueError:
            print("Only enter numbers")

    if len(listToBeSorted) == 0:
        print("Your list is empty.")
    else:
        print("\nYour original list:")
        print(listToBeSorted)

        print("\nYour sorted list:")
        print(sorted(listToBeSorted))

        print("\nThe average number in your list:")
        print(sum(listToBeSorted) / len(listToBeSorted))

    again = input("\nWould you like to sort another list? \nY/N: ")
    if again.lower() in ["y", "yes"]:
        continue
    else:
        break