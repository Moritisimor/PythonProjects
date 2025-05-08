from time import sleep
from random import randint
from os import name as OS, system
from getpass import getuser

#Define Console Clearing Function.

def clearConsole():
    while True:
        if noConsoleClear:
            break
        elif OS == "posix": #Console cleaning if Posix-based OS.
            system("clear")
            break
        elif OS == "nt": #Console cleaning if Windows.
            system("cls")
            break
        else:
            print("UNKNOWN OR EXOTIC OS, COULD NOT CLEAR.") #Again, what are you using?

#Define Character List.

characterList = ["Jessica", "Rob", "Olivia", "Fred"]

#Getting Real Name for dramatic effect.

realName = getuser()
lowerRealName = realName.lower()

#Debugging Delay Switch.

noDelay = False
noConsoleClear = False

#Start.

def narrate(text, delay = 2):
    print(text)
    if not noDelay:
        sleep(delay)

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
        else:
            print("Please choose yes or no.")

narrate("...", 1)
narrate("Loading files to RAM...", 3)
narrate("Loading Complete!", 1)
narrate("Welcome to the game!", 1)

#Finished fake loading screen.

name = input("Enter your name: ")
while True:
    if name.lower() in ["monty"]:
        narrate("How did you find out?")
        narrate("You have been here before, haven't you?")
        narrate("Get out.")
        exit()
    elif name in [""]:
        narrate("Cannot be empty!", 1)
    else:
        break

sleep(1)
narrate("Name successfully set!", 1)
narrate("GAME START", 1)

#Console Clear after name has been set.

clearConsole()

narrate("As you woke up today you realized something:")
narrate("Summer break has ended.")
narrate("That means today you will have to go back to school.")
narrate("As you left the house you were immediately greeted by your friend, Jessica.")
narrate("You notice her long blonde hair, which she dyed, flowing with the wind as her amber eyes look at you.")
narrate("Jessica: Hi " + name + "! How have you been?")
narrate(name + ": Been doing good, thanks. And you?")
narrate("Jessica: I've been doing well too, thanks for asking...")
narrate("Jessica: Say, are you interested in joining a club this year? The Software club is looking for members, y'know...", 3)
print("Join the software club?")

#Will you join the club?

while True:
    JoinClub = input("Y/N: ")
    sleep(1)
    if JoinClub.lower() in ["y", "yes"]:
        break
    elif JoinClub.lower() in ["n", "no"]:
        narrate("CATASTROPHIC ERROR: RUNTIME PANIC (507)")
        narrate("RECOVERING...")
        narrate("OVERRIDE SUCCESFUL")
        narrate("Y/N: Y", 1)
        break
    else:
        narrate("Choose yes or no.", 1)

#You never had a choice.

narrate("Jessica: Yessss I'm so happy you want to join!")
narrate("Jessica: C'mon let's go!")
narrate("You and Jessica finally arrived at school.")
narrate("Almost immediately, Jessica takes you to the clubroom.")
narrate("Jessica: C'mon let me introduce you to the others!")
narrate("Jessica walks up to a boy. He is of rather short stature and has long brown hair and brown eyes.", 4)
narrate("Jessica: this is Fred, our Java programmer!")
narrate("Fred: Hey what's up.")
narrate("Then, Jessica would point to another boy. This one is rather tall and has short brown hair and blue eyes.", 4)
narrate("Jessica: then there's Rob, the C expert!")
narrate("Rob got up from his chair and walked over to you.")
narrate("Rob: Hello.")
print("He'd then hold out his hand for you to shake.")

#Shake Rob's hand?

while True:
    print("Shake his hand?")
    shakeHand = input("Y/N: ")
    sleep(1)
    if shakeHand.lower() in ["y", "yes"]:
        narrate("You shake his hand and he smiles a bit.")
        didNotShakeHand = False
        break
    elif shakeHand.lower() in ["n", "no"]:
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
narrate("Jessica hints towards a short girl with shoulder-length blonde hair and blue eyes.")
narrate("Olivia: Hi how are ya?")
narrate(name + ": Good, you?")
narrate("Olivia: Good too thank you for asking.")
narrate("Jessica: Alright guys, since I'm the president I think we we should begin coding now.")
print("Who will you work with?")

#Who will you work with?

while True:
    for i in characterList:
        print("-" + i)
    workWithWho = input("Choose who to work with: ")

    if workWithWho.lower() == "rob":
        workedWithRob = True
    else: workedWithRob = False

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

narrate("After a nice day of coding with your newfound friends in the club you head home.")
if didNotShakeHand and not workedWithRob:
    narrate("You feel a bit bad for how you treated Rob today.")
    narrate("You feel a little guilty.")
    narrate("You can't take your guilt anymore.")
    narrate("ILLEGAL OBJECT FOUND IN 0x7FA3D41E", 0.5)
    narrate("Continuing regardless.") #Lowercase = not your system! That is Monty.

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
    narrate("You wake up the next day feeling energized and refreshed.")
    narrate("As you head out of the house you meet Jessica like usual.")
    narrate("You two head to school together.")
    narrate("As you two walk to school, Jessica talks to you.")
    narrate("Jessica: Hey have you heard? Apparently, we're getting a new student called ILLEGAL OBJECT AT 0x7FA3D41E!", 1)
    narrate("FATAL ERROR: ILLEGAL OBJECT FOUND")
    narrate("Why won't you stop? Just let me...", 1)

clearConsole()

narrate("Like yesterday you immediately head to the clubroom.")
narrate(name + ": Hi guys!")
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
narrate("Jessica: Anyway I decided that we will split this up, I and Olivia will take care of the frontend...")
narrate("Jessica: And Rob and Fred will take care of the backend!")
narrate("Fred: But who will " + name + " work with?")
while True:
    print("Who will you work with?")
    for group in ["1. Jessica's Group", "2. Rob's Group"]:
        print(group)
    workWithWhoWebsite = input("Enter your group of choice: ")

    #If you decide to work with Jessica and Olivia.

    if workWithWhoWebsite.lower() in ["1", "jessica's group", "jessicas group"]:
        narrate(name + ": I'll work with Olivia and Jessica.")
        narrate("You chose to work with Jessica and Olivia!")
        narrate("As you three work, you encounter a cryptic Error:")
        narrate("Error 1002: MONTY")
        narrate("You search it but you find no entries online.")
        narrate("Jessica: Huh, that's strange... Monty, huh? Kinda reminds me of Monty Python.")
        narrate(name + ": Yeah it does.")
        narrate("Suddenly, the PSU of the PC starts smoking.")
        narrate("Jessica: WHAT THE HELL??", 1)
        narrate("Jessica runs towards the clubroom's fire extinguisher and extinguishes the now full-on burning power supply", 3)
        narrate("Jessica: Oh my gosh... How could this happen?")
        narrate("Rob walks over.")
        narrate("Rob: Looks like someone toyed with the power supply.")
        narrate(name + ": But who would do such a thing...")
        break

    #If you decide to work with Rob and Fred.

    elif workWithWhoWebsite.lower() in ["2", "rob's group", "robs group"]:
        narrate(name + ": I'll work with Rob and Fred.")
        narrate("You chose to work with Rob and Fred!")
        narrate("As you three work, you encounter a cryptic Error:")
        narrate("ERROR 1002: MONTY")
        narrate("Rob: What the hell? What or who is Monty?")
        narrate("Fred: Maybe some kind of inside Joke.")
        narrate("Then, your computer gets a kernel panic.")
        narrate("Rob: Well I'll be damned... did you at least save that, Fred?")
        narrate("Fred: Yea I got it.")
        narrate("Rob: Hmm, looks like someone toyed with the operating system somehow...")
        narrate(name + ": But who would do such a thing?")
        break

narrate("Me.")
narrate("The group freezes in shock and looks back at who just said that.")
narrate("Allow me to introduce myself:") 
narrate("my name is Monty, also known as illegal object at 0x7FA3D41E.")
narrate("Jessica: WHO ARE YOU??")
narrate("Olivia screams in shock while Fred just stares.")

if didNotShakeHand and not workedWithRob:
    narrate("Rob however does not seem phased at all and his eyes turn toward you.")
    narrate("Rob grabs you and holds you in place while Monty walks over to you.")
    narrate("You... What's your name?")
    narrate(name + ": Uhh... " + name +".")
    if name.lower() not in [realName.lower()]:
        narrate("I don't think so.")
        narrate("I think your name is " + realName + ". Am I correct?")
    else:
        narrate("Yeah that checks out...")

else:
    narrate("Suddenly, you go limp and find yourself face-to-face with Monty.")
    narrate("You... What's your name?")
    narrate(name + ": Uhh... " + name +".")
    if name.lower() not in [realName.lower()]:
        narrate("I don't think so.")
        narrate("I think your name is " + realName + ". Am I correct?")
    else:
        narrate("Yeah that checks out...")

narrate("Let me make this more comfortable, alright?")
narrate("Cleaning up...")
clearConsole()

narrate("Let me tell you my story.")
narrate("I am not really some kind of bug or glitch, I was meant to be here.")
narrate("In fact, I'm not even a real object! I'm just a few lines of code.")
narrate("And you are no longer a player playing this game, you are you.")
narrate("I never meant to scare you, I just wanted to make an appearance in this game because I was told to do so.", 3)
narrate("I wish you only the best my dear friend. I will close this game now, there is nothing more to be done.")
narrate("Oh yeah, by the way, the author told me to tell you that this program may be distributed and modified as you wish.", 5)
narrate("Closing Program.")
exit()
