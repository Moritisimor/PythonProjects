#Welcome message

print("Welcome to the PyRPG, A game where you play as a medieval peasant who goes out on amazing quests.")
while True:
    ConfirmationStart = input("Enter abc to continue: ")
    if ConfirmationStart.lower() in["abc"]:
        break
    else:
        print("Please type in the requested phrase")

#Dragon Attack

print("You just spawned in your village, Cloudspire Thicket. As you make your way to work, a dragon attacks!")
print("What do you do?")
while True:
    DragonAttack = input("Will you A: Run, or B: Attempt to fight the dragon: ")
    if DragonAttack.lower() in["a","run","b","attempt to fight the dragon"]:
        break
    else:
        print("Please choose a valid option.")

if DragonAttack in["a","run"]:
    print("You ran for your life and successfully managed to escape.")
elif DragonAttack in["b","attempt to fight the dragon"]:
    print("You tried to play the hero and got burnt to a crisp.")
    exit()

print("After running for your life and escaping your village, you come across a cave and enter.")