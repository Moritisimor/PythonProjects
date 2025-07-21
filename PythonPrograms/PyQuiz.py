from random import randint

print("Welcome to PyQuiz!")
print("You may exit the quiz at any time by typing 'exit'")
cont = input("Press enter to start the quiz: ")
if cont.lower() in ["exit", "quit"]:
    exit()

def quiz(question, correctanswer):
    while True:
        print(question)
        answer = input("Enter your answer: ")
        if answer.lower() == correctanswer:
            print("That is correct!")
        elif answer.lower() == "exit":
            exit()
        else:
            print("That is wrong!")
        break

while True:
    quizlist = [ # Lambda is required to pass the function itself, not its return value (which is None)
        lambda: quiz("What is the largest animal in the world?", "blue whale"),
        lambda: quiz("In which country is Mount Kilimanjaro located?", "tanzania"),
        lambda: quiz("What is the smallest country in the world?", "vatican"),
        lambda: quiz("In which year did World War II begin?", "1939"),
        lambda: quiz("Who was the first human in space?", "yuri gagarin"),
        lambda: quiz("How many stars are on the US flag?", "50"),
        lambda: quiz("What is the fastest land animal?", "cheetah"),
        lambda: quiz("What was the world's first video game?", "pong"),
        lambda: quiz("How many planets are in our solar system?", "8"),
        lambda: quiz("Who is the author of the novel 1984?", "george orwell"),
    ]

    quizSelection = randint(0, len(quizlist))
    quizlist[quizSelection]()