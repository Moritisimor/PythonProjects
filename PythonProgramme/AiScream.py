from time import sleep

print("Ruby-Chan!")
while True:
    Answer = input("Input: ")
    if Answer.lower() in["hai","haii","haiii"]:
        print("Nani ga suki?")
        break
    else:
        print("WRONG!!!")
        exit()


while True:
    Answer = input("Input: ")
    if Answer.lower() in["choco minto","chocominto"]:
        print("Yori mo a na ta!")
        sleep(2)
        break
    else:
        print("WRONG!!!!")
        exit()

print("You have successfully managed to solve my puzzle.")
sleep(1)
print("As a reward you get to know my secret...")
sleep(3)
print("My secret is that I enjoy listening to vocaloid music.")