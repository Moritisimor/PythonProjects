from hashlib import sha256
import tkinter as tk

def makehash():
    hashOutputText.insert("1.0", sha256(hashEntry.get().encode()).hexdigest())

mainWin = tk.Tk()
mainWin.geometry("225x300")
mainWin.title("Hash Generator")

tk.Label(mainWin, text="Welcome to my hash generator!").pack(pady=10)

tk.Label(mainWin, text="Enter your text here").pack(pady=10)
hashEntry = tk.Entry(mainWin)
hashEntry.pack()

tk.Button(mainWin, text="Generate hash", command= lambda: makehash()).pack(pady=10)

tk.Label(mainWin, text="Output").pack()
hashOutputText = tk.Text(mainWin, height=4, width=25)
hashOutputText.pack(pady=10)

mainWin.mainloop()