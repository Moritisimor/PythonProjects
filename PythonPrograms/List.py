def makelist():
    listtobesorted = [] # Start with an empty list.
    print("Enter each number individually and end the list by typing 'end' at your last input or by just leaving it blank.")
    while True:
        try:
            entry = (input("Enter your number: ")).lower().strip()
            if entry in ["end", ""]: # Keywords for breaking the loop and entering the main function.
                break
            else:
                formatentry = float(entry)
                if formatentry.is_integer():
                    formatentry = int(formatentry)
                listtobesorted.append(formatentry)
        except ValueError:
            print("Only enter numbers")
    if listtobesorted: # Handling Lists like a boolean. If empty False else True.
        return listtobesorted # The finished List.
    else:
        return None

def getaverage(varlist):
    if varlist:
        return sum(varlist) / len(varlist)
    else:
        return None

def sortlist(varlist):
    if varlist:
        return sorted(varlist)
    else:
        return None

def main():
    print("Welcome to List.py! \nThis program will allow you to sort numerical lists and calculate the average number.")
    while True:
        finishedlist = makelist()
        sortedlist = sortlist(finishedlist)
        average = getaverage(finishedlist)
        if finishedlist:
            print(f"\nYour original list: \n{finishedlist}")
            print(f"\nYour sorted list: \n{sortedlist}")
            print(f"\nThe average number of your list is: \n{average}")
        else:
            print("It looks like the list you entered was empty.")

        again = input("\nWould you like to sort another list? \nY/N: ")
        if again.lower() in ["y", "yes"]:
            continue
        else:
            break

main()
