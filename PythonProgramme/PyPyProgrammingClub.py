from time import sleep

#Start.

def narrate(text, delay = 2):
    print(text)
    sleep(delay)
        

print("Welcome to the PyPy Programming Club!")
input("Press Enter to start! ")
sleep(1)
narrate("...", 1)
narrate("Loading files to RAM...", 3)
narrate("Loading Complete!", 1)
narrate("Welcome to the game!", 1)

#Finished fake loading screen.

name = input("Enter your name: ")
sleep(1)
narrate("Name succesfully set!", 1)
narrate("As you woke up today you realized something:", 3)
narrate("Summer break has ended.")
narrate("That means today you will have to go back to school.", 3)
narrate("As you left the house you were immediately greeted by your friend, Jessica.", 3)
narrate("Jessica: Hi " + name + "! How have you been?")
narrate(name + ": Been doing good, thanks. And you?")
narrate("Jessica: I've been doing well too thanks for asking...")
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
narrate("Hello.")
narrate("He'd then hold out his hand for you to shake.")

#Shake Robert's hand?

while True:
    ShakeHand = input("Y/N: ")
    sleep(1)
    if ShakeHand in ["y", "yes"]:
        narrate("You shake his hand and he smiles a bit.")
        DidNotShakeHand = False
        break
    elif ShakeHand in ["n", "no"]:
        DidNotShakeHand = True
        narrate("Rob looks a little sad. Why wouldn't you shake his hand?")
        break
    else:
        narrate("Choose yes or no.", 1)

if DidNotShakeHand:
    narrate("Jessica looks a little weirded out.")
else:
    narrate("Jessica looks happy that you're already making friends.")

narrate("Jessica: And then we have our final member: Olivia. She is very good with JavaScript!")
narrate("Olivia: Hi how are ya?")