def makelist():
    listToBeSorted = []
    print("Enter each number individually and end the list by typing 'end' at your last input or by just leaving it blank.")
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
    if listToBeSorted:
        return listToBeSorted

def getaverage(varlist):
    if varlist:
        return sum(varlist) / len(varlist)

def sortlist(varlist):
    if varlist:
        return sorted(varlist)

def main():
    print("Welcome to List.py! \nThis program will allow you to sort numerical lists and calculate the average number.")
    while True:
        finishedList = makelist()
        sortedList = sortlist(finishedList)
        average = getaverage(finishedList)
        if finishedList:
            print(f"\nYour original list: \n{finishedList}")
            print(f"\nYour sorted list: \n{sortedList}")
            print(f"\nThe average number of your list is: \n{average}")
        else:
            print("It looks like the list you entered was empty.")

        again = input("\nWould you like to sort another list? \nY/N: ")
        if again.lower() in ["y", "yes"]:
            continue
        else:
            break

main()
