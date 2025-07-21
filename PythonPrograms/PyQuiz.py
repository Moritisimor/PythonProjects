from random import randint

print("Welcome to PyQuiz!")
input("Press enter to continue: ")

def quiz(question, correctanswer):
    while True:
        print(question)
        answer = input("Enter your answer: ")
        if answer.lower() == correctanswer:
            print("That is correct!")
        else:
            print("That is wrong!")
        break

while True:
    quizSelection = randint(0,9)

    if quizSelection == 0:
        quiz("What is the largest animal in the world?", "blue whale")
        
    elif quizSelection == 1:
        quiz("In which country is Mount Kilimanjaro located?", "tanzania")

    elif quizSelection == 2:
        quiz("What is the smallest country in the world?", "vatican")
    
    elif quizSelection == 3:
        quiz("In which year did World War II begin?", "1939")

    elif quizSelection == 4:
        quiz("Who was the first human in space?", "yuri gagarin")

    elif quizSelection == 5:
        quiz("How many stars are on the US flag?", "50")

    elif quizSelection == 6:
        quiz("What is the fastest land animal?", "cheetah")

    elif quizSelection == 7:
        quiz("What was the world's first video game?", "pong")

    elif quizSelection == 8:
        quiz("How many planets are in our solar system?", "8")

    elif quizSelection == 9:
        quiz("Who is the author of the novel 1984?", "george orwell")

    playAgain = input("Would you like to play again? ")
    if playAgain in ["no", "n"]:
        break