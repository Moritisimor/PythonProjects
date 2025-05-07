from time import sleep
from random import randint
from os import name as OS, system

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
if OS not in["nt", "posix"]:
    narrate("Hello! The game has detected that you are not on a common OS.")
    narrate("First off, respect to you! Second, I would like to warn you that a syscall later WILL NOT work.")
    narrate("However, this doesn't mean that you can't play the game, instead, the console simply won't clear. Not that bad, right?", 3)
    while True:
        print("Continue anyway?")
        quitIfNotCommonOS = input("Y/N: ")
        if quitIfNotCommonOS.lower() in ["n", "no"]:
            exit()
        elif quitIfNotCommonOS.lower() in ["y", "yes"]:
            break


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
        narrate("Jessica: Almost figured you'd choose me. C'mon lets go.")
        narrate("You and Jessica work on a small database. While you work she grows more fond of you.")
        break

    elif workWithWho.lower() in ["rob"]:
        if didNotShakeHand:
            narrate("Rob looks at you a little irritated but decides to work with you.")
            narrate("Rob: Alright I think this experimental kernel is looking pretty good so far.")
            break
        else:
            narrate("Rob smiles at you and gladly works with you.")
            narrate("Rob: Have you developed kernels before? This looks amazing!")
            break

    elif workWithWho.lower() in ["fred"]:
        narrate("Fred gets his laptop out of his bag and opens his IDE of choice.")
        narrate("Fred: Let's get to work then.")
        narrate("You and Fred began working on a game backend with success.")
        break

    elif workWithWho.lower() in ["olivia"]:
        narrate("Olivia sits down at one of the club's computers and pats the chair next to her.")
        narrate("Without exchanging many words you two made a nice looking website.")
        break

    else:
        narrate("Please choose one of the available entries.")

    if workWithWho.lower() == "rob":
        workedWithRob = True
    else: workedWithRob = False

narrate("After a nice day of coding with your newfound friends in the club you head home.")
if didNotShakeHand and not workedWithRob:
    narrate("You feel a bit bad for how you treated Rob today.")
    narrate("You feel a little guilty.")
    narrate("You can't take your guilt anymore.")
    narrate("ILLEGAL OBJECT FOUND IN 0x7FA3D41E")
    narrate("Continuing regardless.") #Lowercase = not your system! That is Monty

narrate("You go to sleep.")
sleepRandom1 = randint(0, 1)
if sleepRandom1 == 0:
    sleepGoodDay1 = False
    narrate("You wake up the next day feeling more tired than usual.")
    narrate("You head out to school, surprised you don't see Jessica on your way.")
    narrate("As you arrive in school you go over to Jessica.")
    narrate(name + ": Where were you? I thought we'd head over to school together like usual.")
    narrate("Jessica: Oh I'm sorry James, today I felt like going to school with ILLEGAL OBJECT AT 0x7FA3D41E.", 1)
    narrate("FATAL ERROR: ILLEGAL OBJECT FOUND")
    narrate("Pesky game, why won't you just let me...", 1)
else:
    sleepGoodDay1 = True
    narrate("You wake up the next day feeling energetic and refreshed.")
    narrate("As you head out of the house you meet Jessica like usual.")
    narrate("You two head to school together.")
    narrate("As you two walk to school, Jessica talks to you.")
    narrate("Jessica: Hey have you heard? Apparently, we're getting a new student called ILLEGAL OBJECT AT 0x7FA3D41E!", 1)
    narrate("FATAL ERROR: ILLEGAL OBJECT FOUND")
    narrate("Why won't you stop? Just let me...", 1)

narrate("TOO MANY ERRORS, CLEANING UP...", 3) 
if OS == "posix": #Console cleaning if Posix-based OS
    system("clear")
elif OS == "nt": #Console cleaning if Windows
    system("cls")
else:
    print("Unknown or exotic operating system. Sorry buddy.") #What are you using at this point?

narrate("Like yesterday you immediately head to the clubroom.")
narrate("name" + ": Hi guys!")
if didNotShakeHand and not workedWithRob:
    narrate("Everyone greets you back except Rob, who just stares at you with his metallic-blue eyes.")
    narrate("A shiver runs down your spine.")
    narrate("Rob walks over to you.")
    narrate("Rob: Monty is watching.")
else:
    narrate("Everyone greets you back.")

narrate("Jessica: Ok guys, I've got an announcement to make!")
narrate("Jessica: The principal has hired us to make a website for our school!")
narrate("Olivia perks up upon hearing the word website and stares at Jessica, smiling.")
narrate("Jessica: Yes Olivia I figured you'd like that.")
