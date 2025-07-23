import tkinter as tk
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

def generaterandomname():
    prefix = prefixList[randint(0, len(prefixList) - 1)]
    suffix = suffixList[randint(0, len(suffixList) - 1)]
    outputText.delete(1.0, tk.END)
    outputText.insert(1.0, f"{prefix}{suffix}{randint(100, 999)}")


MainWindow = tk.Tk()
MainWindow.geometry("275x150")
MainWindow.title("Username Generator")

tk.Label(MainWindow, text="Welcome to the Username Generator!").pack(pady=10)

tk.Button(MainWindow, text="Generate!", command=lambda: generateRandomName()).pack(pady=10)
outputText = tk.Text(MainWindow, height=1, width=25)
outputText.pack(pady=10)
MainWindow.mainloop()