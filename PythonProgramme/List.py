print("Welcome to List.py! This program will allow you to sort numerical lists and calculate the average number.")

while True:
    print("Enter each number individually and end the list by typing 'end' at your last input or by just leaving it blank.")

    listToBeSorted = []

    while True:
        try:
            entry = (input("Enter your number: ")).lower().strip()
            if entry in ["end", ""]:
                break
            else:
                formatEntry = float(entry)
                if formatEntry.is_integer():
                    formatEntry = int(formatEntry)
                listToBeSorted.append(formatEntry)
        except ValueError:
            print("Only enter numbers")

    if len(listToBeSorted) == 0:
        print("Your list is empty.")
    else:
        print(f"\nYour original list: \n{listToBeSorted}")

        if sorted(listToBeSorted) == listToBeSorted:
            print("\nYour list was already sorted.")
        else:
            print(f"\nYour sorted list: \n{sorted(listToBeSorted)}")

        average = sum(listToBeSorted) / len(listToBeSorted)
        if average.is_integer():
            average = int(average)

        print(f"\nThe average number in your list: \n{average}")

    again = input("\nWould you like to sort another list? \nY/N: ")
    if again.lower() in ["y", "yes"]:
        continue
    else:
        break