from random import randint

while True:
    print("Welcome to the Py Number guessing game!")
    while True:
        try:
            toWhatNumber = int(input("Enter the highest number you want to guess up to: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    toThisNumber = randint(0, toWhatNumber)
    while True:
        try:
            guess = int(input(f"Guess any number between 0 and {toWhatNumber}: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if guess == toThisNumber:
        print("You guessed correctly")
    else:
        print("You guessed incorrectly!")
        print(f"The Number was {toThisNumber}!")
    
    while True:
        playAgain = input("Play again? Y/N: ")
        if playAgain.lower() in ["y", "yes"]:
            break
        elif playAgain.lower() in ["no", "n"]:
            exit()
        else:
            print("Please choose yes or no.")