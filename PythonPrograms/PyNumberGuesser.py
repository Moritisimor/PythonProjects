from random import randint

cheat = False # Cheat feature for if you want to be a little cheater. Should be True or False.

while True:
    print("Welcome to the Py Number guessing game!")
    while True:
        try:
            toWhatNumber = int(input("Enter the highest number you want to guess up to: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    randomNumber = randint(0, toWhatNumber)
    while True:
        try:
            if cheat:
                print(f"Your number is: {randomNumber}")
            guess = int(input(f"Guess any number between 0 and {toWhatNumber}: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if guess == randomNumber:
        print("You guessed correctly")
    else:
        print("You guessed incorrectly!")
        if cheat:
            print("How'd you get that wrong?")
        else:
            print(f"The Number was {randomNumber}!")
    
    while True:
        playAgain = input("Play again? Y/N: ")
        if playAgain.lower() in ["y", "yes"]:
            break
        elif playAgain.lower() in ["no", "n"]:
            exit()
        else:
            print("Please choose yes or no.")