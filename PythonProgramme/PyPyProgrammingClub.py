from time import sleep

#Debugging Delay Switch

noDelay = True

#Start.

def narrate(text, delay = 2):
    print(text)
    if not noDelay:
     sleep(delay)
        
characterList = ["Jessica", "Rob", "Olivia", "Fred"]

print("Welcome to the PyPy Programming Club!")
input("Press Enter to start! ")
sleep(1)
narrate("...", 1)
narrate("Loading files to RAM...", 3)
narrate("Loading Complete!", 1)
narrate("Welcome to the game!", 1)

#Finished fake loading screen.

name = input("Enter your name: ")
if name.lower() in ["monty"]:
    narrate("How did you find out?")
    narrate("You have been here before, haven't you?")
    narrate("Get out.")
    exit()

sleep(1)
narrate("Name successfully set!", 1)
narrate("As you woke up today you realized something:", 3)
narrate("Summer break has ended.")
narrate("That means today you will have to go back to school.", 3)
narrate("As you left the house you were immediately greeted by your friend, Jessica.", 3)
narrate("Jessica: Hi " + name + "! How have you been?")
narrate(name + ": Been doing good, thanks. And you?")
narrate("Jessica: I've been doing well too, thanks for asking...")
narrate("Jessica: Say, are you interested in joining a club this year? The Software club is looking for members, y'know...", 3)
narrate("Join the software club?")

#Will you join the club?

while True:
    JoinClub = input("Y/N: ")
    sleep(1)
    if JoinClub.lower() in ["y", "yes"]:
        break
    elif JoinClub.lower() in ["n", "no"]:
        narrate("CATASTROPHIC ERROR: RUNTIME PANIC (507)", 3)
        narrate("RECOVERING...")
        narrate("OVERRIDE SUCCESFUL", 1)
        narrate("Y/N: Y", 1)
        break
    else:
        narrate("Choose yes or no.", 1)

#You never had a choice.

narrate("Jessica: Yessss I'm so happy you want to join!")
narrate("Jessica: C'mon let's go!")
narrate("You and Jessica finally arrived at school.")
narrate("Almost immediately, Jessica takes you to the clubroom.")
narrate("Jessica: this is Fred, our Java programmer!")
narrate("Fred: Hey what's up.")
narrate("Jessica: then there's Rob, the C expert!")
narrate("Rob got up from his chair and walked over to you.")
narrate("Rob: Hello.")
narrate("He'd then hold out his hand for you to shake.")

#Shake Robert's hand?

while True:
    print("Shake his hand?")
    shakeHand = input("Y/N: ")
    sleep(1)
    if shakeHand in ["y", "yes"]:
        narrate("You shake his hand and he smiles a bit.")
        didNotShakeHand = False
        break
    elif shakeHand in ["n", "no"]:
        didNotShakeHand = True
        narrate("Rob looks a little sad. Why wouldn't you shake his hand?")
        break
    else:
        narrate("Choose yes or no.", 1)

if didNotShakeHand:
    narrate("Jessica looks a little weirded out.")
else:
    narrate("Jessica looks happy that you're already making friends.")

narrate("Jessica: And then we have our final member: Olivia. She is very good with JavaScript!")
narrate("Olivia: Hi how are ya?")
narrate(name + ": Good, you?")
narrate("Olivia: Good too thank you for asking.")
narrate("Jessica: Alright guys, since I'm the president I think we we should begin coding now.")
narrate("Who will you work with?")

#Who will you work with?

while True:
    for i in characterList:
        print("-" + i)
    workWithWho = input("Choose who to work with: ")

    if workWithWho.lower() in ["jessica"]:
        workedWithRob = False
        narrate("Jessica: Almost figured you'd choose me. C'mon lets go.")
        narrate("You and Jessica work on a small database. While you work she grows more fond of you.")
        break

    elif workWithWho.lower() in ["rob"]:
        workedWithRob = True
        if didNotShakeHand:
            narrate("Rob looks at you a little irritated but decides to work with you.")
            narrate("Rob: Alright I think this experimental kernel is looking pretty good so far.")
            break
        else:
            narrate("Rob smiles at you and gladly works with you.")
            narrate("Rob: Have you developed kernels before? This looks amazing!")
            break

    elif workWithWho.lower() in ["fred"]:
        workedWithRob = False
        narrate("Fred gets his laptop out of his bag and opens his IDE of choice.")
        narrate("Fred: Let's get to work then.")
        narrate("You and Fred began working on a game backend with success.")
        break

    elif workWithWho.lower() in ["olivia"]:
        workedWithRob = False
        narrate("Olivia sits down at one of the club's computers and pats the chair next to her.")
        narrate("Without exchanging many words you two made a nice looking website.")
        break

    else:
        narrate("Please choose one of the available entries.")

narrate("After a nice day of coding with your newfound friends in the club you head home.")
if didNotShakeHand and not workedWithRob:
    narrate("You feel a bit bad for how you treated Rob today.")
    narrate("You feel a little guilty.")
    narrate("You can't take your guilt anymore.")
    narrate("ILLEGAL OBJECT FOUND IN 0x7FA3D41E")
    narrate("Continuing regardless.") #Lowercase = not your system! That is Monty

narrate("You go to sleep.")
