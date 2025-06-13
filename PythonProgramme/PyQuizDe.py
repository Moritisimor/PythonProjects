from random import randint

print("Willkommen zum Quiz")
input("Bitte drücken Sie Enter um fortzufahren: ")

def quiz(frage, richtigeantwort):
    while True:
        print(frage)
        antwort = input("Geben Sie Ihre Antwort ein: ")
        if antwort.lower() in [richtigeantwort]:
            print("Das ist korrekt!")
        else:
            print("Das ist falsch!")
        break

while True:
    QuizAuswahl = randint (0,9)

    if QuizAuswahl == 0:
        quiz("Was ist das größte Tier der Welt?", "blauwal")
        
    elif QuizAuswahl == 1:
        quiz("In welchem Land liegt der Kilimandscharo?", "tansania")

    elif QuizAuswahl == 2:
        quiz("Was ist der kleinste Staat der Welt?", "vatikan")
    
    elif QuizAuswahl == 3:
        quiz("In welchem Jahr begann der zweite Weltkrieg", "1939")

    elif QuizAuswahl == 4:
        quiz("Wer war der erste Mensch im Weltraum?", "juri gagarin")

    elif QuizAuswahl == 5:
        quiz("Wie viele Sterne hat die Flagge der USA?", "50")

    elif QuizAuswahl == 6:
        quiz("Was ist das schnellste Tier an Land?", "gepard")

    elif QuizAuswahl == 7:
        quiz("Was war das erste Videospiel der Welt?", "pong")

    elif QuizAuswahl == 8:
        quiz("Wie viele Planeten hat unser Sonnensystem?", "8")

    elif QuizAuswahl == 9:
        quiz("Wer ist der Autor von dem Roman 1984?", "george orwell")

    nochMal = input("Möchten Sie noch mal spielen? ")
    if nochMal in ["nein", "n"]:
        break