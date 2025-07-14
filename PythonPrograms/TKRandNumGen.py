import tkinter as tk
from random import randint

def generaterandomnumber() -> None:
    try:
        a = int(firstNumberText.get("1.0", "end-1c"))
        b = int(secondNumberText.get("1.0", "end-1c"))
        if a > b:
            outputNumberLabel.config(text="First number must be smaller than second number.")
        else:
            outputNumberLabel.config(text=str(randint(a, b)))
    except ValueError:
        outputNumberLabel.config(text="Please only enter numbers!")

mainWin = tk.Tk()
mainWin.title("Random Number Generator")
mainWin.geometry("350x315")

titleLabel = tk.Label(mainWin, text = "Welcome to my random number generator!")
titleLabel.pack(pady = 10)

firstNumberLabel = tk.Label(mainWin, text = "Enter your first number")
firstNumberLabel.pack()

firstNumberText = tk.Text(mainWin, width = 8, height = 0.5)
firstNumberText.pack(pady = 10)

secondNumberLabel = tk.Label(mainWin, text = "Enter your second number")
secondNumberLabel.pack()

secondNumberText = tk.Text(mainWin, width = 8, height = 0.5)
secondNumberText.pack(pady = 10)

generateButton = tk.Button(mainWin, text = "Click me!", command = lambda: generaterandomnumber())
generateButton.pack(pady = 20)

outputNumberLabel = tk.Label(mainWin, text = "Your number will go here.")
outputNumberLabel.pack(pady = 15)

mainWin.mainloop()