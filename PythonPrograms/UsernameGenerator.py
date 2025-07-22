from random import randint

prefixList = [
    "Big",
    "Small",
    "Grand",
    "Elegant",
    "Tasty",
    "Rich",
    "Cool",
    "Colorful",
    "Free",
    "Sad"
]
suffixList = [
    "Boy",
    "Gamer",
    "Destroyer",
    "Soldier",
    "Sailor",
    "Pilot",
    "Dog",
    "Thief",
    "Lord",
    "Mage"
]

def generateRandomName():
    prefix = prefixList[randint(0, len(prefixList) - 1)]
    suffix = suffixList[randint(0, len(suffixList) - 1)]
    return f"{prefix}{suffix}{randint(100, 999)}"

print("Welcome to the Username Generator! \nType exit at any time to quit.")
while True:
    if input("Pres enter to generate a random username: ").lower().strip() == "exit":
        break
    print(generateRandomName())