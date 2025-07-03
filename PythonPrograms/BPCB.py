from random import randint
from time import sleep

print("BPCB: Hello! My name is BPCB. That stands for Basic Python Chatbot")
sleep(1)
print("BPCB: You need to type very specifically, my language understanding is rather limited.")

while True:
    message = input("Input: ")
    if message.lower() in["hello", "hi", "hey", "good day"]:
        print("BPCB: Hello! How can I help you today?")

    elif message.lower() in["how are you?","how are ya?","how's it going?"]:
        print("BPCB: I'm good! Thank you for asking!")

    elif message.lower() in["exit","goodbye","bye","cya"]:
        print("BPCB: Goodbye!")
        input("Press enter to quit: ")
        exit()

    elif message.lower() in["tell me a joke"]:
        joke = randint(0, 3)

        if joke == 0:
            print("BPCB: Why don't skeletons fight each other?")
            sleep(2)
            print("BPCB: They don't have the guts!")

        elif joke == 1:
            print("BPCB: I used to play the piano by ear...")
            sleep(2)
            print("BPCB: Now I play with my hands.")

        elif joke == 2:
            print("BPCB: Why did the scarecrow win an award?")
            sleep(2)
            print("BPCB: Because he was outstanding in his field!")

        elif joke == 3:
            print("BPCB: I do have a joke about construction...")
            sleep(2)
            print("BPCB: But I'm still working on it!")

    else:
        print("Sorry, I didn't get that. Like i said my understanding of language is rather limited.")
