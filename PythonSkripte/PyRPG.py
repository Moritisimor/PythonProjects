#Welcome message

print("Welcome to the PyRPG, A game where you play as a medieval peasant who goes out on amazing quests.")
print("To choose an option you may enter the option itself or the corresponding letter.")
print("You always have the option to exit by typing 'exit'")
while True:
    ConfirmationStart = input("Enter abc to continue: ")
    if ConfirmationStart.lower() in["abc","exit"]:
        break
    else:
        print("Please type in the requested phrase")

if ConfirmationStart.lower() in["exit"]:
    exit()

#Dragon Attack

print("You just spawned in your village, Cloudspire Thicket. As you make your way to work, a dragon attacks!")
print("What do you do?")
while True:
    DragonAttack = input("Will you A: Run, or B: Attempt to fight the dragon: ")
    if DragonAttack.lower() in["a","run","b","attempt to fight the dragon","exit"]:
        break
    else:
        print("Please choose a valid option: ")

#What happens after dragon attack

if DragonAttack.lower() in["a","run"]:
    print("You ran for your life and successfully managed to escape.")
elif DragonAttack.lower() in["b","attempt to fight the dragon"]:
    print("You tried to play the hero and got burnt to a crisp.")
    exit()
elif DragonAttack.lower() in["exit"]:
    exit()

print("After running for your life and escaping your village, you now have several options:")
AfterDragonAttack = input("A: enter a cave B: enter a forest C: walk to the nearest city: ")
while True:
    if AfterDragonAttack.lower() in["a","enter a cave","b","enter a forest","c","walk to the nearest city","exit"]:
        break
    else:
        print("Please choose a valid option: ")

if AfterDragonAttack.lower() in["a","enter a cave"]:
    print("As you enter the cave you see a couple of goblins guarding a chest. All you have is a dagger.")
OptionCave = input("A: try to fight them B: run C: run to the nearest city and tell guards: ")
while True:
    if OptionCave in["a","try to fight them","b","run","c","run to the nearest city and tell guards","exit"]:
        break
    else:
        print("Please choose a valid option: ")

if OptionCave.lower() in["a","try to fight them"]:
    print("You tried to fight but were overwhelmed by the sheer amount of goblins and died.")
    exit()
elif OptionCave.lower() in["b","run"]:
    print("You exited the cave and have several options what to do next:")
    CaveNevermind = input("A: enter a forest B: walk to the nearest city: ")
elif OptionCave.lower() in["c","run"]:
    print("You ran to the nearest city, Galgenhall, and told some guards about the cave. They stormed the cave and gave you a reward for telling them.")
    print("Seeing the money, you have the option to comfortably retire. Will you?")
elif OptionCave.lower() in["exit"]:
    exit()
Retire = input("Will you retire?: ")
while True:
    if Retire.lower() in["y","yes","n","no","exit"]:
        break
    else:
        print("Please choose a valid option: ")

if Retire.lower() in["y","yes"]:
    print("You retired and spent the rest of your days living comfortably in Galgenhall.")
    exit()
elif Retire.lower() in["n","no"]:
    print("You decide to not retire and instead go out on more adventures. You have a few options:")
    NoRetirement = input("A: join the army B: set out on your own, independent adventures: ")
elif Retire.lower() in["exit"]:
    exit()