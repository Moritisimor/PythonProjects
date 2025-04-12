from random import randint
from time import sleep

print("Willkommen zum Quiz")
QuizAuswahl = randint (0,9)
input("Bitte drücken Sie Enter um fortzufahren: ")
if QuizAuswahl in [0]:
    Quiz = input("Welches ist das größte Tier der Welt? ")
    if Quiz.lower() in ["blauwal"]:
        print("Das ist richtig.")
        sleep(3)
        exit()
    else:
        print("Das ist falsch.")
        sleep(3)
        exit()

elif QuizAuswahl in [1]:
    Quiz = input("In welchem Land liegt der Kilimandscharo? ")
    if Quiz.lower() in ["tansania"]:
        print("Das ist richtig.")
        sleep(3)
        exit()
    else:
        print("Das ist falsch.")
        sleep(3)
        exit()

elif QuizAuswahl in [2]:
    Quiz = input("Was ist der kleinste Staat der Welt? ")
    if Quiz.lower() in ["vatikan", "vatikanstadt"]:
        print("Das ist richtig.")
        sleep(3)
        exit()
    else:
        print("Das ist falsch.")
        sleep(3)
        exit()

elif QuizAuswahl in [3]:
    Quiz = input("In welchem Jahr begann der zweite Weltkrieg? ")
    if Quiz in ["1939"]:
        print("Das ist richtig.")
        sleep(3)
        exit()
    else:
        print("Das ist falsch.")
        sleep(3)
        exit()

elif QuizAuswahl in [4]:
    Quiz = input("Wer war der erste Mensch im All? ")
    if Quiz.lower() in ["yuri gagarin", "juri gagarin"]:
        print("Das ist richtig.")
        sleep(3)
        exit()
    else:
        print("Das ist falsch.")
        sleep(3)
        exit()

elif QuizAuswahl in [5]:
    Quiz = input("Wie viele Sterne hat die Flagge der USA? ")
    if Quiz.lower() in ["50", "fünfzig"]:
        print("Das ist richtig.")
        sleep(3)
        exit()
    else:
        print("Das ist falsch.")
        sleep(3)
        exit()

elif QuizAuswahl in [6]:
    Quiz = input("Was ist das schnellste Tier an Land? ")
    if Quiz.lower() in ["gepard"]:
        print("Das ist richtig.")
        sleep(3)
        exit()
    else:
        print("Das ist falsch.")
        sleep(3)
        exit()

elif QuizAuswahl in [7]:
    Quiz = input("Was war das erste Videospiel der Welt? ")
    if Quiz.lower() in ["pong"]:
        print("Das ist richtig.")
        sleep(3)
        exit()
    else:
        print("Das ist falsch.")
        sleep(3)
        exit()

elif QuizAuswahl in [8]:
    Quiz = input("Wie viele Planeten hat unser Sonnensystem? ")
    if Quiz.lower() in ["8", "acht"]:
        print("Das ist richtig.")
        sleep(3)
        exit()
    else:
        print("Das ist falsch.")
        sleep(3)
        exit()

elif QuizAuswahl in [9]:
    Quiz = input("Wer ist der Autor von 1984? ")
    if Quiz.lower() in ["george orwell"]:
        print("Das ist richtig.")
        sleep(3)
        exit()
    else:
        print("Das ist falsch.")
        sleep(3)
        exit()