import tkinter as tk
from tkinter import messagebox
from random import randint

def generaterandomnumber():
    try:
        a = int(firstNumberEntry.get())
        b = int(secondNumberEntry.get())
        if a > b:
            messagebox.showerror("Error", "First number must be smaller than second!")
        elif a == b:
            messagebox.showerror("Error", "Numbers can not be equal!")
        else:
            outputNumberLabel.config(text = str(randint(a, b)))
    except ValueError:
        messagebox.showerror("Error", "Only enter numbers and do not leave input fields blank!")

mainWin = tk.Tk() # Create main window
mainWin.title("Random Number Generator") # Set main window title
mainWin.geometry("315x315") # Set main window dimensions

tk.Label(mainWin, text = "Welcome to my random number generator!").pack(pady=10)

tk.Label(mainWin, text = "Enter your first number").pack()
firstNumberEntry = tk.Entry(mainWin)
firstNumberEntry.pack(pady = 10)

tk.Label(mainWin, text = "Enter your second number").pack()
secondNumberEntry = tk.Entry(mainWin)
secondNumberEntry.pack(pady = 10)

tk.Button(mainWin, text = "Generate number!", command = lambda: generaterandomnumber()).pack(pady = 20)

outputNumberLabel = tk.Label(mainWin, text = "Your number will go here.")
outputNumberLabel.pack(pady = 15)

mainWin.mainloop()