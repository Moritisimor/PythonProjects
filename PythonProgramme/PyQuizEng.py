from random import randint
from time import sleep

print("Welcome to the trivia quiz.")
QuizSelection = randint (0,9)
input("Please press Enter to continue: ")
if QuizSelection in [0]:
    Quiz = input("What animal is the largest in the world? ")
    if Quiz.lower() in ["blue whale"]:
        print("That is correct.")
        sleep(3)
        exit()
    else:
        print("That is wrong.")
        sleep(3)
        exit()

elif QuizSelection in [1]:
    Quiz = input("In which country lies the kilimanjaro? ")
    if Quiz.lower() in ["tansania"]:
        print("That is correct.")
        sleep(3)
        exit()
    else:
        print("That is wrong.")
        sleep(3)
        exit()

elif QuizSelection in [2]:
    Quiz = input("What is the smallest state in the world? ")
    if Quiz.lower() in ["vatican", "vatican city"]:
        print("That is correct.")
        sleep(3)
        exit()
    else:
        print("That is wrong.")
        sleep(3)
        exit()

elif QuizSelection in [3]:
    Quiz = input("In what year did the 2nd world war begin? ")
    if Quiz in ["1939"]:
        print("That is correct.")
        sleep(3)
        exit()
    else:
        print("That is wrong.")
        sleep(3)
        exit()

elif QuizSelection in [4]:
    Quiz = input("Who was the first man in space? ")
    if Quiz.lower() in ["yuri gagarin", "juri gagarin"]:
        print("That is correct.")
        sleep(3)
        exit()
    else:
        print("That is wrong.")
        sleep(3)
        exit()

elif QuizSelection in [5]:
    Quiz = input("How many stars does the flag of the USA have? ")
    if Quiz.lower() in ["50", "fifty"]:
        print("That is correct.")
        sleep(3)
        exit()
    else:
        print("That is wrong.")
        sleep(3)
        exit()

elif QuizSelection in [6]:
    Quiz = input("What is the fastest land animal? ")
    if Quiz.lower() in ["cheetah"]:
        print("That is correct.")
        sleep(3)
        exit()
    else:
        print("That is wrong.")
        sleep(3)
        exit()

elif QuizSelection in [7]:
    Quiz = input("What was the first video game in the world? ")
    if Quiz.lower() in ["pong"]:
        print("That is correct.")
        sleep(3)
        exit()
    else:
        print("That is wrong.")
        sleep(3)
        exit()

elif QuizSelection in [8]:
    Quiz = input("How many planets does the solar system have? ")
    if Quiz.lower() in ["8", "eight"]:
        print("That is correct.")
        sleep(3)
        exit()
    else:
        print("That is wrong.")
        sleep(3)
        exit()

elif QuizSelection in [9]:
    Quiz = input("Who is the author of 1984? ")
    if Quiz.lower() in ["george orwell"]:
        print("That is correct.")
        sleep(3)
        exit()
    else:
        print("That is wrong.")
        sleep(3)
        exit()