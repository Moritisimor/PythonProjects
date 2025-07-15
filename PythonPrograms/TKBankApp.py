import tkinter as tk

class User:
    def __init__(self, name, password, money) -> None:
        self.name = name
        self.password = password
        self.money = password

localUser = User(None, None, 0)
def setuser(name, password):
    localUser.name = name
    localUser.password = password

if localUser.name is None:
    loggedin = False
else:
    loggedin = True

def startregwindow() -> None:
    regwindow = tk.Toplevel()
    regwindow.geometry("200x250")
    regwindow.title("Registration Window")

    rwwelcomelabel = tk.Label(regwindow, text="Create a new account here")
    rwwelcomelabel.pack(pady=15)

    rwuserlabel = tk.Label(regwindow, text="Enter your username")
    rwuserlabel.pack(pady=3)

    rwuserentry = tk.Entry(regwindow)
    rwuserentry.pack(pady=5)

    rwpasslabel = tk.Label(regwindow, text="Enter your password")
    rwpasslabel.pack(pady=3)

    rwpassentry = tk.Entry(regwindow)
    rwpassentry.pack(pady=5)

    rwsubmitbutton = tk.Button(regwindow, text="Submit", command=lambda: setuser(rwuserentry.get(), rwpassentry.get()))
    rwsubmitbutton.pack(pady=5)

mainWindow = tk.Tk()
mainWindow.geometry("375x500")
mainWindow.title("Main Menu")

mwWelcomeLabel = tk.Label(mainWindow, text="Welcome to my bank app!")
mwWelcomeLabel.pack(pady=15)

mwLoginStatusLabel = tk.Label(mainWindow, text="")
mwLoginStatusLabel.pack(pady=2)

if loggedin:
    mwLoginStatusLabel.config(text=f"You are logged in as {localUser.name}")
else:
    mwLoginStatusLabel.config(text="You are not logged in")

registerButton = tk.Button(mainWindow, text="Register", command=lambda: startregwindow())
registerButton.pack(pady=20)

mainWindow.mainloop()