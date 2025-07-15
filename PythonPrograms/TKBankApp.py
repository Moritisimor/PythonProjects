import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, name, password, money = 0):
        self.name = name
        self.password = password
        self.money = money

    def authlogin(self, name, password):
        if self.name == name and self.password == password:
            return self
        else:
            return None

userList = []

loggedIn = None

def startregwindow():
    def register(name, password):
        for user in userList:
            if user.name == name:
                messagebox.showerror("Error", "User with this name already exists.", parent=regwindow)
                return

        if rwuserentry == "" or rwpassentry == "":
            messagebox.showerror("Error", "Input fields can not be blank.", parent=regwindow)
        else:
            userList.append(User(name, password))
            messagebox.showinfo("Success", "Succesfully created account!", parent=regwindow)
            regwindow.destroy()

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

    rwsubmitbutton = tk.Button(regwindow, text="Submit", command=lambda: register(rwuserentry.get(), rwpassentry.get()))
    rwsubmitbutton.pack(pady=5)

def startloginwindow():
    def login(name, password):
        global loggedIn
        for user in userList:
            user.authlogin(name, password)
            if user.authlogin(name, password) is not None:
                loggedIn = user.authlogin(name, password)
                break
        if loggedIn is None:
            messagebox.showerror("Error", "Login failed.", parent=loginwindow)
        else:
            messagebox.showinfo("Success", f"Succesfully logged in as {name}", parent=loginwindow)
            loginwindow.destroy()

    loginwindow = tk.Toplevel()
    loginwindow.geometry("225x250")
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
mwWelcomeLabel.pack(pady=10)

mwLoginStatusLabel = tk.Label(mainWindow, text="")
mwLoginStatusLabel.pack(pady=2)

registerButton = tk.Button(mainWindow, text="Register", command=lambda: startregwindow())
registerButton.pack(pady=20)

logInButton = tk.Button(mainWindow, text="Log in", command=lambda: startloginwindow())
logInButton.pack(pady=20)

mainWindow.mainloop()

# I do not recommend using tkinter for stuff like this.