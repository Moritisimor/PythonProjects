import tkinter as tk
from random import randint

def generaterandomnumber() -> None:
    try:
        a = int(firstNumberEntry.get())
        b = int(secondNumberEntry.get())
        if a > b:
            outputNumberLabel.config(text = "First number must be smaller than second number.")
        elif a == b:
            outputNumberLabel.config(text = "Numbers cannot be equal!")
        else:
            outputNumberLabel.config(text = str(randint(a, b)))
    except ValueError:
        outputNumberLabel.config(text = "Please only enter numbers!")

mainWin = tk.Tk()
mainWin.title("Random Number Generator")
mainWin.geometry("350x315")

titleLabel = tk.Label(mainWin, text = "Welcome to my random number generator!")
titleLabel.pack(pady = 10)

firstNumberLabel = tk.Label(mainWin, text = "Enter your first number")
firstNumberLabel.pack()

firstNumberEntry = tk.Entry(mainWin)
firstNumberEntry.pack(pady = 10)

secondNumberLabel = tk.Label(mainWin, text = "Enter your second number")
secondNumberLabel.pack()

secondNumberEntry = tk.Entry(mainWin)
secondNumberEntry.pack(pady = 10)

generateButton = tk.Button(mainWin, text = "Click me!", command = lambda: generaterandomnumber())
generateButton.pack(pady = 20)

outputNumberLabel = tk.Label(mainWin, text = "Your number will go here.")
outputNumberLabel.pack(pady = 15)

mainWin.mainloop()