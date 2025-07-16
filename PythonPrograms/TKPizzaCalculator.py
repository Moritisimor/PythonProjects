import tkinter as tk
from tkinter import messagebox
from math import pi

def calculate():
    try:
        fpsqcm = float(firstPizzaPrice.get().strip()) / (pi * float(firstPizzaRadius.get().strip()) * float(firstPizzaRadius.get().strip()))
        spsqcm = float(secondPizzaPrice.get().strip()) / (pi * float(secondPizzaRadius.get().strip()) * float(secondPizzaRadius.get().strip()))
        firstPricePerSquareCm.config(text=f"{fpsqcm}")
        secondPricePerSquareCm.config(text=f"{spsqcm}")
        if fpsqcm > spsqcm:
            comparisonLabel.config(text="The first pizza offers more value")
        elif fpsqcm < spsqcm:
            comparisonLabel.config(text="The second pizza offers more value")
        else:
            comparisonLabel.config(text="Both pizzas offer the same value")
    except ValueError:
        messagebox.showerror("Error", "Only enter numbers and do not leave input fields blank.")


mainWin = tk.Tk()
mainWin.geometry("250x460")
mainWin.title("Pizza Calculator")

tk.Label(mainWin, text="Calculate and compare pizzas!").pack(pady=5)

tk.Label(mainWin, text="Price of first pizza").pack(pady=5)
firstPizzaPrice = tk.Entry(mainWin)
firstPizzaPrice.pack()

tk.Label(mainWin, text="Radius of first pizza").pack(pady=5)
firstPizzaRadius = tk.Entry(mainWin)
firstPizzaRadius.pack()

tk.Label(mainWin, text="Price of second pizza").pack(pady=5)
secondPizzaPrice = tk.Entry(mainWin)
secondPizzaPrice.pack()

tk.Label(mainWin, text="Radius of second pizza").pack(pady=5)
secondPizzaRadius = tk.Entry(mainWin)
secondPizzaRadius.pack()

tk.Button(mainWin, text="Calculate", command= lambda: calculate()).pack(pady=5)

tk.Label(mainWin, text="Price per cm² of pizza 1").pack(pady=5)
firstPricePerSquareCm = tk.Label(mainWin, text="")
firstPricePerSquareCm.pack()

tk.Label(mainWin, text="Price per cm² of pizza 2").pack(pady=5)
secondPricePerSquareCm = tk.Label(mainWin, text="")
secondPricePerSquareCm.pack()

comparisonLabel = tk.Label(mainWin, text="")
comparisonLabel.pack(pady=5)

mainWin.mainloop()