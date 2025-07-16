import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, name, password, money = 0.0):
        self.name = name
        self.password = password
        self.money = money

    def authlogin(self, name, password):
        if self.name == name and self.password == password:
            return self
        else:
            return None

userList = [
    User("root", "root", 1000), # Starting users
    User("root1", "root1", 1000)
]

loggedIn = User(None, None)

def startregwindow():
    def register(name, password):
        for user in userList:
            if user.name == name:
                messagebox.showerror("Error", "User with this name already exists.", parent=regwindow)
                return

        if rwuserentry.get().strip() == "" or rwpassentry.get().strip() == "":
            messagebox.showerror("Error", "Input fields can not be blank.", parent=regwindow)
        else:
            userList.append(User(name, password))
            messagebox.showinfo("Success", "Succesfully created account!", parent=regwindow)
            regwindow.destroy()

    regwindow = tk.Toplevel()
    regwindow.geometry("200x250")
    regwindow.title("Registration Window")

    tk.Label(regwindow, text="Create a new account here").pack(pady=15)

    tk.Label(regwindow, text="Enter your username").pack(pady=3)
    rwuserentry = tk.Entry(regwindow)
    rwuserentry.pack(pady=5)

    tk.Label(regwindow, text="Enter your password").pack(pady=3)
    rwpassentry = tk.Entry(regwindow, show="*")
    rwpassentry.pack(pady=5)

    tk.Button(regwindow, text="Submit", command=lambda: register(rwuserentry.get(), rwpassentry.get())).pack(pady=5)

def startloginwindow():
    def login(name, password):
        global loggedIn
        for user in userList:
            if user.name == name:
                if user.authlogin(name, password) is not None:
                    loggedIn = user.authlogin(name, password)
                    messagebox.showinfo("Success", f"Succesfully logged in as {name}", parent=loginwindow)
                    mwLoginStatusLabel.config(text=f"Logged in as {loggedIn.name}")
                    mwBalanceLabel.config(text=f"Current Balance: {loggedIn.money} $")
                    loginwindow.destroy()
                    return
        messagebox.showerror("Error", "Could not log in", parent=loginwindow)

    loginwindow = tk.Toplevel()
    loginwindow.geometry("225x250")
    loginwindow.title("Login Window")

    tk.Label(loginwindow, text="Log into an existing account here").pack(pady=15)

    tk.Label(loginwindow, text="Enter your username").pack(pady=5)

    lwuserentry = tk.Entry(loginwindow)
    lwuserentry.pack(pady=5)

    tk.Label(loginwindow, text="Enter your password").pack(pady=3)

    lwpassentry = tk.Entry(loginwindow, show="*")
    lwpassentry.pack(pady=5)

    tk.Button(loginwindow, text="Submit", command=lambda: login(lwuserentry.get(), lwpassentry.get())).pack(pady=5)

def startwithdrawwindow():
    def withdraw():
        if wwwithdrawentry.get().strip() == "":
            messagebox.showerror("Error", "Do not leave input fields blank")
            return
        try:
            loggedIn.money -= float(wwwithdrawentry.get())
            messagebox.showinfo("Success", f"Succesfully withdrew {wwwithdrawentry.get()} $", parent=withdrawwindow)
            mwBalanceLabel.config(text=f"Current Balance: {loggedIn.money}")
            withdrawwindow.destroy()
        except ValueError:
            messagebox.showerror("Error", "Only enter numbers")

    if loggedIn.name is None:
        messagebox.showerror("Error", "You need to log in to withdraw money")
        return
    else:
        withdrawwindow = tk.Toplevel()
        withdrawwindow.geometry("250x150")
        withdrawwindow.title("Withdraw Window")

        tk.Label(withdrawwindow, text="Withdraw money here").pack(pady=5)

        tk.Label(withdrawwindow, text="Enter your desired amount").pack(pady=5)
        wwwithdrawentry = tk.Entry(withdrawwindow)
        wwwithdrawentry.pack(pady=5)

        tk.Button(withdrawwindow, text="Withdraw", command= lambda: withdraw()).pack(pady=5)

def startdepositwindow():
    def deposit():
        if dwdepositentry.get().strip() == "":
            messagebox.showerror("Error", "Do not leave input fields blank")
            return
        try:
            loggedIn.money += float(dwdepositentry.get())
            messagebox.showinfo("Success", f"Succesfully deposited {dwdepositentry.get()} $", parent=depositwindow)
            mwBalanceLabel.config(text=f"Current Balance: {loggedIn.money}")
            depositwindow.destroy()
        except ValueError:
            messagebox.showerror("Error", "Only enter numbers", parent=dwdepositentry)

    if loggedIn.name is None:
        messagebox.showerror("Error", "You need to log in to deposit money")
        return
    else:
        depositwindow = tk.Toplevel()
        depositwindow.geometry("250x150")
        depositwindow.title("Deposit Window")

        tk.Label(depositwindow, text="Deposit money here").pack(pady=5)

        tk.Label(depositwindow, text="Enter your desired amount").pack(pady=5)
        dwdepositentry = tk.Entry(depositwindow)
        dwdepositentry.pack(pady=5)

        tk.Button(depositwindow, text="Deposit", command= lambda: deposit()).pack(pady=5)

def starttransferwindow():
    def transfer():
        if twtransferentry.get().strip() == "":
            messagebox.showerror("Error", "Input fields can not be empty")
            return
        try:
            account = None
            for user in userList:
                if user.name == twaccountentry.get():
                    account = user

            if account is not None:
                loggedIn.money -= int(twtransferentry.get())
                account.money += int(twtransferentry.get())
                messagebox.showinfo("Success", f"Succesfully transfered {twtransferentry.get()} $ to {twaccountentry.get()}", parent=transferwindow)
                mwBalanceLabel.config(text=f"Current Balance: {loggedIn.money} $")
                transferwindow.destroy()
            else:
                messagebox.showerror("Error", "Could not find account", parent=transferwindow)
        except ValueError:
            messagebox.showerror("Error", "Only enter numbers", parent=transferwindow)

    if loggedIn.name is None:
        messagebox.showerror("Error", "You need to log in to transfer money.")
        return
    else:
        transferwindow = tk.Toplevel()
        transferwindow.geometry("300x225")
        transferwindow.title("Transfer Window")

        tk.Label(transferwindow, text="Transfer money here").pack(pady=5)

        tk.Label(transferwindow, text="Enter your desired amount").pack(pady=5)
        twtransferentry = tk.Entry(transferwindow)
        twtransferentry.pack(pady=5)

        tk.Label(transferwindow, text="Enter the account you want to transfer to").pack(pady=5)
        twaccountentry = tk.Entry(transferwindow)
        twaccountentry.pack(pady=5)

        tk.Button(transferwindow, text="Transfer", command=lambda: transfer()).pack(pady=5)

mainWindow = tk.Tk()
mainWindow.geometry("300x325")
mainWindow.title("Main Menu")

tk.Label(mainWindow, text="Welcome to the PyBank app!").pack(pady=5)

mwLoginStatusLabel = tk.Label(mainWindow, text="Not logged in")
mwLoginStatusLabel.pack(pady=5)

tk.Button(mainWindow, text="Log into existing account", command=lambda: startloginwindow()).pack(pady=5)
tk.Button(mainWindow, text="Register new account", command=lambda: startregwindow()).pack()

mwBalanceLabel = tk.Label(mainWindow, text="Log in to see balance")
mwBalanceLabel.pack(pady=15)

tk.Button(mainWindow, text="Withdraw money", command=lambda: startwithdrawwindow()).pack()
tk.Button(mainWindow, text="Deposit Money", command=lambda: startdepositwindow()).pack(pady=5)
tk.Button(mainWindow, text="Transfer Money", command=lambda: starttransferwindow()).pack(pady=5)

mainWindow.mainloop()

# I do not recommend using tkinter for stuff like this.