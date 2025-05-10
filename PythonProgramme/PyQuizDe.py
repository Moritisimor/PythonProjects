from random import randint

print("Willkommen zum Quiz")
input("Bitte drücken Sie Enter um fortzufahren: ")

def Quiz(frage, richtigeAntwort):
    while True:
        print(frage)
        antwort = input("Geben Sie Ihre Antwort ein: ")
        if antwort.lower() in [richtigeAntwort]:
            print("Das ist korrekt!")
            break
        else:
            print("Das ist falsch!")
            break

while True:
    QuizAuswahl = randint (0,9)

    if QuizAuswahl == 0:
        Quiz("Was ist das größte Tier der Welt?", "blauwal")
        
    elif QuizAuswahl == 1:
        Quiz("In welchem Land liegt der Kilimandscharo?", "tansania")

    elif QuizAuswahl == 2:
        Quiz("Was ist der kleinste Staat der Welt?", "vatikan") 
    
    elif QuizAuswahl == 3:
        Quiz("In welchem Jahr begann der zweite Weltkrieg", "1939")

    elif QuizAuswahl == 4:
        Quiz("Wer war der erste Mensch im Weltraum?", "juri gagarin")

    elif QuizAuswahl == 5:
        Quiz("Wie viele Sterne hat die Flagge der USA?", "50")

    elif QuizAuswahl == 6:
        Quiz("Was ist das schnellste Tier an Land?", "gepard")

    elif QuizAuswahl == 7:
        Quiz("Was war das erste Videospiel der Welt?", "pong")

    elif QuizAuswahl == 8:
        Quiz("Wie viele Planeten hat unser Sonnensystem?", "8")

    elif QuizAuswahl == 9:
        Quiz("Wer ist der Autor von dem Roman 1984?", "george orwell")

    nochMal = input("Möchten Sie noch mal spielen? ")
    if nochMal in ["nein", "n"]:
        break