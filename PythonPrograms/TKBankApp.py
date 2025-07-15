import tkinter as tk

class User:
    def __init__(self, name, password, money):
        self.name = name
        self.password = password
        self.money = money

    def authlogin(self, name, password):
        if self.name == name and self.password == password:
            return self
        else:
            return None

userList = [
user1 := User(None, None, 0)
]

loggedIn = None

def setuser(user: User, name, password):
    user.name = name
    user.password = password

def login(name, password):
    global loggedIn
    for user in userList:
        loggedIn = user.authlogin(name, password)

def startregwindow():
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

    rwsubmitbutton = tk.Button(regwindow, text="Submit", command=lambda: setuser(user1, rwuserentry.get(), rwpassentry.get()))
    rwsubmitbutton.pack(pady=5)

def startloginwindow():
    loginwindow = tk.Toplevel()
    loginwindow.geometry("200x250")
    loginwindow.title("Login Window")

    lwwelcomelabel = tk.Label(loginwindow, text="Log into an existing account here")
    lwwelcomelabel.pack(pady=15)

    lwuserlabel = tk.Label(loginwindow, text="Enter your username")
    lwuserlabel.pack(pady=3)

    lwuserentry = tk.Entry(loginwindow)
    lwuserentry.pack(pady=5)

    lwpasslabel = tk.Label(loginwindow, text="Enter your password")
    lwpasslabel.pack(pady=3)

    lwpassentry = tk.Entry(loginwindow)
    lwpassentry.pack(pady=5)

    lwloginbutton = tk.Button(loginwindow, text="Submit", command=lambda: login(lwuserentry.get(), lwpassentry.get()))
    lwloginbutton.pack(pady=5)

mainWindow = tk.Tk()
mainWindow.geometry("375x500")
mainWindow.title("Main Menu")

mwWelcomeLabel = tk.Label(mainWindow, text="Welcome to my bank app!")
mwWelcomeLabel.pack(pady=15)

mwRefreshButton = tk.Button(mainWindow, text="Refresh", command=lambda: mwLoginStatusLabel.config(text=f"Logged in as {loggedIn.name}"))
mwRefreshButton.pack(pady=5)

mwLoginStatusLabel = tk.Label(mainWindow, text="")
mwLoginStatusLabel.pack(pady=2)

registerButton = tk.Button(mainWindow, text="Register", command=lambda: startregwindow())
registerButton.pack(pady=20)

logInButton = tk.Button(mainWindow, text="Log in", command=lambda: startloginwindow())
logInButton.pack(pady=20)

mainWindow.mainloop()